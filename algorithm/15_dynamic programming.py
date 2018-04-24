"""
15. Dynamic Programming

Dynamic programming, like the dived and conquer method, solves leetcode by combining the solutions to subproblems.
("Programming" in this context refers to a tabular method, not to the writing computer code.) As we saw in chapter 2
and 4, divide and conquer algorithms partition the problem into disjoint subproblems, solve the subproblem recursively,
and then combine their solutions to solve the original problem. In contrast, dynamic programming applies when the
subproblems overlap - that is, when subproblems share sub-subproblems. In this context, a divide and conquer algorithm
does more work than necessary, repeatedly solving the common sub-subproblems. A dynamic-programming algorithm solves
each subproblem just once and then saves its answer in a table, thereby avoiding the work of recomputing the answer
every time it solves each sub-subproblems.

We typically apply dynamic programming to optimization leetcode. Such leetcode can have many possible solutions. Each
solution has a value. We call such a solution an optimal (minimum or maximum) value. We call such a solution an
optimal solution to the problem, as opposed to the optimal solution, since there may be several solutions that achieve
the optimal value.

When developing a dynamic programming algorithm, we follow a sequence of four steps:
1. Characterize the structure of an optimal solution.
2. Recursively define the value of an optimal solution.
3. Compute the value of an optimal solution, typically in a bottom-up fashion.
4. Construct an optimal solution from computed information.

Steps 1-3 from the basis of a dynamic programming solution to a problem. If we need only the value of an optimal
solution, and the solution itself, then we can omit step 4. When we do perform step 4, we sometimes maintain additional
information during step 3 so that we can easily construct an optimal solution.

The sections that follow use teh dynamic-programming method to solve some optimization leetcode. Section 15.1 examines
the problem of cutting a rod into rods of smaller length in way that maximizes their total value. Section 15.2 asks how
we can multiply a chain of matrices, while performing the fewest total scalar multiplications. Given these examples of
dynamic programming, section 15.3 discusses two key characteristics that a problem must have for dynamic programming to
be a viable solution technique. section 15.4. then shows how to find the longest common subsequence of two sequences via
dynamic programming. Finally, section 15.5. use dynamic programming to construct inary search trees that are optimal,
given a know distribution of keys to be looked up.

15.1. Rod cutting

Our first example use dynamic programming to solve a simple problem in deciding where to cut steel rods. Serling
Enterprises buys long steal rods nd cuts them into shorter rods, which it then sells, Each cut is free. The management
of Serling Enterprises wants to know the best way to cut up the rods.

We assume that we know, for i = 1, 2, ..., the price pi in teh dollars that Serling Enterprise charges for a rod of
length i inches. rod lengths are always an integeral number of inches.

The rod-cutting problem is the following. Given a rod of length n inches, and a table of prices p1 for i = 1, 2, ... n,
determine the maximum revenue rn obtainable by cutting up the rod and selling the prices. Note that if the prices pn
for a rod of lengh n is large enough, an optimal solution may require no cutting at all.

Consider the case when n = 4. Figure 15.2 shows all the ways to cut up a rod of 4 inches in length, including the way
with no cuts at all, we see that cutting a 4-inch rod into two 2-inch pieces produces revenue p2 + p2 = 5 + 5 = 10,
which is optimal.

We can cut up a rod of length n in 2**n1- different ways, since we have an independent option of cutting, or not cutting
at distance i inches from the left end, for i  = 1, 2, ... n-1. We denote a decomposition into pieces using ordinary
additive notation, so that 7 = 2 + 2 + 3 indicates that a rod of length 7 is cut into three pieces - two of length 2
and one of length 3. If an optimal solution cuts teh rod into k pieces, for some 1 <= k < n, then an optimal
decomposition n = i1 + i2 + ... + ik of the rod into pieces of lengths i1, i2, ..., ik provides maximum corresponding
revenue rn = p1 + p2 + ... + pik

For our sample problem, we can determine the optimal revenue figures ri, for i = 1, 2, ... 10, by inspection, which the
corresponding optimal decompositions.

More generally, we can frame the values rn fro n >= 1 in items of optimal revenues from shorter rods:
rn = max(pn.r1 + rn+1.r2 + ... + r1)

This first argument, pn, corresponds to making no cuts at all and selling the rod fo length n as is. The other n-1
arguments to max corresponding to the maximum revenue obtained by making an initial cut of the rod into two pieces of
size of i and n - i, for each i = 1, 2, ..., n -1, and then optimally cutting up those pieces further, Obtaining
revenues ri and r n-1 from those two pieces. Since we dont' know ahead of time which value of i optimizes revenue, we
have to consider all possible values for i and pick th eone that maximizes revenue, we also have the option of picking
no cut at all if we can obtain more revenue by selling the rod uncut.

Note that to solve the original problem of size n, we solve smaller leetcode of the same type, but of smaller sizes.
Once we make the first cut, we may consider the two pieces as independent instances of the rod-cutting problem. The
overall optimal solution incorporate optimal solution to teh tow related subproblems, maximizing revenue from each
of those two pieces. We say that the rod-cutting problem exhibits optimal substructure: optimal solutions to a problem
incorporate optimal solutions to related subproblems, which we may solve independently.

In a related, but slightly simpler, way to arrange a recursive structure for teh rod cutting problem, we view a
decomposition as consisting of a first piece of length i cut off the left-hand end. and then a right-hand remainder of
length n - i. Only the remainder, and not the first pieces, may be further divided. We may view every decomposition of
length-n rod in this way: as a first piece followed by some no cuts at all as saying that the first pieces has size
i = n and revenue pn and that remainder has size 0 with corresponding revenue r0 = 0, we thus obtain the
rn = max(pi + rn-1)

In this formulation, an optimal solution embodies the solution to only one related subproblem - the remainder - rather
than two.

Recursive top-down implementation

The following procedure implements the computation implicit in equation in a straightforward, top-down, recursive
manner.

cut-rod(p, n)
    if n == 0
        return 0
    q = '-inf'
    for i = 1 to n
        q = max(q, p[i] + cut-rod(p, n - i))
    return q

Procedure cut-rod takes as input an array p[1..n] of prices and an integer n, and it returns the maximum revenue
possible for a rod of length n. If n = 0, no revenue is possible, and so cut-rod returns 0 in the line 2. Line 3
initializes the maximum revenue q to -inf, so that the for loop in 4-5 correctly computes q value; line 6 then returns
the value. A simple induction on n proves that this answer is equal to the desired answer rn, using equation.

If you were to code up cut-rod in your favorite programming language and run it on your computer, you would find that
once the input size becomes moderately large, your program would take long  time to run. For n = 40, you would find that
that your program takes at least several minutes, and most likely more than an hour, in ract, you would find that each
time yo increase n by 1, you program's running time would approximately double.

Why is cut-rod so inefficient? The problem is that cut-rod calls itself recursively over and voer again with the same
parameter values; it solves the same subproblems repeatedly.

To analyze teh running time of cut-rod, let T(n) denote the total number of calls made to cut-rod when called with its
second parameter equal to n, this expression equals the number of nodes in subtree whose root is labeled n in the
recursion tree. The count includes the initial call at its root. Thus T(0) = 1 and the initial 1 for the call at the
root, and the term T(j) counts the number of calls (including recursive calls) due to the call cur-rod(p, n-1), where
j = n-1 as exercise 15.1 1-1 asks you to show.

T(n) = 2**n

and so the running time of cut-rod is exponential in n.

In retrospect, this exponential running time is not so surprising. Cut-rod explicitly considers all the 2**n-1 possible
ways of cutting up a rod of length n, the tree of recursive calls has 2**n-1 leaves, one for each possible way of
cutting up the rod, The labels on the simple path from the root to a leaf give the size of each remaining right-hand
piece before making each cut. That is, the labels give the corresponding cut points, measured from the right-hand end
of the rod.

Using dynamic programming optimal rod cutting

We now show how to convert cut-rod into an efficient algorithm, using dynamic programming.

The dynamic programming method works as follows. Having observed that a naive recursive solution is inefficient because
it solves the same subproblems repeatedly. we arrange for each subproblem to be solved only once, saving its solution.
If we need to refer to this subproblem's solution again later, we can just look it up, rather than recompute it. Dynamic
programming thus uses additional memory to save computation time; it serves an example of a time-memory trade-off. The
savings may be dramatic: an exponential time solution may be transformed to a polynomial time solution. A dynamic
programming solution runs in polynomial time when the number of distinct subproblems involved is polynomial in the input
size and we can solve each such subproblem in polynomial time.

There are usually two equivalent ways to implement a dynamic-programming approach. We shall illustrate both of them with
our rod-cutting example.

The first approach is top-down with memoization. In this approach, we write the procedure recursively in a natural
manner, but modified to save the result of each subproblem (usually in an array or hash table). The procedure now first
checks to see whether is has previously solved this subproblem. If so, it returns the saved value, saving further
computation at this level; If not, the procedure computes the value in the usual manner. We say that the recursive
procedure has been memorized; it "remembers" what result it has computed previously.

The second approach is the bottom-up method. This approach typically depends on some natural notion of the "size" of a
subproblem, such that solving any particular sub problem depends only on solving "smaller" subproblems. We sort the
subproblems by size and solve them in size order, smaller first. When solving a particular subproblem, we have already
solved all of the smaller subproblems its solution depends upon, and we have saved their solutions. We solve each
subproblem only once, and when we first see it, we have already solved all of its prerequisite subproblems.

These two approaches yield algorithms with the same asymptotic running time, except in unusual circumstance where the
top-down approach does not actually recurse to examine all possible subproblems. The button-up approach often has much
constant factors, since it has less overhead for procedure calls.

Here is the pseudocode for the top-down cut-rod procedure, with memoization added:

memorized-cut-rod(p, n)
    let r[0..n] be a new array
    for i = 0 to n
        r[i] = -'inf'
    return memorized-cut-rod-aux(p, n, r)

memorized-cut-rod-aux(p, n, r)
    if r[n] >= 0
        return r[n]
    if n == 0
        q = 0
    else q = -'inf'
        for i = i to n
            q = max(q.p[i] + memorized-cut-rod-aux(p, n-1, r))
    r[n] = q
    return q

Here, the main procedure memorized-cut-rod initializes a new auxiliary array r[0..n] with the vale -inf, a convenient
choice with which to denote 'unknown'. (Known revenues values are always non-negative.) it then calls its helper
routine, memorized-cut-rod. It first checks in line 1 to see whether teh desired value is already known and, if it is,
then line 2 returns it. Otherwise, lines 3-7 compute it teh desired value q in the usual manner. line 8 saves it in
r[n], and line 9 returns it.

The bottom-up version is even simpler:

bottom-up-cut-rod(p, n)
    let r[0..n] be a new array
    r[0] = 0
    for j = i to n
        q = -inf
        for i in = 1 to j
            q = max(q.p[i] + r[j - 1])
        r[j] = q
    return r[n]

For bottom-up dynamic programming approach, bottom-up-cut-rod use the natural ordering of the subproblems: a problem of
size i is "smaller" than a subproblem of size j if i < j. Thus, the procedure solves subproblems of size j = 0,1,...,n
in that order.

Line 1 of procedure bottom-up-cut-rod creates a new array r[0..n] in which to save the results of the subproblems, and
line 2 initializes r[0] to 0, since a rod of length 0 earns no revenue. Line 3-6 solve each subproblem of size j, for
j = 1, 2,..n. In order of increasing size. The approach used to solve a problem of a particular size j is the same as
that used by cut-rod, except that line 6 now directly reference array entry r[j-1] instead of making a recursive call
to solve the subproblems of size j-1. Line 7 saves in r[j] the solution to the subproblem of size j. Finaly, line 8
returns r[n], which equals the optimal value rn.

The bottom-up and top-down versions have the same asymptotic running time. The running time of
procedure bottom-up-cut-rod is O1(n**2), due to its doubly-nested loop structure. The number of iterations of its inner
for loop, in the line 5-6, forms an arithmetic series. The running time of its top-down counterpart,
memoized-cut-rod is also O1(n**2), although this running time may be a little harder to see. Because a recursive call
to solve a previously solved problem just once. It solves subproblems for size 0, 1, .. n. To solve a subproblem of
size n, the for loop of lines 6-7 iterates n times. Thus, the total number of iterations of the for loop, over all
recursive calls of memoized-cut-rod. forms an arithmetic series, giving a total of O1(n**2) iterations, just like the
inner for loop of bottom-up-cut-rod. (We actually are suing a form of aggregate analysis here. We shall see aggregate
analysis in detail in section 17.1)

Subproblem graphs

When we think about a dynamic programming problem, we should understand the set of subproblems involved and how
subproblems depend on one another.

The subproblem graph for the problem embodies exactly this information. Figure 15.4 shows the subproblem graph for the
rod-cutting problem with n = 4, it is a directed graph, containing one vertex for each distinct subproblem. The
subproblem graph has a directed edge form the vertex for subproblem x to teh vertex for subproblem y if determining an
optimal solution for subproblem x involves directly considering an optimal solution for subproblem y. For example, the
subproblem graph contains an edge from x to y if a top-down recursive procedure for solving x directly calls itself to
solve y. We can think of the subproblem graph as a 'reduced' or 'collapsed' version of the recursion tree for the
top-down recursive method, in which we coalesce all nodes for the same subproblem into a single vertex and direct all
edges from parent to child.

The bottom-up method for dynamic programming considers teh vertices of the subproblem graph in such an order that we
solve the subproblems y adjacent to a given subproblem x before we solve subproblem x. (Recall from section B 4 that the
adjacency relation is not necessarily symmetric.) using the terminology from chapter 22, in a bottom-up dynamic
programming algorithm, we consider the vertices of the subproblem graph in an order that is a 'reverse topological sort'
or a 'topological sort of the transpose' (see section 22.4) of the subproblem graph. In other words, no subproblem is
considered until all of the subproblems it depends upon have been solved. Similarly, using notions from the same
chapter, we can view the top-down method (with memoization) for dynamic programming as a 'depth first search' of the
subproblem graph (section 22.3).

The size of hte subproblem graph G = (V, E) can help us determine the running time of the dynamic programming algorithm.
Since we solve each subproblem just once. the running time is the sum of the times needed to solve each subproblem.
Typically, the time to compute the solution to a subproblem is proportional to the degree (number of outgoing edges) of
the corresponding vertex in teh subproblem graph. and the number for subproblems is equal to the number of vertices in
the subproblem graph. In this common case, the running time of dynamic programming is linear in the number of vertices
and edges.

Reconstructing a solution

Our dynamic programming solutions to the rod-cutting problem return the value of an optimal solution. But they do not
return actual solution: a list of piece sizes. We can extend the dynamic programming approach to record not only the
optimal value computed for each subproblem. but also a choice that led to the optimal value. With this information. We
can readily print an optimal solution.

Here is an extended version of bottom-up-cut-rod that computers. For each rod size j, not only the maximum revenue rj,
but also sj, the optimal size of the first piece to cut off:

extended-bottom-up-cut-rod(p, n)
    let r[0..n] and s[0..n] be new arrays
    r[0] = 0
    for j = 1 to n
        q = -inf
        for i = 1 to j
            if q < p[i] + r[j-1]
                q = p[i] + r[j-1]
                s[j] = i
        r[j] = q
    return r and s

This procedure is similar to bottom-up-cut-rod. except that it creates the array s in line 1, and it updates s[j] in
line 8 to hold the optimal size i of the first piece to cut of when solving a subproblem of size j.

The following procedure takes a price table p and a rod size n, and it calls extended-bottom-up-cut-rod(p, 10) would
return the following arrays:

A Call to print-cut-cut-rod-solution(p, 10) would print just 10, but a call with n = 7 would print the cuts 1, and 6.
corresponding to the first optimal decomposition fro r7 given earlier.

15.2 matrix-chain multiplication

Our next example of dynamic programming is an algorithm that solves the problem of matrix-chain multiplication. We are
given a sequence (chain) (A1, A2, ... An) of n matrices so be multiplied, and we wish to compute the product
A1A2...An.
We can evaluate the expression using the standard algorithm for multiplying pairs fo matrices as a subroutine once we
have parenthesized it to resolve all ambiguities in how the matrices are multiplied together. Matrix multiplication is
associative, and so all parenthesizations yield the same product. A product of matrices is fully parenthesized if it
is either a single matrix or the product of two fully parenthesized matrix products, surrounded by parentheses. For
example, if the chain of matrices is <A1, A2, A3, A4>, then we can fully parenthesize the product A1A2A3A4 in five
distinct ways:

How we parenthesize a chain of matrices can have a dramatic impact on the cost fo evaluating the product. Consider first
the cost of multiplying two matrices. The standard algorithm is given by the following pseudocode, which generalizes the
square-matrix-multiply procedure from section 4.2. The attributes rows and columns are teh number of rows and columns in
a matrix.

matrix-multiply(A, B)
    if A.columns != B.rows
        error 'incompatible dimensions'
    else
        let C be a new A.rows x B.columns matrix
        for i = 1 to A.rows
            for j = 1 to B.columns
            cij = 0
            for k = 1 to A.columns
                cij = cij + aik*bkj
        return C

We can multiply tow matrices A and B only if they are compatible: the number of columns of a must equal the number of
rows of B. If A is a p x q matrix and B is a q x r matrix, the resulting matrix C is a p x r matrix, the time to
compute C is dominated by the number of scalar multiplications in line 8, which is pqr. In what follows, we shall
express costs in terms of the number of the scalar multiplications.

To illustrate the different costs incurred by different parenthesizations fo a matrix product, consider the problem
of a chain <A1, A2, A3> of the three matrices.

We state the matrix-chain multiplication problem as follows: given a chain <A1.A2....An> of n matrices, where for i = 1,
2, ... n. matrix Ai has dimension pi-1 x pi, fully parenthesize teh product A1A2...An in a way that minimized the number
of scalar multiplications.

Note that in the matrix-chain multiplication problem, we are not actually multiplying matrices. Our goal is only to
determine an order for multiplying matrices that has the lowest cast. typically, the time invested in determining this
optimal order is more than paid for by the time saved later on when actually performing the matrix multiplications
(such as performing only 7500 scalar multiplications instead of 75,000)

Counting the number of parenthesizations

Before solving the matrix-chain multiplication problem by dynamic programming, let us convince ourselves that
exhaustively checking all possible parenthesizations does not yield an efficient algorithm. Denote the number of
alternative parenthesizations of a sequence of n matrices by P(n). When n = 1, we have just one matrix and therefore
only one way to fully parenthesize the matrix product, When n >= 2, a fully parenthesize matrix product is the product
of two fully parenthesize matrix subproducts, and the split between the two subproducts may occur between teh kth and
(k+1)st matrices for any k = 1, 2, .. n -1. Thus we obtain the recurrence.

Problem asked you to show that the solution to a similar recurrence is the sequence of Catalan numbers, which grows as
M(4**n/N**3/2). A simple exercise is to show that the solution to the recurrence is M(2**n). The number of solutions is
thus exponential in n, and the brute-foce method of exhaustive search makes for a poor strategy when determining how to
optimally parenthesize a matrix chain.

Applying dynamic programming

We shall use the dynamic programming method to determine how optimally parenthesize a matrix chain. In so doing, we
shall follow the four-step sequence that we stated at the beginning of this chapter.
1. Characterize the structure of an optimal solution.
2. Recursively define the value of an optimal solution.
3. Compute the value of an optimal solution.
4. Construct an optimal solution from computed information.

We shall go through these steps in order, demonstrating clearly how we apply each step to the problem.

Step 1: The structure of an optimal parenthesization

For our first step in teh dynamic programming paradigm, we find the optimal substructure and then use it to construct
an optimal solutioin to the problem from optimal solution to subproblems. In the matrix-chain multiplication problem,
we can perform this step as follows, Fore convenience, let us adopt the notation Ai..j, where i <= j, for the matrix
that results from evaluating the product Ai Ai+1 .. Aj. Observe that if tht the problem is nontrivial, i.e. i < j, then
no parenthesize the product Ai Ai+1 .. Aj, we must split th product between Ak and Ak+1 for some integer k in range
i <= k < j. That is, for some value of k, we first compute the matrices Ai..k and Ak+1 and then multiply them together
to produce teh final product Ai..j.

The optimal substructure of this problem is as follows, suppose that to optimally parenthesizing AiAi+1...Aj, we split
the product between Ak and Ak+1, then the way we parenthesize the 'prefix' subchain Ai Ai+1...Ak within this optimal
parenthesization of AiAi+1...Aj must be an optimal parenthesization of AiAi+i...Ak. Why? If there were a less costly way
to parenthesization in the optimal parenthesization of AiAi+i...Aj to produce another way to parenthesize AiAi+1..Aj
whose cost was lower than teh optimum: a contradiction. A similar observation holds for how we parenthesize the
subchain Ak+1 Ak+2 ... Aj in the optimal parenthesization of Ai Ai+1 .. Aj: it must be an optimal parenthesization of
Ak+1 Ak+2 ... Aj.

Now we use our optimal substructure to show that we can construct an optimal solution to the problem from optimal
solutions to subproblems. We have seen that any solution to a nontrivial instance of the matrix-chain multiplication
problem requires us to split the product, and that any optimal solution contains within it optimal solutions to
subproblem instances. Thus, we can built an optimal solution to an instance fo teh matrix-chain multiplication problem
by splitting the problem into two subproblems (optimally parenthesizing Ai Ai+1 ... Ak and Ak+1, Ak+2 ... Aj).
finding optimal solutions to subproblem instance. Thus, we can build an optimal solution to an instance of the
matrix-chain multiplication problem by splitting the problem into two subproblem (optimally parenthesizing). finding
optimal solutions to subproblem instance, and then combining these optimal subproblem solutions. We must ensure that
when we search for correct place to split the product, we have considered all possible places, so that we are sure of
having examined the optimal one.

Step 2: A recursive solution

Next, we define teh cost of an optimal solution recursively in terms of the optimal solutions to subproblems. For the
matrix-chain multiplication problem, we pick as our subproblems teh leetcode of determining the minimum cost of
parenthesizing be the minimum number of scalar multiplications needed to compute the matrix Ai..j; for the full problem,
the lowest-cost way to compute A1..n roudl thus be m[1..n]

We can define m[i.j] recursively as follows. If i = j, the problem is trivial; the chain consists of just one matrix
Ai,j = Ai, so that no scalar multiplications are necessary to compute the product, that m[i,j] = 0, for i = 1, 2 ..n.
To compute m[i,j] when i < j, we take advantage of the structure of an optimal solution from step 1. Let us assume that
to optimal parenthesize, we split the product Ai Ai+1 ... Aj, between Ak and Ak+1. where i <= k < j. then m[i, j] equals
the minimum cost for computing the sub-products Ai..k takes pi-1 pk pj scalar multiplications. Thus, we obtain.

This recursive equation assumes that we know the value of k, which we do not. There are only j-i possible value of k,
however, namely k = i, i + i .. j-1. Since the optimal parenthesization must use one of these values for k, we need only
check them all to find the best. Thus, our recursive definition for the minimum cost of parenthesizing the product
becomes

The min[i,j] value give the costs of optimal solutions to subproblems, but they do not provide all the information we
need to construct an optimal solution. To help us do so, we define s[i, j] equals a value k such that m[i, j] = m[i, k]
+ m[k+1, j] + pi-1pkpj

Steps 3: Computing the optimal costs.

At this point, we could easily write a recursive algoritm based on recurrence to compute the minimum cost for
multiplying. We saw for the rod-cutting problem. and we we shall see the section 15.3, this recursive algorithm takes
exponential time. which is no better than the brute-force method of checking each way of parenthesizing the product.
"""