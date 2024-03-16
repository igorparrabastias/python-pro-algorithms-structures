from graphviz import Digraph

def visualize_bt(tree):
    dot = Digraph(comment='Binary Tree')

    if not tree.root:
        dot.node('null', 'Empty Tree', shape='plaintext')
        return dot

    def add_nodes_edges(node, dot=None):
        if node.left:
            dot.node(str(node.left.data), str(node.left.data))
            dot.edge(str(node.data), str(node.left.data))
            add_nodes_edges(node.left, dot=dot)

        if node.right:
            dot.node(str(node.right.data), str(node.right.data))
            dot.edge(str(node.data), str(node.right.data))
            add_nodes_edges(node.right, dot=dot)

    # Add root node
    dot.node(str(tree.root.data), str(tree.root.data))

    # Add other nodes
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
