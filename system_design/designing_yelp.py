"""
Designing yelp

Let's design a yelp like service, where users can search for nearby places like restaurants, theaters or shopping malls,
etc., and can also add / view reviews of places.

Similar Services: Proximity server.

Difficulty Level: Hard

1. Why yelp or proximity server?

    Proximity servers are used to discover nearby attractions like places, events, etc. If you haven't used yelp.com
    before, please try it before proceeding. you can search for nearby restaurants, theaters, etc., and spend some time
    understanding different options the website offers. This will help you a lot in understanding this chapter better.

2. Requirements and goals fo the system.

    What do we wish to achieve from a yelp like service? Our service will be storing information about different places
    so that users can perform a search on them. upon querying, out service will  return a list of places around the
    user.

    Our yelp-like service should met the following requirements:

    Functional requirements:

        1. user should be able to add /delete /update places.
        2. Given their location (longitude / latitude), users should be able to find all nearby places within a given
        radios.
        3. users should be able to add feedback / review about a place. The feedback can have pictures, text, and
        rating.

    Non-functional requirements:

        1. users should have real-time search experience with minimum latency.
        2. Our service should support a heavy search load. There will be a lot of search requests compared to adding a
        new place.
3. Scale Estimation

    Let's build our system assuming that we have 500M places and 100K queries per seconds (QPS). let's also assume a
    20% growth in the number of places and QPS each year.


4. Each location can have following fields:

    1. Locationid (8 bytes): uniquely identifies a location.
    2. Name (256 bytes)
    3. Latitude (8bytes)
    4. (Longitude (8bytes)
    5. Description (512bytes)
    6. Category (1 byte): E.g., coffee shop, restaurant, theater, etc.

    Although a four bytes number can uniquely identify 500M locations, with future growth in mind, we will go with 8
    bytes for location.

    Total size: 8 + 256 + 8 + 8 + 512 + 1 => 793 bytes.

    We also need to store reviews, photos, and ratings fo a place, we can have a separate table to store reviews for
    Places:

        1. LocationID (8 bytes)
        2. ReviewID (4 bytes): uniquely identifies a review, assuming any location will not have more than 2^32 reviews.
        3. ReviewText9512bytes)
        4. Rating(1 byte): how many stars a place get our of ten.

    Similarly, we can have a separate table to store photos for Places and Reviews.

5. System apis.

    We can have soap or rest apis to expose the functionality of our service. Following could be teh definition of the
    api for searching:

        search(api_dev_key, search_terms, user_location, radius_filter, maximum_result category_filter, sort,
        page_token)

    parameters:

        api_dev_key (string): The API developer key of a registered account. This will be used to, among other things,
        throttle users based on their allocated quota.

        search_terms (string): A string containing the search terms.

        user_location (string): Location of the user performing the search.

        radius_filter (number): optional search radius in meters.

        maximum_results_to_return (number): Number of business results to return.

        category_filter (string): Optional category to filter search results with, e.g., restaurants, shopping centers.

        sort (number): optional sort mode: Best matched (0 - default), minimum distance (1), highest rated (2).

        page-token (string): This token will specify a page in the result set that should be returned.

    returns: (Json)

        A Json containing information about a list of businesses matching the search query. Each result entry will have
        the business name, address, category, rating, and thumbnail.

6. basic system design and algorithm

    At a high level, we need to store and index each dataset described above (places, reviews, etc.) for users to query
    this massive database, the indexing should be read efficient, since while searching for nearby places users expect
    to see the results in real-time.

    Given that the location of a place doesn't change that often, we don't need to worry about frequent updates of
    the data. As a contrast, if we intend to build a service where objects do change their location frequently, e.g.,
    people or taxis, then we might come up with a very different design.

    Let's see want are different ways to store this data and find out which method will suit best for our use cases:

    a. SQL solution

        One simple solution could be to store all the data in a database like mysql. EAch place will be stored in a
        separate row, uniquely identified by locationid. Each place will have its longitude and latitude stored
        separately in two different columns, and to perform a fast search; we should have indexes on both these fields.

        To find all the nearby places of a given location (x, y) within a radius 'D', we can query like this:

        Select * from places where latitude between x-d and x+d and longitude between y-d and y+d

        how efficient this query would be? We have estimated 500M places to be stored in our service, Since we have two
        separated indexes, each index can return a huge list of places, and performing an intersection on those two list
        won't be efficient. Another way to look at this problem is that there could be too many location between x-d and
         x+d and similarly between y-d and y+d. if we can somehow shorten these lists, it can improve the performance
         of our query.

    b. Grids

        We can divide the whole map into smaller grids to group locations into smaller sets, each grid will store all
        the places residing with in a certain range of longitude and latitude. This scheme would enable us to query a
        few grids to find nearby places. Based on given location and radius, we can find all teh nearby grids and then
        only query these grids to find nearby places.

        Let's assume that gridid (a four bytes number) would uniquely identify grids in our system.

        what could be a reasonable grid size? Grid size could be equal to teh distance we would like to query since we
        also want to reduce the number of grids. If the grid size is equal to the distance we want to query, then we
        only need to search within the grid which contains the given location and neighboring eight grids. Since our
        grids would be statically defined (from the fixed grids size), we can easily find the grid number of any
        location (lat, long) and its neighboring grids.

        In the database, we can store the gridid with each location and have an index on it too for faster searching.
        Now, our query will look like:

            select * from paces where latitude between x-d and x_d and longitude between y-d and y+d and gridid in (
            gridid, gridid1, gridid2, gridid3, gridid4, ... gridid8)

        This will undoubtedly improve the runtime of our query.

        should we keep our index in memory? Maintaining the index in memory will improve the performance of our service.
        We can keep our index in a hash table, where 'key' would be the grid number and 'value' would be the list of
        places contained in that grid.

        how much memory will we need to store the index? Let's assume our search radius is 10 miles given that total
        area of the earch is around 200 million square miles; we will have 200 millions grids. We would need a four
        bytes number to uniquely identify each grid, and since locationid is 8bytes, therefore we would need 4GB of
        memory (ignoring hash table overhead) to store the index.

            (4 * 20 M) + (8 * 500M) ~= 4GB

        This solution can still run slow for those grids that have a lot of places since our places re not uniformly
        distributed among grids. We can have a thickly dense area a lot of places, and on the other hand, we can have
        areas which are sparsely populated.

        This problem can be solved if we can dynamically adjust our grid size, such that whenever we have a grid with
        a lot of places we break it down to create smaller grids. One challenge with this approach could be, how
        would we map this grids to locations? Also how can we find all the neighboring grids of grid?

    c. Dynamic size grids

        Let's assume we don't want to have more than 500 places in a grid so that we can have a faster searching. So,
        whenever a grid reaches this limit, we break it down into for grids of equal size and distributed places among
        them. This means thickly populated areas like downtown san francisco will have a lot of grids, and sparsely
        populated area like the pacific ocean will have large grids with places only around the coastal lines.

        what data-structure can hold this information? A tree in which each node has four children can serve our
        purpose. Each node will represent a grid and will contain information about all teh places in that grid. If a
        node reaches our limit of 500 places, we will break it down to create four child nodes under it and distribute
        places among them. In this way, all teh leaf nodes will represent teh grids that cannot be further broken down.
        So leaf nodes will keep a list of paces with them. This is tree structure in which each node can have four
        children is called a QuadTree. todo

        how will we build QuadTree? We will start with one node that would represent the whole world in one grid. Since
        it will have more thant 500 locations, we will break it down into four nodes and distribute locations among
        them. we will keep repeating this process with each child node until there are no nodes left with more than 500
        locations.

        How will we find the grid for a given location? We will start with the root node and search downward to find
        our required node /grid. At each step, we will see if the current node we are visiting has children if it has
        we will move to the child node that contains our desired location and repeat this process. If the node does not
        have any children, then that is our desired node.

        how will we find neighboring grids of a given grid? Since only leaf nods contain a list of locations, we can
        connect all leaf nodes with a doubly linked list. this way we can iterate forward or backward among the
        neighboring leaf nodes to find out our desired locations. Another approach for finding adjacent grids would be
        through parent nodes. We can keep a pointer in each node to access its parent, and since each parent node has
        pointers to all of its children, we can easily find siblings of a node. We can keep expanding our search for
        neighboring grids by going up through the parent pointers.

        Once we have nearby locationids, we can query backend database to find details about those places.

        what will be the search workflow? We will first find the node that contains the user's location. If that node
        has enough desired places, we can return them to the user. If not, we will keep expanding neighboring nodes
        (either through the parent pointer or doubly linked list), until either we find the required number of places
        or exhaust our search based on the maximum radius.

        how much memory will be needed to store the quardtree? for each place, if we cache only locationid and lot/long,
        we would need 12GB to store all places.

            24 * 500M => 12GB

        Since each grid can have maximum 500 places and we have 500M locations, how many total grids we will have?

            500M / 500 => 1M grids

        So, total memory required to hold the whole QuadTree would be 12.01GB. this can easily fit into a modern-day
        server.

        how would we insert a new place into our system? Whenever a new place is added by a user, we need to insert it
        into the database, as well as, in the quadtree. If our tree resides on one server, it is easy to add a new
        place, but if th Quadtree is distributed among different server, first we need to find the grid / server of the
        new place and then add it there. (discussed in the nest section).

7. Data partitioning

    What is we have a huge number of places such that, our index does not fit into a single machine's memory? with 20%
    growth, each year, we will reach the memory limit of the server in the future. Also, what if one server cannot
    serve the desired read traffic? To resolve these issues, we must partition our QuadTree!

    We will explore two solutions here (both of these partitioning schemes can be applied to database too.

    a. Shardign based on regions: We can divide our places into regions (like zip codes), such that all places belong to
    a region will be stored on a fixed node. While storing, we will find the region of each place to find the server
    and store the place there. Similarly, while querying for nearby places, we can ask the region server that contains
    user's location. This approach has a couple of issues:

        1. What if a region becomes hot? There would be a lot of queries on the server holding that region, making it
        perform slow. This will affect the performance of our service.

        2. Over time some regions can end up storing a lot of places compared to others. Hence maintaining a uniform
        distribution of places, while regions are growing, is quite difficult.

    To recover from these situations either we have to repartition our data or use consistent hashing.

    b. Sharding based on locationID: our hash function will map each locationid to a server where we will store that
    place. While building our QuadTree, we will iterate through all the places and calculate the hash of each locationid
    to find a server where it would be stored. To find nearby places of a location we have to query all servers, and
    each server will return a set of nearby places, A centralized server will aggregate these results to return them
    to the user.

    Will we have different QuadTree structure on different partitions? Yes, this can happen, since it is guaranteed
    that we will have an equal number of places in any given grid on all partitions. Though, we do make sure that all
    servers have approximately equal number of Places. This different tree structure on different servers will not cause
    any issue though, as we will be searching all the neighboring grids with the given radius on all partitons.

    Remaining part of this chapter assumes that we have partitioned our data based on locationid.

8. Replication and Fault Tolerance

    having replicas of QuadTree servers can provide an alternate to data partitioning. To distribute read traffic, we
    can have replicas of each QuadTree server. We can have a master-salve configuration, where replicas (slaves) will
    only serve read traffic and all write traffic will first go the master and then applied to slaves. Slaves might
    not have some recently inserted places (a few milliseconds delay will be there), but this could be acceptable.

    What will happen when a QuadTree server dies? We can have a secondary replica of each server, and if primary dies,
    it can take control after the failover. Both primary and secondary servers will have the same QuadTree structure.

    What if both primary and secondary servers die at the same time? We have to allocate a new server and rebuilt the
    same QuadTree on it. How can we do that, since we don't know what places were kept on this server? The brute-force
    solution would be to iterate through the whole database and filter locationids using our hashing function to figure
    out all the requried places that will be stored on this server. This would be inefficient and slow, also during
    the time when the server is being rebuilt; we will not be able to serve any query from it, thus missing some places
    that should have been seen by users.

    how can we efficiently retrieve a mapping between places and QuadTree Server? We have to build a reverse index that
    will map all the places to their quadtree server. We can have a separate quadtree index server that will hold this
    information. We will need to buil a hashmap, where the 'key' wold be the quodtree server number and the 'value'
    would be a hashset containing all the places being kept on that QuadTree server. We need to store locationid and
    lat/long with each places because through this information servers can built their quadtrees. Notice that we are
    keepting places data in a hashset, this will enable us to add /remove places from our index quickly. So now
    whereever a quadtree server needs to rebuild itself, it can simply ask the quadtree index server for all the places
    it needs to store. This approach will surely be quite fast. We whould also have a replica of quadtree index server
    for fault tolerance. If a QuadTree index server dies, it can always rebuilt its index from iterating through the
    database.

9. Cache

    To deal ith hot places, we can introduce a cache in front of our database. We can use an off the shelf solution
    like memcache, which can store all data about hot spaces. Application servers before hitting backend database can
    quickly check if the cache has that place. Based on client's usage pattern, we can adjust how many cache server we
    needed. For cache eviction policy, Least Recently used (LRU) seems suitable for our system.

10. Load balancing (LB)

    We can add LB layer at two places in our system:

        1. between clients and application server
        2. between application servers and backend server.

    Initially, a simple round robin approach can be adopted; that will distribute all incoming requests equally among
    backend servers. This LB simple to implement and does not introduce any overhead. Another benefit of this approach
    is if a server is dead, the load balancer will take it out of the rotation and will stop sending any traffic to it.

    A problem with round robin lb is, it won't take server load into consideration. if a server is overloaded or slow,
    the load balancer will not stop sending new requests to that server. To handle this, a more intelligent lb solution
    would be needed that periodically queries backend server about their load and adjusts traffic based on that.

11. Ranking

    how about if we want to rank the search results not just by proximity but also by popularity or relevance?

    how can we return most popular places with a given radius? Let's assume we keep track of the overall popularity of
    each place. An aggregated number can represent this popularity in our system, e.g., how many stars a place gets out
    of ten (this would be an average of different rankings given by users)? we will store this number in the databases,
    as well as, in the QuadTree. While searching for top 100 paces within a given radius, we can ask each partition of
    the QuadTree to return top 100 places having maximum popularity. Then the aggregator server can determine top 100
    places among all teh places returned by different partitions.

    Remember that we didn't build our system to update place's data frequently. With this design, how can we modify
    popularity of a place in our QuadTree? Although we can search a place and update its popularity in the QuadTree,
    it would take a lot of resources and can affect search requests and system throughput. Assuming popularity of a
    place is not expected to reflect in the system with a few hours, we can decide to update it once or twice a day,
    especially when the load on the system is minimum.

    Our next problem designing uber backend discusses dynamic updates of the quadtree in detail.
"""