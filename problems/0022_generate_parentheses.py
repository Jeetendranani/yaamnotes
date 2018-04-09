"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]

Approach 1: Brute force

Intuition

We can generate all 2**2n sequences of '(' and ')' characters. Then, we will check if each one is valid.

Algorithm

To generate all sequences, we use a recursion. All sequences of length n is just '(' plus all sequences of length n - 1,
and then ')' plus all sequences of length n - 1.

To check whether a sequence is valid, we keep track of balance, the net number of opening brackets minus closing
brackets. If it falls below zero at any time, or doesn't end in zero, the sequence is invalid. - otherwise it is valid.
"""

class Solution(object):
    def generate_parenthesis(self, n):
        def generate(A = []):
            if len(A) == 2*n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans


"""
Approach 2: Backtracking

Intuition and Algorithm

Instead of adding '(' or ')' every time as in approach 1, let's only add them when we know it will remain a valid 
sequence, we can do this by keeping track of the number of opening and closing brackets we have placed so far.

We can start an opening bracket if we still have one (of n) let to place. And we can start a closing bracket if it 
would not exceed the number of opening brackets.
"""


class Solution1(object):
    def generate_parathesis(self, n):
        ans = []
        def backtrack(S='', left=0, right = 0):
            if len(S) == 2 * n:
                ans.append(S)
                return

            if left < n:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)
        backtrack()
        return ans


"""
Approach 3: Closure Number

Intuition

To enumerate something, generally we would like to express it as a sum of disjoint subsets that are easier to count.

Consider the closure number of a valid parentheses sequence S: the least index >= 0 so that S[0], S[1], ..., 
S[2*index+1] is valid. clearly every parentheses sequence has a unique closure number. We can try to enumerate them 
individually.

Algorithm

For each closure number c, we know the starting and ending brackets must be at index 0 and 2*c + 1.
Then, the 2*c elements between must be a valid sequence, plus the rest of the element must be a valid sequence.
"""


class Solution2(object):
    def generate_parenthesis(self, n):
        if n == 0: return ['']
        ans = []
        for c in range(n):
            for left in self.generate_parenthesis(c):
                for right in self.generate_parenthesis(n-1-c):
                    ans.append('({}){}'.format(left, right))
        return ans


"""
Backtracking

Backtracking is a general algorithm for finding all (or some) solutions to some computational problems, notably 
constraint satisfaction problems, that incrementally builds candidates to the solution, and abandons a candidate as soon
as it determines that the candidate cannot possibly be completed to a valid solution.

The classic textbook example of the use of backtracking is the eight queens puzzle, that asks for all arrangements of 
eight chess queens on a standard chessboard so that no queen attacks any other. In the  common backtracking approach, 
the partial candidates are arrangements of k queens in the first k rows of the board, all in different tows and columns.
Any partial solution that contains two mutually attaching queens can be abandoned.

Backtracking can be applied only for problems which admit the concept a partial candidate solution" and a relatively 
quick test of whether it can possible be completed to a valid solution. It is useless, for example, for locating a 
given value in an unordered table. When it is applicable, however, backtracking is often much faster than brute force 
enumeration of all complete candidates, since it can eliminate a large number of candidates with a single test. 

Backtracking is an important tool for solving constraint satisfaction problems, such as crosswords, verbal arithmetic, 
Sudoku, and many other puzzles, It is often th most convenient (if not the most efficient) technique for parsing, for 
the knapsack problem and other combinatorial optimization problem. It is also the basis of the so-called logic
programming languages such as Icon, Planner and Prolog.

Backtracking depends on user-given "black box procedures" that define the problem to be solved, the nature of the 
partial candidates, and how they are extended into complete candidate. It is therefore a metaheuristic rather than a
specific algorithm - although, unlike many other meta-heuristics, it is guaranteed to find all solutions to a finite 
problem in a bounded amount of time.

The term backtrack was coined by American mathematician D. H. Lehmer in the 1950s. The pioneer string-processing 
language SNOBOL (1962) may have been the first to provide a built-in general backtracking facility.

Description of the method

The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various 
ways to give all the possible solutions to the given problem. The completion is done incrementally, bu sequence of 
candidate extension steps.

Conceptually, the partial candidates are represented as the nodes of a tree structure, the potential search tree. Each 
partial candidate is the parent of the candidates that differ from it by single extension step; the leaves of hte tree 
are the partial candidates that cannot be extended any further.

The backtracking algorithm traverses this search tree recursively from the root down, in depth-first order. At each node
c, the algorithm check the whether c can be completed to a valid solution. If it cannot, the whole sub-tree at c is 
skipped (pruned). Otherwise, the algorithm (1) check the whether c itself is a valid solution, and if so reports it to 
the user; and (2) recursively enumerates all sub-trees of c. The two tests and the children of each node are defined by
user-given procedures.

Therefor, the actual search tree that is traversed by the algorithm is only a part of the potential tree. The total cost
of the algorithm is the number of nodes of the actual tree times the cost of obtaining and processing each node. This 
fact should be considered when choosing the potential search tree and implementing the pruning test.

Pseudocode

In order to apply backtracking to a specific class of problems, one must provide the data P for the particular instance 
of hte problem that is to be solved, and six procedural parameters, root, reject, accept, first, next, and output. 
These procedures should take the instance data P as a parameter and should do the following:
    1. root(P): return the partial candidate at the root of the search tree.
    2. reject(P, c): return true only if the partial candidate c is not worth completing.
    3. accept(P, c): return true if c is a solution of P, and false otherwise
    4. first(P, c): generate the first extension of candidate c.
    5. next(P, c): generate the next alternative extension of candidate, after the extension s.
    6. output(P,cO: use hte solution c of P, as appropriate to the application.
    
The backtracking algorithm reduces the problem to the call bt(root(P)), where bt is the following recursive procedure:

procedure bt(c)
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s <- first(P, c)
    while s != ^ do 
        bt(s) 
        s <- next(P, s)
        
ord(c)
    Given a string representing one Unicode character, return an integer representing the unicode code point of that 
    character, For example, ord('a') returns the integer 97. This is the inverse of chr().
    
pow(x, y[, z])
    Return x to the power of y; if z is present , return x to the power y, module z (computed more efficiently than 
    pow(x, y) % z). The two-argument from pow(x, y) is equivalent to using the power operator:
    x**y
    
    The arguments must have numeric types, with mixed operand types, the coercion rules for binary arithmetic operators 
    apply. For int operands, the result has the same type as hte operands (after coercion) unless the second argument 
    is negative; iin that case, all arguments are converted to float and a float result is delivered. 
    
3. Built-in Constants

A small number of constants live in the built-in namespace. They are:

False
    The false value of the bool type. Assignments to False are illegal and raise a SyntaxError.
    
True
    The true value of the bool type.

None
    The sole value of the type NoneType. None is frequently used to represent the absence of a value, as when default
    arguments are not passed to a function.
    
NotImplemented
    Special value which should be returned buy the binary special methods (e.g. __eq__(), __lt__(), __add__(), 
    __rsub__(), etc) to indicate that the operation is not implemented with respect to the other type; may be returned 
    by the in-place binary special methods (e.g. __imul__(), __iand__(), etc.) for the same purpose. Its truth value is 
    true.
    
Ellipses
    The same as ... Special value used mostly in conjunction with extended slicing syntax for user-defined container
    data types.
    
__debug__
    This constant is true if Python was not started with an -O option. See also the assert statement.
    
3.1. Constants added by the site module

The site module (which is imported automatically during startup, except if the -S command-line option is given) add 
several constants to the built-in namespace. They are useful fo the interactive interpreter shell and should not be 
used in programs.

quite(code=None)
exit(code=None)
    Objects that when printed, print a message like "Use quit() or Ctrl+D (i.e. EOF) to exit" and when called, raise
    SystemExit with the specified exit code.
    
copyright
license
credits
    Objects that when printed, print a message like "Type license() to see the full license text", and when called, 
    display the corresponding text in a pager-like fashion (one screen at a time).
    
4. Built-in Types

The following sections describe the standard type that are built into the interpreter.

The principal built-in types are numeric, sequences, mappings, classes, instances and exceptions.

Some collection classes are mutable, the methods that add, subtract, or rearrange their members in place, and don't 
return a specific item. never return the collection instance itself but None.

Some operations are supported by several object types; in particular, practically all objects can be compared, tested
for truth value, and converted to a string (with the repr()) function or the slightly different str() function). The 
latter function is implicitly used when an object is written by the print() function.

4.1. Truth value Testing
Any object can be tested for the truth value, for use in an if or while condition or as operand of the boolean 
operations below. The following values are considered false:
    - None
    - False
    - zero of any numeric type.
    - any empty sequence.
    - any empty mapping.
    - instance of user-defined classes, if the class defines a __bool__() or __len__() method, when that method returns
    the integer zero or bool value False.
    
All other values are considered true - so object of many types are always true.

Operations and built-in functions that have a boolean result always return 0 or False for false and 1 or True for true, 
unless otherwise stated. (Important exception: The boolean operations or and and always return one of there operands.)

4.2. Boolean operations - and, or , not

4.3. Comparisons

There are eight comparison operations in Python. They all have the same priority (which is higher than that of the 
boolean operations). Comparisons can be chained arbitrarily; 

Objects of different types, except different numeric types, never compare equal. Furthermore, some types (for example, 
function objects) support only a degenerate notion of comparison where any two objects of that type are unequal. The <
<=, >= and > operators will raise a TypeError exception when comparing a complex number with another built-in numeric 
type, when the object are of different types that can not be compared, or in other cases where there is no defined 
ordering.

Non-identical instances of a class normally compare as non-equal unless teh defines the __eq__() method.

4.4 Numeric Types

4.4.1 bitwise operations on integer types

4.4.2. Additional methods on integer types

The int type implements the number.Integeral abstract base class. In addition, it provides a few more methods:

int.bit_length()
    Return the number of the bits necessary to represent an integer in binary, excluding the sing and the leading
    zeros:
    
    More precisely, if x nonzero, then x.bit_length() is the unique positive integer k such as that 2**(k-1) <= abs(x) 
    < 2**K. Equivalently, when abs(x) is small enough to have a correctly rounded logarithm, then 
    k = 1 + int(log(abs(x), 2)). if x is zero, then x.bit_length() returns 0.
    
int.to_bytes(length, byteorder, *, signed=False)
    Return an array of bytes representing an integer.
    
    The integer is represented using length bytes. An OverflowError is raised if the integer is not representable with 
    the given number of bytes.
    
    the byteorder argument determines the byte order used to represent the integer. If byteorder is "big", the most
    significant byte is at the beginning of the byte array. If byteorder is 'little', the most significant byte is at 
    the end of the byte array. To request the native byte order of the host system. use sys.byteorder as the byte order
    value.
    
    The signed argument determines whether two's complement is used to represent the integer. If signed is False and 
    negative integer is given, an OverflowError is raised. The default value of signed is False.
    
int.from_bytes(bytes, byteorder, *, signed=False)
    Return the integer represented by the given array of bytes.
    
4.4.3. Additional Methods on Float

float.as_integer_ratio()
    Return a pair of integers whose ratio is exactly equal to the original float and with a positive denominator. Raise
    OverflowError on infinities and a ValueError on NaNs.
    
float.is_integer()
    Return True if the float instance is finite with integral value, and False otherwise.
    
float.hex()
    Return a representation of floating-point number as a hexadecimal string. For finite floating-point numbers, this 
    representation will always include a leading 0x and a trilling p and exponent.
    
classmethod float.fromhex(s)
    Class method to return the float represented by a hexadecimal string s. The string s may have leading and trailing 
    whitespace. 
    
4.4.4. Hashing of numeric types
"""
