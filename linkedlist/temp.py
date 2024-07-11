def small(arr):
    s = 0
    e = len(arr) - 1
    while s < e:
        print("hi")
        m = s + (e - s) // 2
        if arr[m] >= arr[0]:
            s = m + 1
        else:
            e = m

    return s


s = small([3, 4, 5, 1, 2])
print(s)
