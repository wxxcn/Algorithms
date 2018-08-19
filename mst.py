# coding: utf-8


# 邻接链表法表示图，简化版的链表，权重为包含在类中
# 同时将方法与类分离
class LinkGraph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.e = []

# 插入单个边
# def insert(g, u, v):
#     g.adj[u].append(v)
#     g.e.append((u, v))

# 插入所有边
def insert(g, e):
    for u, v in e:
        g.adj[u].append(v)
        g.adj[v].append(u)
        g.e.append((u, v))


# 不相交集合的操作：取并集
def union(x, y, p, r):
    return link(find_set(x, p), find_set(y, p), p, r)


# 不相交集合的操作：按秩连接
def link(x, y, p, r):
    xRoot = find_set(x, p)
    yRoot = find_set(y, p)
    if r[xRoot] > r[yRoot]:
        p[yRoot] = xRoot
    else:
        p[xRoot] = yRoot
        if r[yRoot] == r[xRoot]:
            r[yRoot] += 1


# 不相交集合的操作：路径压缩查找根
def find_set(x, p):
    if p[x] != x:
        p[x] = find_set(p[x], p)

    return p[x]


# 最小生成树kruskal算法
def kruskal(g, w):
    A = []
    # make set
    p = list(range(g.n))
    r = g.n * [0]
    tmp = []
    for i, (u, v) in enumerate(g.e):
        tmp.append((i, w[u][v]))

    tmp = sorted(tmp, key=lambda x: x[1])
    for i, iw in tmp:
        print(i, iw)
        u, v = g.e[i]
        if find_set(u, p) != find_set(v, p):
            union(u, v, p, r)
            A.append((u, v))

    return A


# 为prim算法设计的小根堆，效果不理想
class Heap:
    def __init__(self, arr=None):
        self.arr = arr if arr else []
        self.indexs = list(range(len(arr))) if arr else []
        if self.arr:
            self.buildheap()

    def heappush(self, item, index):
        self.arr.append(item)
        self.indexs.append(index)
        i = len(self.arr) - 1
        parentpos = (i - 1) // 2
        while i > 0 and self.arr[parentpos] > self.arr[i]:
            self.arr[parentpos], self.arr[i] = self.arr[i], self.arr[parentpos]
            self.indexs[parentpos], self.indexs[i] = self.indexs[i], self.indexs[parentpos]
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
            self.indexs[smallest], self.indexs[i] = self.indexs[i], self.indexs[smallest]
            self.heapify(smallest)

    def rise(self, i):
        n = len(self.arr)
        parentpos = (i - 1) // 2
        while i > 0 and self.arr[parentpos] > self.arr[i]:
            self.arr[parentpos], self.arr[i] = self.arr[i], self.arr[parentpos]
            self.indexs[parentpos], self.indexs[i] = self.indexs[i], self.indexs[parentpos]
            i = parentpos
            parentpos = (i - 1) // 2

    def heappop(self):
        if len(self.arr) == 0:
            return None
        elif len(self.arr) == 1:
            item = self.arr.pop()
            index = self.indexs.pop()
        else:
            item = self.arr[0]
            self.arr[0] = self.arr.pop()
            index = self.indexs[0]
            self.indexs[0] = self.indexs.pop()
            self.heapify(0)

        return item, index


# 使用小根堆实现的prim算法，效果不理想，
# 取决于python数组的index方法的时间复杂度，
# 或许可以进一步优化，但数据结构要更复杂
def prim(g, w, r):
    INF = float('inf')
    q = Heap()
    p = []
    for i in range(g.n):
        p.append(None)
        if r == i:
            q.heappush(0, i)
        else:
            q.heappush(INF, i)

    while q.arr:
        _, u = q.heappop()
        for v in g.adj[u]:
            if v in q.indexs:
                index = q.indexs.index(v)
                if w[u][v] < q.arr[index]:
                    p[v] = u
                    q.arr[index] = w[u][v]
                    q.rise(index)

    return p


# 从数组中查找轻量级边，并返回结点u
def find(d, flag):
    u, min_dist = -1, float('inf')
    for i in range(len(d)):
        if flag[i] is False and d[i] < min_dist:
            u, min_dist = i, d[i]

    if u == -1:
        return None

    return u


# prim算法的数组实现，简洁明了，
# 但是时间复杂度稍微高些
def prim1(g, w, r):
    INF = float('inf')
    p = []
    flag = []
    d = []
    for i in range(g.n):
        p.append(None)
        flag.append(False)
        if r == i:
            d.append(0)
        else:
            d.append(INF)

    while True:
        u = find(d, flag)
        if u is None:
            break

        flag[u] = True
        for v in g.adj[u]:
            if flag[v] is False and w[u][v] < d[v]:
                p[v] = u
                d[v] = w[u][v]

    return p


if __name__ == '__main__':
    # 创建图
    INF = float('inf')
    g = LinkGraph(9)
    e = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5),
         (5, 6), (6, 7), (6, 8), (7, 8), (8, 0),
         (8, 1), (2, 7), (2, 5), (3, 5)]
    insert(g, e)
    w = [[INF for _ in range(9)] for _ in range(9)]
    t = [4, 8, 7, 9, 10, 2, 6, 1, 7, 8, 11, 2, 4, 14]
    for i, (u, v) in enumerate(e):
        w[u][v], w[v][u] = t[i], t[i]

    # kruskal算法检验
    # A = kruskal(g, w)
    # print('------------------------------------------------')
    # s = 0
    # for i in A:
    #     print(i)
    #     s += w[i[0]][i[1]]
    #
    # print(s)

    # prinm算法检验
    p = prim(g, w, 0)
    for u, v in enumerate(p):
        print(u, v)
