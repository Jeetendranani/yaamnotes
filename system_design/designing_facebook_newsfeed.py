"""
Designing facebook's newsfeed

Let's design Facebook's newsfeed, which would contains posts, photos, videos and status updates from all the people and
pages a user follows.

similar services: Twitter newsfeed, instagram newsfeed, quora newsfeed

Difficulty level: hard

1. What is facebook's newsfeed?

    Newsfeed is the constantly updating list of stories teh middle of Facebook's homepage. It includes status updates,
    photos, videos, links, app activity and links from people, pages, and groups that a user follows on Facebook. In
    other works, it's a compilation of a complete scrollable version of your and your friends' like story from photos,
    videos, locations, status updates and other activities.

    Any social media site you design - Twitter, instagram or Facebook, you will need some sort of newsfeed system to
    display updates from friends and followers.

2. Requirements and goals of the system.

    Let's design a newsfeed for facebook with the following requirements:

    Functional requirements:

        1. Newsfeed will be generated based on teh posts from the people, pages, and groups that a user follows.
        2. A user may have many friends and follow a large number of pages/ groups.
        3. Feeds may contain images, videos or just text.
        4. Our service should support appending new posts, as they arrive, to the newsfeed for all active users.

    Non-functional requirements:

        1. Our system should be able to generate any user's newsfeed in real-time maximum latency seen by the end user
        could be 2s.

        2. A post shouldn't take more than 5s to make it to a user's feed assuming a new newsfeed request comes in.

3. Capacity Estimation and Constraints

    Let's assume on average a user has 300 friends and follows 200 pages.

    Traffic estimates: Let's assume 300M daily active users, with each user fetching their timeline an average of five
    times a day. This will result in 1.5B newsfeed requests per day or approximately 17,500 request per seconds.

    Storage estimates: On average, let's assume, we would need to have around 500 posts in every user's feed that we
    want to keep in memory for a quick fetch. Let's also assume that on average each post would be 1KB in size. This
    would mean that we need to store roughly 500KB of data per user. To store all this data fro all the active users,
    we would need 150TB of memory. if a server can hold 100GB, we would need around 1500 machines to keep the top 500
    posts in memory for all active users.

4. System apis

    Once we've finalized the requirements, it's always a good idea to define the system apis. This would explicitly
    state what is expected from teh system.

    We can have soap or rest apis to expose the functionality of our service. Following could be definition of the api
    for getting the newsfeed:

        getUserFeed(api_dev_key, user_id, since_id, count, max_id, exclude_replies)

    parameters:

        api_dev_key(string): The api developer key of a registered account. This can be used to, among other things,
        throttle users based on there allocated quota.

        user_id(number): The id of the user for whom the system will generate the newsfeed.

        since_id(number): Optional; returns results with an id greater than (that is, more recent than) the specified
        id.

        count (number): optional; specifies the number of reed items to try and retrieve, up to a maximum of 200 per
        distinct request.
        max_id(number): optional; returns results with an id less than (that is, older than) or equal to the specified
        id.

        exclude_replies(boolean): Optional; this parameter will prevent replies from appearing in the returned timeline.

    Returns: (Json) returns a json object containing a list of feed items.

5. Database Design

    There are three basic objects: User, Entity (e.g., page, group, etc) and Feeditem (or Post). Here are some
    observations about the relationships between these entities:

        - A user can follow entities and can become friends with other users.
        - Both users and tentities can post feeditems which can contain text, images or videos.
        - Each feeditem will have a userid which would point to the user who created it. For simplicity, let's assume
        that only users can create feed items, although on Facebook, Page s can post feed item too.
        - EAch feeditem can optionally have an entityid pointing to the page of the group where that post was created.

    If we are usign a relational database, we would nee to model two relations: user-entity relation and feeditem-media
    relation. Since search user can be friends with many people and follow a lot of entities, we can store this
    relation in a separate table. The "Type" column in "userfollow" identifies if the entity being followed is a user
    or entity. Similarly, we can have a table for feedmedia relation.

        user table
        pk  userid: int
            name: varchar(20)
            email: varchar(32)
            dtaofbirth: datetime
            creationdate: datetime
            lastlogin: datetime

        entity table
        pk  entityid:int
            name: varchar(20)
            type: tinyint
            description: varchar(512)
            creationdate: datetime
            category: smallint
            phone: varchar(12)
            email: varchar(20)

        userfollow table
        pk  userid:int
            entityorfriendid:int

            type:intyint

        feeditem table
        pk  feeditemid:int
            userid:int
            contents:varchar9256)
            entityid:int
            locationlatitute:int
            locationlogitute:int
            creationdate: datetime
            numlikes:int

        feedmedia table
        pk  feeditemid:int
            mediaid:int

        media table
        pk  mediaid:int
            type: smallint
            description varchar(256)
            path: varchar(256)
            locationlatitude:int
            locationilogitude:int
            cretiondata:datetime

6. high Level system design

    At a high level this problem can be divided into two parts:

    Feed generation: Newsfeed is generated from the posts (or feed items) of users and entities (page and groups) that
    a user follows. So, whenever our system receives a request to generate the feed for a user (say jane), we will
    perform following steps:

        1. retrieve ids of all users and entities that Jane follows.
        2. Retrieve latest, most popular and relevant posts for those ids. These are the potential posts that we can
        show in jane's newsfeed.
        3. Rank these posts, based on the relevance to Jane. This represents Jane's current feed.
        4. Store this feed in the cache and return top posts (says 20) to be rendered on jane's feed.
        5. On the front-end when Jane reaches the end of her current feed, she can fetch next 20 posts from the server
        and so on.

    One thing to notice here is that we generated teh feed once and stored it in cache. What about new incoming posts
    from people that Jane follows? If jane is online, we should have a mechanism to rank and add those new posts to her
    feed. We can periodically (say every five minutes) perform the above steps to rank and add the newer posts to her
    feed. Jane can then be notified that there are newer items in her feed that she can fetch.

    Feed publishing: Whenever Jane loads her newsfeed page, she has to request and pull feed items from the server. when
    she reaches the end of her current feed. she can pull more data form teh server. For newer items either the server
    can notify Jane and then she can pull, or the server can push these new posts, we will discuss these options in
    detail later. At a high level, we would need following components in our Newsfeed service:

        1. Web servers: To maintain a connection with the user. This connection will be used to transfer data between
        the user and the server.
        2. Application server: To execute the workflows of storing new posts in the database servers. We would also need
        some application servers to retrieve and push the newsfeed to the end user.
        3. Metadata database and cache: To store the metadta about users, pages and groups.
        4. Posts database and cache: To store metadata bot posts and their contents.
        5. Video and photo storage, and cache: Block storage, to store all the media included in the posts.
        6. Newsfeed generation service: To gather and rank all the relevant posts for a user to generate newsfeed and
        store in the cache. This service would also receive live updates and will add these newer feed items to any
        user's timeline.
        7. Feed notification service: To notify the user that there are newer items available for their newsfeed.

    following is the high-level architecture diagram of our system. user B and C are following user A.

7. Detailed components design

    Let's discuss different components of our system in detail.

    a. Feed generation

        Let's take the simple case of teh newsfeed generation service fetching most recent posts from all teh user and
        entities that Jane follows; the query would look like this:

            SELECT FeedItemID FROM FeedItem WHERE SourceID in (
                SELECT EntityOrFriendID FROM UserFollow WHERE UserID = <current_user_id>
            )
            ORDER BY CreationDate DESC
            LIMIT 100

        Here are issues with this design for a feed generation service:

            1. crazy slow for users with a lot of friends / follows as we have to perform sorting / merging /ranging of
            a huge number of posts.
            2. We generate the timeline when a user loads their page. this would be quite slow and have a high latency.
            3. For live updates, each status update will result in feed updates for all followers, this could result in
            high backlogs in our newsfeed generation service.
            4. For live updates, the server pushing (or notifying about) newer posts to users could lead to very heavy
            loads, especially for people or pages that have a lot of followers. to improve the efficiency, we can
            pre-generate the timeline and store it in a memory.

        Offline generation for newsfeed: We can have dedicated servers that are continuously generating users' newsfeed
        and storing them in memory. So, whenever a user requests for the new posts for their feed, we can simply serve
        it from the pre-generated, stored location. using this scheme user's newsfeed is not compiled on load, but
        rather on a regular basis and returned to users whenever they request for it.

        Whenever this servers need to generate the feed for a user, they would first query to see what was the last time
        the feed was generated for that user. then new feed data would be generated from that time onwards. We can store
        this data in a hash table, where the 'key' would be userid and 'value' would be a struct like this

            Struct {
                LinkedHashMap<FeedItemID> feedItems;
                DateTime lastGenerated;
            }

        We can store feeditemids in a linked hashmap, which will enable us to not only jump to any feed item but also
        iterate through the map easily. Whenever user want to fetch more feed items, they can send the last feeditemid
        they currently see in their newsfeed, we can then jump to that feeditemid in our linked hash map and return
        next batch / page of feed items from there.

        how many feed items should we store in memory for a user's feed? Initially, we can decide to store 500 feed
        items per user, but this number can ba adjusted later based on teh usage pattern. for example, if we assume that
        one page of user's feed has 20 posted and most of user never browser more than ten page of their feed, we can
        decide to store only 200 posts per user. for any user, who wants to see more posts (more than what is stored in
        memory) we can always query back server.

        Should we generate (and keep in memory) newsfeed for all users? There will be a lot of users that don't login
        frequently. Here are a few things we can do to handle this. A simpler approach could be to use an LRU based
        cache that can remove users from memory that haven't accessed their newsfeed for a long time. A smarter solution
        can figure out the login pattern of users to per-generate their newsfeed, e.g., At what time of the day a user
        is active? Which days of hte week a user accesses their newsfeed? etc.


        Let's new discuss some solution to our 'live updates' problems in the following section.

    b. Feed publishing


"""