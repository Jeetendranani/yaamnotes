"""
350 Intersection of Two arrays II

Given two arrays, write a function to compute their intersection.

Example:
    Given number1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2]

Note:
    - Each element in the result should appear as many times as it shows in both arrays.
    - The result can be in any order.

Follow up:
    - What is the given array is already sorted? How would you optimized your algorithm?
    - What if nums1's size is small compared to nums2's size? Which algorithm is better?
    - What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements
    into the memory at once?


Thought process:

    1. Try to find common numbers in both array. Ideally we can solve this with one scan of both arrays.
    2. Scan one of them and convert it to dictionary with its repeated number.
    3. Scan the other one and update the number set and result.
    4. Return the result.
"""
import collections


def intersect(nums1, nums2):

    """
    Time Complexity: O(n)
    Space Complexity: O(n)

    :param nums1:
    :param nums2:
    :return:
    """
    num_set = collections.Counter(nums1)
    res = []
    for i in nums2:
        if i in num_set.keys():
            res.append(i)
            num_set[i] _= 1
            if num_set[i] == 0:
                del num_set[i]
    return res


"""
    If given array is sorted, then we dont need the counter to remember the number of elements, we just need to scan 
    with two pointers.
    1. if a1[i] == a2[j], then add it to result
    2. if a1[i] < a2[j], then i += 1
    3. if a1[i] > a2[j], then j += 1
    4. if one ot then finished, exit the loop
    5. return the result.
    
    
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into 
    the memory at once?
    - if only nums2 cannot fit in memory, put all elements of nums1 into a HashMap, read chunks of array that into the 
    memory, and record the intersections. 
    - If both nums 1 and nums2 are so huge that neither fit into the memory, sort them individually (external sort), 
    then read 2 element from each array at a time in memory, record intersections.
"""