class Occurance:
    def __init__(self):
        pass

    def firstOccurance(self, arr, key):
        s = 0
        e = len(arr) - 1
        ans = -1
        while s <= e:
            m = s + (e - s) // 2

            if arr[m] == key:
                e = m - 1
                ans = m
            elif arr[m] > key:
                e = m - 1
            else:
                s = m + 1
        return ans

    def lastOccurance(self, arr, key):
        s = 0
        e = len(arr) - 1
        ans = -1
        while s <= e:
            m = s + (e - s) // 2

            if arr[m] == key:
                s = m + 1
                ans = m
            elif arr[m] > key:
                e = m - 1
            else:
                s = m + 1
        return ans

    def totalNUmberofOccurnce(self, arr, key):
        first = self.firstOccurance(arr, key)
        last = self.lastOccurance(arr, key)
        if first == -1 or last == -1:
            return -1
        return last - first + 1


bina = Occurance()
# ans = bina.firstOccurance([1, 2, 2, 2, 2, 7], 2)
# ans = bina.lastOccurance([1, 2, 2, 2, 2, 7], 2)
# print(
#     bina.firstOccurance([1, 2, 2, 2, 2, 7], 2),
#     bina.lastOccurance([1, 2, 2, 2, 2, 7], 2),
# )
print(bina.totalNUmberofOccurnce([1, 2, 2, 2, 2, 7], 7))
