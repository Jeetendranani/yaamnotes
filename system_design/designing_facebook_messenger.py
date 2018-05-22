"""
Designing Facebook Messenger

Let's design an instant messaging service like facebook messenger, where user can send text messages to each other
through web and mobile interfaces.

1. What is Facebook Messenger?

    Facebook Messenger is a software application which provides text-based instant messaging service to its users.
    Messenger users can chat with their Facebook Friends both from cell-phone and their website.

2. Requirements and goals of the system.

    Our messenger should meet the following requirements:

    Function requirements:

        1. messenger should support one on one conversations between users.
        2. messenger should keep track of online / offline statues of tis users
        3. messenger should support persistent storage of chat history.

    Non-functional requirements:

        1. user should have real-time chat experience with minimum latency.
        2. our system should be highly consistent; users should be able to see the same chat history on all their
        devices.
        3. messenger's high availability is desirable; we can tolerate lower availability in the interest of
        consistency.

    Extended requirements:

        - Group charts: messenger should support multiple people talking to each other in a group.
        - Push notifications: Messenger should be able to notify users of new messages when they are offline.

3. Capacity Estimation and Constraints

    Let's assume that we have 500 million daily active users and on average each user send 40 messages daily; this
    gives us 20 billion messages per day.

    Storage estimation: let's assume that on average a message is 100 bytes, so to store all the messages for one day
    we would need 2TB of storage.

        20 billion messages * 100 bytes => 2TB /day

    Although Facebook Messenger stores all previous chart history, but just for estimation to save five years of chat
    history, we would need 3.6 petabytes of storage.

        2TB * 365 days * 5 years ~= 3.6 PB

    Other than chat messages, we would also need to store users' information, messages' metadata (id, timestamp, etc).
    Also, above calculations didn't keep data compression and replication in consideration.

    Bandwidth estimation: If our service is getting 2TB of data every day, this will give us 25 MB of incoming data for
    each second.

        2TB / 86400 sec ~= 25 MB/s

    Since each incoming message needs to go out to another user, we will need the same amount of bandwidth 25MB/s for
    both upload and download.

        high level estimates:

        total messages          20 billion per day
        storage for each day    2TB
        storage for 5 years     3.6 PB
        incoming data           25MB/s
        outgoing data           25MB/s

4. High level design

    At a high level, we will need a chat server that would be the central piece orchestrating all the communications
    between users. When a user wants to send a message to another user, they will connect to the chat server and send
    the message to the server; the server then passes that message to the other user and also stores it in the database.

    The detailed workflow would look like this:

        1. user A send a message to user B through the chat server.
        2. The server receives the message and sends an acknowledgment to user A
        3. The server stores the messages in tis database and send teh message to user B
        4. user b receives the message and send the acknowledgment to the server
        5. The server notifies user A that the message has been delivered successfully to user B.

5. Detailed components design

    Let's try to build a simple solution first where everything runs on one server. At teh high level our system needs
    to handle following use cases:

        1. Receive incoming messages and deliver outgoing messages.
        2. Store and retrieve messages from the database.
        3. Keep a record of which user is online or has gone offline and notify all the relevant users about these
        status changes.

    Let's talk about these scenarios one by one:

    a. message handling

        how would we efficiently send/receive messages? To send messages, a user needs to connect to the server and post
        messages for teh other users. To get a message from the server, the user has two options:

        1. pull model: User can periodically ask teh server if there are any new messages for them.
        2. Push model: users can keep a connection open with the server and can depend upon the server to notify them
        whenever there are new message.

        If we go with our first approach, then the server needs to keep track of messages that are still waiting to be
        delivered, and as soon as teh receiving user connects to the server to ask for any new message, the server can
        return all the pending messages. To minimize latency for the user, they have to check the server quite
        frequently, and most of the time they will be getting an empty response if there are no pending message. This
        will waste a lot of resources and does not look like an efficient solution.

        If we go with our second approach, where all the active users keep a connection open with the server, then as
        soon as teh server receives a messages it can immediately pass the message to the intended user. This way, the
        server does not need to keep track of pending messages, and we will have minimum latency, as the messages are
        delivery instantly on the opened connection.

        how will clients maintain an open connection with server? we can use http long polling. In long polling, clients

        long polling todo

        can requests information from the server with the expectation that the server may not respond immediately. If
        the server has no new data fro the client when the poll is received, instead of sending an empty response, the
        server holds the request open and waits for response information to because available. Once it does have new
        information, the server immediately sends the response to the client, completing the open request. upon receipt
        of teh server response, the client can immediately issue another server request for future updates. This gives a
        lot of improvements in latencies, throughputs, and performance. The long polling request can timeout or can
        receive a disconnect from server, in that csae, the client has to open a new request.

        how can server keep track of all opened connection to efficiently redirect messages to the users? The server
        can maintain a hash table, where 'key' would be the userid and 'value' would be the connection object. So
        whenever the server receives a message for a user, it looks up that user in the hash table to find the
        connection object and sends the message on the open request.

        what will happen when the server receives a message for a user who has gone offline? if the receiver has
        disconnected, the server can notify the sender about the delivery failure. If it is a temporary disconnect,
        e.g., the receiver's long-poll request just timed out, then we should expect a reconnect from the user. In that
        case, we can ask the sender to retry sending the message. This retry could be embedded in the client's logic so
        that users dont' have retype the message. The server can also store the message for a while and retry sending
        it once the receiver reconnects.

        how many chat servers we need? Let's plan for 500 million connections at any time. Assuming a modern server can
        handle 500k concurrent connections at any time, we would ned 1k such servers.

        how to know which server holds the connection to which user? We can introduce a software load balancer in front
        of our chat servers; that can map each userid to server to redirect the request.

        how should teh server process a 'deliver message' request? The server needs to do following things upon
        receiving a new message

            1. Store the message in the database
            2. Send the message to the receiver
            3. Send an acknowledgment to the sender.

        The chat server will first find the server that holds the connection for the receiver and pass the message to
        that server to send it to the receiver. The chat server can then send the acknowledgment to the sender; we
        dont' need to wait for storing the message in the database; this can happen in the background. Storing the
        message is discussed in the next section.

        how does the messenger maintain the sequencing of the message? We can store a timestamp with each message, which
        would be the time when teh message is received at the server. But this will still not ensure correct ordering
        of messages for clients. The scenario where the server timestamp connot determine the exact ordering of messages
        would look like this:

            1. user-1 sends a message m1 to the server for use-2.
            2. the server receives m1 at t1
            3. meanwhile, user-2 sends a messages m2 to the server for user-1
            4. the server receives the message m2 at t2, such that t2 > t1.
            5. the server sends message m1 to user-2 and m2 to user-1.

        So user-1 will see m1 first and then m2, whereas user-2 will see m2 first and then m1.

        To resove this, we need to keep a sequence number with every message for each client, this sequence number will
        determine that exact ordering of messages for each user. with this solution, both clients will see a different
        view of message sequence, but this view will be consistent for tehm on all devices.

    b. Storing and retrieving the messages from database

        Whenever the chat server receives a new message, it needs to store it in teh database. To do so, we have two
        options:

            1. Start a separate thread, which will work with the database to store the message.
            2. send an asynchronous request to teh database to store the message.

        We have to keep certain things in mind while designing our database:

            1. how to efficiently work with database connection pool
            2. how to retry failed requests?
            3. where to log those requests that failed even after certain retries?
            4. how to retry these logged requests (that failed after the retry) when issues are resolved?

        which storage system we should use? We need to have a database that can support a very high rate of small
        updates, and also that can fetch a range of records quickly. This is required because we have a huge number of
        small messages that need to be inserted in the database and while querying a user is mostly interested in
        accessing the messages in a sequential manner.

        We cannot user RDBMS like mysql or nosql like mongodb because we cannot afford teh read/write a rwo from the
        database every time a user receives/ sends a message. This will make not only basic operations of our service
        to run with high latency but also create a huge load on databases.

        Both of our requrements can be easily met with a wide-column database solution like HBase. HBase is a

        HBase todo

        column-oriented key-value nosql database that can store multiple values against one key into multiple columns.
        HBase is modeled after google's BitTable and runs on top of Hadoop Distributed File system (HDFS). HBase groups
        data together to store new data in a memory buffer and once the buffer is full, it dumps the data to the disk
        This way of storage not only helps storing a lot of small data quickly but also fetching rows by the key or
        scanning ranges of rows. HBase is also an efficient database to store variable size data, which is also
        required by our service.

        how should clients efficiently fetch data from the server? Clients should paginate while fetching dta from the
        server. page size could be different from different clients, e.g., cell phones have smaller screens, so we need
        lesser number of message / conversations in teh view port.

    c. Managing user's status

        We need to keep track of user's online / offline status and notify all the relevant users whenever a status
        change happens. Since we are maintaining a connection object on the server for all active users, we can easily
        figure out user's current status from this. With 500M active users at any time, if we have to broadcast each
        status change to all teh relevant active users, it will consume a lot of resources. We can do the following
        optimization around this:

            1. whenever a client starts the app, it can pull current status of all users in their friend's list.
            2. Whenever a user sends a message to another user that has gone offline, we can send a failure to the
            sender and update teh status on the client.
            3. Whenever a user comes online, the server can always broadcast that status with a delay of few seconds to
            see if teh user does not go offline immediately.
            4. Client's can pull hte status from the server about those users that are being shown on the user's
            viewport. This should not be frequent operation. As the server is broadcasting the online status of users
            and we can live with the stale offline status of users for a while.
            5. whenever the client starts a new chat with another user, we can pull the status at teh time.

        Design summary: clients will open a connection to the chart server to send a message: the server will then pass
        it to the requested user. All the active users will keep a connection open with the server to receive messages.
        Whenever a new message arrives, the chat server will push it to receiving user on the long pool request.
        Messages can be stored in HBase, which supports quick small updates, and range based searches. The servers can
        broadcast the online status of a user to other relevant users. Clients can pull status updates for users who are
        visible in the client's viewport on a less frequent bases.

6. Data partitioning

    Since we will be storing a lot of data (3.6 PB for five years), we need to distribute it onto multiple database
    servers. Waht would be our partitioning scheme?

    partitioning based on userid: let's assume we partition based on the hash of the userid, so that we can keep all
    messages of a user on the same database. If one DB sharding is 4TB, we will have 3.6PB/4TB ~= 900 shards for five
    year. For simplicity, let's assume we keep 1K shards, so we will find teh sard number by hash(userid) % 1000, and
    then store /retrieve the data from there. This partitioning scheme will also be quick to fetch chat history for any
    user.

    In the beginning, we can start with fewer database servers with multiple partitions on single server. Our hash
    function needs to understand this logical partitioning scheme so that it can map multiple logical partitions on one
    physical server.

    Since we will store an infinite history of messages, we can start with a big number of logical partitions, which
    would be mapped to fewer physical servers, and as our storage demand increases, we can add more physical servers to
    distributed our logical partitions.

    Partitioning based on messagesid: if we store different messages of a user on separated database shard, fetching a
    range of message of a chat would be very slow, so we should not adopt this scheme.

7. Cache

    We can cache a few recent messages (say last 15) in a few recent conversations that are visible in user's viewport
    (say last 15). Since we decided to store all of the user's messages on one shard, cache for a user should
    completely reside on one machine too.

8. Load balancing

    We will need a load balancer in front of our chat servers; that can map userid to a server that holds the
    connection for the user and then direct the request to that server. Similarly, we would need a load balancer for
    our cache servers.

9. Fault tolerance and replication

    What will happen when a chat server fails? Our chat servers are holding connections with the users. If server goes
    down, should we devise a mechanism to transfer those connections to some other servers? it's extremely hard to
    failover TCP connections to other servers; an easier approach can be to have clients automatically reconnect if the
    connection is lost.

    Should we store multiple copies of user messages? We cannot have only one copy of user's data, because if the server
    holdign the data crashes or is down permanently, we don't have any mechanism to recover that data. For this either
    we have to store multiple copies of the data on different servers or use techniques like Reed-Solomon encoding to

    Reed-Solomon todo

    distribute and replicate it.

10 Extended Requirements

    a. Group chat

        We can have separate group-chat objects in our system that can be stored on the cat servers. A group chat object
        is identified by groupchatid and will also maintain a list of people who are part of that chat. Our load
        balancer can direct each group chat message based on groupchatid and server handling that group chat can iterate
        through all the users of the chat to find server handling the connection of each user to deliver the messages.

        In databases, we can store al the group chats in a separate table partitioned based on group chatid.

    b. push notifications

        In our current design user's can only send messages to active users and if the receiving user is offline, we
        send a failure to the sending user. Push notifications will enable our system to send messages to offline users.

        Push notifications only work for mobile clients, each user can optin from their device to get notifications
        whenever there is a new message or event. Each mobile manufacturer maintains a set of servers that handles
        pushing these notifications to the user's device.

        To have push notifications in our system, we should need to set up a notification server, which will take the
        messages for offline users and send them to mobile manufacture's push notification server, which will then
        send them to the user's device.
"""