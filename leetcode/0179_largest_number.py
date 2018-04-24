"""
179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note the result may be every large, so you need to return a string instead of an integer.

Approach 1: Sorting via custom comparator

Intuition

To construct the largest number, we want to ensure that the most significant digits are occupied by the largest digits.

Algorithm:

First, we convert each integer to a string. Then, we sort the array of strings.

While it might be tempting to simply sort the numbers in descending order, this causes leetcode for set of numbers with
the same leading digits. For example, sorting the problem example in descending order would produce the number 9534303,
while the correct answer can be achieved by transposing the 3 and 30. Therefore, for each pairwise comparison during
the sort, we compare the numbers achieved by concatenating the pair in both orders. We can prove that this sorts into
the proper order as following:

Assume that (without loss of generality), for some pair of integers a and b, our comparator dictates that a should
preceding b in sorted order. This means that a_b > b_a (where _ represents concatenation). For the sort to produce an
incorrect ordering, there must be some c for which b precendes c and c precedes a, this is a contradiction because
a_b > b_a and b_c > c_b implies a_c > c _a. In other words, our custom comparator preserves transitivity, so the sort
is correct.

Once the array is sorted, the most "signficant" number will at the front. There is a minor edge case comes up when the
array comesup when the array consists of only 0, we can simply return 0. Otherwise, we built a string out of the sorted
array and return it.
"""


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution:
    def lagest_number(self, nums):
        largest_num = ''.join(sorted(max(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num