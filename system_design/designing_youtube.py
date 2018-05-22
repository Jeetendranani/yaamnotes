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


"""