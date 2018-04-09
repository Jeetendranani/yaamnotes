"""
18. B-Trees

B-trees are balanced search trees designed to work well on disks or other direct access secondary storage devices.
B-trees are similar to red-black trees (Chapter 13), but they are better at minimizing dis i/o operations. Many
database systems use b-trees, or variants of b-trees, to store information.

B-trees differ from red-black trees in that b-tree nodes may have many children, from a few to thousands. That is,
the 'branching factor' of a b-tree can be quite large, although it usually depends on characteristics of the disk unit
used. b-trees are similar to red-black trees in that every n-node b -tree has height O(lgn). The exact height of a
b-tree can be considerably less than that of a red-black tree, however, because its branching factor, and hence the
base of the logarithm tht expresses its height, can be much larger. Therefore, we can also use b-trees to implement
many dynamic-set operations in time O(lgn).

b-trees generalize binary search trees in a natural manner. Figure 18.1 shoes a simple b-trees. if an internal b-tree
node x contains x. n keys, then x has x.n + 1 children. The keys in node x serve as dividing points separating the
range of keys handled by x into x.n+1 sub ranges, each handled by one child of x. When searching for a key in a b-tree,
we make an (x.n + 1)-way decision based on comparisons with the x.n keys stored at node x. The structure of leaf nodes
differs from that of internal nodes; we will examine these differences in section 18.1.

Section 18.1 gives a precise definition of b-trees and proves that the height of a b-tree grows only logarithmically
with the number of nodes it contains. Section 18.2 describes how to search for a key and insert a key into a b-tree,
and section 18.3 discusses deletion. Before proceeding, however, we need to ask why we evaluate data structure
designed to work on a disk differently from data structure designed to work in main random access memory.

Data structures on secondary storage

Computer system take advantage of various technologies that provide memory capacity. The primary memory ( or main
memory) of a computer system normally consists of silicon memory chips. This technology is typically more than an order
of magnitude more expensive per bit stored than magnetic storage technology, such as tapes or disks. most computer
systems also have secondary storage based on magnetic disks; the amount of such secondary storage often exceeds the
amount of primary memory by at least two orders of magnitude.

Figure 18.2 shows a typical disk drive. The drive consists of one or more platters, which rotate at a surface of each
platter. The drive reads and writes each platter by a head at teh end of arm.  The arms can move their heads toward or
away from the spindle. When a given head is stationary, the surface that passes underneath it is called a track.
Multiple platters increase only the disk drives capacity and not its performance.

Although disks are cheaper and have higher capacity than main memory, they are much, much slower because they have
moving mechanical parts. The mechanical motion has two components: platter rotation and arm movements. As of this
writing, commondity disks rotate at speeds of 5,400 - 15,000 revolutions per minute (RPM). We typically see 15,000 RPM
speeds in server-grade drives, 7200 RPM speeds in drives for desktops, and 5400 RPM speeds in drives for laptops.
Although 7200 RPM may seem fast, one rotation takes 8.33 milliseconds, which is over 5 orders of magnitude longer than
the 50 nanoseconds times (more or less) commonly found for silicon memory. In other words, if we have to wait a full
rotation for a particular item to come under the read/write head, we could access main memory more than 100,000 times
during that span, On average we have to wait for only half a rotation, but still, the difference in access times for
silicon memory compared with disks is enormous. Moving the arms also take some time. As of this writing, average access
times for commodity disks are in the range of 8 to 11 milliseconds.

In order to amortize the time spend writing for mechanical movements, disks access not jsut one item but several at a
time. Information is divided into a number of equal-sized pages of bits that appear consecutively with tracks, and each
disk read or write is of one or more entire pages. For a typical disk, a page might be 2**11 to 2**14 bytes in length.
Once teh read/write head is positioned correctly and the disk has rotated to the beginning of the desired page, reading
or writing a magnetic disk is entirely electronic (aside from the rotation of the disk), and the disk can quickly read
and write large amounts of data.

Often, accessing a page of information and readign it from a disk takes longer than examining all the information read.
For this reason, in this chapter we shall look separately at the two principal components of the running time:
    - the number of disk accesses, and
    - the CPU (computing) time

We measure the number of disk accesses in term of the number of pages of information that need to be read from or
written to the disk. We note that disk access time is not constant it depends on the distance between the current
track and the desired track
"""