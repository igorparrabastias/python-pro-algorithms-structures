from graphviz import Digraph

def visualize_bt(tree):
    dot = Digraph(comment='Binary Tree')

    if not tree.root:
        dot.node('null', 'Empty Tree', shape='plaintext')
        return dot

    # Usamos id(node) para asegurar que cada nodo sea único.
    def add_nodes_edges(node, dot=None):
        node_id = str(id(node))  # Identificador único basado en la id de memoria del nodo

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
            add_nodes_edges(child, dot=dot)  # Recursivamente hacer lo mismo para cada hijo

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
            nil_id = f"nil{parent_id}{edge_label}"
            dot.node(nil_id, 'NIL', shape='box', style='filled', fillcolor='grey', fontcolor='white')
            dot.edge(parent_id, nil_id, label=edge_label)
            return

        node_id = str(id(node))  # Identificador único basado en la id de memoria del nodo
        node_label = f"{node.data}\n{node.color.upper()}"

        # Ajusta el color del fondo y de la fuente según el color del nodo
        if node.color == "red":
            dot.node(node_id, node_label, style='filled', fillcolor='white', fontcolor='black')
        else:  # Nodo negro
            dot.node(node_id, node_label, style='filled', fillcolor='black', fontcolor='white')

        # Si el nodo no es la raíz, añade un borde al padre
        if parent_id is not None:
            dot.edge(parent_id, node_id, label=edge_label)

        add_nodes_edges(node.left, dot=dot, parent_id=node_id, edge_label='L')
        add_nodes_edges(node.right, dot=dot, parent_id=node_id, edge_label='R')

    # Inicia el proceso con el nodo raíz
    root_id = str(id(tree.root))
    root_label = f"{tree.root.data}\n{tree.root.color.upper()}"

    if tree.root.color == "red":
        dot.node(root_id, root_label, style='filled', fillcolor='white', fontcolor='black')
    else:  # Nodo raíz negro
        dot.node(root_id, root_label, style='filled', fillcolor='black', fontcolor='white')

    add_nodes_edges(tree.root, dot=dot, parent_id=root_id)

    return dot
