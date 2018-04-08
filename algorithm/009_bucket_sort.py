"""
bucket_sort(A)
    let B[0 .. n -1] be a new array
    n = A.length
    for i = 1 to n - 1
        make B[i] an empty list

    for i = 1 to n
        insert A[i] into list B[nA[i]]

    for i = 0 to n - 1
        sort list B[i] with insertion sort

    concatenate the list B[0], B[1], .. , B[n - 1] together in order
"""