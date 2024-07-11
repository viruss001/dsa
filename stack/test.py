def FindSum(arr):
    sum = arr[0]
    for i in range(1, len(arr)):
        # if min > arr[i]:
        sum += arr[i]
    return sum


print(FindSum([4, 57, 8, 78]))
