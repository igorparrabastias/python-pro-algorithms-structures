from graphviz import Digraph

def visualize(tree):
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
