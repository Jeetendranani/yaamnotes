"""
A solution using divide and conquer

Let's think about how we might solve the maximum subarray problem using divide and conquer technique. Suppose we want
to find a maximum subarray of the subarray A[low .. high]. Divide and conquer suggests that we divide the subarray
into two subarray of as equal size as possible. That is we find the midpoint, say mid, of the subarray, and consider
the subarray A[[low .. mid] and A[mid + 1 .. high]. As figure 4.4(a) shows, any contiguous subarray A[i .. j] of A[low
.. high] must lie in exactly one of the following places:

    - entirely in the subarray A[low .. mid]
    - entirely in the subarray A[mid+1 .. high]
    - crossing the midpoint.

Therefore, a maximum subarray of A[low .. high] must lie in exactly one of these places. In fact, a maximum subarray of
A[low .. high] must have teh greatest sum over all subarray entirely in A[low .. mid], entirely in A[mid + 1 .. high],
or crossing the midpoint. We can find maximum subarrays of A[low .. mid] and A[mid + 1 .. high] recursively, because
these two subproblems are smaller instances of the problem of finding a maximum subarray. Thus, all tht is left to do is
find a maximum subarray that crosses the midpoint, and take a subarray with the largest sum of the three.

we can easily find a maximum subarray crossing the midpoint in time linear in the size of the subarray A[low .. high].
This problem is not a smaller instance of our original problem, because it has the added restriction that the subarray
crossing midpoint is itself made of two subarrays A[i .. mid] and A[mid + 1 .. j], where low <= i <= mid and mid < j <=
high. Therefore, we just need to find maximum subarrays of the form A[i .. mid] and A[mid + 1 .. j] and then combine
them. The procedure FIND_MAX_CROSSING-SUBARRAY takes as input the array A and the indices low, mid, high, and it returns
a tuple containing the indices demarcating a maximum subarray that crosses the midpoint, along with the sum of the
values in a maximum subarray.

FIND-MAX-CROSSING-SUBARRAY(A, low, mid, high)
    left-sum = -'inf'
    sum = 0
    for i = mid down to low
        sum = sum + A[i]
        if sum > let-sum
            left-sum = sum
            max-left = i

    right-sum = -'inf'
    sum = 0
    for j = mid + 1 to high
        sum = sum + A[j]
        if sum > right-sum
            right-sum = sum
            max-right = j

    return (max-left, max-right, left-sum + right-sum)

With a linear-time find-max-crossing-subarray procedure in hand, we can write pseudocode for a divide and conquer
algorithm to solve the maximum subarray problem:

FIND-MAXIMUM-SUBARRAY(A, low, high)
    if high == low
        return (low, high, A[low])
    else:
        mid = [(low + high) // 2]
        (left-low, left-high, left-sum) =
        FIND-MAXIMUM-SUBARRAY(A, low, mid)
        (right-low, right-high, right-sum) =
        FIND-MAXIMUM-SUBARRAY(A, mid + 1, high)
        (cross-low, cross-high, cross-sum) =
        FIND-MAX-CROSSING-SUBARRAY(A, low, mid, high)

        if left-sum >= right-sum and left-sum >= cross-sum
            return (left-low, left-high, left-sum)
        elif right-sum >= left-sum and right-sum >= cross_sum
            return (right-low, right-high, right-sum)
        else
            return (cross-low, cross-high, cross-sum)
"""