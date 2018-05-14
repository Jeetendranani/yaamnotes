"""
Glossary

    floor division:
    An operator, denoted //, that divides two numbers and rounds down (towards zero) to an integer.

    modulus operator:
    An operator, denoted with a percent sign (%), that works on integers and returns the remainder when on number is
    divided by another.

    boolean expression:
    An expression whose value is either True or False.

    relational operator:
    One of the operators that compares its operands: ==, !=, >, >=, <, and <=.

    logical operator:
    One of the operators that combines boolean expressions: and, or, and not.

    conditional statement:
    A statement that controls teh flow of execution depending on some condition.

    condition:
    The boolean expression in a conditional statement that determines which branch runs.

    compound statement:
    A statement that consists of a header and body. The header ends with a colon (:). The body is indented relative to
    the header.

    branch:
    One of the alternative sequences of statements in a conditional statement.

    chained conditional:
    A conditional statement with a series of alternative branches.

    nested conditional:
    A conditional statement that appears in one of the branches of another conditional statement.

    return statement:
    A statement that causes a function to end immediately and return to the caller.

    recursion:
    The process of calling the function that is currently executing.

    base case:
    A conditional branch in a recursive function that does not make a recursive call.

    infinite recursion:
    A recursion that doesn't have a base case, or never reaches it. Eventually, an infinite recursion causes a runtime
    error.

Exercise

5-1

the time module provides a function, also named time, that returns the current Greenwich Mean Time in the "top epoch"
which is an arbitrary time used as a reference point. On Unix systems, the epoch is 1 jan 1970.

    >>> import time
    >>> time.time()

Write a script that reads the current time and converts it to a time of day in hours, minutes, and seconds, plus the
number of days since the epoch.

5-2

Fermat's last theorem says that there are no positive integers a, b, and c such that
    a**n + b**n = c**n
for any values of n greater than 2.

    1. Write a function named check_fermat that takes four parameters - a, b, c, and n - and checks to see if Fermat's
    theorem holds. If n is greater than 2 and a**n + b**n = c**n the program should print, "Holy smokes, Fermat was
    wrong!" Otherwise teh program should print, "No that doesn't work."

    2. Write a function that prompts the user to input values for a, b, c, and n, convert them integers, and use
    check_fermat to check whether they violate Fermat's theorem.

5-3

if you are given three sticks, you may or may not be able to arrange them in a triangle. For example, if one of the
sticks is 12 inches long and the other two are one inches long, you will not be able to get the short sticks to meet
in the middle. For any three lengths, there is a simple test to see if it is possible to form a triangle:
    if any of three lengths is greater than the sum of the other two, then you cant form a triangle. Otherwise, you can.

    1. Write a function named is_triangle that takes three integers as arguments, and prints either "Yes" or "No",
    depending on whether you can or connot form a triangle from sticks with teh given lengths.

    2. Write a function that prompts the user to input three stick lengths, converts them to integers, and use
    is_triangle to check whether sticks with the given lengths can form a triangle.

5-4

What is the output of the following program? Draw a stack diagram that shows the state of the program when it prints the
result.

    def recurse(n, s):
        if n == 0:
            print(s)
        else:
            recurse(n-1, n+s)

    recurse(3,0)

    1. What would happen if you called this function like this: recurse(-1, 0)?

    2. Write a docstring that explains everything someone would need to know in order to use this function (and nothing
    else).

5-5

5-6

"""