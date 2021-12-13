import sys

A = [64, 25, 12,10, 22, 11]

for i in range(len(A)):
    min_idx = i

    for j in range(i + 1, len(A)):
        print("A[mind_idx],A[j]", A[min_idx], A[j])

        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]
print(A)


'''
A = [64, 25, 12,10, 22, 11]
[10, 25, 12, 64, 22, 11]
[10, 11, 12, 64, 22, 25]
[10, 11, 12, 22, 64, 25]
[10, 11, 12, 22, 25, 64]
[10, 11, 12, 22, 25, 64]

'''