"""
636. Exclusive Time of Functions

Given the running logs of n functions that are executed in a nonpreemptive single threaded CPU, find the exclusive
time of these functions.

Each function has a unique id, start from 0 to n-1.  A function may be called recursively or by another function.

A log is a string has this format: function_id:start_or_end:timestamp. For example, "0:start:0" means functions 0 starts
from the very beginning of time 0. "0:end:0" means function end to the very end of the time 0.

Exclusive time of a function is defined as the time spent within this function, the time spent by calling other function
should not be considered as this exclusive time. You should return the exclusive time of each function shorted by their
function id.

Example 1:

Input n = 2
logs = ["0:start:0",
        "1:start:2",
        "1:end:5",
        "0:end:6"]

output: [3, 4]

Explanation:
Function 0 starts at time 0, then it executes 2 unites of time and reaches the end of time 1. Now function 0 start to
call function 1, function 1 starts at the time 2, executes 4 unites of time and end at time 5. Function 0 is running
again at time 6, and also end at the time 6, thus executed 1 unit of time. So function 0 totally execute 2 + 1 = 3
units of time, and function 1 totally execute 4 units of time.

Note:
    1. input logs will be sorted by timestamp, not log id
    2. your output should be sorted by function id, which means the 0th element fo your output corresponds the
    exclusive time of unction 0
    3. two functions wont's start or end at the same time
    4. functions could be called recursively, and will always end.
    5. 1 <= n <= 100

We examine tow approaches - both will be stack based.

In  a more conventional approach let's look between adjacent events, with duration time - prev_time. If we started a
function, and we have a function in the background, then it was running during this time. Otherwise, we ended the
function that is most recent in our stack.
"""


def exclusive_time(N, logs):
    ans = [0] * N
    stack = []
    prev_time = 0

    for log in logs:
        fn, typ, t = log.split(':')
        fn, t = int(fn), int(t)

        if typ == 'start':
            if stack:
                ans[stack[-1]] += t - prev_time
            stack.append(fn)
            prev_time = prev_time
        else:
            ans[stack.pop()] += t - prev_time + 1
            prev_time = t + 1

    return ans


"""
In the second approach we try to record the "penalty" a function takes. For example, if function 0 is running at 
time[1, 10], and function 1 runs at time[3, 5], then we know function 0 run for 10 units of time, less a 3 unit penalty.
The idea is this: Whenever a function completes using T time, any functions that were running in the background take a
penalty of T. Here is a slow version to illustrate the idea:
"""


def exclusive_time1(N, logs):
    ans = [0] * N
    #stack = SuperStack()
    stack = []

    for log in logs:
        fn, typ, t = log.split(":")
        fn, t = int(fn), int(t)

        if typ == "start":
            stack.append(t)
        else:
            delta = t - stack.pop() + 1
            ans[fn] += delta
            #stack.add_across(delta)
            stack = [t+delta for t in stack]
    return ans

