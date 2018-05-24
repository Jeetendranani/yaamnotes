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


"""