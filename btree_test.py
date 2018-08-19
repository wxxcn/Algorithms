# -*- coding: utf-8 -*-
from btree import *
import numpy as np
import queue


def dfs(node):
    print(node.keys)
    if node.children:
        for child in node.children:
            dfs(child)

# 删除叶子结点上的空孩子
def remove_leaf(node):
    if node.children:
        if not node.children[0].keys:
            node.children = []
        for child in node.children:
            remove_leaf(child)


if __name__ == '__main__':
    bt = BTree(3)
    # l = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    # np.random.shuffle(l)
    # for i in l:
    #     bt.insert(i)
    n = Node()
    bt.root = n
    q = queue.deque()
    q.append(n)
    lines = ['P', 'C G M', 'T X', 'A B', 'D E F', 'J K L', 'N O',
             'Q R S', 'U V', 'Y Z']
    for line in lines:
        cur = q.popleft()
        keys = line
        keys = keys.strip().split()
        if keys:
            cur.keys = keys
            for _ in range(len(cur.keys) + 1):
                n = Node()
                n.parent = cur
                cur.children.append(n)
                q.append(n)
        else:
            break

    remove_leaf(bt.root)

    dfs(bt.root)
    print('---------------------------------------------------')
    cur, i = bt.search('A')
    print(cur.keys)
    print(cur.children)
    print('---------------------------------------------------')
    for k in ['F', 'M', 'G', 'D', 'B']:
        bt.delete(k)
        dfs(bt.root)
        print('---------------------------------------------------')


