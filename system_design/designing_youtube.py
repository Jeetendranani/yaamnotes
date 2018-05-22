"""
Designing youtube

Let's design a video sharing service like youtube, where users will be able to upload/view/search videos.

Similar servers: vimeo.com, dailymotion.com, veoh.com, netflex.com
Difficulty Level: Medium

1. Why youtube?

    youtube is one of the most popular video sharing websites in the world. users of the service can upload, view, rate
    and report videos as well as add comments on videos.

2. Requirements and goals of the system.

    For teh sake of this exercise, we plan to design a simple version of youtube with following requirements:

    Functional Requirements:

        1. User should be able to upload videos.
        2. user should be able to share an view videos
        3. user can perform searches based on video titles.
        4. Our services should be able to record states of videos, e.g., likes / dislikes, total number of views, etc.
        5. Users should be able to add and view comments on videos.

    Non-functional requirements

        1. The system should be highly reliable, any video uploaded should not be lost
        2. The system should be highly available. consistency can take a hit (in the interest of availability), if a
        user doesn't see a video for a while, it should be fine.
        3. Users should have real time experience while watching videos and should not feel any lag.

    Not in scope: Video recommendation, most popular videos, channels, and subscriptions, watch later, favorites. etc.

3. Capacity Estimation and Constrains

    Let's assume we have 1.5 billion total users, 800 million of whom are daily active users. If, on the average, a user
    views five videos per day, total video views per second would be:

        800M * 5/86400 sec => 46k videos /sec

    Let's assume our upload: view ratio is 1: 200 i.e., for every video upload we have 200 video viewed, giving us
    230 videos uploaded per second.

        46K / 200 => 230 video / sec

    Storage Estimates: Let's assume that every minutes 500 hours worth of videos are uploaded to youtube. If on average,
    one minute of video needs 50MB of storage (videos need to be stored in multiple formats), total storage needed for
    videos uploaded in a minutes would be:

        500 hours * 60 min * 50MB => 1500GB/min (25GB/sec)

    These number are estimated, ignoring video compression and replication, which would change your estimates.

    Bandwidth estimates: With 500 hours of video uploads per minutes, assuming each video upload takes a bandwidth of
    10MB/min, we would be getting 300GB of upload every minute.

        500 hours * 60 mins * 10MB => 300GB /min (5GB/sec)

    Assuming an upload: view ratio of 1:200, we would need 1TB/s outgoing bandwidth.

4. System APIs

    We can have soap or rest apis to expose the functionality of our service. Following could be the definitions of the
    apis for uploading and searching videos:

        uploadVideo(api_dev_key, video_title, vide_description, tags[], category_id)

    Parameters:

        api_dev_key(sting): The api developer key of a registered account. This will be sued to, among other things,
        throttle users based on their allocated quota.

        video_title(string): title of the video

        video_description(string): optional description of the video.

        tags(string): optional tags for the video.

        category_id(string): category of the video, e.g., Film, Song, People, etc.

        default_language(string): For example English, Mandariin, hindi, etc.

        recordign_detaisl(string): Location where the video was recorded.

        video_contents(stream): Video to be uploaded.

    Returns: (string)

    A successful upload will return http 202 (request accepted), and once the video encoding is completed, the user
    is notified through email with a link to access the video. We can also expose a queryable api to let users
    know the current of their uploaded video.

        searchVideo(api_dev_key, search_query, user_location, maximum_videos_to_return)

    Parameters:

        api_dev_key(string): The api developer key of a registered account of our service.
        search_query(string): A string containing the search terms
        user_location(string): optional location of the user performing the search.
        maximum_videos_to_return(number): Maximum umber of results returned in one request.
        page_token(string): This token will specify a page in the result set that should be returned.

    returns: (json)

    A json containing information about the list of video resources matching the search query. Each video resource
    will have a video title, a thumbnail, a video creation date and how many views it has.

5. high level design

    At a high-level we would need following components:

        1. processing queue: each uploaded video will be pushed to a processing queue, to be de-queued later for
        encoding, thumbnail generation, and storage.

        2. encoder: to encode each uploaded video into multiple formats.

        3. Thumbnails generator: we need to have a few thumbnails for each video.

        4. video and thumbnail storage: we need to store video and thumbnail files in some distributed file storage.

        5. user database: we would need some database to store user's information. e.g., name email, address, etc.

        6. video metadata storage: metadata database will store all the information about videos like title, file path
        in the system, uploading user, total views, likes, dislikes, etc. Also, it will be used to store all the video
        comments.

6. database schema

    video metadata storage - mysql

    videos metadata can be stored in my sql database. following information should be stored with each video:

        - videoid
        - title
        - description
        - size
        - thumbnail
        - uploader /user
        - total number of likes
        - total number of dislikes
        - total number of views

    for each video comment, we need to store following information:

        - commentsid
        - videoid
        - usedid
        - comment
        - timeofcreation

    user data storage - my sql

        - userid
        - name
        - email
        - address
        - age
        - registration details

7. Detailed component design

    The service would be read-heavy, so we will focus on building a system that can retrieve videos quickly. We can
    expect our read: write ratio as 200:1, which means for every video uplaod there are 200 videos views.

    where would videos be stored? Videos can be stored in a distributed file storage system like HDFS or GlusterFS

    HDFS todo
    GlusterFS todo

    how should we efficiently manage traffic? We should segregate our read traffic from write. Since we will be having
    multiple copies of each video, we can distribute our read traffic on different servers. For metadata, we can have
    master-slave configurations, where writes will go to master first and then replayed at all the salves. Such
    configurations can cause some staleness in data, e.g. when a new video is added, its metadata would be inserted in
    the master first, and before it gets replayed at teh slave, our slaves would not be able to see it and therefore
    will be returning stale results to the user. this staleness might be acceptable in our system. as it would be very
    short lived and the user will be able to see the new videos after a few milliseconds.

    where would thumbnails be stored? There will be a lot more thumbnails than videos. If we assume that every video
    will have five thumbnails, we ned to have a very efficient storage system that can serve a huge read traffic.
    There will be two consideration before deciding which storage system will be used for thumbnails:

        1. thumbnails are small files, say maximum 5KB each
        2. Read traffic for thumbnails will be huge compared to videos. Users will be watching one video at a time, but
        they might be looking at a page tht has 20 thumbnails of other videos.

    Let's evaluate storing all the thumbnails on disk. Given that we have a huge umber of files; to read these files we
    have to perform a lot of seeks to different locations on the disk. This is quite inefficient and will result in
    higher latencies.

    Bigtable can be a reasonable choice here, as it combines multiple files into one block to store on the disk and is

    bigtable todo

    very efficient in reading a small amount of data. Both of these are the two biggest requirements of our service.
    Keeping hot thumbnails in th cache will also help in improving the latencies and given that thumbnails files are
    smaller in size, we can easily cache a large number of such files in memory.

    Video uploads: Since videos could be huge, if while uploading, the connection drops, we should support resuming
    from the same point.

    video encoding: newly uploaded videos are stored on the server, and a new task is added to hte processing queue to
    encoding the video into multiple formats. Once all the encoding is completed; uploader is notified, and video is
    made available for view/sharing.

8. Metadata sharding

    Since we have a huge number of new videos every day and our read load is extremely high too, we need to distribute
    our data onto multiple machines so that we can perform read/ write operations efficiently. We have many options to
    shard our data. Let's go through different strategies of sharding this data one by one:

    sharding based on userid: we can try storing all the data for a particular user on one server. While storing, we can
    pass the userid to our hash function which will map the user to a database server where we will store all the
    metadata for that user's videos, while querying for videos of a user, we can ask our hash function to find the
    server holding user's data and then read it from there. To search videos by titles, we will have to query all
    servers, and each server will return a set of videos. A centralized server will then aggregate and rank these
    results before returning them to the user.

    This approach as coupe of issues:

        1. What if a user becomes popular? there could be a lot of queries on the server holding that user, creating a
        performance bottleneck. this will affect the overall performance of our service.

        2. Over time, some users can end up storing a lot of videos compared to other. maintaining a uniform
        distribution of growing user's data is quite diffecult.

    The recover from these situations either we have to repartition /redistribution our data or user consistent hashing
    to balance the load between servers.

    Sharding bases on videoid: Our hash function will map each videoid to random server where we will store that video's
    metadata. To find videos of a user we will query all server, and each server willreturn a set of videos. A
    centralized server will aggregate and rank these results before returning them to hte user. The approach solver our
    problem of popular user but shifts it to popular videos.

    We can further improve our performance by introducing cache to store hot videos in front of the database servers.

9. Video Deduplication

    With a huge number of users, uploading a massive amount of video data, our service will have to deal with widespread
    video duplication. Duplicate videos often differ in aspect ratios or encodings, can contains overlays or additional
    borders, or can be expects form a longer, original video. the proliferation of duplicate videos can have an impact
    on many levels:

        1. Data storage: We could be wasting storage space by keeping multiple copies of the same video.
        2. Caching: duplicate videos would result in degraded cache efficiency by taking up space that could be used
        for unique content.
        3. Network usage: Increasing the amount of dta that must be send over the network to in-network caching systems.
        4. Energy consumption: Higher storage, inefficient cache, and network usage will result in energy wastage.

    For the end user, these inefficiencies will be realized in the form duplicate search results, longer video startup
    times, and interrupted streaming.

    for our service, deduplication makes most sense early, when a user is uploading a video; as compared to
    post-processing it to find duplicate videos later. Inline deduplication will save us a lot of resources that can be
    used to encode, transfer and store the duplicate copy of the video. As soon as any user starts uploading a video,
    our service can run video matching algorithms (e.g., Block Matching, Phase correlation, etc.) to find duplications,

    Block Matching todo
    Phase correlation todo

    if we already have a copy of the video being uploaded, we can either stop the upload and use the existing copy or
    the newly uploaded video if ti is of higher quality. If the newly uploaded video is a subpart of an existing video
    or vice versa, we can intelligently divide the video into small chunks, so that we only upload those parts that are
    missing.

10. Load Balancing

    We should use consistent hashing among our cache servers, which will also help in balancing the load between cache
    servers. Since we will be using a static hash-based scheme to map videos to hostnames, it can lead to uneven load
    on the logical replicas due to hte different popularity for each video. For instance, if a video becomes popular,
    the logical replica corresponding to that video will experience more traffic than other servers. These uneven loads
    for logical replicas can then translate into uneven load distribution on corresponding physical servers. To resolve
    this issue, any busy server in one location can redirect a client to a less busy server in the same cache location.
    We can use dynamic http redirection for this scenario.

    dynamic http redirection todo

    however, the use of redirections also has its drawbacks. First, since our service tries to load balance locally, it
    leads to multiple redirections if the host that receives the redirection can't serve the video. Also each
    redirection requires a client to make an additional http request; it also leads to higher delays before the video
    starts playing back. Moreover, intertier (or cross data-center) redirections lead a client to a distant cache
    location because the higher tier caches are only present at a small number of locations.

11. Cache

    To serve globally distributed users, our service needs a massive-scale video delivery system. Our service should
    push its content closer to the user using a large number of geographically distributed video cache servers. We need
    to have a strategy that would maximize user performance and also evenly distributes the load on its cache server.

    We can introduce a cache for metadata servers to cache hot database rows, using memcache to cache the data and
    application servers before hitting database can quickly check if the cache has the desired rows. Least recently
    used (LRU) can be a reasonable cache eviction policy for our system. Under this policy, we discard the least
    recently viewed row first.

    how can we build more intelligent cache? If we go with 80-20 rule, i.e., 20% of daily read volume for video is
    generating 80% of traffic, meaning that certain videos are so popular that the majority of people view them; It
    follows that we can try caching 20% of daily read volume of videos and metadata.

12. Content delivery network (CDN)

    A CDN is a system of distributed servers that deliver web content to a user based on the geographic locations of
    teh user, the origin of the web page and a content delivery server. Take a look at 'CDN' section in our caching
    chapter.

    CDN todo

    Our service can move most popular videos to CDNs:

        - CDNs replicate content in multiple places. There's a better chance of videos being closer to the user and with
        fewer hops, videos will stream from a friendlier network.

        - CDN machines make heavy use of caching and can mostly serve videos out of memory.

    Less popular videos (1-20 views per day) that are not cached by CDNs can be served by our servers in various data
    centers.

13. Fault Tolerance

    We should use consistent hashing for distribution among database servers. Consistent hashing will not only help in
    replacing a dead server but also helpl in distributing load among servers.
"""