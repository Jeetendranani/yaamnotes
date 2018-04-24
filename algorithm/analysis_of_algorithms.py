"""
Why performance analysis?
Many thins need to be taken care of:
    - user friendliness
    - modularity
    - security
    - maintainability
Why worry bout performance?

We can have all of these only if we have performance. Speed is fun!

How can we find out which algorithm is better?
Asymptotic analysis

We can have three cases to analyze an algorithm:
    1. The worst case
    2. The average case
    3. The best case

    todo: CMake

    Worst case analysis (Usually Done)
    in the worst case analysis, we calculate upper bound on running time of an algorithm. We must know the case that
    causes maximum number of operations to be executed. For linear search, the worst case happens when the element to
    be searched (x in the above code) is not present in the array. When x  is not present, the search() functions
    compares it with all the elements of arr[] one by one. Therefore, the worst case time complexity of linear search
    would be Theta(n).

    Average case analysis (Sometimes done)
    In average case analysis, the we take all possible inputs and calculate computing time for all of the inputs. Sum
    all the calculated values and divide the sum by total numbers of input. We must know (or predict) distribution of
    cases. For the linear search problem, let us assume that all cases are uniformly distributed (including the case of
    x not being present in array). So we sum all the case and divide the sum by (n + 1). Following is the value of
    average time complexity.

    Average case time = Theta(n)

    Best case analysis (Bogus)

    todo: letax

Asymptotic Notations
    1. Theta Notation: The theta notation bounds a functions from above and below, so it defines exact asymptotic
    behavior.

    A simple wy to get Theta notation of an expression is to drop low order terms and ignore leading constants. For
    example, consider the following expression. 3n**3 + 6n**2 + 6000 = Theta(n**3).

    Dropping lower order terms is always fine because there will always be an n0 after which Theta(n**3) has higher
    values than Theta(n**2) irrespective of the constants involved.

    For a given function g(n), we denote Theta((g(n)) is following get of functions.
    Theta(g(n)) = {f(n): There exists positive constants c1, c2, and n0 such that 0 <= c1*g(n) <= f(n) <= c2*g(n)
    for all n >= n0}

    The above definition means, if f(n) is theta of g(n), then teh value f(n) is always between c1*g(n) and c2*g(n)
    for large values of n (n >= n0). The definition of theta also requires that f(n) must be non-negative for values
    of n greater than n0.

    2. Beg O notation: The big O notation defines an upper bound of an algorithm, it bounds a function only from above.
    For example, consider the case of insertion sort. It takes linear time in the best case and quadratic time in worst
    case. We can safely say that the time complexity of insertion sort is O(n^2). note that O(n^2) also covers linear
    time. if we use Theta notation to present time complexity of insertion sort, we have to use two statements for best
    and worst cases:
        1. the worst case time complexity of insertion sort is Theta(n^2).
        2. The best case time complexity of insertion sort is Theta(n).

    The Big O notation is useful when we only have upper bound on time complexity of an algorithm. many times we easily
    find an upper bound by simply looking at the algorithm.

    O(g(n)) = {f(n): there exist positive constants c and n0 such that 0 <= f(n) <= cg(n) for all n >= n0}

    3. Omega notation: Just as Big O notation provides an asymptotic upper bound on a function, Omega notation provides
    an asymptotic lower bound.
    Omega notation can be user when we have lower bound on time complexity of an algorithm. As discussed in the previous
    post, the best case performance of an algorithms is generally not userl, the Omega notaion is the least used
    notation among all three.

    For a given function g(n), we denote by Omega the set of functions.
    Omega(g(n)) = {f(n): there exists positive constants c and n0 such that 0 <= cg(n) <= f(n) for all n >= n0}

Analysis of loops:
    1. O(1): The time complexity of a function (or set of statement) is considered as O(1) if it doesn't contain loop,
    recursion and call to any other non-constant time function.

    // Set of non-recursive and non-loop statements

    A loop or recursion that runs a constant number of time is also considered as O(1). For example the following loop
    is O(1).

    //Here c is a constant
    for (int i = 0; i < c; i++)
    {
        // some O(1) expression
    }

    2. O(n): Time complexity of a loop considered as O(n) if the loop variables is incremented / decremented by a
    constant amount.

    // here c is a positive integer constant
    for (int i = 0; i < n; i += c)
    {
        // some O(1) expressions
    }

    for (int i = n; i > 0; i -= c)
    {
        // some O(1) expressions
    }

    3. O(n^c): Time complexity of nested loops is equal to the number of times the innermost statement is executed.
    Foe example:

    for (int i = 1; i < n; i += c)
    {
        for (int j = 1; j < n; J += c)
        {
            //some O(1) expression
        }
    }

    for (int i = n; i > 0; i -= c)
    {
        for (int j = n; j > 0; j -= c)
        {
            // some O(1) expressions
        }
    }

    4. O(logn) Time complexity of a loop is considered as O(logn) if the loop variables is divided / multiplied by a
    constant amount.

    for (int i = 1; i < n; i *= c)
    {
        // some O(1) expressions
    }

    for (int i = n; i > 0; i /= c)
    {
        // some O(1) expressions
    }

    5. O(loglogn) Time complexity of a loop is considered as O(loglogn) if the loop variables is reduced /  increased
    exponentially by amount.

    // here c is a constant greater than 1
    for (int i = 2; i <= n; i = pow(i, c))
    {
        // Some O(1) expressions
    }

    // Here fun is sqrt or cube root or any other constant root
    for (int i = n; i > 0; i = fun(i))
    {
        // some O(1) expressions
    }

    how to combine time complexities of consecutive loops?

    When where are consecutive loops, we calculate time complexity as sum of time complexities of individual loops.

    for (int i = 1; i <= m; i += c)
    {
        // some O(1) expressions
    }

    for (int i = 1; i <= n; i += c)
    {
        // some O(1) expressions
    }

    Time complexity is O(m) + O(n) = O(m+n) if n == m, the time complexity becomes O(2n) = O(n).

    How to calculate time complexity of recursive functions?
    Time complexity of a recursive function can be written as a mathematical recurrence relation. To calculate time
    complexity, we must know how to solve recurrences, we will soon be discussing recurrence solving techniques as
    separate post.

Solving recurrences

Many algorithms are recursive in nature. When we analyze them, we get a recurrence relation for time complexity. We get
running time on an input of sie n as a function of n and the running time on inputs of smaller sizes. For example in
Merge sort, the sort a given array, we divide it in two halves and recursively repeat the process for the two halves.
Finally we merge the results. Time complexity of merge sort can be written as T(n) = 2T(n/2) + cn. There are many other
algorithms like Binary Search, Tower of Hanoi, etc.

There are mainly three ways for solving recurrences.

1. Substitution Method: We make a guess for the solution and then we use mathematical induction to prove the guess is
correct or incorrect.
    For example consider teh recurrence T(n) = 2T(n/2) + n

    We guess teh solution as T(n) = O(nlogn) now we use induction to prove our guess.

    we need to prove that t(n) <= cnlogn. We can assume that it is true for values smaller than n.

    T(n) = 2T(n/2) + n
    <= cn/2log(n/2) + n
    = cnlogn - cnlog2 + n
    = cnlogn - cn + n
    <= cnlogn

2. Recurrence tree method: In this method, we draw a recurrence tree and calculate the time taken by every level of
tree. Finally, we sum the work down at all levels. To draw the recurrence tree, we start from the given recurrence and
keep drawing till we find a patten among levels. The pattern is typically a arithmetic or geometric series.

    For example consider the recurrence relation
    T(n) = T(n/4) + T(n/2) + cn^2

            cn^2
            /   \
        T(n/4)   T(n/2)

    if we further break down the expression T(n/4) and T(n/2), we get following recurrence tree.
    To know the value of the T(n), we need to calculate sum of the tree nodes level by level. If we sum the above tree
    level by level, we gt the following series
    T(n) = c(n^2 + 5(n^2)/16 + 25(n^2)/256 + ...
    the above series is geometrical progression with ratio 5/16.

    To get an upper bound, we can sum the infinite series.
    we get the sum as (n^2)/(1-5/16) which is O(n^2)

3. Master method
Master method is the direct ay to get the solution. The master method works only for following type of recurrences or
for recurrences that can be transformed to following type.

    T(n) = aT(n/b) + f(n) where n >= 1 and b > 1

    There are following three cases:
    1. If f(n) = Theta(n^c) where c < logba then T(n) = Theta(n^logba)
    2. If f(n) = Theta(n^c) where c = logba then T(n) = Theta(n^clogn)
    3. If f(n) = Theta(n^c) where c > logba then T(n) = Theta(f(n))

how does this work?
Master method is mainly derived from recurrence tree method. If we draw recurrence tree of T(n) = aT(n/b) + f(n), we
can see that the work done at root is f(n) and work done at all leaves is Theta(n^c) where c is logba. And the height
of recurrence tree is logbn.

In recurrence tree method, we calculate total work done. If the work done at leaves is polynomially more, then leaves
are the dominant part. and our result becomes the work down at leaves (Case 1), if work done at leaves and root is
asymptotically same. then our result becomes height multiplied by work down at any level (case 2). If the work down at
at root is asymptotically more, then our result becomes work down at root(case 3).

Examples of some standard algorithms whose time complexity can be evaluated using master method.
Merge sort: T(n) = 2T(n/2) + Theta(n). It falls in case 2 as c is 1 and logba is also 1. So the solution is Theta(nlogn)
Binary Search: T(n) = T(n/2) + Theta(1). It also falls in case 2 as c is 0 and logba is also 0. so the solution is
Theta(logn).


Amortized analysis

Splay tree todo:

Let us consider an example of a simple hash table insertions. How dow e decide tables size? There is a trade-off
between space and time, if we make ahsh-table size big, search time becomes fast, but space required becomes high.

The solution to this trade-off problem is use Dynamic Table or Array). The idea is to increase size of table whenever it
becomes full. Following are the seps to following when table becomes full.
    1. Allocate memory for a larger table of size, typically twice the old table.
    2. Copy the contents of old table to new table.
    3. Free the old table.
    If the table has space available, we simply insert new item in available space.

So using amortized analysis, we could prove that the Dynamic table scheme has O(1) insertion time which is great result
used in hashing. Also the concept of dynamic table is using in vectors in C++, arraylist in java.

Following are few important notes:
    1. Amortized cost of sequence of operations can be seen as expenses of a salaried person. The average monthly
    expense of the person is less than or equal to the salary, but the person can spend more money in a particular month
    by buying a car or something. In other months, he or she sames money for the expensive month.

    2. The above amortized analysis done for Dynamic array example is called aggregate method. There are two more
    powerful ways to do amortized analysis called accounting method todo
    and potential method - todo:

    3. The amortized analysis doesn't involve probability. There is also another different notion of average case
    running time where algorithms use randomization to make them faster and expected running time is faster then the
    worst case running time. These algorithms are analyzed using randomized analysis.

What does 'Space complexity' mean?

The term space complexity is misused for auxiliary space at many place. Following are the correct definitions of
Auxiliary space and space complexity.

auxiliary space is the extra space or temporary space used by an algorithm.

space complexity of an algorithm is total space taken by the algorithm with respect to the input size. Space complexity
includes both auxiliary space and space used by input.

for example, if we want to compare standard sorting algorithms on the basis of space, then auxiliary space would be a
better criteria than space complexity. Merge sort use O(n) auxiliary space, insertion sort and help sort use O(1)
auxiliary space, space complexity of all this sorting algorithms is O(n) though.

Pseudo-polynomial Algorithms

What is pseudo-polynomial?
An algorithm whose worst case time complexity depends on numeric value of input (not number of inputs) is called
pseudo-polynomial algorithm. For example, consider the problem of counting frequencies of all elements in an array
of positive numbers. A pseudo-polynomial solution for this is to first find the maximum value, then iterate from 1 to
maximum value, find its frequency in array. This solution requires time according to the maximum value in input array,
therefore pseudo polynomial. On the other hand, an algorithm whose time  complexity is only base on number elements in
array (not vlaue) is considered the polynomial algorithm.

Pseudo-polynomial and NP-completeness

Some NP-complete problems - todo:
has pseudo polynomial solutions. For example, dynamic programming solution of 0-1 knapsack, subset sun, and partition
problems re pseudo polynomial. NP complete problem that can be solved using pseudo polynomial time  algorithms are
called weakly NP-complete

NP-completeness

We have been writing about efficient algorithms to solve complex problems, like shortest path, euler graph - todo:
, minimum spanning tree, etc. Those were all success stories of algorithm designers. In this post, failure stories
 of computer science are discussed.

Can all computational problem be solved by computer? There are computational problems that can not be solved by
algorithms even with unlimited time. For example Turing Halting problem (Given a problem and an input, whether the
program will eventually halt when run with that input, or will run forever) Alan Turing proved that general algorithm
to solve the halting problem for all possible program input pairs can't exist. A key part of the proof is, Turing
machine was used as a mathematical definition of a computer and program (Source Halting Problem). - todo:

Status of NP complete problems is another failure story, NP complete problems are problems whose status is unknown.
No polynomial time algorithm has yet been discovered for any NP complete problem, nor has anybody yet been able to prove
that no polynomial-time exist for any of them. The interesting part is, if any one of the NP complete problems can be
solved in polynomial time, then all of them can be solved.

What are NP, P, NP-complete and NP-hard problems?

P is set of problems that can be solved by deterministic Turing machine in polynomial time.

NP is set of decision problems that can be solved by a non-deterministic turning machine - todo:
in polynomial time. P is subset of NP. (any problem that can be solved by deterministic machine in polynomial time can
also be solved by on-deterministic machine in polynomial time.)

Informally, NP is set of decision problems which can be solved by a polynomial time via a "Lucky solution", a magical
algorithm that always makes a right guess among the given set of choices (source ref 1)

NP-complete problems are the hardset problem in NP set. A decision problem L is NP-complete if:
1. L is in NP (any given solution for NP-complete problem can be verified quickly, but there is no efficient known
solution)
2. Every problem in NP is reducible to L in polynomial time (reduction is defined below).

Quick sort time complexity:
The worst case of quick sort occurs when the picked pivot is always on eof the corner elements is sorted array. In
worst case, Quick-sort recursively calls one subproblem with size (n-1). So recurrence is T(n) = T(n-1) + T(0) + O(n)

"""