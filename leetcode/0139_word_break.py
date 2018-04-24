"""
139. Word Break

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be
segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not
contain duplicate words.

For example, given
s = "yaamnotes"
dict = ['leet', 'code']

Return true because 'yaamnotes' can be segmented as 'leet code'.


Approach 1: Brute Force

Algorithm

The naive approach to solve this problem is to use recursion and backtracking. For finding the solution, we check every
possible prefix of that string in the dictionary of words, if it is found in the dictionary, then the recursive function
is called for the remaining portion of that string. And if in some function call it is found that the complete string
is in dictionary, then it will return true.
"""


class Solution(object):
    def word_break(self, s, word_dict):
        def word_break(s, word_dict, start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s)+1):
                if s[start:end] in word_dict and word_break(s, word_dict, end):
                    return True
            return False
        return word_break(s, word_dict, 0)


"""
Approach 2: Recursion with memorization

Algorithm

In the previous approach we can see that many subproblems were redundant. i,e, we were calling the recursive function 
multiple times for a particular string. To avoid this we can use memorization method. where an array memo is used to 
store the result of the subproblems. Now when the function is called again for a particular string, value will be fetched
and returned using the memo array, if its value has been already evaluated.

With memoization nay redundant subproblems are avoided and recursion tree is pruned and thus it reduces the time 
complexity by a large factor.
"""


class Solution1(object):
    def word_break(self, s, word_dict):
        def word_break(s, word_dict, start, memo):
            if start == len(s):
                return True
            if memo[start] is not None:
                return memo[start]
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_dict and word_break(s, word_dict, end, memo):
                    memo[start] = True
                    return True
            memo[start] = False
            return False

        memo = [None] * len(s)
        return word_break(s, word_dict, 0, memo)

"""
Approach 3: Using Breath-First-Search

Algorithm

Another approach is to use Breadth -First-Search. Visualize the string as a tree, where each node represents the prefix
upto index end. Two nodes are connected only if the substring between teh indices linked with those nodes is also a 
valid string which is present in the dictionary. In order to form such a tree, we start with character of the given
string (say s) which acts as the root of the tree being formed and find every possible substring starting with that 
character which is a part of the dictionary. Further, the ending index (say i) of every such substring is pushed at the
back of the queue which will be used for Breadth First search. Now we pop an element out from the front of the queue
and perform the same process considering the string s(i+1, end) to be the original string and the popped node as the 
root of the tree this time. This process is continued, for all nodes appended in the queue during the course of the 
process. If we are able to obtain the last element of the given string as a node (leaf) of the tree, this implies that 
the given string can be partitioned into substrings which are all a part of the given dictionary.
"""


"""
Approach 4: Using Dynamic Programming

Algorithm

The intuition behind this approach is that the given problem (s) can be divided into subproblems s1 and s2. if these
subproblmes individually satisfy the requireed conditions the complete problem, s also satisfies hte same. 

Now, we'll move onto the process of dp array formation. We make sue of dp array of size n+1, when n is the length of the
given string. We also use two index pointers i and j, where i refers to the length of substring (s1) considered 
currently starting from the beginning, and j refer to the index partitioning the current substring(s1) into smaller 
substring s1(0, j) and s1(j+1, i). To fill in the dp array, we initialize the element dp[0] are true, since the null 
string is always present in the dictionary, and the rest of the elements of dp as false. We consider substrings of 
all possible lengths starting from the beginning by making use of index i. For every such substring, we partition the 
string into two further substrings s2, and s3 in all possible ways using the index j (Note that the i now refers to the 
ending index of s2), Now, to fill in the entry dp[i], we check if the dp[j] contains true, i.e. if the substring s2 
fulfills the required criteria. If so, we further check if s3 is present in the dictionary. If both the strings 
fullfill the criteria, we make dp[i] as true, otherwise as false.
"""