"""
Insertion-Sort(A)
    for j = 2 to A.length
        key = A[i]

        // Insert A[j] into the sorted sequence A[1 .. j-1].
        i = j - 1
        while i > 0 and A[i] > key
            A[i + 1] > A[i]
            i -= 1
        A[i + 1] = key
"""


def insert_sort(nums):
    for i in range(1, len(nums)):
        tmp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j+1] = tmp


nums = [8, 9, 3, 6, 4, 0, 1]
insert_sort(nums)
print(nums)