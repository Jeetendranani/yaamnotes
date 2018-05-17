"""
SQL vs. NoSQL

In the world of databases, there tow main types of solutions: SQL and NoSQL - or relational databases and non-relational
databases. Both of them differ in the way they were built, the kind of information they store, and how they store it.

Relational databases are structured and have predefined schemas, like phone books that store phone numbers and
addresses. Non-relational databases are unstructured, distributed and have a dynamic schema, like file folders that
holders that hold everything from a person's address and phone number to their Facebook 'likes' and online shopping
preferences.

SQL

Relational databases store data in rows and columns. Each row contains all teh information about one entity, and columns
are all the separate data points. Some of the most popular relational database are MySQL, Oracle, MS SQL Server, SQLite,
Postgres, MariaDB, etc.

NoSQL

Following are most common types of NoSQL:

key-value stores: Data is stored in an array of key-value paris. The 'key' is an attribute name, which is linked to a
'value'. Well-known key value stores include Redis, Voldemort and Dynamo.

Document Databases: In these databases data is stored in documents, instead of rows and columns in a table, and these
documents are grouped together in collections. Each document can have an entirely different structure. Document
databases include the CouchDB and MongoDB.

Wide-column Databases: Instead of 'tables,' in columnar databases we have column families, which are containers for
rows. Unlike relational databases, we dont' need to know all the columns up front, and each rwo doesn't have to have
the same number of columns. Columnar databases are best suited for analyzing large datasets - bi names include
Cassandra and HBase.

Graph Databases: These database are used to store data whose relations are best represented in a graph. Data is saved
in graph structures with nodes (entities), properties (information about the entities) and lines (connections between
the entities). Examples of graph database include Neo4J and InfiniteGraph.

High level difference between SQL and NoSQL

Storage: SQL stores data in tables, where each rwo represents an entity, and each column represents a data point about
that entity; for example, if we are storing a car entity in a table, different columns could be "Color', 'make',
'Model', and so on.

noSQL database have different data storage models. The main ones are key-value, document, graph and cloumnar. We will
discuss difference between these databases below.

Schema: In SQL, each record confirms to a fixed schema, meaning the columns must be decide and chosen before data entry
and each row must have data for each column. The schema can be altered later, but it involves modifying the whole
database and going offline.

Whereas in NoSQL, schemas are dynamic. columns can be added on the fly, and each 'row' (or equivalent) doesn't have to
contains data for each 'column'.

Querying: SQL databases uses SQL (structured query language) for defining and manipulating the data, which is very
powerful. In NoSQL database, queries are focused on a collection of documents. Sometimes it is also called UnQL
(Unstructured Query Language). Different databases have different syntax for using UnQL.

Scalability: In most common situations, SQL databases are vertically scalable, i.e., by increasing the horsepower of the
hardware (higher memory, CPU, etc.), which can get very expensive. It is possible to scale a relational database across
multiple servers, but this is a challenging and time-consuming process.

On the other hand, NoSQL databases are horizontally scalable, meaning we can add more server easily in our NoSQL
databases infrastructure to handle large traffic. Any cheap commodity hardware or cloud instances can host NoSQL
databases, thus making it a lot more cost-effective than vertical scaling. A lot of NoSQL technologies also distribute
data across servers automatically.

Reliability or ACID compliancy (Atomicity, consistency, isolation, durability): The vast majority of relational database
are ACID compliant. So, when it comes to data reliability and safe guarantee of performing transactions, SQL databases
are still the better bet.

Most of the NoSQL solutions sacrifice ACID compliance for performance and scalability.

SQL vs. NoSQL - which one to use?

When it comes to database technology, there's no one size fits all solution. That's why many businesses rely on both
relational and non-relational databases for different needs. Even as NoSQL databases are gaining popularity for their
speed and scalability, there are still situations where a highly structured SQL database may perform better; choosing
the right technology hinges on the use case.

Reasons to use SQL databases

Here are a few reasons to choose a SQL databases;

1. We need to ensure ACID compliance. ACID compliance reduces anomalies and protects the integrity of your database by
prescribing exactly how transactions interact with the database. Generally, NoSQL databases sacrifice ACID compliance
for scalability and processing speed, but for many e-commerce and financial applications, an ACID compliant database
remains teh preferred option.

2. your dta is structured and unchanging. If your business is not experiencing massive growth that would require more
servers and if you're only working with data that's consistent, then they may be no reason to use a system designed to
support a variety of data types and high traffic volume.

When all the other components of our application are fast and seamless, NoSQL databases prevent data from being the
bottleneck. Big data is contributing to a large success for NoSQL databases, mainly because it handles dta differently
than the traditional relational databases. A few popular examples of NoSQL databases are MongoDB, CouchDB, Cassantra,
and HBase.

1. Storing large volumes of data that often have little to no structure. A NoSQL database sets no limits on the types
of data we can store together and allows us to add different new types as the need changes. With document-based
databases, you can store data in one place without having to define what "types" of data those are in advance.

2. Making the most of cloud computing and storage. Could based storage is an excellent cost-saving solution but requires
data to be easily spread across multiple servers to scale up. Using commodity (affordable, smaller) hardware on site or
in the cloud saves you the hassle of additional software, and NoSQL databases like Cassandra are designed to be scaled
across multiple data centers out of the box without a lot of headaches.

3. Rapid development. NoSQL is extremely useful for rapid development as it doesnt need to be prepped ahead of time. If
you'are working on quick iterations of your system which require making frequent updates to the data structure without
a lot of downtime between versions, a relational database will slow you down.
"""