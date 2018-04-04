"""
85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 6
"""

class Solution:
    def largest_rectangle_area(self, height):
        stack = []
        i, area = 0, 0
        while i < len(height):
            if stack == [] or height[i] > height[stack[len(stack) - 1]]:
                stack.append(i)
            else:
                curr = stack.pop()
                width = i if stack == [] else i - stack[len(stack) - 1] - 1
                area = max(area, width * height[curr])
                i -= 1
            i += 1

        while stack != []:
            curr = stack.pop()
            width = i if stack == [] else len(height) - stack[len(stack) - 1] - 1
            area = max(area, width * height[curr])

        return area

    def maximal_rectangle(self, matrix):
        if matrix == []:
            return 0

        a = [0 for i in range(len(matrix[0]))]
        max_area = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                a[j] = a[j] + 1 if matrix[i][j] == '1' else 0

            max_area = max(max_area, self.largest_rectangle_area(a))

        return max_area

