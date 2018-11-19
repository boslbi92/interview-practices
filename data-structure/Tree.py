

class Node():
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

    def insert(self, value):
        if self.value == value:
            return False
        elif self.value > value:
            if self.left is not None:
                return self.left.insert(value)
            else:
                self.left = Node(value)
                return True
        else:
            if self.right is not None:
                return self.right.insert(value)
            else:
                self.right = Node(value)
                return True
        return False

    def find(self, value):
        if self.value == value:
            return True
        elif self.value > value:
            if self.left is not None:
                return self.left.find(value)
            else:
                self.left = Node(value)
                return True
        else:
            if self.right is not None:
                return self.right.find(value)
            else:
                self.right = Node(value)
                return True
        return False

    def preorder(self, value):
        if self.value == value:
            return True
        if self.left:
            self.left.preorder(value)
        if self.right:
            self.right.preorder(value)

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return True
        else:
            self.root.insert(value)

    def find(self, value):
        if self.root is None:
            return False
        return self.root.find(value)

    def preorder_traversal(self, value):
        if self.root is None:
            return False
        return self.root.preorder(value)


