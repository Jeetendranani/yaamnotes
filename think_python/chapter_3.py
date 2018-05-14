"""
Functions

Composition

So far, we have looked at teh elements of a program - variables, expressions, and statements - in isolation, without
talking about how to combine them.

One of them most useful features of programming languages is their ability to take small building blocks and compose
them.

Why functions?

It may not be clear why it is worth the trouble to divide a program into functions. There are several reasons:

    - creating a new function gives you an opportunity to name a group of statements, which makes your program easier
    to read and debug.

    - Functions can make a program smaller by eliminating repetitive code. Later, if you make a change, you only have
    to make it in one place.

    - Dividing a long program into functions allows you to debug the parts one at a time and then assemble them into a
    working whole.

    - Well-designed functions are often useful for many programs. Once you write and debug one, you can reuse it.

Debugging

One of the most important skills you will acquire is debugging. Although it can be frustrating, debugging is one of the
most intellectually rich, challenging, and interesting parts of programming.

In some ways debugging is like detective work. You are confronted with clues and you have to infer the processes and
events that led to the results you see.

Debugging is also like an experimental science. Once you have an idea about what is going wrong, you modify your
program and try again. If your hypothesis was correct, you can predict teh result of the modification, and you take a
step closer to a working program. If your hypothesis was wrong, you have to come up with a new one. As Sherlock Holmes
pointed out, "When you have eliminated the impossible, whatever remains, however improbable, must be the truth."

For some people, programming and debugging are the same thing. That is, programming is the process of gradually
debugging a program until it does what you want. The idea is that you should start with a working program and make
small modifications, debugging them as you go.

For example, Linux is an operating system that contains millions of lines of coe, but it started out as a simple
program Linus Torvalds used to explore the intel 80386 chip. According to Larry Greenfield, "One of Linus's earlier
projects was a program that would switch between printing AAAA and BBBB. This later evolved to Linux."

Glossary

    function:
    A named sequence of statements that performs some useful operation. Functions may or may not take arguments and may
    or may not produce a result.

    function definition:
    A statement that creates a new function, specifying tis name, parameters, and the statements it contains.

    function object:
    A value created by a function definition. The name of the function is a variable that refers to a function object.

    header:
    The first lien of a unction definition.

    body:
    The sequence of statements inside a function definition.

    parameter:
    A name used inside a function to reer to teh value passed as an argument.

    function call:
    A statement that runs a function. It consists of the function name followed by an arguments list in parentheses.

    argument:
    A value provided to a function when the function is called. This value is assigned to the corresponding parameter
    in the function.

    local variable:
    A variable defined inside a function. A local variable can only be used inside its function.

    return value:
    The result of a function. If a function call is used as an expression, the result value is the value of the
    expression.

    fruitful function:
    A function that returns a value.

    void function:
    A function that always return None.

    None:
    A special value returned by void functions.

    module:
    A file that contains a collection of related functions and other definitions.

    import statement:
    A statement that reads a module file and creates module object.

    module object:
    A value created by an import statement that provides access to the values defined in a module.

    dot notation:
    The syntax for calling a function in another module by specifying the module name followed by a dot and the function
    name.

    composition:
    Using an expression as part of larger expression, or a statement as part of larger starement.

    flow of execution:
    The order statement run in.

    stack diagram:
    A graphical representation of a stack of functions, their variables, and the values they refer to.

    frame:
    A box in a stack diagram that represents a function call. It contains the local variables and parameters of the
    function.

    traceback:
    A list of the function that are executing, printed when an exception occurs.

Exercises

3-1

Write a function named right_justify that takes a string named s as a parameter an print the string with enough leading
spaces to that the last letter of the string is in column 70 of the display:

Hint: use string concatenation and repetition. Also Python provides a built-in function called len that return the
length of a string, so the value of len('monoty') is 5.

3-2

A function object is a value you can assign to a variable or pass as an argument. For example, do_twice is function that
takes a function object as an argument and calls it twice:
    def do_twice(f):
        f()
        f()

Here's an example that uses do_twice to call a function named print_spam twice:
    def print_spam():
        print('spam')

    do_twice(print_span)

1. Type this example into a script and test it.
"""