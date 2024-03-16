class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new_node = Node(key)
        if not self.root:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)

            # Si el nodo actual no tiene hijo izquierdo, lo insertamos aquí.
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            # Si el nodo actual no tiene hijo derecho, lo insertamos aquí.
            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)

