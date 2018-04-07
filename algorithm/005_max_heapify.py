"""
MAX-HEAPIFY(A, i)
    l = LEFT(i)
    r = RIGHT(i)
    if l <= A.heap-size and A[l] > A[i]
        largest = l
    else
        largest = i

    if r <= A.heap-size and A[r] > A[largest]
        largest = r

    if largest != i
        exchange A[i] with A[largest]
        MAX-HEAPIFY(A, largest)


BUILD-MAX-HEAP(A)
    A.heap-size = A.length
    for i = [A.length/2] down to 1
        MAX-HEAPIFY(A, i)

HEAPSORT(A)
    BUILD-MAX-HEAP(A)
    for i = A.length down to 2
        exchangeA[1] with A[i]
        A.heap-size -= 1
        MAX-HEAPIFY(A, 1)
"""


def heap_sort(nums):
    build_max_heap(nums)
    heap_size = len(nums)
    for i in range(len(nums)-1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        heap_size -= 1
        max_heapify(nums, 0, heap_size)


def build_max_heap(nums):
    heap_size = len(nums)
    for i in range(len(nums)//2, -1, -1):
        max_heapify(nums, i, heap_size)


def max_heapify(nums, i, heap_size):
    l = left(i)
    r = right(i)
    if l < heap_size and nums[l] > nums[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and nums[r] > nums[largest]:
        largest = r

    if largest != i:
        nums[largest], nums[i] = nums[i], nums[largest]
        max_heapify(nums, largest, heap_size)


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


nums = [7, 9, 2, 3, 8, 5, 0]
heap_sort(nums)
print(nums)