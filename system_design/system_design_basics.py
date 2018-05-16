"""
Whenever we are designing a large system, we need to consider few things:

    1. what are different architectural pieces that can be used?
    2. how do these pieces work with each other?
    3. how can we best utilize these pieces, what are teh right tradeoffs?

Investing in scaling before it is needed is generally not a smart business proposition; however, some forethought into
the design can save valuable time and resources in the future. In the following chapters, we will focus on some of the
core building blocks of scalable systems. Familiarizing with these concepts would greatly benefit in understanding
distributed system design problems discussed later. In the next section, we will go through consistent hashing, CAP
theorem, load balancing, caching, data partitioning, indexes, proxies, queues, replication, and choosing between SQL
and noSQL.

Let's start with consistent hashing.
"""