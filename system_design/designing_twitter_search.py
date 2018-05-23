"""
Design twitter search

Twitter is one of the largest social networking service where users can share photos, news, and text-based messages. In
this chapter, we will design an service that can store and search user tweets.

Similar Problems: Tweet search.
Difficulty Level: Medium

1. What is twitter search?

    Twitter user can update their status whenever they like. Each status consists of plain text, and our goal is to
    design a system that allows searching over all the user statues.

2. Requirements and goals of the system

    - let's assume twitter has 1.5 billion total user with 800 million daily active users.
    - On the average twitter gets 400 million status updates every day.
    - Average size of a status is 300 bytes.
    - Let's assume there will be 500M searches every day.
    - The search query will consist of multiple words combined with AND/OR.

    We need to design a system that can efficiently store and query user status.

3. Capacity Estimation and Constraints

    Storage capacity: Since we have 400 million new statuses every day and each status on average is 300 bytes,
    therefore total storage we need, will be:

        400M * 300 => 112GB/day

    Total storage per second:

        112GB/86400 sec ~= 1.3MB/second

4. System APIs

    We can have soap or rest apis to expose functionality of our service; following could be teh definition of search
    API:

        search(api_dev_key, search_terms, maximum_results_to_return, sort, page_token)

    parameters:

        api_dev_key(string): the api developer key of a registered account. this will be used to, among other things,
        throttle users based on their allocated quota.

        search_terms(string): a string containing the search terms.

        maximum_results_to_return(number): number of status message to return.

        sort(number): optional sort mode: latest first (0 - default), best matched (1), most liked (2).

        page_token(string): this token will specify a page in the result set that should be returned.

    returns: (json)

    A json containing information about a list of status messages matching the search query, each result entry can have
    the user id & name, status text, status id, creation time, number of likes, etc.

5. High level design

    At the high level, we need to store all the status in a database, and also build an index that can keep track of
    which word appears in which status. This index will help us quickly find statuses that suers are trying to search.

    index server todo

6. Detailed components design

    1. Storage: We need to store 112GB of new data every day. Given this huge amount of data, we need to come up with
    a data partitioning scheme that will be efficiently distributing it onto multiple servers. If we plan for next
    five years, we will need following storage:

        112GB * 365 days * 5 => 200 TB

    if we never want to be more than 80% full, we would need 240TB. Let's assume that we want to keep an extra copy of
    all teh statues for fault tolerance, then our total storage requirement will be 480TB. If we assume a modern server
    can store up to 4TB of data, then we would need 120 such servers to hold all of the required data for next five
    years.

    Let's start with a simplistic design where we store our statuses in a mysql database. We can assume to store our
    statuses in a table having two columns, statusids are system-wide unique, we can define a hash function that can
    map a statusid to a storage server, where we can store that status object.

    how can we create system wide unique statusids? If we are getting 400m new statuses each day, then how many status
    objects we can expect in five years?

        400M * 365 days * 5 years => 730 billion

    This means we would need a five bytes number to identify statusids uniquely. let's assueme we have a service that
    can generate a unique statusid whenever we need to store an object (we will discuss this in detail later). We can
    feed the statusid to our hash function to find the storage server and store our status object there.

    2. index: what should our index look like? Since our status queries will consist of words, therefore, let's build
    our index that can tell us which word comes in which status object. Let's first estimate how big our index will be.
    If we want to build an index for all the english words and some famous nouns like people names, city names, etc. and
    if we assume that we have around 300k english words and 200k nouns, then we wil hav 500k total words in our index.
    let's assume that the average length of a word is five characters. If we are keeping our index in memory, we would
    need 2.5 BM of memory to store all the words:

        500k * 5 => 2.5MB

    Let's assume that we want to keep the index in memory for all the statues objects for only past two years. Since
    we will be getting 730B status objects in 5 years, this will give us 292B status messages in two years. Given that,
    each statusid will be 5 bytes, how much memory will we need to store all teh statusids?

        292B * 5 => 1460 GB

    So our index would be like a big distributed hash table, where 'key' would be the word, and 'value' will be a list
    of status_ids of all those status objects which contains that word. Assuming on teh average we have 40 words in
    each status and since we will not be indexing prepositions and other small words like 'the', 'an', 'and' etc., let's
    assume we will have around 15 words in each status that need to be indexed. This means each statusId will stored 15
    times in our index. So total memory will need to store our index:

        (1460 * 15) + 2.5MB ~= 21 TB

    Assuming a high-end server has 144GB of memory, we would need 152 such servers to hold our index.

    We can shard our data based on two criteria:

    sharding based on words: While building our index, we will iterate through all the words of a status and calculate
    the hash of each word to find the server where it would be indexed. To find all statuses containing a specific
    word we ahve to query only that server which contains this word.

    we have a couple of issues with this approach:

        1. What if a word becomes hot? There would be a lot of queries on the server holding that word. This high load
        will affect the performance of our server.

        2. Over time some words can end up storing a lot of statusid compared to others, therefore, maintaining a
        uniform distribution of words while statues are growing is quite difficult.

    To recover from this situations either we have to repartition our data with use consistent hashing.

    Sharding based on the status on the status object: while string, we will pass the statusid to our hash function to
    find the server and index all the words of teh status on that server. While querying for a particular word, we have
    to query all teh servers, and each server will return a set of statusids. A centralized server will aggregate these
    results to return them to the user.

7. Fault tolerance

    Wht will happen when an index server dies? We can have a secondary replica of each server, and if the primary
    server dies it can take control after the failover. Both primary and secondary servers will have the same copy of
    the index.

    What if both primary and secondary server die at the same time? We have to allocate a new server and rebuild the
    same index on it. How can we do that? We dont' know what word / statues were kept on this server. if we were using
    'Sharding based on teh status objects', the brute-foce solution would be to iterate through the whole database and
    filter statusids using our hash function to figure out all the required status that will be stored on this server.
    This would be inefficient and also during the time when the server is being rebuilt we will not be able to serve
    any query from it. thus missing some statuses that should have been seen by the user.

    How can we efficiently retrieve a mapping between statuses and index server? We have to build a reverse index that
    will map all the statusid to there index server. our index-builder server can hold this information. We will need to
    build a hash table, where the 'key' would be the index server number and the value would be a hashset containing all
    the statusids being kept at that index server. notice that we are keeping all the statusids in a hashset, this will
    enable us to add /remove statuses from our index quickly, so now whenever an index server has to rebuild itself, it
    can simply ask the index-builder server for all the statues it needs to store, and then fetch those statuses to
    build the index. This approach will surely be quite fast. We should also have a replica of index-builder server for
    fault tolerance.

8. Cache

    To deal with hot status objects, we can introduce a cache in front of our database. We can use memcache, which can
    store all such hot status objects in memory. Application servers before hitting backend database can quickly check
    if the cache has that status object. Based on clients usage pattern we can adjust how many cache servers we need.
    For cache eviction policy, Least Recently Used (LRU) seems suitable for our system.

9. Load Balancing

    We can add load balancing layer at two places in our system:

        1. Between Clients and applications server
        2. Between application server and backend server

    Initially, a simple round robin approach can be adopted; that distributes incoming requests equally among backend
    servers. This LB is simple to implement and does not introduce any overhead. Another benefit of this approach is if
    server is dead, LB will take it out of the rotation and will stop sending any traffic to it. A problem with Round
    Robin LB is, it wont' take server laod into consideration. If a server is overloaded or slow, the LB will not
    stop sending new requests to that server. To handle this, a more intelligent LB solution can be placed that
    periodically queries backend server about their load and adjust traffic based on that.

10. Ranking

    How about if we want to rank the search results by social graph distance, popularity, relevance, etc?

    Let's assue we want to rank statuses on popularity, like, how many likes or comments a status is getting, etc. In
    such a case our ranking algorithm can calculate a 'popularity number' (based on teh number of likes etc), and store
    it with the index. Each partition can sort the results based on this popularity number before returning results to
    the aggregator server. The aggregator server combines all these results, sort them based on the popularity number
    and sends the top results to the user.
"""