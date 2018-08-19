# coding: utf-8


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    def __init__(self, m):
        self.m = m
        self.table = m * [None]
        self.state = m * ['idle']

    def div_hash(self, key):
        return hash(key) % self.m

    def linear_hash(self, key, i):
        h = 0
        for c in key:
            h = ord(c) + h * 127

        return (h + i) % self.m

    def search(self, key):
        for i in range(self.m):
            h = self.linear_hash(key, i)
            if self.state[h] == 'idle':
                return None

            if self.state[h] == 'busy' and self.table[h].key == key:
                return self.table[h].value

        return None

    def insert(self, key, value):
        i = 0
        while i < self.m:
            h = self.linear_hash(key, i)
            if self.state[h] != 'busy':
                self.state[h] = 'busy'
                self.table[h] = Node(key, value)
                break

            i += 1

        if i >= self.m:
            print('hash map overflow')
        else:
            print('insert success')

    def delete(self, key):
        i = 0
        while i < self.m:
            h = self.linear_hash(key, i)
            if self.state[h] == 'busy' and self.table[h].key == key:
                self.state[h] = 'dirty'
                break

            i += 1

        if i < self.m:
            print('delete success')
        else:
            print('no such data with key %s' % key)

    def iterative(self):
        for i in range(self.m):
            if self.state[i] == 'busy':
                print(self.table[i].key)
            else:
                print(None)


if __name__ == '__main__':
    hmap = HashMap(5)
    keys = ['python', 'c1', 'c6', 'java']
    for v, k in enumerate(keys):
        hmap.insert(k, v)

    print('--------------------------------------')
    hmap.iterative()
    print('--------------------------------------')
    hmap.delete('c1')
    print('--------------------------------------')
    print(hmap.search('c6'))
    print('--------------------------------------')
    hmap.iterative()






