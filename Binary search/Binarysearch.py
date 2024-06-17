class Binary_search:
    def __init__(self):
        pass

    def binary_search(self, arr, key):
        s = 0
        e = len(arr) - 1
        while s <= e:
            m = s + (e - s) // 2

            if arr[m] == key:
                return m
            elif arr[m] > key:
                e = m - 1
            else:
                s = m + 1
        return -1


if __name__ == "__main__":
    bina = Binary_search()
    ans = bina.binary_search([1, 2, 3], 4)
    print(ans)
