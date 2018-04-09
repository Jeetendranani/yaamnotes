"""
72. Edit distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation
is counted as 1 step)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""

class Solution(object):
    def mim_distance(self, word1, word2):
        m, n = len(word1) + 1, len(word2) + 1
        dp = [[0 for i in range(n)] for j in range(m)]

        for i in range(n):
            dp[0][i] = i
        for j in range(m):
            dp[j][0] = j

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] +
                               (0 if word2[j - 1] == word1[i - 1] else 1))
        return dp[m-1][n-1]