"""
Debugging

Three kinds of errors can occur in a program: syntax errors, runtime errors, and semantic errors. It is useful to
distinguish between them in order to track them down more quickly.

    Syntax error:
    "Syntax" refers to the structure of a program and the rules about that structure.

    If there is a syntax error anywhere in your program, Python displays an error messages and quits, and you will not
    be able to run the program. during the first few weeks of your programming career, you might spend a lot of time
    tracking down syntax errors. As you gain experience, you will make fewer errors and find them faster.

    Runtime error:
    The second type of error is a runtime error, so called because the error does not appear until the program has
    started running. These errors are also called exceptions because they usually indicate that something exceptional
    (and bad) has happened.

    Runtime errors are rare in the simple programs you will see in the first few chapters, so it might be a while before
    you encounter one.

    Semantic error:
    The third type of error is "semantic", which means related to meaning. If there is a semantic error in your program,
    it will run without generating error messages, but it will not do the right thing. If will do something else.
    Specifically, it will do what you told it to do.

    Identifying semantic errors can be tricky because it requires you to work backward by looking at the output of the
    program and trying to figure out what it is doing.

Glossary

    variable:
    A name that refers to a value.

    assignment:
    A statement that assigns a value to a variable.

    state diagram:
    A graphical representation of a set of variables and the values they refer to.

    keyword:
    A reserved word that is used to parse a program; you cannot use keywords like if, def, and while as variable names.

    operand:
    One of the values on which an operator operates.

    expression:
    A combination of variables, operators, and values that represents a single result.

    evaluate:
    To simplify an expression by performing the operations in order to yield a single value.

    statement:
    A section of code that represents a command or action. So far, the statements we have seen are assignments and
    print statements.

    execute:
    to run a statement and do what is says.

    interactive mode:
    A way of using the Python interpreter by typing code at the prompt.

    script mode:
    A way of using the Python interpreter to read code from a script and run it.

    script:
    A program stored in a file.

    order of operations:
    Rules governing the order in which expressions involving multiple operators and operands are evaluated.

    concatenate:
    To join two operands end to end.

    comment:
    Information in a program htat is meant for other programmers (or anyone reading the source code) and has no effect
    on the execution of program.

    syntax error:
    An error in a program that makes it impossible to parse (and therefore impossible to interpret).

    exception:
    An error that is detected while teh program is running.

    semantics:
    The meaning of a program.

    Semantic error:
    An error in a program that makes it do something other than what the programmer intended.

Exercises

2-1

Repeating my advice from teh previous chapter, whenever you learn a new feature, you should try it out in interactive
mode and make errors on purpose to see what goes wrong.

    - We've seen that n = 42 is legal. What about 42 = n?
    * SyntaxError: can't assign to literal

    - how about x = y = 1?
    * same x = 1, y = 1

    - In some languages every statement ends with a semicolon, ;. What happens if you put a semicolon at the end of a
    Python statements?
    * works fine

    - What if you put a period at teh end of the statement?
    * SyntaxError: invalid syntax

    - In math notation you can multiply x and y like this xy. What happens if you try that in Python?
    * NameError: name 'ab' is not defined.

2-2

Practice using the Python interpreter as a calculator:

    1. The volume of a sphere with radius r is 4/3*pi*r**3. What is the volume of a sphere with radius 5?
    - 523.34

    2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for teh first
    copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

    3. If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 mer mile), then 3 miles at tempo (7:12 per
    mile) and 1 mile at an easy pace again, what time do I get home for breakfast?
"""