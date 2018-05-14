"""
The goal of this book is to teach you think like a computer scientist. This way of thinking combines some of the best
features of mathematics, engineering, and natural science. Like mathematicians, computer scientists use formal
language to denote ideas (specifically computations). Like engineers, they design things, assembling components into
systems and evaluating tradeoffs among alternatives. Like scientists, they observe the behavior of complex systems, from
hypotheses, and test predictions.

The single most important skill for a computer scientists is problem solving. Problem solving means the ability to
formulate problems, think creatively about solutions, and express a solution clearly and accurately. As it turns out,
the process of learning to program is an excellent opportunity to practice problem-solving skills. That's why this
chapter is called "the way of the program".

What is a program?

The details look different in different languages, but a few basic instructions appear in just about every language:
- input
- output
- math
- conditional execution
- repetition

Believe it or not, that's pretty much all there is to it. Every program you've ever used, no matter how complicated, is
made up of instructions that look pretty much like these. So you can think of programming as the process of breaking a
large, complex task into smaller and smaller and smaller subtasks until the subtasks are simple enough to be performed
with one of these basic instructions.

Formal and Natural languages

Natural languages are the language people speak, such as English, Spanish, and French. They were not designed by
people, they evolved naturally.

Formal languages are languages that are designed by people for specific applications. For example, teh notation that
mathematicians used is a formal language that is particularly good and at denoting relationships among numbers and
symbols. Chemists use a formal language to represent the chemical structure of molecules. And most importantly:
    Programming languages are formal languages that have been designed to express computations.

Formal languages tend to have strict syntax rules that govern the structure of statements.

Syntax rules come in two flavors, pertaining to tokens and structure. Tokens are the basic elements of the languages,
such as works, numbers, and chemical elements.

The second type of syntax rule pertains to the way tokens are combined.

When you read a sentence in English or a statement in a formal language, you have to figure out the structure. This
process is called parsing.

Although formal and natural languages have many features in common - tokens, structure, and syntax - there are some
differences:

    - Ambiguity:
    Natural languages are full of ambiguity, which people deal with by using contextual clues and other information.
    Formal languages are designed to be nearly or completely unambiguous, which means that any statement has exactly
    one meaning, regardless of context.

    - redundancy:
    In order to make up for ambiguity and reduce misunderstandings, natural languages employ lots of redundancy. As a
    result, they are often verbose. Formal languages are less redundant and more concise.

    - literalness:
    Natural languages are full of idiom and metaphor. If I say, "The penny dropped", there is probably no penny and
    nothing dropped (this idiom means that someone understood something after a period of confusion). Formal languages
    mean exactly what they say.

Formal languages are more dense than natural languages, so it takes longer to read them. Also, the structure is
important, so it is not always best to read from top to bottom, left to right. Instead, learn to parse the program in
your head, identifying the tokens and interpreting the structure. Finally, the details matter. Small errors in spelling
and punctuation, which you can get away with in natural languages, can make a big difference in a formal language.


Glossary

problem solving:
    The process of formulating a problem, finding a solution, and expressing it.

high-level language:
    A programming language like Python that is designed to be easy for humans to read and write.

low-level language:
    A programming language that is designed to be easy for a computer to run; also called "machine language" or
    "assembly language".

portability:
    A property of a program that can run on more than one kind of computer.

interpreter:
    A program that reads another program and executes it.

prompt:
    Characters displayed by the interpreter to indicate that is ready to take input from the user.

program:
    A set of instructions that specifies a computation.

print statement:
    An instructions that cause the Python interpreter to display a value on the screen.

operator:
    A special symbol that represents a simple computation like addition, multiplication, or string concatenation.

value:
    One of the basic units of data, like a number or string, that a program manipulates.

type:
    A category of values. The types we have seen so far are integers, floating point number and strings.

integer:
    A type that represents whole numbers.

floating-point:
    A type that represents numbers with fractional parts.

string:
    A type that represents sequences of characters.

natural language:
    Any one of the languages that people speak that evolved naturally.

formal language:
    Any one of the languages that people have designed for specific purposes, such as representing mathematical ideas
    or computer programs; all programming languages are formal languages.

token:
    One of teh basic elements of the syntactic structure of a program, analogous to a word in a natural language.

syntax:
    The rules that govern the structure of program.

parse:
    To examine a program and analyze the syntactic structure.

bug:
    An error in a program.

debugging:
    The process of finding and correcting bugs.


Exercises

1-1
It is a good idea to read this book in front of a computer so you can try out the examples as you go.

whenever you are experimenting with a new feature, you should try to make mistakes. For example, in the "Hello world!"
program, what happens if you leave out one of the quotation marks? What is you leave out both? What if you spell print
wrong?

This kind of experiment helps you remember what you read; it also helps when you are programming, because you get to
know what teh error messages mean. it is better to make mistakes now and on purpose than later and accidentally.

1. In a print statement, what happens if you leave out one of the parentheses, or both?
    - SyntaxError: EOL while scanning string literal.
    - SyntaxError: Invalid syntax
    - 'hello' is not defined

2. If you are trying to print a string, what happens if you leave out on eof the quotation marks, or both?
    - SyntaxError.
    - variable is not defined.

3. you can use a minus sing to make a negative number like -2. What happens if you put a plus sign before a number?
What about 2++2?
    - +2 is the same as 2
    - 2++2 = 4

4. In math notation, leading zeros are okay, as in 02. What happens if you try this in Python?
    - invalid token. todo python compiler

5. What happens if you have two values with no operator between them?
    - invalid syntax

1-2

Start the python interpreter and use it as a calculator.

1. How many seconds are there in 42 minutes 42 seconds?
    - 2562

2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
    - 6.21

4. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and
seconds)? What is your average speed in miles per hour?
    - 8.73
"""