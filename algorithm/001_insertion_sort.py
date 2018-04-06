"""
Insertion-Sort(A)
    for j = 2 to A.length
        key = A[i]

        // Insert A[j] into the sorted sequence A[1 .. j-1].
        i = j - 1
        while i > 0 and A[i] > key
            A[i + 1] > A[i]
            i -= 1
        A[i + 1] = key
"""


def insert_sort(nums):
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j+1] = tmp


nums = [8, 9, 3, 6, 4, 0, 1]
insert_sort(nums)
print(nums)


"""
2.3 Designing algorithms

We can choose from a wide range of algorithm design techniques. For insertion sort, we used an incremental approach:
having sorted the sub-array A[1 .. j - 1], we inserted the single element A[j] into its proper place, yielding the 
sorted sub-array [1 .. j].

In this section, we examine an alternative design approach, know as "divide and conquer", which we shall explore in more
detail in chapter 4. we'll use divide and conquer to design a sorting algorithm whose worst-case running time is much 
less than that of insertion sort. On advantage of divide and conquer algorithms is that their running times are often 
easily determined using techniques that we will see in chapter 4.

Most professional programmers that I've encountered are not well prepared to tackle algorithm design problems. This is
a pity, because the techniques of algorithm design from one of the core practical technologies of computer science. 
Designing correct, efficient and implementable algorithms for real-word problems requires access to two distinct bodies
of knowledge:
- Techniques - Good algorithm designers understand several fundamental algorithm design techniques, including data 
structures, dynamic programming, depth-frist search, backtracking, and heuristics. Perhaps the single most important 
design technique is modeling, he part of abstracting a messy real-world application into a clean problem suitable for
algorithmic attack.

- Resources - Good algorithm designers stand on the shoulders of giants. Rather than laboring from scratch to produce
a new algorithms for every task, they can figure out what is known about a particular problem. Rather than 
re-implementing popular algorithms from scratch, they seek existing implementations to serve as a starting point. they 
are familiar with many classic algorithmic problems, which provide sufficient source material to model most any 
application.

Three aspects of the algorithm design manual have been particularly beloved:
    1. The catalog of algorithmic problems, 
    2. The war stories
    3. The electronic component of the book
    
2.3.1. the divide and conquer approach

    Divide the problem into number of sub-problems that are smaller instances of the same problem
    Conquer the sub-problems by solving them recursively. If the sub-problem size are small enough, however,just resole
    the sub-problems in a straightforward manner.
    combine the solutions to the sub-problems into the solution for hte original problem
    
    Divide: Divide hte n-element sequence to be sorted into two subsequence of n/2 elements each.
    Conquer: sort the two sub-sequences recursively using merge sort.
    Combine: Merge the two sorted sub-sequences to produce the sorted answer.
    
    The recursion "Bottoms out" when the sequence has only 1 element, in which case there is no work to be done, since 
    every 1 is already sorted order.
    
    The key operation of the merge sort algorithm is the merging of two sorted sequences in the combine step. We merge
    by calling an auxiliary procedure merge(a, p, q, r), where a is an array, and p, q, and r are indices into the array 
    such that p <= q < r, the procedure assures that teh sub-arrays a[p .. q] and a [q + 1 .. r] are in sorted order.
    The procedure assumes that teh sub-arrays A[p .. q] and A[q + 1 .. r] are in sorted order. It merges them to form a 
    single sorted sub-array that replaces the current sub-array A[p .. r].
    
    Our merge procedure takes time O(n), where n = r - p + 1 isi the total number of elements being merged, and it 
    works as follows. Returning to our card playing motif
"""