# -*- coding: utf-8 -*-


class Node:
    def __init__(self, k):
        self.key = k
        self.parent = None
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def search(self, k):
        cur = self.root
        while cur:
            if k < cur.key:
                cur = cur.left
            elif k > cur.key:
                cur = cur.right
            else:
                break

        return cur

    def insert(self, k):
        p = None
        cur = self.root
        while cur:
            p = cur
            if k < cur.key:
                cur = cur.left
            elif k > cur.key:
                cur = cur.right
            else:
                break

        if p is None:
            self.root = Node(k)
        elif k < p.key:
            p.left = Node(k)
            p.left.parent = p
        else:
            p.right = Node(k)
            p.right.parent = p

    def minimum(self, node):
        while node.left:
            node = node.left

        return node

    def maximum(self, node):
        while node.right:
            node = node.right

        return node

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v:
            v.parent = u.parent

    def delete(self, k):
        cur = self.search(k)
        if cur is None:
            print('there is no value k')
            return -1

        if cur.left is None:
            self.transplant(cur, cur.right)
        elif cur.right is None:
            self.transplant(cur, cur.left)
        else:
            tmp = self.minimum(cur.right)
            if tmp.parent != cur:
                self.transplant(tmp, tmp.right)
                tmp.right = cur.right
                tmp.right.parent = tmp

            self.transplant(cur, tmp)
            tmp.left = cur.left
            tmp.left.parent = tmp

    def midsort(self, t):
        if t:
            self.midsort(t.left)
            print(t.key, t.parent.key if t.parent else -1)
            self.midsort(t.right)


if __name__ == '__main__':
    t = Tree()
    keys = [11, 2, 14, 1, 7, 15, 5, 8, 4]
    for key in keys:
        t.insert(key)

    t.midsort(t.root)
    t.delete(2)
    print('------------------------------------------')
    t.midsort(t.root)







