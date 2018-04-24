"""
229. Majority Element II

Given an integer array of size n, find all elements that appear more than [n/3] times. The algorithm should run in
linear time and in O(1) space
"""


class Solution:
    def majority_element(self, nums):
        n1 = n2 = None
        c1 = c2 = 0
        for i in nums:
            if n1 == i:
                c1 += 1
            elif n2 == i:
                c2 += 1
            elif c1 == 0:
                n1, c1 = i, 1
            elif c2 == 0:
                n2, c2 = i, 1
            else:
                c1, c2 = c1 - 1, c2 - 1

        return [n for n in [n1, n2] if n is not None and nums.count(n) > len(nums)//3]


"""
Introduction to Algorithm

I. Foundations
    1. The role of the algorithm in computing
    2. Getting started
    3. Growth of functions
    4. Divide and conquer
    5. Probabilistic analysis and randomized algorithms
    
II. Sorting and Order Statistics
    6. Heepsort
    7. Quicksort
    8. Sorting in Linear Time
    9. Medians and orders statistics
    
III. Data structures
    10. Elementary Data Structures
    11. Hash Tables
    12. Binary Search Trees
    13. Red-Black Trees
    14. Augmenting Data Structure
    
IV. Advanced Design and Analysis Techniques
    15. Dynamic Programming
    16. Greedy Algorithms
    17. Amortized Analysis
    
V. Advanced Data Structures
    18. B-Trees
    19. Fibonacci Heaps
    20. van Emde Boas trees
    21. Data Structures for Disjoint Sets.
    
VI. Graph Algorithms
    22. Elementary graph algorithms
    23. Minimum spanning trees
    24. Single source shortest path.
    25. All-pairs shortest paths
    26. Maximum Flow
    
VII. Selected Topics
    27. Multi-threaded Algorithms
    28. Matrix Operations
    29. Linear Programming
    30. Polynomials and the FFT
    31. Number-Theoretic Algorithms
    32. String matching
    33. Computational geometry
    34. NP-completeness
    35. Approximation algorithms
    
VIII. Appendix: Mathematical Background
    A. Summations
    B. Sets, Etc.
    C. Counting and Probability
    D. Matrices
    
1. Foundations

This part will start you thinking about designing and analyzing algorithms. It is intended to be a gentle introduction 
to hwo we specify algorithms, some of the design strategies we will use throughout this book, and many of the 
fundamental ideas used in algorithm analysis. Later part of this book will built upon this base.

Chapter 1 provides an overview of algorithms and their place in modern computing systems. This chapter defines what a 
algorithm is and lists some examples. It also makes a case that we should consider algorithms as a technology, 
alongside technologies such as fast hardware, graphical user interfaces, object-oriented system, and networks.

In chapter 2, we see our first algorithms, which solve the problem of sorting a sequence of n numbers. They are written
in a pseudocode which, although not directly translatable to any conventional programming language, conveys the 
structure of the algorithm clearly enough that you should be able to implement it in the language of your choice. The 
sorting algorithm we examine are insertion sort, which use an incremental approach, an merge sort, which uses a 
recursive technique known as "divide and conquer'. Although the time each requires increases withe the value n, the 
rate of increase differs between the two algorithms. We determine these running times in chapter 2, and we develop a
useful notation to express them.

Chapter 3 precisely defines this notation, which we call asymptotic notation. It starts by defining several asymptotic
notations, which we use for bounding algorithm running time above and/or below. The rest of chapter 3 is primarily a 
presentation of mathematical notation, more to ensure that your use of notation matches that in this book than to teach
you new mathematical concepts.

Chapter 4 delves further into the divide and conquer method introduced in chapter 2. It provides additional examples of 
divide and conquer algorithms, including Strassen's surprising method for multi-playing two square matrices. Chapter 4 
contains methods for solving recurences, which are useful for describing the running times of recursive algorithms. 
One powerful technique is the "master method", which we often use to solve recurrences that arise from divide and 
conquer algorithms. Although much of chapter 4 is devoted to proving the correctness of the master method, you may skip
this proof yet still employ the master method.

Chapter 5 introduces probabilistic analysis and randomized algorithms. we typically use probabilistic analysis to 
determine the running time of an algorithm in cases in which, due to the presence of an inherent probability 
distribution, the running time may differ on different inputs of the same size. In some cases, we assume that the inputs
conform over all possible distribution, so that we are averaging the running time over all possible inputs. In other
cases, the probability distribution comes not from the inputs but from random choices made during the course of the 
algorithm. An algorithm whose behavior is determined not only by its input but by the values produced by random-number 
generator is a randomized algorithm. We can use randomized algorithms to enforce a probability distribution on the 
inputs - thereby ensuring that no particular input always causes poor performance - or even to bound the error rate of 
algorithms that are allowed to produce incorrect results on a limited basis.

Appendices A-D contain other mathematical material that you will find helpful as you read this book. You are likely to 
have seen much of hte material in the appendix chapters before having read this book (although the specific definitions
and notational conventions we use may differ in some cases from what you have seen in the past), and so you should 
think of the Appendices as reference material. On the other hand, you probably have not already seen most of the 
material in Part!, All the chapter in part 1 and the appendices are written with a tutorial flavor.

1. The role of algorithms in computing

What are algorithms? Why is the study of algorithms worthwhile? What is the role of algorithms relative to other
technologies used in computer? In this chapter, we will answer these questions.

1.1. Algorithms

Informally, an algorithm is any well-defined computational procedure that takes some value, or set of values, as input
and produce some value, or set of values, as output. An algorithm is thus a sequence of computational steps that 
transform the input into the output.

We can also view an algorithms as a tool for solving a well-specified computational problem. The statement of the
problem specifies in general terms the desired input/output relationship.

For example, we might need to sort a sequence of numbers into non decreasing order. This problem arises frequently in 
practice and provides fertil ground for introducing many standard design techniques and analysis tools. 

Insertion sort (A)
    for j = 2 to A.length
        key = A[j]
        //Insert A[j] into the sorted sequence A[1 .. j - 1].
        i = j - 1
        while i > 0 and A[i] > key
            A[i + i] = A[i]
            i = i - 1
        A[i + 1] = key
"""
