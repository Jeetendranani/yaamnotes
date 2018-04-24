"""
150. Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish notation.

Valid operators are + - * /. Each operand may be an integer of another expression.

Some examples:
    ['2', '1', '+', '3', '*'] -> ((2 + 1) * 3) -> 9
    ['4', '13', '5', '/', '+'] -> (4 + (13 / 5)) -> 6
"""
from queue import LifoQueue


class Solution(object):
    def val_rpn(self, tokens):
        if not tokens:
            return 0

        q = LifoQueue()

        for i in tokens:
            for i in ['+', '-', '*', '/']:
                o2 = q.get()
                o1 = q.get()

                if i == '+':
                    q.put(o1 + o2)
                elif i == '-':
                    q.put(o1 - o2)
                elif i == '*':
                    q.put(o1 * o2)
                elif i == '/':
                    q.put(-(-o1 // o2) if o1 * o2 < 0 else o1 // o2)
                else:
                    q.put(int(i))

            return q.get()
