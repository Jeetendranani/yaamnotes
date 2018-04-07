"""
4. Divide and conquer

In section 2.3.1, we saw how merge sort serves as an example of the divide and conquer paradigm. Recall that in divide
and conquer, we solve a problem recursively, applying three stesp at each level of the recursion:

Divide the problem into a number of subproblems that are smaller instance of the same problem.
Conquer the subproblems by solving them recursively. If the subproblem sizes are small enough, however, just solve the
subproblems in a straightforward manner.
Combine the solutions to the subproblems into the solution for the original problem.

When the subproblems are large enough to solve recursively, we call that the recursive case. Once the subproblems
become small evough that we no longer recurse, we say the recursion "bottoms out" and that we have gotten down to the
base case. Sometimes, in addition to subproblems that are smaller instance of the same problem, we consider solving such
subproblems as part of combine step.

In this chapter, we shall see more algorithms based on divide and conquer. The first one solves the maximum subarray
problem: it takes as input an array of numbers, and it determines the contiguous subarray whose values have the greatest
sum. Then we shall see two divide and conquer algorithm for multiplying n x n matrices. One runs in O(n**3) time, which
is no better than the straightforward method of multiplying square matrices. But the other, Strassen's algorithm, runs
in O(n**2.81) time, which beats the straightforward method asymptotically.

Recurrences

Recurrences go hand in hand with the divide and conquer paradigm, because they give us a natural way to characterize
the running times of divide and conquer algorithms. A recurrence is an equation or inequality that describes a function
in terms of its value on smaller inputs. For example, in section 2.3.2 we described the worst-case running time T(n) of
the MERGE-SORT procedure by the recurrence whose solution we claimed to be T(n) = O(n lgn).

Recurrences can take many form. For examples, a recursive algorithm might divide subproblems into unequal sizes, such
as 2/3 and 1/3 split. If the divide and combine steps take linear time, such an algorithm would give rise to the
recurrence T(n) = T(2n/3) + T(1n/3) + O(1).

Subproblems are not necessarily constrained to being a constant fraction of the original problem size. for example, a
recursive version of linear search would create just one subproblem containing only one element fewer than the
original problem. Each recursive call would take constant time plus the time for the recursive call it makes, yielding
the recurrence T(n) = T(n-1) + O(1).

This chapter offers three methods for solving recurrences - that is, for obtaining asymptotic O or O1 bounds on the
solution:

- In the substitution method, we guess a bound and then use mathematical induction to prove our guess correct.
- The recursion-tree method converts the recurrence into a tree whose nodes represent the cost incurred at various
levels of the recursion. We use techniques for bounding summations to solve the recurrence.
- The master method provides bounds for recurrences of the form T(n) = aT(n/b) + f(n) where a >= 1, b > 1, and f(n) is
a given function. such recurrences arise frequently. A recurrence of the form in equation characterizes a divide and
conquer algorithm that create a subproblems, each of which is 1/b the size of the original problem, and in which the
divide and combine steps together take f(n) time.

To use the master method, you will need to memorize three cases, but one you do that, you will easily be able to
determine asymptotic bounds for many simple recurrences. We will use the master method to determine the running  times
of the divide and conquer algorithms for the maximum subarray problem and for matrix multiplication, as well as for
other algorithms based on divide and conquer elsewhere in this book.

Occasionally, we shall see recurrences that are not equalities but rather inequalities, such as T(n) <= 2T(n/2) + O1(n).
Because such a recurrence states only an upper bound on T(n), we will couch its solution using O-notation rather than
O1-notation. Similarly, if the inequality were reversed to T(n) >= 2T(n/2) + O1(n), then because the recurrence gives
only a lower bound on T(n), we would use M-notation.

Technicalities in recurrences

In practice, we neglect certain technical details when we state and solve recurrences. For example, if we call Merge
sort on n elements, when nis odd, we end up with subproblem of size [n/2] and [n/2]. Neither size is actually n/2,
because n/2 is not integer when n is odd, Technically, the recurrence describing the worst-case running time of
Merge-sort is really.

Boundary conditions represent another class of the details that we typically ignore. Since the sunning time of an
algorithm on a constant-sized input is a constant, the recurrences that arise from teh running times of algorithms
generally have T(n) = O1(1) for sufficiently small n. consequently, for convenience, we shall generate omit statements
of the boundary conditions of recurrences and assume that T(n) is constant for small n. For example, we normally
state recurrence as T(n) - 2T(n/2) + O1(n). without explicitly giving values for small n. The reason is that although
changing the value of T(1) changes the next solution to the recurrence, the solution typically doesn't change by more
than constant factor, and so the order of growth is unchanged.

When we state and solve recurrences, we often omit floors, ceilings, and boundary conditions. We forge ahead without
these details and later determine whether or not they matter. They usually do not, but you should know when they do.
Experience helps, and so do some theorems stating that these details do not affect the asymptotic bounds of many
recurrences characterizing divide and conquer algorithms. In this chapter, however, we shall address some of these
details and illustrate the fine points of recurrence solution methods.

4.1. The maximum subarray problem

Suppose that you been offered the opportunity to invest in the Volatile Chemical Corporation. Like the chemicals the
company produces, the stock price of the volatile chemical corporation is rather volatile. You are allowed to buy one
unit of stock only one time and sell it at a late day, buying and selling after the close of trading for the day. To
compensate for this restriction, you are allowed to learn what the prices will be in the future. your goal is no
maximize your profit. Figure 4.1 shows the price of the stock over a 17-day period. You may buy the stock at any one
time, starting after day 0, when hte price is $100 per share, of course you would want to "buy low, sell high" - buy at
the lowest possible price and later on sell at the highest possible price - to maximize your profit. Unfortunately,
you might not be able to buy at the lowest prices and them sell at the highest price within a given period. In Figure
4.1 the lowest price occurs after day 7, which occurs after the highest prices, after day 1.

You might think that you can always maximize profit by either buying at the lowest prices or selling at the highest
price. For example, in Figure 4.1, we would maximize profit buying at the lowest price after day 7. If this strategy
always worked, then it would be easy to determine how to maximize profit find the highest and the lowest prices, and t
hen work left from the highest later price, and take teh pair with the greater difference. Figure 4.2 shows a simple
counterexample. demonstrating that teh maximum profit sometimes comes neither by buying at eh lowest price nor by
selling at the highest price.

A brute-force solution

We can easily devise a brute-force solution to this problem just try every possible pair of buy and cell dates in which
the buy date precedes the sell date. A period of n days has (n/2) such pairs of dates. Since (n/2) is O1(n**2), and the
best we can hope for is to evaluate each of dates in constant time, this approach would take M(n**2) time, can we do
better?

A transformation

In order to design an algorithm with an O(n**2) running time, we will look at the input in a slightly different way.
We want to find a sequence of days over which the net change from the first day to the last is maximum. Instead of
looking for at the daily prices, let us instead consider the daily change in price, where the change on dai i is the
difference between the prices after day i - 1, and after day i. The table in Figure 4.1 shows these daily changes in
the bottom row. If we treat this row as an array A, shown in Figure 4.3, we now wan tto find the nonempty, contiguous
subarray of A whose values have the largest sum. We call this contiguous subarray the maximum subarray.
"""