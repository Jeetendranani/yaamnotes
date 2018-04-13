"""
494. Target Sum

You are given a list of non-negative integers, a1, a2, ... an, and a target S. Now you have 2 symbols + and -. For each
integer, you should choose one from + or - as its new symbol.

Find our how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
input: nums is [1, 1, 1, 1, 1], S is 3.
output: 5
explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be targets.

Note:
    1. The length of the given array is positive and will not exceed 20
    2. the sum of elements in the given array will not exceed 1000
    3. Your output anser is guaranteed to be fitted in 32-bit integer
"""


class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        def calculate(nums, pos, total, S):
            if pos == len(nums) - 1:
                if total == S:
                    self.count += 1
                return
            calculate(nums, pos + 1, total + nums[pos+1], S)
            calculate(nums, pos + 1, total - nums[pos+1], S)

        self.count = 0
        calculate(nums, 0, nums[0], S)
        calculate(nums, 0, -nums[0], S)

        return self.count


s = Solution()
total = s.findTargetSumWays([10,9,6,4,19,0,41,30,27,15,14,39,33,7,34,17,24,46,2,46], 45)

print(total)


"""
Approach 2: Recursion with memoization

Algorithm

It can be easily observed that the last approach, a lot of redundant function calls could be made with the same value of 
i as the current index and the same value of sum as the recurrent sum, since the same values could be obtained through 
multiple paths in the recursion tree. Tin oder to remove this redundancy, we make use of memoization as well to store
the result which have been calculated earlier.

Thus, for every call to calculate(nums, i, sum, S), we store the obtained in memo[i][sum + 1000]. the factor of 1000 has
been added as an offset to the sum value to map all the sums possible to positive integer range. By making using the
memoization, we can prune the search space to a good extend.
"""