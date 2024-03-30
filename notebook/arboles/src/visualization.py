from graphviz import Digraph


def visualize_bt(tree):
    dot = Digraph(comment='Binary Tree')

    if not tree.root:
        dot.node('null', 'Empty Tree', shape='plaintext')
        return dot

    # Usamos id(node) para asegurar que cada nodo sea único.
    def add_nodes_edges(node, dot=None):
        # Identificador único basado en la id de memoria del nodo
        node_id = str(id(node))

        if node.left:
            left_id = str(id(node.left))
            dot.node(left_id, str(node.left.data))
            dot.edge(node_id, left_id, label='L')
            add_nodes_edges(node.left, dot=dot)

        if node.right:
            right_id = str(id(node.right))
            dot.node(right_id, str(node.right.data))
            dot.edge(node_id, right_id, label='R')
            add_nodes_edges(node.right, dot=dot)

    # Inicia el proceso con el nodo raíz
    root_id = str(id(tree.root))
    dot.node(root_id, str(tree.root.data))
    add_nodes_edges(tree.root, dot=dot)

    return dot


def visualize_t(tree):
    dot = Digraph(comment='N-ary Tree')

    if not tree.root:
        dot.node('null', 'Empty Tree', shape='plaintext')
        return dot

    def add_nodes_edges(node, dot=None):
        # Agregar los hijos del nodo actual al gráfico y conectarlos
        for child in node.children:
            dot.node(str(child.data), str(child.data))
            dot.edge(str(node.data), str(child.data))
            # Recursivamente hacer lo mismo para cada hijo
            add_nodes_edges(child, dot=dot)

    # Agregar nodo raíz
    dot.node(str(tree.root.data), str(tree.root.data))

    # Agregar otros nodos empezando desde la raíz
    add_nodes_edges(tree.root, dot=dot)

    return dot


def visualize_rbtree(tree):
    dot = Digraph(comment='Red-Black Tree')

    if not tree.root or tree.root == tree.NIL:
        dot.node('null', 'Empty Tree', shape='plaintext')
        return dot

    def add_nodes_edges(node, dot=None, parent_id=None, edge_label=''):
        if node == tree.NIL:
            # Crear un nodo NIL único para cada posición
            nil_id = f"nil{parent_id}{edge_label}"
            dot.node(nil_id, 'NIL', shape='box', style='filled',
                     fillcolor='grey', fontcolor='white')
            if parent_id is not None:  # Asegurarse de que el nodo raíz no se autoconecte
                dot.edge(parent_id, nil_id, label=edge_label)
            return

        # Identificador único basado en la id de memoria del nodo
        node_id = str(id(node))
        node_label = f"{node.data}\n{node.color.upper()}"

        # Ajusta el color del fondo y de la fuente según el color del nodo
        if node.color == "red":
            dot.node(node_id, node_label, style='filled',
                     fillcolor='white', fontcolor='black')
        else:  # Nodo negro
            dot.node(node_id, node_label, style='filled',
                     fillcolor='black', fontcolor='white')

        # Conectar con el nodo padre si existe
        if parent_id is not None:
            dot.edge(parent_id, node_id, label=edge_label)

        add_nodes_edges(node.left, dot=dot, parent_id=node_id, edge_label='L')
        add_nodes_edges(node.right, dot=dot, parent_id=node_id, edge_label='R')

    # Inicia el proceso con el nodo raíz sin intentar conectarlo a un nodo padre
    add_nodes_edges(tree.root, dot=dot)

    return dot


def visualize_b_tree(root):
    dot = Digraph(comment='B Tree / B+ Tree')

    if not root:
        dot.node('null', 'Empty Tree', shape='plaintext')
        return dot

    def add_nodes_edges(node, dot=None, parent_id=None):
        # Crear un identificador único para el nodo actual basado en sus claves
        node_id = '-'.join(str(key) for key in node.keys)
        if parent_id is not None:
            # Conectar el nodo actual con su padre
            dot.edge(parent_id, node_id)
        else:
            # Si no hay padre, es la raíz
            dot.node(node_id, label='|'.join(str(key) for key in node.keys))

        if node.children:
            # El nodo no es una hoja, continuar con sus hijos
            for child in node.children:
                if child:  # Verificar si el hijo no es None
                    add_nodes_edges(child, dot=dot, parent_id=node_id)
        else:
            # Para árboles B+, conectar hojas entre sí
            # Este código no implementa la conexión secuencial explícita entre hojas.
            if node != root and len(node.keys) > 0:
                dot.node(node_id, label='|'.join(str(key)
                         for key in node.keys) + '|', shape='record')

    # Comenzar la visualización desde la raíz
    add_nodes_edges(root, dot=dot)

    return dot
