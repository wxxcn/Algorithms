# coding: utf-8


# 插入排序
def insert_sort(arr):
    n = len(arr)
    for i in range(1, n):
        t, j = arr[i], i - 1
        while j >= 0 and arr[j] > t:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = t


# 快速排序
def quick_sort(arr, l=None, r=None):
    if l is None:
        l = 0

    if r is None:
        r = len(arr) - 1

    if l < r:
        t = arr[r]
        i, j = l, l
        while i < r:
            if arr[i] < t:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1

            i += 1

        arr[j], arr[r] = arr[r], arr[j]
        quick_sort(arr, l, j - 1)
        quick_sort(arr, j + 1, r)


# 归并排序
def merge_sort(arr, l=None, r=None):
    n = len(arr)
    if l is None:
        l = 0
    if r is None:
        r = n

    if r > l + 1:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m, r)
        j, k = l, m
        t = []
        for i in range(l, r):
            t1 = arr[j] if j < m else arr[k] + 1
            t2 = arr[k] if k < r else arr[j] + 1
            if t1 < t2:
                t.append(t1)
                j += 1
            else:
                t.append(t2)
                k += 1

        for i in range(l, r):
            arr[i] = t[i - l]
        # n1 = m - l
        # n2 = r - m
        # i, j = 0, 0
        # t = []
        # while i < n1 and j < n2:
        #     if arr[l + i] < arr[m + j]:
        #         t.append(arr[l + i])
        #         i += 1
        #     else:
        #         t.append(arr[m + j])
        #         j += 1
        #
        # while i < n1:
        #     t.append(arr[l + i])
        #     i += 1
        #
        # while j < n2:
        #     t.append(arr[m + j])
        #     j += 1
        #
        # for i, item in enumerate(t):
        #     arr[l + i] = item


if __name__ == '__main__':
    import numpy as np
    arr = np.random.randint(0, 100, 10)
    print(arr)
    merge_sort(arr)
    print(arr)


