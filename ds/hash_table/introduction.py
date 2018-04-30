"""
Introduction

hash table is a data structure which organizes data using hash functions in order to support quick insertion and search.

There are two different kinds of hash tables: hash set and hash map.

    - The hash set is one of the implementations of set data structure to store no repeated values.
    - The hash map is on eof the implementations of a map data structure to store (key, value) pairs.

It is easy to use a hash table with the help of standard template libraries. Most common languages such as Java, C++
and python support both hash set and hash map.

by choosing a proper hash function, the hash table can achieve wonderful performance in both insertion and search.

In this card, we will answer the following questions:

    1. what is the principle of a hash table?
    2. how to design a hash table?
    3. How to use hash set to solve duplicates related problems?
    4. How to use hash mpa to aggregate information by key?
    5. how to design a proper key when using a hash table?

And we also provide exercises for you to be familiar with hash table.

Design a hash table

In this chapter, we will discuss the underlying principle of the hash table.

After completing this chapter, you should be able to answer the following questions:

    1. What is the principle of hash table?
    2. Which factors wil influence the choice of hash function and collision resolution strategy?
    3. understand the difference between a hash set and a hash map.
    4. how to design a simple version of hash set and a hash map as in a typical standard template library.
    5. what is the complexity of insertion and lookup operations.

the principle of hash table

As we mentioned in the introduction, hash table is a data structure which organizes data using hash functions in order
to support quick insertion and search. In this article, we will take a look at the principle of the hash table.

The principle of hash table
The key idea of hash table is to use a hash function to map keys to buckets. To be more specific,
    1. When we insert a new key, the hash function will decide which bucket the key should be assigned and the key will
    be stored in teh corresponding bucket;
    2. when we want to search for a key, the hash table will use the same hash function to find the corresponding
    bucket and search only in the specific bucket.

keys to design a hash table

There are two essential factors that you should pay attention to when you are going to design a hash table.

1. hash function
The hash function is the most important component of a hash table which is used to map the key to a specific bucket. In
the example in previous article, we use y = x % 5 as a hash function, where x is the key value and y is the index of
the assigned bucket.

The hash function will depend on the range of the key values and the number of buckets.

Here are some examples of hash functions:

It is an open problem to design a hash function. the idea is to try to assign the key to the bucket as uniform as you
can. Ideally, a prefect hash function will be a one one mapping between the key and the bucket, however, in most cases
a hash function is not prefect and it is a tradeoff between the amount of buckets and the capacity of a bucket.

2. Collision resolution

Ideally, if our hash function is perfect one one mapping, we will not need to handle collisions. Unfortunately, in most
cases, collisions are almost inevitable. For instance, in our previous hash function (y = x % 5), both 1087 and 2 are
assigned to bucket 2. That is a collision.

A collision resolution algorithm should solve teh following questions:
    1. How to organize the values in the same bucket?
    2. What if too many values are assigned to the same buckets?
    3. how to search a target values in a specific bucket?
This questions are related to the capacity of the bucket, and the number of keys which might be mapped into the same
bucket according to our hash function.
"""