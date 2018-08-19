# coding: utf-8


# max heap function
def max_heap_sort(heap, size):
    '''
    对堆进行原址排序
    :param heap: 堆
    :param size: 堆的size
    :return: None
    '''
    build_max_heap(heap)
    for i in reversed(range(1, size)):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, 0, i)

def build_max_heap(heap):
    '''
    创建一个大根堆，从列表中创建一个大根堆
    :param heap: 数组
    :return: None
    '''
    n = len(heap)
    for i in reversed(range(n // 2)):
        max_heapify(heap, i, n)


def max_heapify(heap, i, n=None):
    '''
    调整根结点为i的堆，假设根的左右孩子均为最大堆，为自顶向上的方法
    :param heap: 数组
    :param i: index
    :return: None
    '''
    if n is None:
        n = len(heap)

    left = i * 2 + 1
    right = left + 1
    largest = i
    if left < n and heap[left] > heap[largest]:
        largest = left

    if right < n and heap[right] > heap[largest]:
        largest = right

    if largest != i:
        heap[largest], heap[i] = heap[i], heap[largest]
        max_heapify(heap, largest, n)


def max_heappop(heap):
    n = len(heap)
    if n == 0:
        return None
    elif n == 1:
        item = heap.pop()
    else:
        item = heap[0]
        heap[0] = heap.pop()
        max_heapify(heap, 0)

    return item


def max_heappush(heap, item):
    heap.append(item)
    i = len(heap) - 1
    parentpos = (i - 1) // 2
    while i > 0 and heap[parentpos] < heap[i]:
        heap[parentpos], heap[i] = heap[i], heap[parentpos]
        i = parentpos
        parentpos = (i - 1) // 2


# 小根堆类
class Heap:
    def __init__(self, arr=None):
        self.arr = arr if arr else []
        if self.arr:
            self.buildheap()

    def heappush(self, item):
        self.arr.append(item)
        i = len(self.arr) - 1
        parentpos = (i - 1) // 2
        while i > 0 and self.arr[parentpos] > self.arr[i]:
            self.arr[parentpos], self.arr[i] = self.arr[i], self.arr[parentpos]
            i = parentpos
            parentpos = (i - 1) // 2

    def buildheap(self):
        n = len(self.arr)
        for i in reversed(range(n // 2)):
            self.heapify(i)

    def heapify(self, i):
        n = len(self.arr)
        left = 2 * i + 1
        right = left + 1
        smallest = i
        if left < n and self.arr[left] < self.arr[smallest]:
            smallest = left

        if right < n and self.arr[right] < self.arr[smallest]:
            smallest = right

        if smallest != i:
            self.arr[smallest], self.arr[i] = self.arr[i], self.arr[smallest]
            self.heapify(smallest)

    def heappop(self):
        n = len(self.arr)
        if n == 0:
            return None
        elif n == 1:
            item = self.arr.pop()
        else:
            item = self.arr[0]
            self.arr[0] = self.arr.pop()
            self.heapify(0)

        return item

# 小根堆函数
def build_min_heap(heap):
    n = len(heap)
    for i in reversed(range(n // 2 + 1)):
        min_heapify(heap, i, n)

def min_heapify(heap, i, n=None):
    if n is None:
        n = len(heap)

    while i < n:
        left = 2 * i + 1
        right = left + 1
        smallest = i
        if left < n and heap[left] < heap[smallest]:
            smallest = left

        if right < n and heap[right] < heap[smallest]:
            smallest = right

        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
        else:
            break


def min_heap_sort(heap):
    n = len(heap)
    for i in reversed(range(1, n)):
        heap[0], heap[i] = heap[i], heap[0]
        min_heapify(heap, 0, i)


def min_heappop(heap):
    n = len(heap)
    if n == 0:
        return None
    elif n == 1:
        item = heap.pop()
    else:
        item = heap[0]
        heap[0] = heap.pop()
        min_heapify(heap, 0)

    return item


def min_heappush(heap, item):
    heap.append(item)
    i = len(heap) - 1
    parentpos = (i - 1) // 2
    while i > 0 and heap[parentpos] > heap[i]:
        heap[parentpos], heap[i] = heap[i], heap[parentpos]
        i = parentpos
        parentpos = (i - 1) // 2


if __name__ == '__main__':
    # 大根堆测试
    # heap = []
    # for i in range(10):
    #     max_heappush(heap, i)
    #
    # print(heap)
    # max_heap_sort(heap)
    # print(heap)
    # build_max_heap(heap)
    # print(heap)
    # print(max_heappop(heap))
    # print(heap)

    # Heap 类测试
    keys = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    heap = Heap(keys)
    print(heap.arr)
    for i in range(1, 21, 2):
        heap.heappush(i)

    print(heap.arr)
    print(heap.heappop())
    print(heap.arr)

    # 小根堆测试
    # heap = []
    # for k in keys:
    #     min_heappush(heap, k)
    #
    # print(heap)
    # min_heap_sort(heap)
    # print(heap)
    # build_min_heap(heap)
    # print(heap)
    # print(min_heappop(heap))
    # print(heap)





