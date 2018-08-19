# -*- coding: utf-8 -*-


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next =None


# 链接法解决冲突
class HashTable:
    def __init__(self, m):
        self.m = m
        self.table = m * [None]

    def insert(self, key, value):
        h = self.div_hash(key)
        if self.table[h] is None:
            self.table[h] = Node(key, value)
        else:
            n1 = self.table[h]
            n2 = Node(key, value)
            self.table[h] = n2
            n2.next = n1
            n1.pre = n2

    def delete(self, key):
        h = self.div_hash(key)
        n = self.table[h]
        while n and n.key != key:
            n = n.next

        if n is None:
            print('no such data with key: %s' % key)
            return -1
        else:
            if n.pre is None:
                self.table[h] = n.next
            else:
                n.pre.next = n.next

            if n.next:
                n.next.pre = n.pre

            return 0

    def search(self, key):
        h = self.div_hash(key)
        n = self.table[h]
        while n and n.key != key:
            n = n.next

        if n is None:
            print('no such data with key: %s' % key)
            return -1
        else:
            return n.value

    def div_hash(self, key):
        # 对于链接法， 一个成功的查找需要的时间是O(1 + alpha)
        # alpha = n / m 可以根据alpha求得较好的m, m一般为素数
        h = 0
        for c in key:
            h = ord(c) + h * 127

        return h % self.m

    def mul_hash(self, key):
        h = 0
        for c in key:
            h = ord(c) + h * 128

        return int(self.m * (0.618 * h - int(0.618 * h)))

    def traver(self):
        for i in range(self.m):
            n = self.table[i]
            print('------------------%d-------------------' % i)
            while n:
                print(n.key)
                n = n.next


if __name__ == '__main__':
    ht = HashTable(8)
    keys = ['python', 'c', 'java', 'c++', 'php', 'R', 'matlab',
            'kotlin', 'javascript', 'css', 'html', 'swift']
            # 'android', 'ios', 'windows', 'linux', 'mac']
    for v, k in enumerate(keys):
        ht.insert(k, v)

    ht.traver()
    # ht.delete('css')
    # ht.delete('python')
    # ht.delete('matlab')
    # ht.delete('R')
    # ht.traver()
