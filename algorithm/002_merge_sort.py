"""
MERGE(A, p, q, r)
    n1 = q - p + 1
    n2 = r - q
    Let L[1 .. n1 + 1] and R[1, n2 + 1] be new arrays
    for i = 1 to n1
        L[i] = A[p + i - 1]
    for j = 1 to n2
        R[j] = A[q + j]
    L[n1 + 1] = 'inf'
    R[n2 + 1] = 'inf'
    i = 1
    j = 1
    for k = p to r
        if L[i] <= R[j]
            A[k] = L[i]
            i += 1
        else
            A[k] = R[j]
            j += 1

MERGE-SORT(A, p, r)
    if p < r
        q = [(p + r)//2]
        MERGE-SORT(A, p, q)
        MERGE-SORT(A, q + 1, r)
        MERGE(A, p, q, r)
"""


def merge_sort(nums, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(nums, p, q)
        merge_sort(nums, q + 1, r)
        merge(nums, p, q, r)


def merge(nums, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    left = [float('inf')] * (n1 + 1)
    right = [float('inf')] * (n2 + 1)

    for i in range(n1):
        left[i] = nums[p + i]
    for j in range(n2):
        right[j] = nums[q + j + 1]

    i, j = 0, 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1


nums = [5, 2, 4, 7, 1, 3, 2, 6]
p = 0
r = len(nums) - 1
merge_sort(nums, p, r)
print(nums)


"""
2.3.2 Analyzing divide and conquer algorithms

When an algorithm contains a recursive call to itself, we can often describe its running time by a recurrence equation
or recurrence, which describes the overall running time on a problem of size n in terms of the running time and 
smaller inputs. We can then use mathematical tools to solve the recurrence and provide bounds on the performance of the 
algorithm.

A recurrence for the running time of the divide and conquer algorithm falls out from the three steps of the basic 
paradigm. As before, we let T(n) be the running time on a problem of size n. If the problem size is small enough, say
n <= c for some constant c, the straightforward solution takes constant time, which we write as O(1). Suppose that our 
division of the problem yields a sub-problems, each of which is 1/b the size of the original. (For merge sort, both a 
and b are 2, but we shall see many divide and conquer algorithm in which a != b.) It takes time T(n/b) to solve one 
problem of size n/b, and so it takes time aT(n/b) to solve a problem o of them. If we take D(n) time to divide the 
problem into subproblems and C(n) time to combine the solution to the subproblems into the solution to the original
problem, we get the recurrence

In chapter 4, we shall see how to solve common recurrences of this form.



"""
