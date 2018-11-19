

class Node():
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

class DoublyLinkedList():
    def __init__(self):
        self.head = None

    def add(self, value):
        new_node = Node(value)

        # initialize head for first time
        if self.head == None:
            self.head = new_node
        else:
            # traverse until the end and insert
            root = self.head
            while(root.next_node is not None):
                root = root.next_node
            root.next_node = new_node
            new_node.prev_node = root

    def add_beginning(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head.prev_node = new_node
        self.head = new_node

    def remove(self, value):
        root = self.head
        if root == None:
            return False
        if root.value == value:
            self.head = root.next_node
            self.head.prev_node = None

        while(root.next_node is not None):
            middle = root.next_node
            if middle.value == value:
                root.next_node = middle.next_node
                middle.next_node.prev_node = root
                return True
            else:
                root = middle

        return False



