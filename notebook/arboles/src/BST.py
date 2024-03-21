# Clase que representa un nodo individual en el árbol
class Node:
    # Inicializa un nuevo nodo con datos pasados como parámetro
    def __init__(self, data):
        self.left = None  # Nodo izquierdo inicializado en None
        self.right = None  # Nodo derecho inicializado en None
        self.data = data  # Almacena los datos en el nodo

# Clase que representa un Árbol Binario de Búsqueda (BST)
class BST:
    # Inicializa un árbol binario de búsqueda vacío
    def __init__(self):
        self.root = None  # Raíz del árbol inicializada en None

    # Inserta un elemento nuevo en el árbol
    def insert(self, data):
        # Si la raíz es None, se crea el nodo raíz con la data proporcionada
        if self.root is None:
            self.root = Node(data)
        else:
            # De lo contrario, se llama al método recursivo para insertar en la posición adecuada
            self._insert_recursive(self.root, data)

    # Método auxiliar recursivo para insertar datos en el árbol
    def _insert_recursive(self, current_node, data):
        if data < current_node.data:  # Si la data es menor que la del nodo actual
            if current_node.left is None:  # Si no hay nodo izquierdo, inserta aquí
                current_node.left = Node(data)
            else:
                # En caso contrario, hacer una llamada recursiva hacia la izquierda
                self._insert_recursive(current_node.left, data)
        else:  # Si la data es mayor o igual que la del nodo actual
            if current_node.right is None:  # Si no hay nodo derecho, inserta aquí
                current_node.right = Node(data)
            else:
                # En caso contrario, hacer una llamada recursiva hacia la derecha
                self._insert_recursive(current_node.right, data)
