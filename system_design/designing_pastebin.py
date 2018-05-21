"""
Designing Pastebin

Let's design a Pastebin like web service, where users can store plan text. Users of the service will enter a piece of
text and get a randomly generated url to access it.

Similar services: pasted.co, hastebin.com, chopapp.com
Difficulty Level: Easy

1. What is Pastebin?

    Pastebin like service enable users to store plain text or images over the network (typically the internet) and
    generate unique urls to access the uploaded data such service are also used to share data over the network quickly,
    as users would just need to pass the url to let other users see it.

2. Requirements and Goals of the system

    Our pastebin service should meet the following requirements:

    Functional requirements:

        1. Users should be able to uploaad or "paste" there data and get a unique URL to access it.
        2. Users will only be able to upload text.
        3. Data and links will expire after a specific timespan automatically; users should also to be able to specify
        expiration time.
        4. Users should optionally be able to pick a custom alias for their paste.

    Non-functional Requirements:

        1. The system should be highly reliable, and data uploaded should not be lost.
        2. The system should be highly available. This is required because if our service is down, users will not be
        able to access there pasters.
        3. Users should be able to access there pastes in real-time with minimum latency.
        4. Paste links should not be guessable (not predictable).

    Extend requirements:

        1. Analytics, e.g., how many times a redirection happened?
        2. Our service should also be accessible through Rest APIs by other services.

3. Some design considerations

    Pastebin shares some requirements with url shortening service, but there are some additional design considerations
    we should keep in mind.

    What should be the limit on the amount of text user can paste at a time? We can limit users not to have Pastes
    bigger than 10MB to stop teh abuse of the service.

    Should we impose size limits on custom urls? Since our service supports custom urls, user can pick any url that
    they like, but providing a custom url is not mandatory. However, it is reasonable (and often desirable) to impose a
    size limit on custom urls, so that we have a consistent url databases.

4. Capacity Estimation and Constrains

    Our services would be read heavy; there will be more read requests compared to new pastes creation. We can assume
    5:1 ratio between read and write.

    Traffic estimates: Pastebin services are not expected to have traffic similar to Twitter or Facebook, le'ts assume
    here that we get one million new pastes added to our system every day. This leaves us with five million reads per
    day.

    New pastes per second:

        1M/(24hours * 3600seconds) ~= 12 pastes/sec

    Paste reads per second:

        5M / (24 hours * 3600 seconds) ~= 58 reads/sec

    Storage estimates: User can upload maximum 10MB of data; commonly Pastebin like services are used to share source
    code, configs or logs. Such test are not huge, so lets' assume that each paste on average contains 10KB.

    At this rate, will will be storing 10GB of data per day.

        1M * 10KB => 10 GB/day

    if we want to store this data for ten years, we would need the total storage capacity of 36TB.

    With 1M pastes every day we will have 3.6 billion pastes in 10 years. We need to generate and store keys to uniquely
    identify these pastes. If we base64 encoding ([A-Z, a-z, 0-9, -, .]) we would need six letters strings:

        64 ^ 6 = 68.7 billion unique strings

    If it takes one byte to shore one character, total size required to store 3.6B keys would be:

        3.6B * 6 => 22GB

    22GB is negligible compared to 36TB. To keep some margin, will will assume a 70% capacity model (meaning we don't
    want to user more than 70% of our total storage capacity at any point), which raise our storage needs up to 47TB.

    Bandwidth estimates: For write requests, we expect 12 new pastes per second, resulting in 120KB of ingress per
    seconds.

        12 * 10KB => 120 KB/s

    as for read request, we expect 58 requests per second. Therefore, total data egress (send to users) will be
    0.6 MB/s.

        58 * 10KB => 0.6 MB/s

    Although total ingress and egress are not big, we should keep these numbers in mind while designing our service.

    Memory estimates: We can cache some of the hot pastes that are frequently accessed. Following 80-30 rule, meaning
    20% hot pastes generate 80% traffic, we would like to cache these 20% pastes.

    Since we have 5M read requests per day, to cache 20% of these requests, we would need:

        0.2 * 5M ( 10KB ~= 10GB

5. System APIs

    We can have sopa or rest APIs to expose the functionality of our service. Following could be the definitions of the
    APIs to create/retrieve/delete Pastes:

        addPaste(api_dev_key, paste_data, custom_url=None user_name=None, paste_name

        Parameters:

            api_dev_key(string): The API developer key of a registered account. This will be used to, among other
            things, throttle users based on their allocated quota.
            past_data(string): Textual data of the paste.
            custom_url(string): Optional custom url.
            user_name(string): Optional user name to be used to generate url.
            paste_name(string): Optional name of the paste.
            expire_data(string): Optional expiration date for the paste.

        Returns(String):

        A successful insertion returns the url through which the paste can be accessed, otherwise, returns an error
        code.

        Similarly, we can have retrieve and delete and paste apis:

            getPaste(api_dev_key, api_paste_key)

        Where "pai_paste_key" is a string representing the paste key of the paste to be retrieved. This API will return
        the textual data of the paste.

            deletePaste(api_dev_key, api_paste_key)

        A successful deletion returns 'true', otherwise returns 'false'.

6. Database design

    A few observations about nature of the data we are going to store:

        1. We need to store billions of records.
        2. Each metadata object we are going to store would be small (less than 100 bytes).
        3. Each paste object we are storing can be of medium size (it can be a few MB).
        4. There are no relationships between records, except if we want to store which user created what paste.
        5. Our service is read heavy.

    Database schema:

    We would need two tables, one for storing information about the pastes and the other for users' data.

        paste table
        pk  hash: varchar(16)
            originalurl: varchar(512)
            contentpath: varchar(512)
            expirationdate: datetime
            userid:int
            creationdate: datetime

        user table
        pk  userid: int
            name: varchar(20)
            email:varchar(32)
            creationdate: datetime
            lastlogin: datetime

7. High level design

    At a high level, we need an application layer that will serve all the read and write requests. Application layer
    will talk to a storage layer to store and retrieve data. We can segregate our storage layer with one database
    storing metadata related to each paste, users, etc. While the otehr storing paste contents in some sort of block
    storage or database. This division of date will allow us to scale them individually.

8. Component design

    a. Application layer

        Our application latyer will process all incoming and outgoing requests. The application servers will be talking
        to the backend data store components to server the requests.

        how to handle a write request? Upon receiving a write request, our application server will generate a six-letter
        random string, which would serer as the key of the paste (if the user has not provided a custom key). The
        application server will then store the contents of the paste and the generated key in teh database. After here
        could be that teh insertion fails because of a duplicate key. Since we are generating a random key, there is a
        possibility that the newly generated key could match an existing one. In that case, we should regenerate a new
        key and try agian. We should keep retrying until we dont' see a failure due to the duplicate key. We should
        return an error to the user if the custom key they have provided is already present in our database.

        Another solution of the above problem could be to run a standalone Key Generation Service (KGS) that generate
        random six letter strings beforehand and stores them in database (let's call it key-db). Whenever we want to
        store a new paste, we will just take one of the already generated keys and use it. This approach will make
        thins quite simple and fast since we will not be worrying about duplications or collisions. KGS will make sure
        all the keys inserted in key-db are unique. KGS can use two tables to store keys, one for key that are not used
        yet and one for all the used keys. As soon as KGS give some keys to any application server, it can move these
        to the used keys table. KGS can always keep some keys in memory so that whenever a server needs them, it can
        quickly provide them. As soon as KGS loads some keys in memory, it can move them to used keys table, this way
        we can make sure each server gets unique keys. If KGS dies before using all the keys loaded in memory, we will
        be wasting those keys. We can ignore these keys given a huge number of keys we have.

        isn't KGS single point of failure? Yes, it is. To solve this, we can have a standby replica of KGS, and whenever
        the primary server dies, it can take over to generate and provides keys.

        can each app server cache some keys from key-db? Yes, can surely speed things up. Although in this case, if
        application server dies before consuming all the keys, we will end up losing those keys. This could be
        acceptable since we have 68B unique six letters keys, which are a lot more than we require.

        How to handle a paste read request? Upon receiving a read paste request, the application service layer contacts
        the datastore. The datastore searches for the key, and if it is found, return the paste's contents. Otherwise,
        an error code is returned.

    b. Datastore layer

        We can divide our datastore layer into two:

        1. Metadata database: we can use a relational database like mysql or distributed key-value store like dynamo
        or cassandra.

        2. Block storage: we can store our contents in a block storage that could be distributed file storage or an
        sql-like database. Whenever we feel like hitting our full capacity on content storage, we can easily increase
        it by adding more servers.

9. Purging or DB Cleanup

10. Data partitioning and replication

11. cache and load balancer

12. security and permissions


"""