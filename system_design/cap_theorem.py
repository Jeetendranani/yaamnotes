"""
CAP Theorem

CAP theorem states that it is impossible for a distributed software system to simultaneously provide more than two out
of three of the following guarantees (CAP): Consistency, Availability and Partition tolerance. When we design a
distributed system, trading off among CAP is almost the first thing we want to consider. CAP theorem syas while
designing a distributed system we can pick only two of:

Consistency: All nodes see the same data at the same time. Consistency is achieved by updating several nodes before
allow further reads.

Availability: Every request gests a response on success/failure. Availability is achieved by replicating teh data across
different servers.

Partition tolerance: System continues to work despite message loss or partial failure. A system that is partition
tolerant can sustain any amount of network failure that doesn't result in a failure of the entire network. Data is
sufficiently replicated across combinations of nodes and networks to keep the system up through intermittent outages.

We cannot build a general data store that is continually available, sequentially consistent and tolerant to any
partition failures. We can only build a system that has any two of these three properties. Because, to be consistent,
all nodes should be see the same set of updates in teh same order. But if the network suffers a partition, updates in
one partition might not make it to the other partitions before a client reads from the out-of-date partition after
having read from the up-to-date one. The only that can be done to cope with this possibility is to stop serving requests
from the out-of-date partition, but then the service is no longer 100% available.
"""