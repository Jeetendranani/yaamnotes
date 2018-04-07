"""
quick_sort(A, p, r)
    if p < r
        q = partition(a, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(Q, q + q, r)

partition(A, p, r)
    x = A[r]
    i == p - 1
    for j = p to r - 1
        if a[j] <= x
            i += 1
            exchange A[i] with a[j]
    exchange A[i + 1] with A[r]
    return i + 1
"""


def quick_sort(nums, p, r):
    if p < r:
        q = partition(nums, p, r)
        quick_sort(nums, p, q - 1)
        quick_sort(nums, q + 1, r)


def partition(nums, p, r):
    x = nums[r]
    i = p - 1
    for j in range(p, r):
        if nums[j] <= x:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[r] = nums[r], nums[i + 1]

    return i + 1


nums = [9, 5, 8, 2, 10, 4, 6, 0]
quick_sort(nums, 0, len(nums)-1)
print(nums)