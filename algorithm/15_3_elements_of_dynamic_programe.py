"""
15.3. Elements of dynamic programming

Although we have just worked through two examples of the dynamic programming method. you might still be wondering just
when the method applies. From an engineering perspective, when should we look for a dynamic programming solution to a
problem? In  this section, we examine the two key ingredients that an optimization problem must have in order for
synamic programming to apply: optimal substructure and overlapping subproblems. We also revisited and discuss more fully
hwo memoization might help up take advantage of the overlapping subproblems property in the top-down recursive approach.

Optimal substructure

The first step in solving an optimization problem by dynamic programming is to characterize the structure of an optimal
solution. Recall that a problem exhibits optimal substructure if an optimal solution to the problem contains within
it optimal solution to subproblems. Whenever a problem exhibits optimal substructure, we have a good clue that dynamic
programming might apply. (As chapter 16 discuss, it also might mean that a greedy strategy applies, however) in dynamic
programming, we build an optimal solution to teh problem from optimal solutions to subproblems. Consequently, we must
take care to ensure that the range of subproblems we consider includes those used in an optimal solution.

We discovered optimal substructure in both of the problems we have examined in this chapter so far. In section 15.1, we
observed that the optimal way of cutting up a rod of length n( if we make any cuts at all) involves optimally cutting up
the two pieces resulting from the fist cut, In section 15.2, we observed that an optimal parenthesizing of A that spits
the product between Ak an Ak+1 contains within it optimal solutions to the problems of parenthesizing.

you will find yourself following a common pattern in discovering optimal substructure:

1. you show that a solution to the problem consists of making a choice, such as choosing an initial cut in a rod or
choosing an index at which to split the matrix chain. Making this choice leaves one or more subproblems to be solved.

2. you suppose that for a given problem, you are given the coice that leads to an optimal solution. you do not concern
yourself yet with how to determine this choice. You just assume that it has been given to you.

3. Given this choice, you determine which subproblems ensure and how to best characterize the resulting space of
subproblems.

4. You show that the solutions to the subproblems used within an optimal solution to the problem must themselves be
optimal by using a 'cut and paste' technique. You do so by supposing that each of subproblem solution is not optimal
and then deriving a contradiction. In particular, by 'cutting out' the non-optimal solution to each subproblem and
'pasting in' the optimal one, you show that you can get a better solution to the original problem, thus contradicting
your supposition tht you already had an optimal solution. If an optimal solution gives rise to more than one
subproblem, they are typically so similar that you can modify the cut and paste argument for one ot apply to the other
with little effort.

To characterize the space of subproblems, a good rule of thumb says to try to keep the space as simple as possible and
then explained it as necessary. For example, the space of subproblems that we considered for the rod-cutting problem
contained the of optimal cutting up a rod of length i for each i. This subproblem space worked well, and we ahd no need
to try a more general space of subproblems.

Conversely, suppose that we had tried to constrain our subproblem space for matrix-chain multiplication to matrix
products of the form before an optimal parenthesization must split this product between and from some . Unless we could
guarantee that k always equals j - 1, we would find tht we had subproblems of hte form and, and that the latter
subproblem is not of the form. For this problem, we needed to allow our subproblems to vary at 'both ends', that is, to
allow both i and j to vary in the subproblem.

Optimal substructure varies across problem domains in tow ways:

1. How many subproblems can optimal solution to the original problem uses, and

2. how many choices we have in determining which subproblems(s) to use in an optimal solution.

In the rod-cutting problem, an optimal solution for cutting up a rod of size n uses just one subproblem (of size n - 1),
but we must consider n choices for i in order to determine which one yield an optimal solution. Matrix-chain
multiplication for the subchain serves as an example with tow subproblem and j-1 choices. For a given matrix at which we
split the product, we have two subproblems parenthesizing and parenthesizing and we must solve both of them optimally.
Once we determine the optimal solutions to subproblems, we choose form among candidates for the index k.

Informally, the running time of a dynamic programming algorithm depends on the product of two factors: the number of
subproblems overall and how many choice we look at for each subproblem. In rod cutting, we has ((n) subproblems overall,
and at most n choices to examine for each, yielding an O(n**2) running time.

Usually, the subproblem graph gives an alternative way to perform the same analysis. Each vertex corresponds to a
subproblem, and the choices for a problem are the edges incident to that subproblem. Recall that in rod cutting, the
subproblem graph had n vertices and at most n edges per vertex, yielding an O(n) running time. For matrix-chain
multiplication, if we were to draw the subproblem graph, it would have O1(n**2) vertices and each vertex would have
degree at most n-1, giving a total of O(n**3) vertices and edges.

Dynamic programming often use optimal substructure in a bottom-up fashion. This is, we first find optimal solutions to
subproblems and having solved the subproblems, we find aan optimal solution to the problem. Finding an optimal solution
to the problems, entails making a choice among subproblems as to which we will use in solving the problem. The cost of
the problem solution is usually the subproblem costs plus a cost that is directly attributable to the choice itself. In
rod cutting.

In chapter 16, we shall examine 'greedy algorithms' which hve many similarities to dynamic programming. In particular,
problems to which greedy algorithms apply have optimal substructure. One major difference between greedy algorithms and
dynamic programming is that instead of first finding optimal solutions to subproblems and then making an informed
choice, greedy algorithms first make a greedy choice - the choice that looks best at the time - and then solve resulting
subproblem, without bothering to solve all possible related smaller problems. Surprisingly, in some cases this strategy
works!

Subtlities

You should be careful not to assume tht optimal substructure applies when it does not. Consider the following two
problems in which we are gien a directed graph G = (V, E) and vertices u, v belongs to V.

Overlapping subproblems

Reconstructing an optimal solution

As a practical matter, we often store which choice we made in each subproblem in a table ao that we do not have to
reconstruct this information from the costs that we sored.

Fore matrix-chain multiplication, the table s[i, j] saves us a significant amount of work when reconstructing an
optimal solution. Suppose that we did not maintain the s[i,j] table, having filed in only the table m[i, j] containing
optimal subproblem costs. We choose from among j -i possibilities when we determining which subproblems to use in an
optimal solution to parenthesizing and is not a constant. Therefore, it would take O1(1) item to reconstruct which
subproblems we chose from a solution to given problem, by storing in s[i, j] the index of the matrix at which we split
the product, We can reconstruct each choice in O(1) time.

Memoization
"""