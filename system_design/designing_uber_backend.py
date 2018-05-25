"""
Designing uber backend

Let's design a ride-sharing service like uber, which connects passengers who need a ride with drivers who have a car.

Similar Service: Lyft, Didi, Via, Sidecar etc.

Difficulty level: Hard

Prerequisite: Designing Yelp

1. What is uber?

    Uber enables its customers to book drivers for taxi rides. uber drivers use their personal cars to drive customers
    around. both customers and drivers communicate with each other through their smartphones using uber app.

2. requirements and goals of the system

    Let's start with building a simpler version of Uber.

    There are two kinds of users in our system 1. Drivers 2. customers.

        - Drivers need to regularly notify the service about their current location and their availability to pick
        passengers.

        - passengers get to see all the nearby available drivers.

        - customer can request a ride; nearby drivers are notified that a customer is ready to be picked up.

        - Once a driver and customer accept a ride, they can constantly see each other's current location, until the
        trip finishes.

        - upon reaching the destination, the driver marks teh journey complete to become available for the next ride.

3. Capacity Estimation and Constraints

    - Let's assume we have 300M customer and 1M drivers, with 1M daily active customers and 500K daily active drivers.
    - Let's assume 1M daily rides.
    - Let's asssume that all active drivers notify their current location every three seconds.
    - Once a custmer puts a request for a ride, the system should be able to contact drivers in real-time.

4. Basic System design and algorithm

    We will take th solution discussed in Designing yelp and modify it to make it work for above-mentioned 'uber' use
    cases. The biggest difference we have is that our QuadTree was not bult keeping in mind that there will be frequent
    updates to it. So, we have two issues with our dynamic grid solution:

        - since all active drivers are reporting their locations every three seconds, we need to update our data
        structures to reflect that. If we have to update the quadtree for every changes in the driver's position, it
        will take a lot of time and resources. To update a driver to its new location, we must find the right grid
        based on the drivers' previous location. If the new position does not belong to the current grid, we have to
        remove the driver from the current grid and move /reinsert the user to the current grid. After this move, if
        the new grid reaches the maximum limit of drivers, we have to repartition it.

        - We need to have a quick mechanism to propagate current location of all the nearby drivers to any active
        customer in that data. Also, when a ride is in progress, our system needs to notify both driver and passenger
        about the current location of the car.

    Although our quadtree helps us find neaby driver quickly, a fast update in the tree is not guaranteed.

    do we need to modify our quadtree every time a driver reorts their location? If we dont update our quadtree with
    every update from the driver, it will have some old data and will not refect the current location of driers
    correctly. If you recall, our purpose of building the quadtree was to find nearby drivers (or places) efficiently.
    since all active drivers report their location every three seconds, hence there wil be lot more updates happening
    to our tree than querying for nearby drivers. So what if we keep teh latest position reported by all drivers in a
    hash table and update our quadtree a little less frequent? Let's assume we guarantee that a driver's current
    location will be reflected in the quadtree within 15 seconds. Meanwhile, we will maintain a hash table that will
    store the current location reported by drivers; let's call this driver location ht.

    how much memory we need for driverlocatinht? We need to tore dirverid, their present and old location in the hash
    table. So we need total 35 bytes to store one record:
        1. Driverid (3bytes - 1 million drivers)
        2. old latitude (8 bytes)
        3. old longitude (8 bytes)
        4. new latitude (8 bytes)
        5. new longitude (8 bytes)
        total = 35 bytes

    If we have 1 million total drivers, we need the following memory (ignoring hash table overhead):

        1 million * 35 bytes => 35 MB

    How much bandwidth our service will consume to receive location updates from all drivers? If we get DriverId and
    their location, it will be (3 + 16 => 19bytes). If we receive this information every three seconds from one million
    drivers, we will be getting 19MB per three seconds.

    Do we need to distribute driverlocationht onto multiple servers? Although our memory and bandwidth requirements do
    not dictate that, since all this information can easily fit on one server, but for scalability, performance, and
    fault tolerance we should distribute teh hash table onto multiple servers. We can distribute based on the driverid
    to make the distribution completely random. Let's call teh machine holding driverhocationht, driver location server.
    Other than storing driver's location, each of these servers will do two things:

        1. As soon as teh serer receives an update fro a drivers' location, they will broadcast that information to all
        the interested customers.

        2. The server needs to notify respective QuadTree server to refresh the driver's location. As discussed above,
        this can happen every 10 seconds.

    How can we efficiently broadcast driver's location to customers? We can have a push model, where the server will
    push the positions to all teh relevant users. We can have a dedicated Notification server that can broadcast the
    current location of drivers to all the interesting customers. We can build our Notification service on publisher/
    subscriber model. When a customer opens the uber app on their cell phone, they query teh server to find nearby
    dirvers. On th server side, before returning the list of drivers to the customer, we will subscribe the customer
    for all the updates from those drivers. We can maintain a list of customers (subscribers) interested in knowing
    the location of a driver and whenever we have an update in driverlocationht for that driver, we can broadcast the
    current location of the driver to all subscribed customers. This way our system makes sure that we always show
    driver's current position to the customer.

    how much memory we need to store all these subscriptions? As we have estimated above we will have 1M daily active
    customers and 500K daily active drivers. On the average let's assume that five customers subscribe one driver. Let's
    assume we store all this information in a hash table so that we can update it efficiently. We need to store driver
    and customer ids to maintain the subscriptions. Assuming we will need 3 bytes for driverid and 8 bytes for
    customerid, we will ned 21MB of memory.

        (500K * 3) + (500K * 5 * 8) ~= 21 MB

    how much bandwidth we need to broadcast the driver's location to customers? For every active driver we have five
    subscribers, so total subscribers we have:

        5 * 500 K => 2.5M

    To all these customers we need to send driverid (3 bytes) and their location (16 bytes) every second, so we need
    the following bandwidth:

        2.5M * 19 bytes => 47.5 MB/s

    how can we efficiently implement Notification service? We can either use http long polling or push notifications.

    how the new publishers / drivers will get added for a current customer? As we have proposed above that customers
    will be subscribed to nearby drivers when they open the uber app for the first time, what will happen when a new
    driver enters teh area the customer is looking at? To add a new customer / driver subscription dynamically, we need
    to keep track of the area the customer is watching. This will make our solution complicated, what if instead of
    pushing this information, clients pull it from the server?

    how about if clients pull information about nearby dirvers from the server? clients can send their current location,
    and the server will find all the nearby drivers form the quadtree to return them to the client. Upon receiving this
    information, the client can update their screen to reflect current positions of the drivers. Clients can query
    every five seconds to limit the number of round trips to teh server. This solution looks quite simpler compared
    to the push model described above.

    Do we need to repartition a grid as soon as it reaches maximum limit? we can have a cushion to let each grid grow
    a little bigger beyond the limit before we decide to partition it. Let's say our grids can grow / shrink extra 10%
    before we partition / merge them. This should decrease the load for grid partition or merge on high traffic grids.

    how would "request ride" use case work?

    1. The customer will put a request for a ride.
    2. one of the aggregator servers will take the request and asks quadtree servers to return nearby drivers.
    3. The aggregator server collects all teh results and sort them by ratings.
    4. The aggregator server will send a notification to the top (say three) drivers simultaneously, whichever driver
    accepts the request first will be assigned the ride. the other drivers will receive a cancellation request. if none
    of the three drivers respond, teh aggregator will request a ride from the next three driers from the list.
    5. once a driver accepts a request, the customer is notified.

5. Fault Tolerance and Replication

    what if a driver location server or notification server dies? We would need replicas of these servers, so that if
    the primary dies the secondary can take control. Also, we can store this data in some persistent storage like ssds
    that can provide fast ios; this will ensure that if both primary and secondary servers die we can recover the data
    from teh persistent storage.

6. Ranking

    How about if we want to rank the search results not just by proximity but also by popularity or relevance?

    how can we return top rated drivers within a given radius? Let's assume we keep track of the overall ratings of each
    driver in our database and quadtree. An aggregated number can represent this popularity in our system, e.g., how
    many stars a driver gets our of tem? While searching for top 10 drivers with a given radius, we can ask each
    partition of quadtree to return top 10 drivers with maximum rating. The aggregator server can them determine top
    10 drivers among all teh drivers returned by different partitions.

7. Advanced Issues

    1. How to handle clients on slow and disconnecting networks?
    2. What if a client gets disconnected when it was a part of a ride? how will we handle billing in such a scenario?
    3. How about if clients pull all the information as compared to server always pushing it?
"""