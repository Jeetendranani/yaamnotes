"""
Problems

2-1 Insertion sort on small arrays in merge sort

Although merge sort runs in O(n lgn) worst-case and insertion sort runs in O(n**2) worst case time, the constant
factors in insertion sort can make it faster in practice for small problem sizes on many machines, Thurs, it makes
sense to coarsen the leaves of the recursion by using insertion sort with the merge sort when subproblem become
sufficiently small. consider a modification on merge sort in which n/k sublists of length k are sorted suing insertion
sort and the merge using teh standard merging mechanism, where k is a value to be determined.

a. Show that insertion sort can sort the n/k sublists, ech of length k, in O(nk) worst-case time.

b. Show how to merge the sublists in O(n lo(n/k)) worst-case time.

c. Given that the modified algorithm runs in O(nk + n lg(n/k) worst-case time, what is the largest value of k as
function of n for which the modified algorithm has the same running time as standard merge sort, in terms of
O - notation?

d. How should we choose k in practice?

2-2 Correctness of bubblesort

Bubble sort is a popular, but inefficient, sorting algorithm. It works by repeatedly swapping adjacent elements that
are out of order.

BUBBLESORT(A)
    for i = 1 to A.length - 1
        for j = A.length - 1 down to i + 1
            if A[j] < A[j - 1]
                exchange A[j] with A[j - 1]
"""


def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]


nums = [9,8,7,6,3,4,5,2,0,1]
bubble_sort(nums)
print(nums)