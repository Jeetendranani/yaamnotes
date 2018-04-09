"""
Facebook


Crush your interview
the path to an offer


how do i prepare? know...
    the process
    the material
    how to communicate


1. chat with a recruiter - the interview really starts here.
2. complete 1-2 phone screens - heads up: you'll be expected to code!
3. on site interviews - typically 3-5 person interviews, conducted onsite at Facebook HQ in CA.


The path to an offer
1. rock the interview
    a) Ninja: coding
    b) Pirate: architecture design
    c) Jedi: Fit & Fast Projects

2. Post Interview


Goals of a coding interview
Get signal on thins we do at work everyday:
    - how you think and tackle hard problems
    - how you consider engineering trade-offs (memory vs time)
    - how you communicate in English about code
    - Limits of what you know
        So stay calm and think out loud!


What is covered?
    - Data structures and algorithms
        - Implement, not memorize
        - Discuss complexity (space and time trade-offs)
        - common library functions are fair game
    - Specific questions about concepts are rare
        - Unless you claim to be an expert or need teh concept
    Use your most comfortable language


During the interview
    - step 1: ask a lot of questions
        - until you fully understand problem space & constraints
        - validate or state any assumptions
        - draw pictures to help you better understand problem
    - step 2: focus on getting a working solution first
        - handle every corner case
    - step 3: iterate
        - we expect clean production quality code
        Test Your code!


Given an array of size N in which every number is between 1 and N, determine if there are any duplicates.


step1: ask questions
are there any details i need? restrictions?
    - can I destroy or modify the array?
    - can i use additional space?
    - will the array ever be empty?
    - are they all integers?


step 2: get a base solution
what's the best way to solve this that  i'ma sure i can code?

discuss with your interviewer, they are trained to lead you


O(n**2)
Good starting point, but we can do better!


O(n.log(n))
Know your language


Question two:
An atm can only dispense values of $1, $5, $20, and $50. Return the number of unique ways that a $ amount of x can be
tendered:
    - ($1, $5) is distinct from ($5, $1)

    input: 4 - output: 1
    input: 100 - output: 954515231698
    input: 6 - output: 3


1. ask questions
    - are there any detail i need?
    - restrictions?
2. base solution
    - what kind of problem is this?
    - what's the brute force solution?
3. How can we make it better?


Question Three:
Given the root of a binary tree, return a new data structure, which is an collection of linked list to a shared root.


1. ask questions
    - are there any details i need?
    - restrictions?
2. base solution
    - what kind of problem is this?
    - what's the brute force solution?
3. how can we make it better?


Question Four (Homework):
Given an N by N grid of positive integers which represent terrain heights, determine how many grid locations will have
water flow over the continental divide (N x N diagonal, 1-1, 2-2, etc) when it rains, not including the divide itself.


Keep talking and don't think to yourself!


Architecture design question
- Design a solution for a high level problem. e.g. facebook chat
    - see an outdated design at pages 18-24 of http://bit.ly/1s5lhbb
- Draw a diagram of distributed system architecture. No code

Architecture design key points
- it is meant to be open-ended. by yourself!
- Thought process is as important as teh outcome
- focus on architecture diagram rather than algorithm details
important stuff: alternatives, tradeoff, distributed systems, how to scale to 1 billion users, fault tolerance,
reliability, availability, bottleneck, performance, cost, simplicity, how a request flows through the system e2e
- Preparation: study examples of distributed systems.


Fit & Past project Questions
- Be yourself - it's ok to say you don't know something
- Be prepared to talk about common questions
    - Most recent, most challenging, favorite project, what motivates you, how you work with others...
    - Context, action, result
    - if a tech is on  your resume, know it
- Be reflective when preparing (lessons learned)


After the interview
- Have 1 or 2 questions prepared to the interviewer
    - you are interviewing the company as well.
    - focus on what matters most to you
- contact recruiter with any questions or follow ups


Main Takeaways
- Think our loud
- Ask lots of qestions
- Dont' write terrible code :)
- Test your code
- Know distributed systems
- Be yourself

Best way to prepare is to practice


Final Tips
- Get a friend to do a mock interview, then swap
- For phone screens, go somewhere
    - Quiet
    - with a good internet connection
- Practice on a white board
    - leave whitespace between questions
    - Time yourself


Online resources
- Facebook interview blog post: http://on.fb.me/1mkgotv
- coding practice
    - http://www.careercup.com/page
    - http://codedata.com/kata/codedata-intro/
- Facebook engineering page:
    - http://facebook.com/engineering
- Tech talks
    - https://www.facebook.com/engineering/app_260691170608423
-Open source at facebook
    - https://developers.facebook.com/opensource/
- General news
    - http://techcrunch.com/tag/facebook/
"""