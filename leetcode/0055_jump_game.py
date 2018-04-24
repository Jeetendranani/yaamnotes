"""
55. Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:

A = [2, 3, 1, 1, 4], return True
A = [3, 2, 1, 0, 4], return False


Naming

- We call a position in the array a "good index" if starting at that position, we can reach the last index. Otherwise,
that index is called a 'bad index'. The problem then reduces to whether or not index 0 is a 'good index'.

Solution

This is a dynamic programming question. Usually, solving and fully understand a dynamic programming leetcode is a 4
step progress:

1. start withe the recursive backtracking solution
2. optimized by using a memoization table (top-down dynamic process)
3. remove the need for recursion (bottom-up dynamic programming)
4. Apply final tricks to reduce the time/ memory complexity.

All solutions presented below produce the correct result, but they differ in run time and memory requirements.

Approach 1: Backtracking

This is the inefficient solution where we try every single jump pattern that takes us from the first position to the
last. We start from the first position and jump to every index that is reachable, we repeat the process until last
index reached, when stuck, backtrack.

Approach 2: Dynamic programming top-down

Approach 3: Dynamic programming bottom-up

Approach 4: Greedy
"""


class Solution:
    def can_jump(self, nums):
        position = 0
        for i in range(len(nums)):
            position = max(position, i + nums[i])
            if position >= len(nums) - 1:
                return True
            if position <= i:
                return False
