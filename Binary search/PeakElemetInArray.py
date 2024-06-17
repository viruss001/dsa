class PeakElement:
    def __init__(self):
        pass

    def peakElement(self, arr):
        s = 0
        e = len(arr) - 1
        while s <= e:
            m = s + (e - s) // 2
            if arr[m] > arr[m + 1] and arr[m] > arr[m - 1]:
                return m
            elif arr[m] > arr[m + 1]:
                e = m
            else:
                s = m + 1

        return -1


suraj = PeakElement()
print(suraj.peakElement([5, 4, 3]))
