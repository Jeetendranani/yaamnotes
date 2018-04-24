"""
Dynamic programming - Overlapping subproblems Property

Dynamic programming is an algorithmic paradigm that solves a given complex problem by breaking it into subproblems and
stores the results of subproblems to avoid computing the same result again. Following are the two main properties of
a problem that suggest that teh given problem can be solved using dynamic programming.

In this post, we will discuss first property (overlapping subproblem) in detail. The second property of dynamic
programming is discussed in next post.

    1. Overlapping subproblems
    2. Optimal substructure

1. Overlapping subproblems:
Like divide and conquer, dynamic programming combines solutions to sub-problems. Dynamic programming is mainly used
when solutions of same subproblems are needed again and again. In dynamic programming, computed solutions to subproblems
are stored in a table so that these dont' have to recomputed. So dynamic programming is not useful when where are no
common (overlapping) subproblems because there is no point storing the solution if they are not needed again. For
example, Binary Search doesn't have common subproblems. If we take example of following recursive problem for Fibonacci
Numbers, there are many subproblems which are solved again and again.
"""


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


"""
a) memoization (top down): The memoized program for a problem is similar to the recursive version a small modification 
that it looks ito a lookup table before computing solutions. We initialize a lookup array with all initial values as 
None. Where we need solution to a subproblem, we first look into the lookup table. If the precomputed value is there 
then we return that value, otherwise we calculate the value and put the result in lookup table so that it can be reused
later.
"""


def fib(n, lookup):
    if n < 2:
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2)

    return lookup[n]


"""
b) Tabulation (Bottom up): The tabulated program for a given problem builds a table in bottom up fashion and returns the 
last entry from table. For example, for the same fibonacci number, we first calculate fib(0) then fib(1) then fib(3) and
so on. So literally, we are building the solution of subproblems bottom-up.
"""


def fib1(n):
    f = [0] * (n+1)

    f[1] = 1

    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]

    return f[n]


"""
both tabulated and memoized store the solutions of subproblems. In memoized version, table is filled on demand while in
Tabulated version, starting from the first entry, all entries are filled one by one. Unlike the tabulated version, all 
entries of the lookup table are not necessarily filled in memoized version. For example, Memoized solution of the 
LCS problem - todo:
doesn't necessarily fill all entries.

To see the optimization achieved by memoized and tabulated solutions over the basic recursive solution, see the time 
taken by following return for calculating 40th fibonacci number:


Dynamic program - Optimal substructure property

2) Optimal substructure: A given problems has optimal substructure property if optimal solution of given problem can be
obtained by using optimal solutions of its subproblems.

For example, the shortest path problem has following optimal substructure property:
if a node x lies in the shortest path from a source node u to destination node v then the shortest path from u to v is
combination of shortest path from u to x and shortest path from x to v. The standard all pair shortest path algorithm 
like floyed warshall and bellmen ford are typical examples of dynamic programming.

- Longest increasing subsequence
Optimal substructure:
Let arr[0..n-1] be the input array and L[i] be the length of the lis ending at index i such that [i] is the element of 
the LIS. Then L(i) can be recursively written as:
L(i) = 1 + max(L(j) where 0 < j < i and arr[j] < arr[i]; or L(i) = 1, if no such j exists.
To find the LIS for a given array, we need to return max(L(i)) where 0 < i < n.
Thus, we see th LIS problem satisfies the optimal substructure property as the main problem can be solved using 
solutions to subproblems. 
Following is a simple recursive implementation of the LIS problem. It follows the recursive structure discussed above.

- longest common subsequence

The naive solution for this problem is to generate all subsequence of both given sequences and find the longest matching
subsequence, this solution is exponential in term of time complexity. Let us see how this problem possesses both 
important properties of a dynamic programming problem.

1) Optimal substructure:
Let the input sequences be x[0..m-1] and y[0..n-1] of lengths m and n respectively. And let L(x[0..m-1], y[0..n-1]) be
the length of LCS of the two sequences x and y. Following is the recursive definition of L(x[0..m-1], y[0..n-1])

If last characters of both sequences match (or x[m-1] == y[n-1]) then
L(x[0..m-1], y[0..n-1]) = 1 + L(x[0..m-2], y[0..n-2])
if last characters of both sequences do not mach (or x[m-1] != y[n-1]) then
L(x[0..m-1],y[0..n-1]) = max(L(x[0..m-2],y[0..n-1]), L(x[0..m-1], y[0..n-2])

2) Overlapping subproblems:
Following is the simple recursive implementation of the LCS problem. The implementation simply follows the recursive
structure mentioned above. 
"""


def lcs(x, y, m, n):
    if m == 0 or n == 0:
        return 0
    elif x[m-1] == y[n-1]:
        return 1 + lcs(x, y, m-1, n-1)
    else:
        return max(lcs(x, y, m-1, n), lcs(x, y, m, n-1))


"""
Time complexity of the above naive recursive approach is O(2^n) in worst case and worst case happens when all characters
of x and y mismatch. Considering the above implementation, following is the partial recursion tree for input string 
"AXYT" and "AYZX"
So the problem has overlapping substructure property and re-computation of same subproblems can be avoided by either 
using memoization or tabulation. Following is the tabulation implementation for the lcs problem.
"""


def lcs1(x, y):
    m = len(x)
    n = len(y)

    l = [[None] * (n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif x[i-1] == y[j-1]:
                l[i][j] = l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i-1][j], l[i][j-1])

    return l[m][n]


x = "AGGTAB"
y = "GXTXAYB"
print(lcs1(x, y))


"""
How to sole a dynamic programming problem?
Dynamic programming (DP) is a technique that solves some particular type of problems in Polynomial time. Dynamic 
programming solution are faster than exponential brute method and can be easily proved for their correctness. Before
we study how to think dynamically for a problem, we need to learn: 
    1. Overlapping subproblems
    2. Optimal substructure property
    
    Steps to solve a dp:
    1. Identify if it is a dp problem
    2. decide a state expression with least parameters
    3. formulate state relationship
    4. do tabulation (or add memoization)
    
Step 1: How to classify a problem as a dynamic programming problem?
    - Typically, all the problems that require to maximize or minimize certain quantity or counting problems that say 
    to count the arrangements under certain condition or certain probability problems can be solved by using DP.
    - All DP problems satisfy the overlapping subproblems property and most of the classic dynamic problems also 
    satisfy the optimal substructure property. Once, we observe these properties in a given problem, be sure that it 
    can be solved using dp.
    
Step 2: Deciding the state
    DP problems are all about state and their transition. This is the most basic step which must be done very carefully
    because the state transition depends on the choice of sate definition you make. So let's see what do we mean by the
    term "state".
    
    State A state can be defined as the set of parameters that can uniquely identify a certain position or standing in 
    the given problem. This set of parameters should be as small as possible to reduce state space.
    
    For example: In our famous Knapsack problem, we define our state by two parameters index and weight. ie. 
    DP[index][weight]. Here DP[index][weight] tell us hte maximum profit it can make by taking items from range 0 to 
    index having the capacity of sack to be weight. Therefore, here the parameters index and weight together can 
    uniquely identify a subproblem for teh knapsack problem.
    
    so our first step will be deciding a state for th problem after identifying that the problem is a dp problem.
    As we know dp is all about using calculated results to formulate the final result.
    So, our next step will be find a relation between previous state to reach the current state.
    
Step 3: Formulating a relation among the states
    This aprt is the hardest part of for solving a DP problem and requires a lots of intuition, observation and
    practice. Let's understand it by considering a sample problem.
    
    Given 3 numbers {1, 3, 5}, we need to tell the total number of ways we can form a number N using the sum of the 
    given of the given tree numbers. (Allowing repetitions and different arrangements).
    
    Total number of ways to form 6 is: 8
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 3
    1 + 1 + 3 + 1
    1 + 3 + 1 + 1
    3 + 1 + 1 + 1
    3 + 3
    1 + 5
    5 + 1
    
    Let's think dynamically for this problem. So, first of all, we decide a state for teh given problem. We will take a
    parameter n to decide state as it can uniquely identify an subproblem. So our state dp will look like state(n). 
    Here, state(n) means the total number of arrangements to form n by using (1, 3, 5) as elements.
    
    Now we need to compute state(n).
    
    How to do it?
    
    So here the intuition comes into action. As we can only use 1, 3 or 5 to form a given number. Let us assume that we 
    know the result for n = 1, 2, 3, 4, 5; being termilogistic let us say we know the result for teh 
    state(n=1), state(n=2), state(n=3) ... state(n=6)
    
    Now, we wish to know the result of the state(7), see, we can only add 1, 3, 5. Now we can get a sum total of 7 by 
    the following 3 ways:
Step 4: adding memoization or tabulation for the state


Tabulation vs Memoization

Prerequisite - DP, how to solve dp problems?
There are following tow different ways to store the values so that the values of a problem can be reused. Here, will 
discuss two patterns of solving dp problem:
    1. Tabulation: Bottom up
    2. Memoization: Top Down
    
Before getting to the definition of the above two terms consider the below statements:
    - version 1: I will study the theory of dp, then i will practice some problems on classic dp and hence I will master
    dp.
    - version 2: To master dp, I would have to practice dp problems and to practice problems - firstly, I would have to 
    study some theory of dp.
    
Both the above version say the same thing, just the difference lies in the way of conveying the message and that's 
exactly what bottom up and top down dp do. version 1 can be related to as bottom up and version two related to as dop 
down.

Bitmasking and dp - count ways to assign unique cap to every person

The 100 different types of caps each having a unique id from 1 to 100. Also, there 'n' person each having a collection
of variable number of caps. One day all of these persons decide to go in a party wearing a cap but to look unique they
decided that none of them will wear the same type of cap. So, count the total number of arrangements or ways such that 
None of them is wearing types of caps.

constraints 1 <= n <= 10 example:

First line contains value of n, next n lines contain collections of all the n persons.

input: 
3
5 100 1     // collection of first person
2           // collection of second person
5 100       // collection of third person

output: 
4
explanation: All valid possible ways are (5, 2, 100), (100, 2, 5), (1, 2, 5) and (1, 2, 100)

Since, the number of ways could be large, so output modulo 10000007

What is bitmasking?
Suppose we have a collection of elements which are numbered from 1 to N. If we want to represent a subset of this set
then it can be encoded by a sequence of N bits (we usually call this sequence a "mask"). In our chosen subset the i-th
element belongs to it if and only if the i-th bit of the mask i set. i.e., it equals to 1.
"""