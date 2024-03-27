class Node:
    # Constructor para el nodo
    def __init__(self, data, color="red"):
        self.data = data
        self.color = color
        self.parent = None
        self.left = None
        self.right = None

class RBTree:
    # Constructor para el árbol rojo-negro
    def __init__(self):
        self.NIL = Node(data=None, color="black")
        self.root = self.NIL

    # ---- Sección: Métodos de Inserción ---- #

    # Método para insertar un nuevo nodo
    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        # Búsqueda del lugar adecuado para la inserción
        while current != self.NIL:
            parent = current
            if new_node.data < current.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        # Determinación de la posición del nuevo nodo dentro del árbol
        if parent is None:
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        # Establecer el color inicial del nuevo nodo a rojo
        new_node.color = "red"
        # Llamar al método para corregir la inserción
        self.fix_insert(new_node)

    # ---- Sección: Métodos auxiliares de Inserción ---- #

    # Método para corregir las propiedades después de la inserción
    def fix_insert(self, new_node):
        # Mientras que no se llegue a la raíz y el padre sea rojo
        while new_node != self.root and new_node.parent.color == "red":

            # Si el padre es hijo izquierdo
            if new_node.parent == new_node.parent.parent.left:
                uncle = new_node.parent.parent.right
                # Caso 1
                if uncle.color == "red":
                    new_node.parent.color = "black"
                    uncle.color = "black"
                    new_node.parent.parent.color = "red"
                    new_node = new_node.parent.parent
                else:
                    # Caso 2: si el nuevo nodo es el hijo derecho
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.left_rotate(new_node)
                    # Caso 3
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    self.right_rotate(new_node.parent.parent)
            else:
                # Los mismos casos pero con el padre siendo hijo derecho
                uncle = new_node.parent.parent.left
                # Caso 1
                if uncle.color == "red":
                    new_node.parent.color = "black"
                    uncle.color = "black"
                    new_node.parent.parent.color = "red"
                    new_node = new_node.parent.parent
                else:
                    # Caso 2: si el nuevo nodo es el hijo izquierdo
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.right_rotate(new_node)
                    # Caso 3
                    new_node.parent.color = "black"
                    new_node.parent.parent.color = "red"
                    self.left_rotate(new_node.parent.parent)

        # Aseguramos que la raíz siempre sea negra
        self.root.color = "black"

    # Método para realizar rotación izquierda
    def left_rotate(self, node):
        # Establecer y como el hijo derecho del nodo actual
        y = node.right
        # Trasladar el hijo izquierdo de y al hijo derecho de node
        node.right = y.left
        if y.left != self.NIL:
            # Si el hijo izquierdo de y no es NIL, actualizar su padre
            y.left.parent = node
        # Hacer que el padre de y sea el padre de node
        y.parent = node.parent
        if node.parent is None:
            # Si node es la raíz, hacer a y la nueva raíz
            self.root = y
        elif node == node.parent.left:
            # Si node es hijo izquierdo, actualizar el hijo izquierdo de su
            # padre a y
            node.parent.left = y
        else:
            # Si node es hijo derecho, actualizar el hijo derecho de su
            # padre a y
            node.parent.right = y
        # Colocar node a la izquierda de y
        y.left = node
        # Hacer que el padre de node sea y
        node.parent = y

    # Método para realizar rotación derecha
    def right_rotate(self, node):
        # Establecer x como el hijo izquierdo del nodo actual
        x = node.left
        # Trasladar el hijo derecho de x al hijo izquierdo de node
        node.left = x.right
        if x.right != self.NIL:
            # Si el hijo derecho de x no es NIL, actualizar su padre
            x.right.parent = node
        # Hacer que el padre de x sea el padre de node
        x.parent = node.parent
        if node.parent is None:
            # Si node es la raíz, hacer a x la nueva raíz
            self.root = x
        elif node == node.parent.right:
            # Si node es hijo derecho, actualizar el hijo derecho de su
            # padre a x
            node.parent.right = x
        else:
            # Si node es hijo izquierdo, actualizar el hijo izquierdo de su
            # padre a x
            node.parent.left = x
        # Colocar node a la derecha de x
        x.right = node
        # Hacer que el padre de node sea x
        node.parent = x

