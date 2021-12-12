def binarySearch(arr, start, end, target):

    while start <= end:
        mid = (start + end)// 2;

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            start = mid + 1

        else:
            end = mid - 1
    return -1

arr = [2, 3, 4, 10, 40,500,1010,1010,111]
target = 10

result = binarySearch(arr, 0, len(arr) - 1, target)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
