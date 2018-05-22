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


"""