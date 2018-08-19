# coding: utf-8


# 定义无穷
INF = float('inf')


# 定义邻接链表的结点
class Node:
    def __init__(self, v, w):
        self.v = v
        self.w = w
        self.pre = None
        self.next = None


# 定义邻接链表
class LinkGraph:
    def __init__(self, n):
        self.n = n
        self.adj = n * [None]

    def insert(self, u, v, w):
        cur = self.adj[u]
        node = Node(v, w)
        self.adj[u] = node
        if cur:
            cur.pre = node

        node.next = cur

    # 广度优先搜索
    def bfs(self, s):
        d = self.n * [INF]
        color = self.n * ['white']
        parent = self.n * [None]

        d[s] = 0
        color[s] = 'gray'
        queue = [s]
        while queue:
            u = queue.pop(0)
            node = self.adj[u]
            while node:
                v = node.v
                if color[v] == 'white':
                    color[v] = 'gray'
                    d[v] = d[u] + 1
                    parent[v] = u
                    queue.append(v)

                node = node.next

            color[u] = 'black'

        return parent

    # 深度优先搜索子过程，从一个结点开始深度优先搜索
    def dfs_visit(self, u, color, parent, d, f, time):
        time[0] += 1
        d[u] = time[0]
        color[u] = 'gray'
        cur = self.adj[u]
        while cur:
            v = cur.v
            if color[v] == 'white':
                parent[v] = u
                self.dfs_visit(v, color, parent, d, f, time)
            cur = cur.next
        time[0] += 1
        f[u] = time[0]
        color[u] = 'black'

    # 深度优先搜索
    def dfs(self):
        color = self.n * ['white']
        parent = self.n * [None]
        d = self.n * [-1]
        f = self.n * [-1]
        time = [0]
        for u in range(self.n):
            if color[u] == 'white':
                self.dfs_visit(u, color, parent, d, f, time)

        return d, f, parent

    # 图的转置，即边反向
    def reverse(self):
        g = LinkGraph(self.n)
        for i in range(self.n):
            cur = self.adj[i]
            while cur:
                v = cur.v
                g.insert(v, i, 1)
                cur = cur.next

        return g

    # 强连通分量
    def scc(self):
        g = self.reverse()
        flag = g.n * [False]
        q = []
        for u in range(g.n):
            if not flag[u]:
                g.dfs_scc(u, flag, -1, q=q)

        count = 0
        flag = self.n * [False]
        com = self.n * [-1]
        for u in q:
            if not flag[u]:
                self.dfs_scc(u, flag, count, com)
                count += 1

        return com

    # 为求解强连通分量设计的深度优先搜索子过程
    def dfs_scc(self, u, flag, count, com=None, q=None):
        flag[u] = True
        if com:
            com[u] = count

        cur = self.adj[u]
        while cur:
            v = cur.v
            if not flag[v]:
                self.dfs_scc(v, flag, count, com, q)

            cur = cur.next

        if q is not None:
            q.insert(0, u)

    # 打印广度优先搜索树
    def print_bfs(self, s, v, parent):
        if v == s:
            print(s)
        else:
            path = []
            cur = v
            while parent[cur]:
                path.append(cur)
                cur = parent[cur]

            if cur == s:
                path.append(s)
                path = reversed(path)
                print('%d to %d: %s' % (s, v, '->'.join(map(str, path))))
            else:
                print('no path from %d to %d' % (s, v))


if __name__ == '__main__':
    # 广度优先搜索
    # g = LinkGraph(8)
    # edges = [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (4, 5), (4, 6), (4, 7), (5, 6), (6, 7)]
    # edges += list(map(lambda x: (x[1], x[0]), edges))
    # print(edges)
    # for u, v in edges:
    #     g.insert(u, v, 1)
    #
    # parent = g.bfs(2)
    # for v in range(8):
    #     if v != 2:
    #         g.print_bfs(2, v, parent)

    # 深度优先搜索
    # g = LinkGraph(6)
    # edges = [(0, 3), (0, 1), (1, 2), (2, 3), (3, 1), (4, 2), (4, 5), (5, 5)]
    # for u, v in edges:
    #     g.insert(u, v, 1)
    #
    # d, f, parent = g.dfs()
    # for i in range(g.n):
    #     print(i, d[i], f[i])

    # 强连通分量
    g = LinkGraph(8)
    edges = [(0, 1), (1, 2), (2, 3), (2, 4), (2, 0), (0, 3),
             (2, 4), (4, 5), (3, 5), (5, 3), (4, 6), (6, 4),
             (5, 7), (6, 7), (7, 7)]
    for u, v in edges:
        g.insert(u, v, 1)

    com = g.scc()
    for i, item in enumerate(com):
        print(i, item)


    