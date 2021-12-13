def Linear_search(arr, n, target):

    for i in range(0, n):

        if (arr[i] == target):
            return i

    return -1

arr = [1, 0, 100, 50, 30]

target = 30

result = Linear_search(arr, len(arr), target)
if (result == -1):
    print("Nothing")
else:
    print("arr index is", result)
