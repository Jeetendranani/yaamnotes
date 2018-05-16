"""
Lots of people struggle with syste design interview (SDIs) primarily because of:

    1. unstructured nature of SDIs, where you're asked to work on an open-ended design problem that doesn't have a
    standard answer.
    2. Your lack of experience in developing large scales systems and
    3. you're not spend enough time to prepare for SDIs.

Just like coding interviews, candidates who haven't spend time preparing for SDIs mostly perform poorly. This gets
aggravated when you're interviewing at the top companies like Google, Facebook, Uber, etc. In these companies, if a
candidate doesn't perform above average, they have a limited chance to get an offer. On the other hand, a good
performance always results in a better offer (high position and salary), since it reflects your ability to handle
complex systems.

In this course, we'll follow a step by step approach to solve multiple design problems. Here are those seven steps:

Step 1: Requirements clarifications

    Always ask questions to find the exact scope of the problem you're solving. Design questions are mostly open-ended,
    and they dont' have one correct answer, that's why clarifying ambiguities early in the interview become critical.
    candidates who spend enough time to clearly define the end goals of the system, always have a better chance to be
    successful in the interview. Also, since you only have 35-40 minutes to design a large system, you should clarify
    what parts of the system you would be focusing on.

    under each step, we'll try to give examples of different design considerations for developing a twitter-like
    service.

    Here are some questions for designing twitter that should be answered before moving on to next steps:

    - will users of our service be able to post tweets and follow other people?
    - should we also design to create and display user's timeline?
    - will tweets contain photos and videos?
    - are we focusing on backend only or we are developing front-end too?
    - will users be able to search tweets?
    - do we need to display hot trending topics?
    - would there be any push notification for new (or important) tweets

    All such question will determine how our end design will look like.

step 2: System interface definition

    Define what APIs are expected from the system. This would not only establish the exact contract expected from the
    system but would also ensure if you haven't gotten any requirements wrong. Some examples for our twitter-like
    service would be:

Step 3: Back of the envelope estimation

    It's always a good idea to estimate the scale of the system you're going to design. This would also help later when
    you'll be focusing on teh scaling, partitioning, load balancing and caching.

    - what scale is expected from the system (e.g., number of new tweets, number of tweet views, how many timeline
    generations per sec, etc.)?
    - how much storage would we need? we'll have different numbers if users can have photos and videos in their tweets.
    - Waht network bandwidth usage are we expecting? This would be crucial in deciding how would we manage traffic and
    balance load between servers.

step 4: Defining data model

    Defining the data model early will clarify how data will flow among different components of the system. Later, it
    will guide towards data partitioning and management. Candidate should be able to identify various entities of the
    system, how they will interact with each other and different aspect of data management like storage, transportation,
    encryption, etc. Here are some entities for our twitter-like service:

    - user: userid, name, email, dob, creationdate, lastlogin, etc.
    - tweet: tweetid, content, tweetlocation, numberoflikes, timestamp, etc.
    - userfollowos: userid1, userid2
    - favoritetweets: userid, tweetid, timestamp

    which database system should we use? would NoSQL like cassandra best fits our needs, or we should use mySQL-like
    solution. what kind of block storage should we use to store photos and videos?

steps 5: high-level design

    draw a block diagram with 5-6 boxes representing core components of your system. you should identify enough
    components that are needed to solve the actual problem from end to end.

    for twitter, at a high level, we would need multiple application server to serve all read/write requests with load
    balancers in front of them for traffic distributions. If we're assuming that we'll have a lot more read traffic
    (as compared to write), we can decide to have separate servers for handling these scenarios. On the backend, we
    need an efficient databases that can store all the tweets and can support a huge number of reads. We would also
    need a distributed file storage system for storing photos and videos.

steps 6: detailed design

    Dig deeper into 2-3 components; interviewers feedback should always guild you towards which parts of system she
    wants you to explain further. You should be able to provide different approaches, their pros and cons, and why
    would you choose one? Remember there is no single answer, they only thing important is to consider tradeoffs
    between different options while keeping system constraints in mind.

    - Since we'll be storing a huge amount of data, how should we partition our data to distribute it to multiple
    databases? should we try to store all the data of a user on the same database? what issue can it cause?

    - how would we handle hot users, who tweet a lot or follow lots of people?
    - since user's timemline will contain most recent (and relevant) tweets, should we try to store our data in such a
    way that is optimized to scan latest tweets?
    - how much and at which layer should we introduce cache to speed things up?
    - what components need better load balancing?

step 7: identify and resolving bottlenecks

    try to discuss as many bottlenecks as possible and different approaches to mitigate them.

    - Is there any single point of failure in our system? What are we doing to mitigate it?
    - Do we've enough replicas of the data so that if we lose a few servers, we can still serve our users?
    - similarly, do we've enough copies of different services running, such that a few failures will not cause total
    system shutdown?
    - how are we monitoring the performance of our service? do we get alerts whenever critical components fail or
    their performance degrade?

In summary, preparation and being organized during the interview are the keys to be successful in system design
interviews.
"""