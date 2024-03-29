class Node:
    def __init__(self, data):
        # Constructor de la clase Nodo.
        # 'data' contiene el valor almacenado en el nodo.
        # 'left' apunta al hijo izquierdo del nodo (None si no tiene).
        # 'right' apunta al hijo derecho del nodo (None si no tiene).
        # 'parent' apunta al nodo padre (None si es la raíz).
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


class SplayTree:
    def __init__(self):
        # Constructor de la clase SplayTree.
        # Inicializa un árbol splay sin nodos, por lo tanto 'root' es None.
        self.root = None

    def rotate_left(self, x):
        # Realiza una rotación hacia la izquierda en el nodo x para reestructurar el árbol.
        # Este movimiento promueve el nodo derecho de x (y) a la posición de x,
        # Mientras que x se convierte en el hijo izquierdo de y.
        y = x.right
        x.right = y.left

        if y.left:
            y.left.parent = x

        y.parent = x.parent

        if not x.parent:
            print(f"Rotación izquierda: {x.data} ahora es la nueva raíz.")
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotate_right(self, x):
        # Realiza una rotación hacia la derecha en el nodo x para reestructurar el árbol.
        # Este movimiento promueve el nodo izquierdo de x (y) a la posición de x,
        # Mientras que x se convierte en el hijo derecho de y.
        y = x.left
        x.left = y.right

        if y.right:
            y.right.parent = x

        y.parent = x.parent

        if not x.parent:
            print(f"Rotación derecha: {x.data} ahora es la nueva raíz.")
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y

    def splay(self, x):
        # Realiza la operación de 'splay' en el nodo x. El objetivo es traer el nodo x a la raíz del árbol,
        # mediante una serie de rotaciones, para optimizar tiempos de acceso futuros a este nodo.
        while x.parent:
            if not x.parent.parent:
                if x == x.parent.left:
                    print(f"Splay - rotación a la derecha (Zig): {x.data}")
                    self.rotate_right(x.parent)
                else:
                    print(f"Splay - rotación a la izquierda (Zag): {x.data}")
                    self.rotate_left(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                print(
                    f"Splay - doble rotación a la derecha (Zig-Zig): {x.data}")
                self.rotate_right(x.parent.parent)
                self.rotate_right(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                print(
                    f"Splay - doble rotación a la izquierda (Zag-Zag): {x.data}")
                self.rotate_left(x.parent.parent)
                self.rotate_left(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                print(
                    f"Splay - rotación a la izquierda seguido de rotación a la derecha (Zag-Zig): {x.data}")
                self.rotate_left(x.parent)
                self.rotate_right(x.parent)
            else:
                print(
                    f"Splay - rotación a la derecha seguido de rotación a la izquierda (Zig-Zag): {x.data}")
                self.rotate_right(x.parent)
                self.rotate_left(x.parent)

    def insert(self, data):
        # Insertar un nuevo dato en el árbol splay.
        # El método encuentra la posición correcta del nuevo nodo y luego realiza un 'splay' de este.
        print(f"Insertar: {data}")
        node = Node(data)
        y = None
        x = self.root

        # Buscar dónde insertar el nuevo nodo.
        while x:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y

        # Si el árbol estaba vacío, el nuevo nodo será la raíz.
        if y is None:
            self.root = node
        else:
            # Si el valor es menor, inserta a la izquierda, sino a la derecha.
            if node.data < y.data:
                y.left = node
            else:
                y.right = node

        # Una vez insertado el nodo, es necesario hacer un 'splay' para optimizar futuros accesos.
        self.splay(node)

    def find(self, data):
        # Busca un nodo por su valor y realiza un 'splay' de este.
        # Esto colocará al nodo encontrado como la raíz del árbol,
        # o la última posición accedida en caso de no encontrarlo.
        print(f"Buscar: {data}")
        x = self.root
        while x:
            if data < x.data:
                x = x.left
            elif data > x.data:
                x = x.right
            else:
                # Si se encuentra el dato, se realiza un 'splay' del nodo.
                self.splay(x)
                return x

        # Si no se encuentra el dato, devuelve None.
        return None
