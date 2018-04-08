"""
11. Hash Tables

Many applications require a dynamic set that supports only the dictionary operation insert, search, and delete. For
example, a compiler that translates a programming language maintains a symbol table, in which the keys of elements are
arbitrary character strings corresponding to identifiers in the language. A hash table is an effective data structure
for implementing dictionaries. Although searching for an element in a hash table can take as long as searching for an
element in a linked list O1(n) in worst case - in practice, hashing performs extremely well. Under reasonable
assumptions, the average time to search for an element in a hash table is O(1).

A hash table generalizes the simpler notion of an ordinary array. Directly addressing into an ordinary array makes
effective use of our ability to examine an arbitrary position in an array in O(1) time, section 11.1 discusses direct
addressing in more detail. We can take advantage of direct addressing when we can afford to allocate an array that has
one position for every possible key.

When the number of keys actually stored is small relative to the total number of possible keys, hash tables become an
effective alternative to directly addressing an array, since a hash table typically uses an array of size proportional
to teh number of keys actually stored. Instead of using the key as an array index directly, the array index is computed
from the key, section 11.2 presents the main ideas, focusing on 'chaining' as a way to handle 'collisions', in which
more that one key maps to the same array index. Section 11.3 describes how we can compute array indices from keys
using hash functions. We present and analyze several variations on the basic theme. Section 11.4 looks at 'open
addressing', which is another way to deal with collisions. The bottom line is that hashing is an extremely effective
and practical technique: the basic dictionary operations require only O(1) time on the average. Section 11.5 explains
how 'prefect hashing' can support searches in O(1) worst case time. when the set of keys being stored is static (this
is, when the set of keys never changes once stored.)
"""