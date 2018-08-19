# -*- coding; utf-8 -*-


class Node:
    def __init__(self, key, color):
        self.parent = None
        self.key = key
        self.color = color
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = Node(-1, 'black')
        self.root = self.nil

    def left_rotate(self, x):
        # 假设x的右孩子不为nil
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        # 假设x的左孩子不为nil
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.parent = y

    def insert(self, z):
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right

        if y == self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.parent = y
        z.left = self.nil
        z.right = self.nil
        z.color = 'red'
        self.insert_fix(z)

    def insert_fix(self, z):
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    y.color = 'black'
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)

                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    y.color = 'black'
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)

                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.left_rotate(z.parent.parent)

        self.root.color = 'black'

    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.nil:
            node = node.left

        return node

    def delete(self, z):
        y = z
        y_origin_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_origin_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        print(x.key, x.color, x.parent.key)
        if y_origin_color == 'black':
            self.delete_fix(x)

    def delete_fix(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.color = 'red'
                        w.left.color = 'black'
                        self.right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.color = 'red'
                        w.right.color = 'black'
                        self.left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = 'black'

    def midsort(self, x):
        if x != self.nil:
            self.midsort(x.left)
            print(x.key, x.color, x.parent.key)
            self.midsort(x.right)

    def search(self, k):
        cur = self.root
        while cur != self.nil:
            if k < cur.key:
                cur = cur.left
            elif k > cur.key:
                cur = cur.right
            else:
                return cur

        return None


if __name__ == '__main__':
    t = RBTree()
    keys = [11, 2, 14, 1, 7, 15, 5, 8]
    for key in keys:
        t.insert(Node(key, 'red'))

    # t.midsort(t.root)
    # print('-------------------------------------')
    # z = t.search(7)
    # t.delete(z)
    # print('-------------------------------------')
    # t.midsort(t.root)

    z = t.search(5)
    n = Node(4, 'red')
    z.left = n
    n.parent = z
    n.left = t.nil
    n.right = t.nil
    import graphviz

    drawer = graphviz.Graph('rbtree')

    def visual(n, drawer):
        drawer.node(str(n.key), shape='circle', fontcolor='white', style='filled', color=n.color)
        if n.left.left is not None:
            drawer.edge(str(n.key), str(n.left.key))
            visual(n.left, drawer)

        if n.right.right is not None:
            drawer.edge(str(n.key), str(n.right.key))
            visual(n.right, drawer)


    visual(t.root, drawer)
    drawer.view()









