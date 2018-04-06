"""
788. Rotated Digits

X is a good number if after rotating digit individually by 180 degrees, we get a valid number that is different from X.
Each digit must be rotated - we cannot to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to
each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become
invalid.

Now given a positive number N, how many number X from 1 to N are good?

Example:
    Input: 10
    Output: 4
    Explanation:
    There are four good numbers in the range [1, 10]: 2, 5, 6, 9.

    Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:
    N will be in range [1, 10000].

Approach 1: Brute force

Intuition:

For each X from 1 to N, let's analyze where X is good.
    - If X has a digit does not have valid rotation (3, 4, or 7), then it can't be good.
    - If X doesn't have a digit that rotate to a different digits (2, 5, 6, 9), it can't be good because X will be the
    same after rotation.
    - Otherwise, x will successfully rotate to a valid different number.

Algorithm

To handle checking the digits of X, we showcase two implementations. The most obvious way is to parse the string;
Another way is to recursively check the last digits of X.

See the comments in each implementation for more details.
"""


class Solution:
    def rotatd_digits(self, n):
        ans = 0

        for x in range(1, n+1):
            s = str(x)

            ans += (all(d not in '347' for d in s)
                    and any(d in '2569' for d in s))
        return ans


"""
Approach 2: Dynamic Programming On Digits

Intuition

Say we are writing a good number digit by digit. The necessary and sufficient conditions are: we need to write using 
digits from 0125689, write a number less than or equal to N, and write at least one digit from 2569. 

We can use dynamic programming to solve this efficiently. Our state will be how many digits i we have written, 
whether we have previously written a j th digit lower than the jth digit of N, and whether we have previously written
a digit from 2569. We will represent this state by three variables: i, equality_flag, involution_flag.

dp(i, equality_flag, involution_flag) will represent the number of ways to write the suffix of N corresponding to these
above conditions. The answer we want is dp(0, True, False).

Algorithm 

If equality_flag is true, the ith digit (0 indexed) will be at most the ith digit of N. For each digit d, we determine
if we can write d based on the flags that are currently set.

In the below implementations, we showcase both top-down and bottom-up approaches. The four lines the top-down approach
(Python) from for d in range(... to before memo[...] = ans clearly illustrates the recursive relationship between 
states in our dynamic programming.
"""


class Solution(object):
    def rotate_digits(self, n):
        A = map(int, str(n))

        memo = {}

        def dp(i, equlity_flag, involution_flag):
            if i == len(A):
                return +involution_flag

            if (i, equlity_flag, involution_flag) not in memo:
                ans = 0
                for d in range(A[i] + 1 if equlity_flag else 10):
                    if d in {3, 4, 7}:
                        continue
                    ans += dp(i + 1, equlity_flag and d == A[i], involution_flag or d in {2, 5, 6, 9})
                memo[i, equlity_flag, involution_flag] = ans
            return memo[i, equlity_flag, involution_flag]

        return dp(0, True, False)