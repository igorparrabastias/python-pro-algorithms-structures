class Node:
    def __init__(self, data, color="red"):
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

class RBTree:
    def __init__(self):
        self.NIL = Node(data=None, color="black")
        self.root = self.NIL

    # -------------- Section: Insertion Methods -------------- #

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "red"
        self.fix_insert(new_node)

    def fix_insert(self, new_node):
        while new_node != self.root and new_node.parent.color == "red":
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                if uncle.color == "red":  # Caso 1
                    new_node.parent.color = "black"
                    uncle.color = "black"
                    new_node.parent.parent.color = "red"
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:  # Caso 2
                        new_node = new_node.parent
                        self.left_rotate(new_node)
                    # Caso 3
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    self.right_rotate(new_node.parent.parent)
            else:
                # Los mismos casos pero con el tío siendo el hijo izquierdo
                uncle = new_node.parent.parent.left
                if uncle.color == "red":  # Caso 1
                    new_node.parent.color = "black"
                    uncle.color = "black"
                    new_node.parent.parent.color = "red"
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:  # Caso 2
                        new_node = new_node.parent
                        self.right_rotate(new_node)
                    # Caso 3
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    self.left_rotate(new_node.parent.parent)
        self.root.color = "black"

    def left_rotate(self, node):
        # Implementación de la rotación izquierda
        y = node.right
        node.right = y.left
        if y.left != self.NIL:
            y.left.parent = node
        y.parent = node.parent
        if node.parent is None:
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
        y.left = node
        node.parent = y

    def right_rotate(self, node):
        # Implementación de la rotación derecha
        x = node.left
        node.left = x.right
        if x.right != self.NIL:
            x.right.parent = node
        x.parent = node.parent
        if node.parent is None:
            self.root = x
        elif node == node.parent.right:
            node.parent.right = x
        else:
            node.parent.left = x
        x.right = node
        node.parent = x
