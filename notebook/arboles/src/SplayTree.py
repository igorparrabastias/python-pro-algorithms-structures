# La clase Node define la estructura básica de un nodo dentro de un árbol
# binario.
class Node:
    # El método inicializador crea un nuevo nodo con el dato proporcionado y
    # establece sus hijos izquierdo y derecho a None.
    def __init__(self, data):
        self.data = data  # Almacena el dato pasado al nodo.
        self.left = None  # Inicializa el hijo izquierdo del nodo como None.
        self.right = None  # Inicializa el hijo derecho del nodo como None.

# La clase SplayTree representa un árbol splay, un tipo especial de árbol de
# búsqueda binario.
class SplayTree:
    # El método inicializador crea un nuevo árbol splay sin nodos (es decir, con
    # la raíz igual a None).
    def __init__(self):
        self.root = None  # Establece la raíz del árbol a None.

    # Método para realizar una rotación a la derecha en el árbol.
    def rightRotate(self, x):
        print(f"Realizando rotación a la derecha en el nodo con dato {x.data}")
        y = x.left
        x.left = y.right
        y.right = x
        return y  # Retorna el nuevo subárbol después de la rotación.

    # Método para realizar una rotación a la izquierda en el árbol.
    def leftRotate(self, x):
        print(f"Realizando rotación a la izquierda en el nodo con dato {x.data}")
        y = x.right
        x.right = y.left
        y.left = x
        return y  # Retorna el nuevo subárbol después de la rotación.

    # Método splay ajusta el árbol para que el nodo con el dato buscado sea
    # movido a la raíz.
    def splay(self, root, data):
        # Si la raíz es None o contiene el dato buscado, no se realiza ninguna
        # acción.
        if root is None or root.data == data:
            return root

        # Si el dato es menor que el dato en la raíz, se realizan operaciones en
        # el subárbol izquierdo.
        if root.data > data:
            # Si no hay subárbol izquierdo, no se puede continuar y se retorna
            # la raíz.
            if root.left is None:
                return root
            # Rotaciones dobles o simples se realizan dependiendo del valor del
            # hijo izquierdo.
            if root.left.data > data:
                root.left.left = self.splay(root.left.left, data)
                root = self.rightRotate(root)
            elif root.left.data < data:
                root.left.right = self.splay(root.left.right, data)
                if root.left.right:
                    root.left = self.leftRotate(root.left)
            return self.rightRotate(root) if root.left else root

        # Si el dato es mayor que el dato en la raíz, se realizan operaciones en
        # el subárbol derecho.
        else:
            # Si no hay subárbol derecho, no se puede continuar y se retorna la
            # raíz.
            if root.right is None:
                return root
            # Rotaciones dobles o simples se realizan dependiendo del valor del
            # hijo derecho.
            if root.right.data > data:
                root.right.left = self.splay(root.right.left, data)
                if root.right.left:
                    root.right = self.rightRotate(root.right)
            elif root.right.data < data:
                root.right.right = self.splay(root.right.right, data)
                root = self.leftRotate(root)
            return self.leftRotate(root) if root.right else root

    # Método para insertar un nuevo dato en el árbol.
    def insert(self, data):
        print(f"Insertando dato {data} en el árbol")
        # Si el árbol está vacío, se crea una nueva raíz con el dato.
        if not self.root:
            self.root = Node(data)
            return
        # Se realiza la operación splay para el dato y se ajusta el árbol.
        self.root = self.splay(self.root, data)
        # Si el dato ya existe en el árbol, no se realiza la inserción.
        if self.root.data == data:
            return
        # Se crea un nuevo nodo y se reajusta el árbol con este nuevo nodo como
        # raíz.
        new_node = Node(data)
        if self.root.data > data:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None
        # Se establece el nuevo nodo como la raíz del árbol.
        self.root = new_node
        print(f"Dato {data} insertado exitosamente")
