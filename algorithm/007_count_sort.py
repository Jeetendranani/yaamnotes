"""
count_sort(A, B, k):

for i in range(k):
    B[i] = 0

for j in range(len(A)):
    b[A[j]] += 1
j = 0
for i in range(k):
    for n in range(B[i]):
        A[j] = i
        j += 1
"""


def count_sort(nums1, nums2, k):
    nums2 = [0] * k

    for i in range(len(nums1)):
        nums2[nums1[i]] += 1

    i = 0
    for j in range(k):
        for n in range(nums2[j]):
            nums1[i] = j
            i += 1


nums1 = [1, 2, 3, 3, 2, 1, 5, 6, 0, 1, 4]
nums2 = []
count_sort(nums1, nums2, 7)
print(nums1)
