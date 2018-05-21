"""
Designing a url shortening service like TinyURL

Let's design a url shortening service like TinyURL. This service will provide short aliases redirecting to long URLs.

Similar services: bit.ly, goo.gl, 2020.fm etc.

Difficulty Level: Easy


1. Why do we need url shortening?

    url shortening is used to create shorter aliases for long urls. Users redirected to the original url when they hit
    these aliases. A shorter version of any url would save a lot of space whenever we use it. e.g., when printing or
    tweeting as tweets have a character limit.

    For example, if we shorten this page through tinyurl:
    long url
    we would get:
    short url

    The shortened url is nealy 1/3rd of the size of the actual url.

    url shortening is used for optimizing links across devices, tracking individual links to analyze audience and campaign
    performance, and hiding affiliated original urls, etc.

    If you haven't used tinyurl.com before, please try creating a new shortened url and spend some time going through
    different options their service offers. This will help you a log in understanding this chapter better.

2. Requirements and Goals of the system

    You should always clarify requirements at the beginning of he interview and should ask questions to find the exact
    scope of the system that interview has in mind.

    our url shortener system should meet the following requirements:

    functional requirements:
    1. Given a url, our service should generate a shorter and unique alias of it.
    2. When users access a shorter url, our service should redirect them to the original link.
    3. users should optionally be able to pick a custom alias for their url.
    4. links will expire after a specific time span automatically; users should also be able to specify expiration time.

    non-function requirements:
    1. the system should be highly available. This is required because if our service is down, all the url redirections will
    start failing.
    2. url redirection should happen in real-time with minimum latency.
    3. shortened links should not be guessable (not predicable).

    extended requirements:
    1. Analytics, e.g. how many times redirections happened?
    2. our service should also be accessible through rest apis by other services.

3. Capacity Estimation and Constraints

    Our system would be read-heavy; there would be lots of redirection requests compared to new url shortenings. Let's
    assume 100:1 ratio between read and write.

    - Traffic estimates: If we assume that we would have 500M new urls shortenings per month, we can expect (100 * 500M
    => 50B) redirections during the same time. What would be queries per second (qps) for our system?

    New urls shortening per seconds:

        500m / (30days * 24hours * 3600 seconds) ~= 200 urls/s

    urls redirections per second:

        50b / (30days * 24hours *3600seconds) ~= 19k/s

    - Storage estimates: Since we expect to have 500M new urls every month and if we would keeping these objects for
    five years; total number of objects will be storing would be 30 billion.

        500million * 5 years * 12 months = 30 billion

    Let's assume that each object we are storing can be of 500 bytes (just a ballpark, we will dig into it later); we
    would need 15TB of total storage:

        30 billion * 500 bytes = 15TB

    - Bandwidth estimates: For write requests, since every second we expect 200 new urls, total incoming data for our
    service would be 100kb per second.

        200 * 500bytes = 100 kb/s

    For read requests, since every second we expect ~ 19k urls redirections, total outgoing data for our service would
    be 9MB per second.

        ~19k*500 bytes ~= 9MB/s

    Memory estimates: If we want to cache some of the hot urls that are frequently accessed, how much memory would we
    need to store them? If we follow the 80-20 rule, meaning 20% of urls generating 80% of traffic, we would like to
    cache these 20% hot urls.

    Since we have 19k requests per second, we would be getting 1.7 billion requests per day.

        19k * 3600 seconds * 24 hours ~= 1.7 billion

    To cache 20% of this requests, we would need 170GB of memory.

        0.2 * 1.7 billion * 500bytes ~= 170GB

    High level estimates: Assuming 500 million new urls per month and 100:1 read: write ratio, following is the summary
    of the high level estimates for our service:

        new urls            200/s
        url redirections    19k/s
        incoming data       100KB/s
        outgoing data       9MB/s
        Storage for 5 years 15TB
        Memory for cache    170GB

4. System APIs

    Once we've finalized the requirements, it's always a good idea define the system apis, this would explicitly state
    what is expected from the system.

    We can have soap or rest apis to expose the functionality of our service. Following could be the definitions of the
    apis for creating and deleting urls:

        creatURL(api_dev_key, original_url, custom_alias=None user_name=None, expire_date=None)

        Parameters:
            api_dev_key(sting): The API developer key of a registered account. This will be sued to, among other things,
            throttle users based on their allocated quota.

            original_url(string): Original url to be shorted.
            custom_alias(string): Optional custom key for the url
            user_name(string): optional user name to be used in encoding.
            expire_data(string): optional expiration data for the shortened url

        return: (string)
            A successful insertion return teh shortened url, otherwise, return an error code.

        deleteURL(api_dev_key, url_key)

        Where "url_key" is a string representing the shortened url to be retrieved. A successful deletion returns 'url
        removed'.

    How do we detect and prevent abuse? For instance, any service can put us out of business by consuming all our keys
    in the current design. To prevent abuse, we can limit users through their api_dev_key, how many url they can create
    or access in a certain time.

5. Database Design

    Defining the DB schema in the early stages of the interview would help to understand the data flow among various
    components and later would guide towards the data partitioning.

    A few observations about nature of data we are going to store:
        1. we need to store billions of records.
        2. Each object we are going to store is small (less than 1k).
        3. There are no relationships between records, except if we want to store which user created what url.
        4. our service is read heavy.

    Database schema:

    We would need two tables, one for storing information about the url mappings and the other for user's data.

        url table

        pk  hash: varchar(16)
            originalurl: varchar(512)
            creationdate: datetime
            expreationdate: datetime
            userid: int

        user table
        pk  userid:int
            name: varchar(20)
            email: varchar(32)
            creationdate: datetime
            lastlogin: datetime

    What kind of database should we use? Since we are likely going to store billions of rows and we dont' need to use
    relationship between objects - a nosql key-value store like dynamo or cassandra is a better choice, which would also
    be easier to scale. Please see sql vs nosql for more details. If we choose nosql, we cann't store userid in the url
    table (as there no foreign keys in nosql), for that we would need a third table which will store the mapping
    between the url and user.

6. Basic system design and algorithm

    The problem we are solving here is to generate a short and unique key for the given url. In the above-mentioned
    example, the shortened url we got was: "", the last six characters of this url is teh short key we want to generate,
    we'll explore two solutions here:

    a. Encoding actual url

        We can compute a unique hash (e.g., MD5 or SHA256, etc.) of the given url. The hash can then be encoded for
        displaying, This encoding could be base36([a-z, 0-9]) or base62([A-Z, a-z-0-9]) and if we add '-' and '.', we can
        use base64 encoding. A reasonalbe question would be:
        what should be the length of the short key? 6, 8, 10 characters?

        Using base64 encoding, a 6 latter long key would result in 64^6 ~= 68.7 billion possible strings.
        using bases65 encoding, an 8 letter long key would result in 64^8 ~= 281 trillion possible strings.

        with 68.7B unique strings, let's assume for our system six letters key would suffice.

        md5 todo
        sha256 todo

        base36 todo
        base62 todo
        base64 todo

        What are different issues with our solution? We have the following couple of problems with our encoding scheme:

        1. If multiple users enter the same url, they can get the same shortened url, which is not acceptable.

        2. What if parts of the url are url-encoded? and are identical except for the url encoding.

        Workaround for the issues: We can append an increasing sequence number to each input url to make it unique and
        then generate a hash of it. we don't need to sore this sequence number in the database, though. Possible
        problems with this approach could be how big this sequence number would be, can it overflow? Appending an
        increasing sequence number will impact performance fo the service too.

        Another solution would be, to append user id (which should be unique) to the input url. However, if the user
        has not signed in, we can ask the user to choose a uniqueness key, even after this if we have a conflict, we
        have keep generating a key until we get a unique one.

    b. generating keys offline

        We can have a standalone key generation service (KGS) that generates random six letter strings beforehand and
        store them in a database (let's call it key-db). Whenever we want to shorten a url, we will just take one of the
        already generated keys and use it. This approach will make things quite simple and fast since we will not be
        encoding the url or worrying about duplications or collisions. KGS will make sure all the keys inserted in
        key-db are unique.

        can concurrency cause problem? As soon as key is used, it should be marked in the database, so that it doesn't
        get used again. If there are multiple servers reading keys concurrently, we might get a scenario where two or
        more servers try to read the same key from the database. How can we solve this concurrency problem? todo

        Servers can use KGS to read/mark keys in the database, KGS can use two tables to store keys, one for keys that
        are not used yet and one for all the used keys. As soon as KGS gives keys to one of the servers, it can move
        them to teh used keys table. KGS can always keep some keys in memory so that whenever a server need them, it
        can quickly provide them. For simplicity, as soon as KGS loads some keys in memory, it can move them to used
        key table. This ways we can make sure each server gets unique keys. If KGS dies before assigning all the loaded
        keys to some server, we will be wasting those keys, which we can ignore given a huge number of keys we have.
        KGS also has to make sure not to give teh same key to multiple servers. For that, is must synchronize (or get
        a lock to) the data structure holding the keys before removing keys from it and giving them to a server.

        What would be teh key-db size? With base64 encoding, we can generate 68.7B unique six letters keys. If we need
        one bytes to store one alpha-numeric character, we can store all these keys in:

            6(character per key) * 68.7B (unique keys) => 412.GB

        Isn't KGS the single point of failure? Yes, it is. To solve this, we can have a standby replica of KGS, and
        whatever the primary server dies, it can take over to generate and provide keys.

        Can each app server cache some keys from key-db? yes, this can surely speed things up, Although in this case, if
        the application server dies before consuming all the keys, we will end up losing those keys. This could be
        acceptable since we have 68B unique six letters keys.

        how would we perform a key lookup? We can look up hte key in our database or key-value store to get the full
        url. If it's present, issues a '302 redirect" status back to the browser, passing the stored url in the
        'location' field. If that key is not present in our system, issue a '404 not found' status, or redirect the
        user back to the homepage.

        should we impose size limits on custom aliases? Since our service supports custom aliases, users can pick any
        'key' they like, but providing a custom alias is not mandatory. however, it is reasonable (and often desirable)
        to impose a size limit on a custom alias, so that we have consistent url database. Let's assume users can
        specify maximum 16 characters long customer key (as reflected in the above database schema).

7. Data partitioning and replication

    To scale out our DB, we need to partition it so that it can store information about billions of url. We need to
    come up with a partitioning scheme that would divide and store out data to different db servers.

    a. range based partitioning: We can store urls in separate partitions based on the first letter of the url or the
    hash key. Hence we save all the urls starting with letter 'A' in one partition and those that start with letter 'B'
    into another partition and so on. This approach is called range based partitioning We can even combine certain less
    frequently occurring letters into one database partition. We should come up with this partitioning scheme statically
    so that we can always store /find a file in a predictable manner.

    the main problem with this approach is that it can lead to unbalanced servers, for instance; if we decide to put all
    urls starting with letter 'E' into a db partition, but later we realize that we have too many urls that start with
    letter 'E', which we can't fit into one DB partition.

    b. hash-based partitioning: In this scheme, we take a hash of the object we are storing, and based on this hash we
    figure out the db partition to which this object should go. In our case, we can take the hash of the 'key' or the
    actual url to determine the partition to store the file. Our hashing function will randomly distribute urls into
    different partitions, e.g., our hashing function can always map any key to a number between [1..256], and this
    number would represent the partition to store our object.

    This approach can still lead to overloaded partitions, which can be solved by using consistent hashing.

8. Cache

    We can cache urls that are frequently accessed. We ca use some off-the-shelf solution like Memcache, that can store
    full urls with there respective hashes. The application servers, before hitting bckend storage, can quickly check
    if the cache has desired url.

    how much cache should we have? We can start with 20% of daily traffic and based on clients usage pattern we can
    adjust how many cache servers we need. As we estimated above we need 15GB memory to chache 20% daily traffic that
    can easily fit into one server.

    which cache eviction policy would best fit our needs? When the cache is full, and we want to replace a link with a
    newer / hotter url, how would we choose? Least Recently Used (LRU) can be reasonable policy for our system. Under
    this policy, we discard the least recently used url first. We can use linked hash map or a similar data structure
    to store our urls and hashes, which will also keep track of which urls are accessed recently.

    To further increase teh efficiency, we can replicate our caching servers to distribute load between them.

    how can each cache replica be updated? Whenever there is a cache miss, our server would be hitting backend database.
    Whenever this happens, we can update the cache and pass the new entry to all the cache replicas. Each replica can
    update there caches by adding the new entry. If a replica already ahs the entry, it can simply ignore it.

9. Load balancer (LB)

    We can add load balancing layer at three places in our system:

    1. Between clients and applications servers
    2. Between application server and database servers
    3. Between application server and cache servers

    Initially, a simple round robin approach can be adopted; that distributes incoming requests equally among backend
    servers. This LB is simple to implement and does not introduce an overhead. Another benefit of this approach is if
    a server is dead, LB will take it our of the rotation and will stop sending any traffic to it. A problem with Round
    Robin LB is, it wont' take server load into consideration. If a server is overloaded or slow, the LB will not stop
    sending new requests to that server. To handle this, a more intelligent LB solution can be placed that periodically
    queries backend server about its load and adjusts traffic based on that.

10. Purging or DB cleanup

    Should entries stick around forever or should they be purged? If a user-specified expiration time is reached, what
    should happen to the link? If we chose to actively search for expired links to remove them, it would put a lot of
    pressure on our database. We can slowly remove expired links and do a lazy cleanup too. Our service will make sure
    that only expired links will be deleted, although some expired links can live longer but will never be return to
    users.

    - Whenever a user tries to access an expired link, we can delete the link and return an error to the user.
    - A separate cleanup can run periodically to remove expired links from our storage and cache. This service should be
    very lightweight and can be scheduled to run only when the user traffic is expected to be low.
    - We can have a default expiration for each link, e.g., two years.
    - After removing an expired link, we can put the key back in the key-db to be reused.
    - Should we remove links that haven't been visited in some length of time, says six months? this could be tricky,
    Since storage is getting cheap, we can decide to keep links forever.

11. Telemetry

    How many times a short url has been used, wht were user locations, etc.? how would we store these statistics? If it
    is part of a DB rwo that gets updated on each view, what will happen when a popular url is slammed with a large
    number of concurrent request?

    We can have statistics about the country of the visitor, date and time of access, web page that refers the click,
    browser or platform from where the page was accessed and more.

12. Security and permissions

    Can user create private urls or allow a particular set of users to access a url?

    We can store permission level (public / private) with each url in the database, we can also create a separate table
    to store userids that have permission to see a specific url. If a user does not have permission and try to access a
    url, we can send an error (http 401) back, Given that, we are storing our date in a nosql wide-column database like
    cassandra, the key for the table storing permission would be the 'hash' (or the KGS generated 'key'), and the
    columns will store the userids of those users that have permission to see this url.
"""