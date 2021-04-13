RED = "RED"
BLACK = "BLACK"


class Node:
    def __init__(self, key=None, parent=None, color=RED):
        self.key = key
        self.color = color
        self.parent = parent
        self.left = None
        self.right = None

    def paint(self, color):
        self.color = color

    def isleft(self):
        return self.parent and self is self.parent.left

    def isright(self):
        return self.parent and self is self.parent.right

    def brother(self):
        if self.isleft():
            return self.parent.right
        if self.isright():
            return self.parent.left
        return None

    def uncle(self):
        if self.parent is None:
            return None
        return self.parent.brother()


class RBTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.iterations_insert = 0
        self.iterations_search = 0
        self.iterations_remove = 0
        self.result = []

    def isred(self, node):
        return node and node.color == RED

    def isblack(self, node):
        return node is None or node.color == BLACK

    def newparent(self, node):
        if node is None:
            return None
        if node.left:
            p = node.left
            while p.right:
                p = p.right
            return p
        while node.parent and node is node.parent.left:
            node = node.parent
        return node.parent

    def heir(self, node):
        if node is None:
            return None
        if node.right:
            s = node.right
            while s.left:
                s = s.left
            return s
        while node.parent and node is node.parent.right:
            node = node.parent
        return node.parent

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            self.size += 1
            self.moreinsert(self.root)
            return

        parent = self.root
        node = self.root
        flag = True
        while node:
            parent = node
            self.iterations_insert += 1
            if key > node.key:
                node = node.right
                flag = True
            elif key <= node.key:
                node = node.left
                flag = False
            else:
                node.key = key
                return
        self.iterations_insert += 1
        new = Node(key=key, parent=parent)
        if flag:
            parent.right = new
        else:
            parent.left = new
        self.size += 1
        self.moreinsert(new)

    def moreinsert(self, node):
        parent = node.parent
        if parent is None:
            node.paint(BLACK)
            return
        if self.isblack(parent): return
        grand = parent.parent
        grand.paint(RED)
        uncle = parent.brother()
        if self.isred(uncle):
            parent.paint(BLACK)
            uncle.paint(BLACK)
            self.moreinsert(grand)
            return
        if parent.isleft():
            if node.isleft():
                parent.paint(BLACK)
            else:
                node.paint(BLACK)
                self.leftrotate(parent)
            self.rightrotate(grand)

        else:
            if node.isleft():
                node.paint(BLACK)
                self.rightrotate(parent)
            else:
                parent.paint(BLACK)
            self.leftrotate(grand)

    def search(self, key, subtree):
        self.iterations_search += 1
        if subtree is None:
            return None
        elif key < subtree.key:
            return self.search(key, subtree.left)
        elif key > subtree.key:
            return self.search(key, subtree.right)
        else:
            return subtree

    def remove(self, key):
        node = self.search(key, self.root)
        if node is None:
            return
        self.size -= 1
        if node.left and node.right:
            n = self.heir(node)
            node.key = n.key
            node = n
        change = None
        if node.left:
            change = node.left
        else:
            change = node.right
        if change:
            change.parent = node.parent
            if node.parent is None:
                self.root = change
            elif node.parent.left is node:
                node.parent.left = change
            else:
                node.parent.right = change
            self.moreremove(change)
            node.left = node.right = node.parent = None
        elif node.parent is None:
            self.root = None
            self.moreremove(node)
        else:
            if node is node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            self.moreremove(node)
            node.parent = None

    def moreremove(self, node):
        if self.isred(node):
            node.paint(BLACK)
            return
        parent = node.parent
        if parent is None:
            return
        left = node.isleft() or parent.left is None
        sibling = parent.right if left else parent.left
        if left:
            if self.isred(sibling):
                sibling.paint(BLACK)
                parent.paint(RED)
                self.leftrotate(parent)
                sibling = parent.right
            if self.isblack(sibling.left) and self.isblack(sibling.right):
                parentBlack = self.isblack(parent)
                parent.paint(BLACK)
                sibling.paint(RED)
                if parentBlack:
                    if parent.isleft():
                        self.moreremove(parent)
            else:
                if sibling.right.isblack():
                    self.rightrotate(sibling)
                    sibling = parent.right
                    sibling.color = parent.color
                    parent.paint(BLACK)
                    sibling.right.paint(BLACK)
                    self.leftrotate(parent)
        else:
            if self.isred(sibling):
                sibling.paint(BLACK)
                parent.paint(RED)
                self.rightrotate(parent)
                sibling = parent.left
            if self.isblack(sibling.left) and self.isblack(sibling.right):
                parentBlack = parent.isblack()
                parent.paint(BLACK)
                sibling.paint(RED)
                if parentBlack:
                    if parent.isleft():
                        self.moreremove(parent)
            else:
                if self.isblack(sibling.left):
                    self.leftrotate(sibling)
                    sibling = parent.left
                sibling.color = parent.color
                parent.paint(BLACK)
                sibling.left.color = BLACK
                self.rightrotate(parent)

    def leftrotate(self, grand):
        parent = grand.right
        child = parent.left
        grand.right = child
        parent.left = grand
        self.morerotate(grand, parent, child)

    def rightrotate(self, grand):
        parent = grand.left
        child = parent.right
        grand.left = child
        parent.right = grand
        self.morerotate(grand, parent, child)

    def morerotate(self, grand, parent, child):
        if grand.isleft():
            grand.parent.left = parent
        elif grand.isright():
            grand.parent.right = parent
        else:
            self.root = parent
        if child:
            child.parent = grand
        parent.parent = grand.parent
        grand.parent = parent

    def printsort(self, subtree):
        if subtree is not None:
            self.printsort(subtree.left)
            print(str(subtree.key))
            self.printsort(subtree.right)

    def getsorted(self, subtree):
        if subtree is not None:
            self.getsorted(subtree.left)
            self.result.append(subtree.key)
            self.getsorted(subtree.right)