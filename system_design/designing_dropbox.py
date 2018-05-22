"""
Designing Dropbox

Let's design a file hosting service like dropbox or google drive. could file stroage enables users to store their data
on remote servers. Usually, these are maintained by could storage providers and made available to users over a network
(typically through the internet). Users pay for their could data storage on a monthly basis.

Similar Services: OneDrive, Google Drive

Difficulty Level: Medium

1. Why could storage?

    Cloud file storage service have become very popular recently as they simplify the storage and exchange of digital
    resources among multiple devices. The shift from using single personal computers to using multiple devices with
    different platforms and operating systems such as smartphones and tables and their portable access from various
    geographical locations at any time is believed to be accountable for the huge popularity of cloud storage services.
    Some of the top benefits of such services are:

    Availability: The motto of coud storage services is to have data availability anywhere anytime. Users can access
    their files /photos from any device whenever and wherever they like.

    Reliability and Durability; Another benefit of cloud storage is that it offers 100% reliability and durability of
    data. Cloud storage ensures that users will never lose their data, by keeping multiple copies of the data stored on
    different geographically located servers.

    Scalability: Users will never have to worry about getting out of storage space, with could storage, you have
    unlimited storage as long as you are ready to pay for it.

    if you havent' used dropbox.com before, we would highly recommend creating an account there and uploading /editing
    a file and also going through different options their service offers. This will help you a lot in understanding
    this chapter better.

2. Requirements and goals of the system

    you should always clarify requirements at the beginning of the interview and should ask questions to find the exact
    scope of the system that the interviewer has in mind.

    What do we wish achieve from a cloud storage system? Here are the top-level requirements for our system:

        1. users should be able to upload and download their files/photos from any device.
        2. users should be able to share files or folders with other users.
        3. our service should support automatic synchronization between devices, i.e., after updating a file on one
        devices, it should get synchronized on all devices.
        4. The system should support storing alrge files up to a GB.
        5. ACIDity is required. Atomicity, Consistency, ISolation and Durability of a file operations should be
        guaranteed.
        6. Our system should support offline editing. users should be able to add / delete / modify files while offline,
        and as soon as they come online, all their changes should be synced to the remote servers and other online
        devices.

    Extended requirements

        - The system should support snapshotting of the data, so that users can go back to any version of the files.

3. Some design considerations

    - We should expect huge read and write volumes.
    - Read to write ratio is expected to be nearly the same.
    - internally, files can be stored in samll parts of chunks (says 4MB), this can provide a lot of benefits e.g. all
    failed operations shall only be retried for smaller part of a file. If user fails to upload a file, then only the
    failing chunk will be retried.
    - We can reduce the amount of date exchange by transferring updated chunks only.
    - By removing duplicate chunks, we can save storage space and bandwidth usage.
    - Keeping a local copy of the metadata (file name, size, etc) with the client can save us a lot of round trips to
    the server.
    - For small changes, clients can intelligently upload the diffs instead of the whole chunk.

4. Capacity Estimation and Constraints

    - Let's assume that we have 500M total users, and 100M daily active users (DAU).
    - Let's assume that on average each user connects from three different devices.
    - On average if a user has 200 files / photos. We will have 100 billion total files.
    - Lets' assume tht average files size is 100 KB, this would give us ten petabytes of total storage.

        100B * 100BK => 10 PB

    - Let's also assume that we will have one million active connections per minutes.

5. High Level Design

    The user will specify a folder as the workspace on their device, Any file / photo / folder placed in this folder
    will be uploaded to the cloud, and whenever a file is modified or deleted, it will be reflected in the same way
    in the cloud storage. The user can specify similar workspaces on all their device and any modification done on one
    device will be propagated to all other devices to have the same view of the workspace everywhere.

    At a high level, we need to store files and their metadata information like File Name, File size, Directory, etc.,
    and who this file is shared with. So, we need some servers that can help the clients to upload/download files to
    cloud storage and some servers that can facilitate updating metadata about files and users. We also need some
    mechanism to notify all clients whenever an update happens so they can synchronize their files.

    As shown in the diagram below, block servers will work with the clients to upload /download files from cloud
    storage, and metadata servers will keep metadata of files updated in a sql or nosql database. Synchronization
    servers will handle the workflow of notifying all clients about different changes for synchronization.

6. Component Design

    let's go through the major components of our system one by one.

    a. Client

        The client application monitors the workspace folder on user's machine and syncs all files/ folders in it with
        the remote cloud storage. The client application will work with the storage servers to upload, download and
        modify actual files to backend cloud storage. The client also interacts with the remote synchronization
        service to handle any file metadata updates e.g. change in the file name, size, modification date. etc.

        Here are some of the essential operations of the clients:

        1. upload and download files.
        2. delete file changes in teh workspace folder.
        3. handle conflict due to offline or concurrent updates.

        how do we handle the transfer efficiently? As mentioned above, we can break each file into smaller chunks so
        that we transfer only those chunks that are modified and not the whole file. Let's say we divide each file
        into fixed size of 4MB chunks. We can statically calculate what could be an optimal chunk size based on:

            1. Storage devices we use in the could to optimize space utilization and input / output operationis per
            seconds (IOPS)
            2. Network bandwidth
            3. Average file size in the storage etc.

        in our metadata, we should also keep a record of each file and the chunks that constitute it.

        should we keep a of metadata with client? keeping a local copy of metadata not only enable use to do offline
        updates but also saves a lot of round trips to update remote metadata.

        how can clients efficiently listen to changes happening on other clients? One solution could be that the client
        periodically check with the server if there are any changes. the problem with this approach is that we will
        have a delay in reflecting changes locally as clients will be checking for changes periodically compared to
        server notifying whenever there is some changes. If the client frequently checks the server for changes, it
        will not only be wasting bandwidth, as the server has to return empty response most of the time but will also
        be keeping the server busy. Pulling information in this manner is not scalable too.

        A solution to above problem could be to use http long polling. With long polling, the client requests
        information from the server with the expectation that the server may not respond immediately. If the server
        has no new data for the client when the poll is received, instead of sending an empty response, the server holds
        the request open and waits for response information to become available. Once it does have new information, the
        server immediately sends an http/s response to the client completing the open http/s request. upon receipt of
        the server response, the client can immediately issue another server request for future updates.

        Based on the above considerations we can divided our client into following four parts:

            1. Internal metadata database will keep track of all the files, chunks, their versions, and their location
            in the file system.

            2. chunker will split hte files into smaller pieces called chunks. It will also be responsible for
            reconstructing a file from tis chunks. Our chunking algorithm will detect the parts of the files tha have
            been modified by the user and only transfer those parts to the cloud storage; this will save us bandwidth
            and synchronization time.

            3. watcher will monitor the local workspace folders and notify the indexer (discussed below) of any action
            performed by the user, e.g. when user screate, delete, or update files or folders. Watcher also listens to
            any changes happening on other clients that are broadcasted by synchronization service.

            4. Indexer will process the events received from the watcher and update the internal metadata database with
            information about the chunks of the modified files. Once teh chunks are successfully submitted / downloaded
            to teh could storage, the idexer will communicate with the remote synchronization service to broadcast
            changes to other clients and update remote database.

            indexer todo

        how should clients handle slow servers? clients should exponentially back-off if the server is busy /not
        responding. Meaning, if a server is too slow to respond, clients should delay their retries, and this delay
        should increase exponentially.

        Should mobile clients sync remote changes immediately? Unlike desktop or web clients, that check for file
        changes on a regular basis, mobile, clients usually sync on demand to save user's bandwidth and space.

    b. metadata database

        The metadata database is responsible for maintaining the versioning and metadata information about files /
        chunks, users, and workspaces. The metadata database can be a relational database such as mySQL, or a nosql
        databse such as dynamodb. Regardless of the type of the database, the synchronization service should be able to
        provide consistent view of the file using a database, especially if more than on user work with the same file
        simultaneously. Since noSQL data stores do not support ACID properties in favor of scalability and performance,
        we need to incorporate the support for ACID properties programmatically in the logic of our synchronization
        services in case we opt for this kind of databases. However, using a relational database can simplify the
        implementation of the synchronization service as they natively support ACID properties.

        ACID todo

        Metadata Database should be storing information about following objects:

            1. chunks
            2. files
            3. user
            4. devices
            5. workspace (sync folder)

    c. Synchronization service

        The synchronization service is the component that processes file updates made by a client and applies changes to
        other subscribed clients. It also synchronizes clients local databases with the information stored in the remote
        Metadata DB. The synchronization service is the most important part of the system architecture due to its
        critical roles in managing the metadata and synchronizing users' files. Desktop clients communicate with the
        synchronization service to either obtain update from teh cloud storage or send files or updates to the cloud
        storage and potentially other users. If a client was offline for period, it polls the system for new updates as
        soon as it becomes online. When the synchronization service receives an update request, it checks with the
        metadta database for consistency and then proceeds with the update. Subsequently, a notification is sent to all
        subscribed user or devices to report the file update.

        The synchronization service should be designed in such a way to transmit less data between clients and the
        cloud storage to achieve better response time. To meet this design goal, the synchronization service can employ
        a differencing algorithm to reduce the amount of the data that needs to be synchronized. Instead of transmitting
        entire files from clients to the server or vice versa, we can just transmit the difference between two versions
        of a file. Therefore, only the part of the file that has been changed is transmitted. This also decrease
        bandwidth consumption and cloud data storage for the end user. As described above we will be dividing our files
        into 4MB chunks and will be transferring modified chunks only. Server and clients can calculate a hash (e.g.,
        SHA-256) to see whether to updte the local copy of a chunk or not. On server if we already have a chunk with a
        similar hash (even from another user) we dont' need to create another copy, we can use the same chunk. This is
        discussed in detail later under data de-duplication.

        To be able to provide an efficient and scalable synchronization protocol we can consider using a communication
        middleware between clients and the synchronization service. The message middleware should provide scalable
        message queuing and change notification to support a high number of clients using pull or push strategies. This
        way, multiple synchronization service instances can receive requests from a global request queue, and the
        communication middleware will be able to balance their load.

    d. Message Queueing Service

        An important part of our architecture is a messaging middleware that should be able to handle a substantial
        number of requests. A scalable message queueing service that supports asynchronous message-based communication
        between clients and the synchronization service instances best fits the requirements of our application. The
        message queuing service supports asynchronous and loosely coupled message-based communication between
        distributed components of the system. The message Queueing service should be able to efficiently store and
        number of messages in a highly available, reliable and scalable queue.

        Message queuing service will implement two types of queues in our system. The request queue is a global queue,
        and all clients will share it. Client's requests to update the metadata database will be sent to the request
        queue first, from there synchronization service will take it to update metadata. The response queues that
        correspond to individual subscribed clients are responsible for delivering the update messages to each client.
        Since a message will be deleted from the queue once received by a client, we need to create separate response
        queues for each subscribed client to share update messages.

        Message queue todo

    e. Cloud/Block Storage

        Cloud / Block storage stores chunks of files uploaded by the users. Clients directly interact with the storage
        to send and receive objects from it. Separation of the metadata from storage enables us to use any storage
        either in cloud or in house.

7. File processing workflow

    The sequence below shows the interaction between the components of the application in a scenario when client A
    updates a file that is shared with client B and C, so they should receive the update too. If the other clients were
    not online at the time of the update, the message queue service keeps the update notifications in separate response
    queues for teh until they become online later.

        1. Client A uploads chunks to cloud storage.
        2. Client A updates metadata and commits changes.
        3. Client A gets confirmation, and notifications are sent to client B and client C about the changes.
        4. Client B and C receive metadata changes and download updated chunks.

8. DAte deduplication

    Data deduplication is a technique for eliminating duplicate copies of data to improve storage utilization. It can
    also be applied to network data transfers to reduce the number fo bytes that must be sent, for each new incoming
    chunk, we can calculate a hash of it and compare that hash with all the hashes of the existing chunks to see if we
    already have some chunk present in our storage.

    We can implement deduplication in two ways in our system:

        a. Post-process deduplication

        with post process deduplication, new chunks are first stored on the storage device, and later some process
        analyzes teh data looking for duplication. The benefits is that clients will not need to wait for the hash
        calculation or lookup to complete before storing the data, thereby ensuring that there is no degradation in
        storage performance. Drawbacks of this approach are:

            1. We will unnecessarily be storing duplicate data, though for a short time.
            2. Duplicate data will be transferred consuming bandwidth.

        b. In-line deduplication

        Alternatively, deduplication hash calculations can be done in real-time as the clients are entering data on
        their device. If our system identifies a chunk which it has already stored, only a reference to the existing
        chunk will be added in the metadata, rather than the full copy of the chunk. This approach will gives us
        optimal network and storage usage.

9. Metadata Partitioning

    To scale out metadata DB, we need to partition it so that it can store information about millions of users and
    billions of files / chunks. We need to come up with a partitioning scheme that would divide and store our date to
    different db servers.

    1. Vertical partitioning: we can partition our database in such a way that we store tables related to one particular
    feature on one server. For example we can store all the user related tables in one database and all files /chunks
    related tables in another database. Although this approach is straightforward to implement it has some issues:

        1. Will we still have scale issues? wht if we have trillions of chunks to be stored and our database connot
        support to store such huge number of records? How would we further partition such tables?

        2. Joining two tables in two separate database can cause performance and consistency issues. How frequently do
        we have to join user and files tables?

    2. Range based partitioning: What if we store files / chunks in separate partitions based on the first letter of
    the file path. So, we save all the files starting with letter 'A' in one partition and those that start with letter
    'B' into another partition and so on. This approach is called ranged based partitioning. We can even combine
    certain less frequently occurring letters into one database partition. We should come up with this partitioning
    scheme statically so that we can always store / find a file in a predictable manner.

    The main problem with this approach is that it can lead to unbalanced servers. For example, if we decide to put all
    files starting with letter 'E' into a DB partition, and later we realize that we have too many files that start with
    letter 'E', to such an extent that we conn't fit them into one DB partition.

    3. Hash-Based partitioning: In this scheme we take a hash of the object we are storing and based on this hash we
    figure out hte db partition to which this object should go. In our case, we can take the hash of the 'FileId' of the
    file object we are storing to determine the partition the file will be stored. Our hashing unction will randomly
    distribute objects into different partitions. e.g., our hashing function can always map any id to an number between
    [1...256], and this number would be the partition we will store our object.

    This approach can still lead to overloaded partitions, which can be solved by using consistent hashing.

10. caching

    We can have two kinds of caches in our system. To deal with hot files/ chunks, we can introduce a cache for block
    storage. We can use an off-the-shelf solution like memcache, that can store whole chunks with their respective
    ids/ hashes, and block servers before hitting block storage can quickly check if the cache has desired chunk. Based
    on clients useage pattern we can determine how many cache server we need. A high-end commercial server can have up
    to 144GB of memory; so one such server can chek 36K chunks.

    Which cache replacement policy would best fit our needs? When the cache is full, and we want to replace a chunk
    with a newer / hotter chunk, how would we choose? least Recently Used (LRU) can be reasonable policy for our system.
    Under this policy, we discard the least recently used chunk first.

    Similarly, we can have a cache for Metadata DB.

11. Load Balancer (LB)

    We can add load balancing layer at two places in our systems:

        1. Between clients and block servers
        2. Between clients and metadata servers.

    Initially, a simple round robin approach can be adopted; that distributes incoming requests equally among backend
    servers. This LB is simple to implement and does not introduce any overhead. another benefit of this approach is
    if a server is dead, LB will take it out of the rotation and will stop sending any traffic to it. A problem with
    round robin LB is, it won't take server load into consideration. If a server is overloaded or slow, the LB will
    not stop sending new requests to that server. To handle this, a more intelligent LB solution can be placed that
    periodically queries backend server about their load and adjusts traffic based on that.

12. Security, permission and file sharing

    One of primary concern users will have while storing their files in the cloud would be the privacy and security of
    their data. Especially since in our system user can share their files with other user or even make them public to
    share it with everyone. To handle this, we will be storing permission of each file in our metadata DB to reflect
    what files are visible or modifiable by any user.
"""
