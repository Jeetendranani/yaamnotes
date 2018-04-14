"""
Step 3: Understanding bottlenecks

Most likely your high-level design will have one or more bottlenecks given the constraints of the problem. This is
perfectly ok. you are not expected to design a system from the ground up, which immediately handles all the load in the
world. it just needs to be scalable, in order for you to be able to improve it using some standard tools and techniques.

Now that you have your high-level design, start thinking about what bottlenecks is has. Perhaps your system needs a load
balance and many machines behind it to handle the user requests. Or maybe teh data is so huge that you need to
distribute your database on multiple machines. What are some of the downsides that occur from doing that? Is the
database too slow and does it need some in-memory caching?

These are just examples of questions that you may have to answer in order to make your solution complete. It may be the
case that the interviewer wants to direct the discussion in one particular direction. Then, maybe you wont' need to
address all the bottlenecks but rather talk in more depth about one particular area. In any case, you need to be able
to identify the weak spots in a system and be able to resolve them.

Remember, usually each solution is a trade-off of some kind. Changing something will worsen something else. However, the
important thing is to be able to talk about these trade-offs, and to measure their impact on the system given the
constraints and use cases defined.

Once you've outlined the code bottlenecks you see, you can start addressing them in the next step.
"""