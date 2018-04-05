"""
316. Remove Duplicate Letters

Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only
once. You mush make sure your result is the smallest in lexicographical order among all possible results.

Example:
    Given "bcabc"
    Return "abc"

    Given "cbacdcbc"
    Return "acdb"


Approach 1: Greedy
"""
import collections


class Solution:
    def remove_duplicate_letters(self, s):
        ans = ''
        for x in range(len(set(s))):
            top, idx = s[0], 0
            counter = collections.Counter(s)

            for y in range(len(s)):
                if top > s[y]:
                    top, idx = s[y], y
                if counter[s[y]] == 1:
                    break

                counter[s[y]] -= 1
            ans += top
            s = s[idx + 1:].replace(top, '')
        return ans


t = Solution()
print(t.remove_duplicate_letters("bcabc"))