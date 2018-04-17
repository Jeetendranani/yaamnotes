"""
673. Number of Longest Increasing Subsequence

Given an unsorted array of integers. find the number of longest increasing subsequence.

Example 1:
input: [1, 3, 5, 4, 7]
output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
input: [2, 2, 2, 2, 2]
output: 5
Explanation: the length of longest continuous increasing subsequence is 1, and there are 5 subsequence's length is 1,
so output 5.

Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

Approach 1: Dynamic Programming

Intuition and Algorithm
Suppose for sequences ending at nums[i], we knew the length length[i] of the longest sequences, and the number count[i]
of such sequences with that length.

For every i < j with A[i] < A[j], we might append A[j] to a longest subsequence ending at A[i]. It means that we have
demonstrated count[i] subsequence of length[i] + 1.

Now if those sequences are are longer than length[j], then we know we have count[i] sequence of this length. If these
sequences are equal in length length[j], then we know that there are now count[i] additional sequences to be counted of
that length (ie. count[j] += count[i]).
"""


class Solution(object):
    def find_number_of_lis(self, nums):
        N = len(nums)

        if N <= 1:
            return N

        lengths = [0] * N
        counts = [0] * N

        for j, num in enumerate(nums):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)


