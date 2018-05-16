"""
Data Partitioning

Data partitioning (also known as sharding) is a technique to break up a big database (DB) into many smaller parts. It
is the process of splitting up DB/table across multiple machine to improve the manage-ability, performance, availability
and load balancing of an application. The justification for data sharding is that, after a certain scale point, it is
cheaper and more feasible to scale horizontally by adding more machines than to grow it vertically by adding beefier
servers.

1. Partitioning methods

There are many different schemes one could use to decide how to break up an application database into multiple smaller
DBs. Below are three of the most popular schemes used by various large scale applications.

a. Horizontal partitioning: In this scheme, we put different rows into different tables. For example, if we are storing
different places in a table, we can decide that locations with ZIP codes less than 10000 are stored in one table, and
places with zip codes greater than 1000 are stored in a separate table. This is also called a range based sharding, as
we are storing different ranges of data in a separate tables.

The key problem with this approach is that if the values whose range is used for sharding isn't chosen carefully, then
the partitioning scheme will lead to unbalanced servers. In the previous example, splitting location based on there
zip codes assumes that places will be evenly distributed across the different zip codes. this assumption is not valid
as there will be a lot of places in a thickly populated area like Manhattan compared to its suburb cities.

b. vertical partitioning: In this scheme, we divide our data to store tales related to a specific feature to there
own server. For example, if we are building Instangram like application, where we needed to store data related to users,
all the photos they upload and people they follow, we can decide to place user profile information on one DB server,
friends lists on another and photos on a third server.

Vertical partitioning is straightforward to implement and has a low impact on the application. The main problem with
this approach is that if our application experiences additional growth, then it may be necessary to further partition
a feature specific DB across various servers (e.g. it would not be possible for a single server to handle all the
metadata queries for 10 billion photos by 140 millions users).

c. Directory based partitioning: A loosely coupled approach to work around issues mentioned in above scheme is to
create a lookup service which knows your current partitioning scheme and abstracts it away from the DB access code. So,
to find out where does a particular data entiry resides, we query our directory server that holds the mapping between
each tuple key to its DB server. This loosely coupled approach means we can perform tasks like adding servers to the
DB pool or change our partitioning scheme without having to impact your application.

2. Partitioning Criteria


"""