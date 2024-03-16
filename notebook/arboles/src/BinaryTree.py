class Node:
    def __init__(self, key):
        self.left = None          # Inicializa el hijo izquierdo como None
        self.right = None         # Inicializa el hijo derecho como None
        self.data = key           # Establece el valor de datos para el nodo

class BinaryTree:
    def __init__(self):
        self.root = None          # Inicializa el nodo raíz como None al crear una nueva instancia de Árbol Binario

    def insert(self, key):
        new_node = Node(key)      # Crea un nuevo nodo con la clave proporcionada
        if not self.root:         # Si el árbol está vacío,
            self.root = new_node  # establece el nuevo nodo como la raíz y devuelve

        queue = [self.root]       # Crea una cola comenzando con el nodo raíz
        while queue:
            current = queue.pop(0)   # Desencola el elemento frontal de la cola

            # Si el nodo actual no tiene un hijo izquierdo, inserta el nuevo nodo aquí
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)  # Agrega el hijo izquierdo a la cola

            # Si el nodo actual no tiene un hijo derecho, inserta el nuevo nodo aquí
            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)  # Agrega el hijo derecho a la cola


