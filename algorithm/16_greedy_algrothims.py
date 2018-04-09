"""
16. Greedy Algorithms

Algorithms for optimization problems typically go through a sequence of steps, with a set of choices at each step. For
many optimization problems, using dynamic programming to determine the best choices is overkill; simpler, more efficient
algorithms will do. A greedy algorithm always makes the choice that looks best at the moment. That is, it makes a
locally optimal choice in the hope that this choice will lead to a globally optimal solution. This chapter explores
optimization problems for which greedy algorithms provide optimal solutions. Before reading chapter, you should read
abut dynamic programming in chapter 15, particularly section 15.3.

Greedy algorithms fo not always yield optimal solutions, but for many problems they do. We shall first examine, in
section 16.1, a simple but nontrivial problem, the activity-selection problem, for which a greedy algorithm efficiently
computes an optimal solution. We shall arrive at the greedy algoritm by first considering a dynamic programming
approach and then showing that we can always make greedy choices to arrive at an optimal solution. section 16.2 reviews
the basic elements fo teh greedy approach, giving a direct approach for proving greedy algorithms correct. Section 16.3
presents an important application of greedy techniques: designing data compression (Huffuman) codes, In section 16.4,
we investigate some of the theory underlying combinatorial structures called "matroids" for which a greedy algorithm
always produces an optimal solution. Finally, section 16.5 applies matroids to solve a problem of scheduling unit-time
tasks with deadlines and penalties.

The greedy method is si quite powerful and words well for a wide range of problems, Later chapters will present many
algorithm that we can view as applications of the greedy method, including minimum spanning tree algorithm, Digkstr's
algorithm for shortest paths form a single source. and Chvatil's greedy set covering heuristic. Minimum spanning tree
algorithms furnish a classic example fo the greedy method, Although you can read this chapter and chapter 23
independently of each other. you might find it useful to read them together.

16.2 Elements of the greedy strategy

A greedy algorithm obtains an optimal solution to a problem by making a sequence of choices. At each decision point,
the algorithm makes choice that seems best at the moment. This heuristic strategy does not always produce an optimal
solution, but as we saw in the activity selection problem, sometimes it does, this sectin discusses some of the general
properties of greedy methods.

The process that we followed in section 16.1 to develop a greedy algorithms was a bit more involved than is typical.
We went through the following steps:

1. Determine the optimal substructure of the problem

2. Develop a recursive solution.

3. Show that if we make the greedy choice, then only one subproblem remains.

4. Prove that it is always safe to make the greedy choice.

5. Develop a recursive algorithm that implements the greedy strategy.

6. Convert the recursive algorithm to an iterative algorithm.

In going through these steps, we saw in great detail teh dynamic programming underpinnings of a greedy algorithm. For
example, in the activity-selection problem, we first defined the subproblems Sij, where both i and j varied. We then
found that if we always made the greedy choice, we could restrict the subproblems to be of the form Sk.

Alternatively, we could have fashioned our optimal substructure with a greedy choice in mind, so that the choice leaves
just one subproblem to solve. In the activity-selection problem, we could have started by dropping the second subscript
and defining subproblems of the form Sk. Then, we could have proven that a greedy choice (the first activity am to
finish in Sk), combined with an optimal solution to the remaining set sm of compatible activities, yield an optimal
solution to Sk. More generally, we design greedy algorithms according to the following sequence of steps:

1. Cast the optimization problem as one in which we make a choice and are left with one subproblem to solve.

2. Prove that there is always an optimal solution to the original problem that problem that makes the greedy choice, so
that the greedy choice is always safe.

3. Demonstrate optimal substructure by showing that, having made the greedy choice, what remains is a subproblem with
the property that if we combine an optimal solution to the subproblem with the greedy choice we have made, we arrive at
an optimal solution to the subproblem with the greedy choice we have made, we arrive at an optimal solution to the
original problem.

We shall use this more direct proess in later sections of this chapter, Nevertheless, beneath every greedy algorithm,
there is almost always a more cumbersome dynamic-programming solution.

How can we tell whether a gredy algorithm will solve a particular optimization problem? no way works all the time, but
the greedy-choice property and optimal substructure are the two key ingredients. If we can demonstrate that the problem
has these properties, then we are well on the way to developing a greedy algorithm for it.

Greedy choice property

The first key ingredient is the greedy choice property: we can assemble a globally optimal solution by making local
optimal (greedy choices. In other words, when we are considering which choice to make, we make the choice that looks
best in the current problem. without considering results from subproblems.

Here is where greedy algorithms differ from dynamic programming. In dynamic programming, we make a choice at each step,
but the choice usually depends on the solutions to subproblems. Consequently, we typically solve dynamic programming
problems in a bottom up manner, progressing from smaller subproblems to larger subproblems. (Alternatively, we can
solve them top down, but memoizing. Of course, even though the code works top down, we still must solve the subproblem
before making a choice.) In a greedy algorithm, we make whatever choice seems best at the moment and then solve the
subproblem that remains. The choice made by greedy algorithm may depend on choices so far, but it cannot depend on any
future choices or on the solutions to subproblems, thus unlike dynamic programming, which solves the subproblems before
making the first choice, a greedy algorithm makes its fist choice before solving any subproblems. A dynamic programming
algorithm proceeds bottom up, whereas a greedy strategy usually progresses in a top down fashion, making one greedy
choice after another, reducing each given problem instance to a smaller one.

Of course, we must prove that a greedy choice at each step yields a globally optimal solution. Typically, as in the case
of Theorem 16.1, the proof examines a globally optimal solution to some subproblem. It then shows how to modify the
solution to substitute the greedy choice for some other choice, resulting in one similar, but smaller, subproblem.

We can usually make teh greedy choice more efficiently that we have to consider a wider set of choices.

Optimal substructure

A problem exhibits optimal substructure if an optimal solution to the problem contains within it optimal solutions to
assessing the applicability of dynamic programming as well as greedy algorithms.

We usually use a more direct approach regarding optimal substructure when applying it to greedy algorithm. As mentioned
above, we have the luxury of assuming that we arrived at a subproblem by having made the greedy choice in the
subproblem, combined with the greedy choice already made, yields an optimal solution to the original problem. This
schema implicitly uses induction on the subproblems to prove that making the greedy choice at every steps produces an
optimal solution.

Greedy versus dynamic programming

Because both the greedy and dynamic programming strategies exploit optimal substructure, you might be tempted to
generated a dynamic programming solution to a problem when a greedy solution suffices or conversely, you might
mistakenly think that a greedy solution works when in fact a dynamic programming solution is required. To illustrate
the subtlities between the two techniques, let us investigate tow variants of a classical optimization problem.

The 0-1 knapsack problem is the following. A thief robbing a store finds n items. Thi ith item is worth vi, dollars and
weighs wi pounds, where he an carry at most W pounds in his knapsack, for some integer W. which items should be take?
(We call this the 0-1 knapsack problem because for each item, the thief must either take it or leave it behind; he can't
take fractional amount of an item or take an item more than once).

In the fractional knapsack problem, the setup is the same, but the thief can take fraction of items, rather having to
make a binary choice for each item. You can think of an item in the 0-1 knapsack problem as being like gold ingot and an
item in the fraction knapsack problem
"""