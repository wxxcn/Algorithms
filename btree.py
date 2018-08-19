# -*- coding: utf-8 -*-


class Node:
    def __init__(self):
        self.parent = None
        self.keys = []
        self.children = []


class BTree:
    def __init__(self, t):
        self.t = t
        self.root = None

    def search(self, k):
        current = self.root
        while current:
            i, key = 0, current.keys[0]
            for i, key in enumerate(current.keys):
                if k <= key:
                    break

            if k == key:
                return current, i
            elif current.children:
                current = current.children[i]
            else:
                return None

    def insert(self, k):
        if self.root:
            if len(self.root.keys) == 2 * self.t - 1:
                r = self.root
                self.root = Node()
                self.root.children.append(r)
                r.parent = self.root
                self.split_node(self.root, 0)
                self.insert_not_full(self.root, k)
            else:
                self.insert_not_full(self.root, k)
        else:
            self.root = Node()
            self.root.keys.append(k)

    def split_node(self, x, i):
        z = Node()
        y = x.children[i]
        for _ in range(0, self.t - 1):
            z.keys.append(y.keys[self.t])
            y.keys.pop(self.t)

        if y.children:
            for _ in range(0, self.t):
                z.children.append(y.children[self.t])
                y.children.pop(self.t)

        x.keys.insert(i, y.keys[self.t - 1])
        y.keys.pop(self.t - 1)
        x.children.insert(i + 1, z)
        z.parent = x

    def insert_not_full(self, x, k):
        if not x.children:  # 为叶结点
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1

            x.keys.insert(i, k)
        else:
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1

            if len(x.children[i].keys) == 2 * self.t - 1:
                self.split_node(x, i)
                if k > x.keys[i]:
                    i = i + 1

            self.insert_not_full(x.children[i], k)

    def delete(self, k):
        self.__delete(self.root, k)
        if len(self.root.keys) == 0:
            self.root = self.root.children[0]
            self.root.parent = None

    def __delete(self, node, k):
        if node.children:
            i = 0
            while i < len(node.keys) and k > node.keys[i]:
                i += 1

            # 算法导论情况2
            if k == node.keys[i]:
                y = node.children[i]
                z = node.children[i + 1]
                # 2a
                if len(y.keys) >= self.t:
                    tmp = y
                    while tmp.children:
                        tmp = tmp.children[-1]

                    node.keys[i] = tmp.keys[-1]
                    self.__delete(y, tmp.keys[-1])
                # 2b
                elif len(z.keys) >= self.t:
                    tmp = z
                    while tmp.children:
                        tmp = tmp.children[0]

                    node.keys[i] = tmp.keys[0]
                    self.__delete(z, tmp.keys[0])
                # 2c
                else:
                    node.keys.pop(i)
                    node.children.pop(i + 1)
                    y.keys.append(k)
                    for key in z.keys:
                        y.keys.append(key)

                    for child in z.children:
                        y.children.append(child)
                    self.__delete(y, k)
            # 算法导论情况3
            else:
                y = node.children[i]
                if len(y.keys) == self.t - 1:
                    if i - 1 >= 0 and len(node.children[i - 1].keys) >= self.t:
                        y.keys.insert(0, node.keys[i - 1])
                        z = node.children[i - 1]
                        if z.children:
                            y.children.insert(0, z.children.pop(-1))
                        node.keys[i - 1] = z.keys.pop(-1)
                    elif i + 1 < len(node.children) and len(node.children[i + 1].keys) >= self.t:
                        y.keys.append(node.keys[i])
                        z = node.children[i + 1]
                        if z.children:
                            y.children.append(z.children.pop(0))
                        node.keys[i] = z.keys.pop(0)
                    else:
                        if i - 1 >= 0:
                            z = node.children[i - 1]
                            z.keys.append(node.keys[i - 1])
                            for key in y.keys:
                                z.keys.append(key)
                            for child in y.children:
                                z.children.append(child)
                            node.keys.pop(i - 1)
                            node.children.pop(i)
                            self.__delete(z, k)

                        if i + 1 < len(node.children):
                            z = node.children[i + 1]
                            y.keys.append(node.keys[i])
                            for key in z.keys:
                                y.keys.append(key)

                            for child in z.children:
                                y.children.append(child)

                            node.keys.pop(i)
                            node.children.pop(i + 1)
                            self.__delete(y, k)
                else:
                    self.__delete(y, k)
        # 算法导论情况1
        else:
            i = 0
            while i < len(node.keys) and k > node.keys[i]:
                i += 1

            if k == node.keys[i]:
                node.keys.pop(i)

