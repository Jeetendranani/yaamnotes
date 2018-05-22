"""
Designing Twitter

Let's design a twitter like social networking service. Users of the service will be able to post tweets, follow other
people and favorite tweets.

Difficulty level: Medium

1. What is twitter?

    Twitter is an online social networking service where post and read short 140 character messages called "tweets".
    Registered users can post and read tweets, but those who are not registered can only read them. Users access Twitter
    through their website interface, SMS or mobile app.

2. Requirements and goals of the system

    We will designing a simpler version of Twitter with following requirements:

    Functional Requirements

        1. User should be able to post new tweets.
        2. A user should be able to follow other users.
        3. Users should be able to mark tweets favorite.
        4. The service should be able to create and display user's timeline consisting of top tweets from all the people
        the user follows.
        5. Tweets can contain photos and videos.

    Non-functional requirements

        1. Our service needs to be highly available.
        2. Acceptable latency of teh system is 200ms for timeline generation.
        3. consistency can take a hit (in the interest of availability), if a user doesn't see a tweet for a while, it
        should be fine.

    Extended Requirements

        1. Searching tweets
        2. Reply to a tweet
        3. Trending topics - current hot topics / searches
        4. Tagging other users
        5. Tweet notification
        6. Who to follow? Suggestions?
        7. Moments

3. Capacity Estimation and Constraints

    Let's assume we have one billion total users, with 200 million daily active user (DAU). Also, we have 100 million
    new tweets every day, and on average each user follows 200 people.

    how many favorites per day? If on average each user favorites five tweets per day, we will have:

        200M users * 5 favorites => 1B favorites

    how many total tweet-views our system will generate? Let's assume on average a user visits their timeline two times
    a day and visits five other people's pages. One each page if a user sees 20 tweets, total-views our system will
    generate:

        200M DAU * ((2 + 5) * 20 tweets) => 28 B/ day

    Storage estimates let's say each tweet has 140 characters and we need two bytes to store a character without
    compression. Let's assume we need 30 bytes to store metadata with each tweet (like id, timestamp, userid, etc).
    Total storage we would need:

        100M * (280 + 30) bytes => 30GB /day

    What would be our storage needs for five years? how much storage would need for user's data, follows, favorites? We
    will leave this for exercise.

    Not all tweets will have media, let's assume that on average every fifth tweet has a photo and every tenth has a
    video. Let's also assume on average a photo is 200KB and a video is 2MB. This will lead us to have 24TB of new media
    every day.

    Bandwidth Estimates Since total ingress is 24TB per day, this would translate into 290BM/sec.

    Remember that we have 28B tweet views per day, We must show the photo of every tweet (if it has a photo), but
    let's assume that the users watch every 3rd video they see in their timeline. So total egress will be:

        (28B * 280 bytes) / 86400s of text => 93 MB/s
        + (28B/5 * 200 KB) / 86400s of photos => 13GB/s
        + (28G/10/3 * 2MB) / 86400s of videos => 22 GB/s

        total ~= 35GB/s

4. System APIs

    Once we've finalized the requirements, it's always a good idea to define the system APIs, this would explicitly
    state what is expected from teh system.

    We can have soap or rest apis to expose the functionality of our service. Following could be teh definition of the
    api for posting a new tweet:

        tweet(api_dev_key, tweet_data, tweet_location, user_location, media_ids, max)

    Parameters:

        api_dev_key(string): The api developer key of a registered account. This will be used to, among other things,
        throttle users based on their allocated quota.

        tweet_data(string): The text of the tweet, typically up to 140 characters.

        tweet_location(string): Optional location (longitude, latitude) this tweet refers to.

        user_location(string): optional location (longitute, latitude) of the user adding the tweet.

        media_ids (number[]): optional list of media_ids to be associated with the tweet. (all the media photo, video,
        etc.) need to be uploaded separately.

    Returns: (String)

        A successful post will return the url to access that tweet. Otherwise, an appropriate http error is returned.

5. high level system design

    We need a system that can efficiently store all the new tweets, 100M/86400s => 1150 tweets per second and read
    28B/86400 => 325 K tweets per seconds. It is clear from teh requirements that this will be a read-heavy system.

    At a high level, we ned multiple application servers to serve all these requests with load balancer in front of
    them for traffic distributions. On the backend, we need an efficient database that can store al the new tweets and
    can support a huge number of reads. We would also need some file storage to store photos and videos.

    Although our expected daily write load is 100 million and read load is 28 billion tweets. This means, on average our
    system will receive around 1160 new tweets and 325k read requests per second. This traffic will be distributed
    unevenly throughout the day, though, at peak time we should expected at least a few thousand write requests and
    around 1M read request per second. We should keep this thing in mind while designing the architecture of our system.

6. Database schema

    We need to store data about users, their tweets, their favorite tweets, and people they follow. For choosing between
    SQL and NoSQL databases to store the above schema, please see 'database schema' under designing instagram.

7. Data sharding

    Since we have a huge number of new tweets every day and our read load is extremely high too. We need to distribute
    our data onto multiple machines such that we can read/write it efficiently. We have many options to shard our data;
    let's go through them one by one:

    sharding based on userid: We can try storing all the data of a user on one server. While storing, we can pass the
    userid to our hash function tht will map the user to a database server where we will store all of the user's tweet,
    favorites, follows, etc. While querying for tweets / follows / favorites of a user, we can ask our hash function
    where can we find teh data of a user and then read it from there. This approach has a couple of issues:

        1. what if a user becomes hot? there could be a lot of queries on the server holding the user. This high load
        will affect the performance of our service.

        2. Over time some users can end up storing a lot of tweets or have a lot fo follows compared to others.
        Maintaining a uniform distribution of growing user's data is quite difficult.

    To recover from these situation either we have to repartition / redistribute our data or user consistent hashing.

    sharding based on Tweetid: our hash function will map each tweetid to a random server where we will store that
    tweet. To search tweets, we have to query all servers, and each server will return a set of tweets. A centralized
    server will aggregate these results to return them to the users. Let's look into timeline generation example, here
    are the number of steps our system has to perform to generate a user's timeline:

        1. Our application (app) server will find all the people the user follows.
        2. App server will send the query to all database servers to find tweet from these people.
        3. Each database server will find the tweets for each user, sort them by recency and return teh top tweets.
        3. App server will merge all the results and sort them  again to return the top results to the user.

    This approach solves the problem of hot users, but in contrast to sharding by userid, we have to query all
    database partitions to find tweets of a user, which can result in higher latencies.

    We can further improve our performance by introducing cache to store hot tweets in front of th database servers.

    Sharding based on tweet creation time: Storing tweets based on recency will give us the advantage of fetching all
    top of tweets quickly, and we only have to query a very small set of servers. But the problem here is that the
    traffic load will not be distributed. e.g., while writing, all new tweets will be going to one server, and the
    remaining servers will be sitting idle. Similarly while reading, the server holding latest data will have a very
    high load as compared the servers holding old data.

    what if we can combine sharding by tweedid and tweet creation time? If we cont store tweet creation time separately
    and user the tweetid to reflect that, we can get benefits of both approaches, this way it wil be quite quick to find
    latest tweets. For this, we must make each tweetid universally unique in our system, and each tweetid should cotain
    timestamp too.

    We can u9se epoch time for this. Let's say our tweetid will have two parts; the first part will be representing
    epoch secons and the second part will be an auto-incrementing sequence. So, to make a new tweetid, we can take
    the current epoch time and append an auto-incrementing number to it. We can figure out shard number from this
    tweetid and store it here.

    What could be the size of our tweetid? let's say our epoch tie starts today, how many bits we would need to store
    the number of seconds for next 50 years?

        86400sec / day * 365 (days a year) * 50 years => 1.6B

    We would need 31 bits to store this number. since on average we are expecting 1150 new tweets per second, we can
    allocate 17 bits to store auto incremented sequence: this will make our tweetid 48 bits long. So every second we can
    store (2^17 => 130K) new tweets. We can reset our auto incrementing sequence every second. For fault tolerance and
    better performance, we can have two database servers to generate auto-incrementing keys for us. One generating
    even numbered keys and the other generating odd numbered keys.

    If we assume our current epoch seconds are "1483228800", our tweetid will look like this:

    If we mke our tweetid 64 bits (8 bytes) long, we can eassily sotre tweets for next 100 years and also store them for
    mili-seconds granularity.

8. Cache

    We can introduce a cache for database servers to cache hot tweets and users. We can use an off the shelf solution

    off the shelf solution todo

    like Memcache that can store the whole tweet objects. Application servers before hitting database can quickly check
    if the cache has desired tweets. Based on clients' useage pattern we can determine how many cache servers we need.

    which cache replacement policy would best fit our needs? When the cache is full, and we want to replace a tweet with
    a newer/ hotter tweet, how would we choose? Least Recently Userd (LRU) can be a reasonable policy for our system.
    Under this policy, we discard the latest recently viewed tweet first.

    how can we have more intelligent cache? If we go with 80-20 rule, that is 20% of tweets are generating 80% of read
    traffic which means that certain tweets are so popular that majority of people read them. This dictates that we
    can try to cache 20% of daily read volume from each shard.

    what if we cache the latest data? Our service can benefit from this approach. Let's say if 80% of our users see
    tweets from past three days only; we can try to cache all the tweets from past three days. Let's say we have
    dedicated cache servers that cache all the tweets from all users from past three days. As estimated above, we are
    getting 100 million new tweets or 30GB of new data every day (without photos and videos). If we want to store all
    the tweets from last three days, we would need less than 100GB of memory. This data can easily fit into one server,
    but we should replicate it onto multiple servers to distribute all the read traffic to reduce the load on cache
    servers. So whenever we are generating a users' timeline, we can ask the cache servers if they have all teh recent
    tweets for that user, if yes, we can simply return all the data from teh cache. If we dont' have enough tweets in
    the cache, we have to query backend to fetch that data. On a similar design, we can try caching photos and videos
    from last three days.

    Our cache would be like a hash table, where 'key' would be 'ownerid' and 'value' would be a doubly linked list
    containing all the tweets from that user in past three days. Since we want to retrieve most recent data first, we
    can always insert new tweets at the head of the linked list. which means all the older tweets will be near the tail
    of the linked list. Therefore, we can remove tweets from the tail to make space for newer tweets.

9. timeline generation

    For a detailed discussion about timeline generation, take a look at Designing Facebook's newsfeed.

10. Replication and Fault Tolerance

    Since our system is read-heavy, we can have multiple secondary database servers for each db partition. Secondary
    servers will be used for read traffic only. All writes will first go to the primary server and then will be
    replicated to secondary servers. This scheme will also give us fault tolerance, as whenever the primary server goes
    down, we can failover to teh secondary server.

11. Load balancing

    We can add load balancing layer at three places in our system:

        1. Between clients and applications server
        2. Between application server and database replication servers
        3. Between aggregation servers and cache servers

    Initially, a simple round robin approach can be adopted; that distributes incoming requests equally among servers.
    This LB is simple to implement and does not introduce any overhead. Another benefit of this approach is if a
    server is dead, LB will take it our of the rotation and will stop sending any traffic to it. A problem with Round
    robin LB is, it won't take server load into consideration. If a server is overloaded or slow, the LB will not stop
    spending new requests to that server. To handle this, a more intelligent LB solution can be placed that periodically
    queries backed server about their load and adjust traffic based on that.

12. Monitoring

    having the ability to monitor our system is crucial. We should constantly collect data to get an instant insight
    into how our system is doing. We can collect following metrics / counters to get an understanding of the performance
    of our service:

        1. New tweets per day/ second, what is the daily peak?
        2. Timeline delivery stats, how many tweets per day / second our service is delivering.
        3. Average latency that is seen by the user to refresh timeline.

    By monitoring these counters, we will realize if we need more replication or load balancing or caching, etc.

13. Extended requirements

    how to serve feeds? Get all the latest tweets from the people someone follows and merge / sort them by time. use
    pagination to fetch / show tweets. Only fetch top N tweets from all teh people someone follows. This N will depend
    on the client's Viewport, as on mobile we show fewer tweets compared to a web client. We  can also cache next top
    to speed things up.

    Alternately, we can pre-generate the feed to improve efficiency, for details please see 'ranking and timeline
    generation' under designing instagram.

    retweet: with each tweet object in the database, we can store the id of original tweet and not store any contents on
    this retweet object.

    Trending topics: We can cache most frequently occurring hashtags or searched queries in the last N seconds and keep
    updating them after every M seconds. We can rank trending topics based on the frequency of tweets or search queries
    or retweets or likes. We can give more weight to topics which are shown to more people.

    who to follow? how to give suggestions? This feature will improve user engagement. We can suggest friends of people
    someone follows. We can go two or three level down to find famous people for the suggestions. We can give preference
    to people with more followers.

    As only a few suggestions can be made at any time, use machine learning (ML) to shuffle and re-prioritize. ML
    signals could include people with recently increased follow-ship, common followers if the other person is following
    this user, common location or interests, etc.

    Moments: Get top news for different websites for past 1 or 2 hours, figure out related tweets, prioritize them,
    categorize them (news, support, financials entertainment, etc) using ML - supervised learning or Clustering. Then
    we can show these articles as trending topics in Moments.

    Search: Search involves Indexing, Ranking, and Retrieval of tweets, A similar solution is discussed in our next
    problem design twitter search.
"""