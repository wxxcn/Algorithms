# coding: utf-8


# 定义无穷
INF = float('inf')


# 定义图
class Graph:
    def __init__(self, n):
        self.n = n
        self.e = []
        self.w = [[0 if i == j else INF for j in range(n)] for i in range(n)]


# 插入结点，并设置权重矩阵
def insert(g, u, v, w):
    g.e.append((u, v))
    g.w[u][v] = w


# 单源最短路径算法
# bellman_ford算法
def bellman_ford(g, s):
    d, p = [], []
    for i in range(g.n):
        d.append(INF)
        p.append(None)

    d[s] = 0
    for i in range(g.n - 1):
        for u, v in g.e:
            if d[v] > d[u] + g.w[u][v]:
                d[v] = d[u] + g.w[u][v]
                p[v] = u

    for u, v in g.e:
        if d[v] > d[u] + g.w[u][v]:
            return False, p, d

    return True, p, d


# dijkstra算法
def dijkstra(g, s):
    d, p, flag = [], [], []
    for _ in range(g.n):
        d.append(INF)
        p.append(None)
        flag.append(False)

    d[s] = 0
    while True:
        u = find(d, flag)
        if u is None:
            break
        flag[u] = True
        for v, weight in enumerate(g.w[u]):
            if weight < INF:
                if d[v] > d[u] + weight:
                    d[v] = d[u] + weight
                    p[v] = u

    return p, d


# 查找估计最短路径最小的结点
def find(d, flag):
    index, min_dist = -1, INF
    for i in range(len(d)):
        if flag[i] is False and d[i] < min_dist:
            index = i
            min_dist = d[i]

    if index == -1:
        return None

    return index


# 深度优先搜索进行拓扑排序
def dfs(g, u, f, flag=None):
    flag = flag if flag else g.n * [False]
    flag[u] = True
    for v, weight in enumerate(g.w[u]):
        if flag[v] is False and weight < INF:
            dfs(g, v, f, flag)

    f.insert(0, u)


# 有向无环图拓扑排序
def dag_short_path(g, s):
    d, p = [], []
    for i in range(g.n):
        d.append(INF)
        p.append(None)

    d[s] = 0
    f = []
    dfs(g, s, f)
    for u in f:
        for v, weight in enumerate(g.w[u]):
            if weight < INF:
                if d[v] > d[u] + weight:
                    d[v] = d[u] + weight
                    p[v] = u

    return p, d


# 扩展最短路径
def extend_paths(l, w):
    n = len(l)
    y = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if y[i][j] > l[i][k] + w[k][j]:
                    y[i][j] = l[i][k] + w[k][j]

    return y


# 根据最短路径求取前驱结点矩阵
# 未解决权值为0环可能出现的问题
def get_all_paths(g, d):
    n = g.n
    p = [[i if g.w[i][j] < INF else None for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if g.w[i][j] != d[i][j]:
                for k in range(n):
                    if k == j:
                        continue

                    if d[i][k] + g.w[k][j] == d[i][j]:
                        p[i][j] = k

    return p


# 所有结点对的最短路径算法
# 重复平方法
def all_short_paths(g):
    n = g.n
    l = g.w
    m = 1
    while m < n - 1:
        l= extend_paths(l, l)
        m = 2 * m

    p = get_all_paths(g, l)
    return l, p


# 重复平方法的原始思路
def slow_all_short_paths(g):
    n = g.n
    l = g.w
    m = 1
    while m < n - 1:
        l = extend_paths(l, g.w)
        m += 1

    p = get_all_paths(g, d)
    return l, p


# floyd_warshall算法 大赞
def floyd_warshall(g):
    n = g.n
    d, p = [], []
    for i in range(n):
        d.append([])
        p.append([])
        for j in range(n):
            d[i].append(g.w[i][j])
            if i != j and g.w[i][j] < INF:
                p[i].append(i)
            else:
                p[i].append(None)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
                    p[i][j] = p[k][j]

    return d, p


if __name__ == '__main__':
    # 单源最短路径算法验证
    # bellman_ford 算法
    # t = [(0, 1, 6), (1, 2, 5), (2, 1, -2), (3, 2, 7), (4, 3, 9),
    #      (1, 4, 8), (0, 4, 7), (4, 2, -3), (1, 3, -4), (3, 0, 2)]
    # g = Graph(5)
    # for u, v, w in t:
    #     insert(g, u, v, w)
    #
    # flag, p, d = bellman_ford(g, 0)
    # print(flag, p)
    # s = 0
    # dijkstra 算法
    # t = [(0, 1, 10), (1, 2, 1), (2, 3, 4), (3, 2, 6), (4, 3, 2),
    #      (4, 1, 3), (1, 4, 2), (0, 4, 5), (3, 0, 7), (4, 2, 9)]
    # g = Graph(5)
    # for u, v, w in t:
    #     insert(g, u, v, w)
    # p, d = dijkstra(g, 0)
    # 有向无环图 拓扑排序 最短路径算法
    # t = [(0, 1, 5), (0, 2, 3), (1, 2, 2), (1, 3, 6), (2, 3, 7),
    #      (2, 4, 4), (2, 5, 2), (3, 4, -1), (3, 5, 1), (4, 5, -2)]
    # n = 6
    # g = Graph(n)
    # for u, v, w in t:
    #     insert(g, u, v, w)
    # s = 1
    # p, d = dag_short_path(g, 1)
    # print(p)
    # for i in range(g.n):
    #     if i == s:
    #         continue
    #     j = i
    #     path = []
    #     while p[j] is not None:
    #         path.insert(0, j)
    #         j = p[j]
    #
    #     if j == s:
    #         path.insert(0, j)
    #         print('%d to %d: %s distance: %d' % (s, i, '->'.join(map(str, path)), d[i]))
    #
    #     else:
    #         print('no path from %d to %d' % (s, i))
    # 单源最短路径算法验证

    # 所有结点对的最短路径算法验证
    # 重复平方法
    # t = [(0, 1, 3), (0, 2, 8), (0, 4, -4), (1, 3, 1), (1, 4, 7),
    #      (2, 1, 4), (3, 2, -5), (3, 0, 2), (4, 3, 6)]
    # g = Graph(5)
    # for u, v, w in t:
    #     insert(g, u, v, w)
    #
    # d, p = all_short_paths(g)
    # p[0][3] = 4

    # floyd_warshall算法
    t = [(0, 1, 3), (0, 2, 8), (0, 4, -4), (1, 3, 1), (1, 4, 7),
         (2, 1, 4), (3, 2, -5), (3, 0, 2), (4, 3, 6)]
    g = Graph(5)
    for u, v, w in t:
        insert(g, u, v, w)
    d, p = floyd_warshall(g)
    for i in p:
        print('\t'.join(map(str, i)))
    for i in range(g.n):
        print('source %d' % i)
        for j in range(g.n):
            if j == i:
                continue
            k = j
            path = []
            while p[i][k] is not None:
                path.insert(0, k)
                k = p[i][k]

            if k == i:
                path.insert(0, i)
                print('%d to %d: %s distance: %d' % (i, j, '->'.join(map(str, path)), d[i][j]))
            else:
                print('no path from %d to %d' % (i, j))