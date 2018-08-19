# coding: utf-8


class Node:
    def __init__(self):
        self.p = None
        self.rank = -1


def make_set(x):
    x.p = x
    x.rank = 0


def union(x, y):
    link(find_set(x), find_set(y))


def link(x, y):
    if x.rank > y.rank:
        y.p = x
    else:
        x.p = y
        if x.rank == y.rank:
            y.rank += 1


def find_set(x):
    if x.p != x:
        x.p = find_set(x.p)

    return x.p


if __name__ == '__main__':
    d = dict()
    v = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    e = [('a', 'b'), ('b', 'c'), ('b', 'd'), ('e', 'f'), ('e', 'g'), ('h', 'i')]
    for item in v:
        d[v] = Node()
        make_set(d[v])

    for u, v in e:
        union(d[u], d[v])
