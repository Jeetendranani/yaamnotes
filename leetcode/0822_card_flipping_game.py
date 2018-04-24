"""
On a table are N cards, with a positive integer printed on the front and back of each card (possibly different).
We flip any number of cards, and after we choose one card.
If the number x on the back of the chosen card is not on the front of any card, then this number is good.
What is the smallest number that is good? if no number is good, output 0.
Here, founts[i] and backs[i] represent the number on the front and back of card i.
A flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.

Example:
    Input: fronts = [1, 2, 4, 4, 7], backs = [1, 3, 4, 1, 3]
    output: 2
    explanation: If we flip the second card, the fronts are [1, 3, 4, 4, 7] and the backs are [1, 2, 4, 1, 3].
    We choose the second card, which has number 2 on the back, and it isn't on the front of any card, so 2 is the good.
"""


class Solution:
    def good_value(self, fronts, backs):
        numbers = set(fronts + backs)
        for n in sorted(numbers):
            if all(f != n or b != n for f, b in zip(fronts, backs)):
                return n
        return 0

