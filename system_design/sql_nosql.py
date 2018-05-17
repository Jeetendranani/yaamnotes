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

Schema: In SQL,
"""