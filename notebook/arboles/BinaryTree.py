from graphviz import Digraph

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def agregar_nodos_edges(arbol, grafico, etiquetas, nil_counter=[0]):
    if arbol is not None:
        # Agregar el nodo actual al gráfico
        grafico.node(str(arbol.valor), label=str(arbol.valor))
        etiquetas[arbol.valor] = str(len(etiquetas) + 1)

        # Si el nodo actual tiene hijo izquierdo, agregar nodo y arista al gráfico
        if arbol.izquierda is not None:
            grafico.edge(str(arbol.valor), str(arbol.izquierda.valor))
            agregar_nodos_edges(arbol.izquierda, grafico, etiquetas)
        else:
            # Agregar un nodo 'nil' invisible para mantener la estructura del árbol
            nil_counter[0] += 1
            grafico.node(f'nil{nil_counter[0]}', style='invisible')
            grafico.edge(str(arbol.valor), f'nil{nil_counter[0]}', style='invisible')

        # Si el nodo actual tiene hijo derecho, agregar nodo y arista al gráfico
        if arbol.derecha is not None:
            grafico.edge(str(arbol.valor), str(arbol.derecha.valor))
            agregar_nodos_edges(arbol.derecha, grafico, etiquetas)
        else:
            # Agregar un nodo 'nil' invisible para mantener la estructura del árbol
            nil_counter[0] += 1
            grafico.node(f'nil{nil_counter[0]}', style='invisible')
            grafico.edge(str(arbol.valor), f'nil{nil_counter[0]}', style='invisible')

def graficar_arbol(arbol, tipo_recorrido):
    grafico = Digraph(comment=f'Árbol {tipo_recorrido}')

    # Establece la dirección del gráfico de arriba hacia abajo
    grafico.attr(rankdir='TB')

    # Diccionario para mantener el seguimiento del orden de los nodos visitados
    etiquetas = {}

    # Agrega los nodos y las aristas al gráfico
    agregar_nodos_edges(arbol, grafico, etiquetas)

    # Etiquetas para el tipo de recorrido (preorden, inorden, postorden)
    for nodo, visita in etiquetas.items():
        grafico.node(str(nodo), f'{nodo}\n({visita})')

    # Renderiza y muestra el gráfico
    grafico.render(f'arbol_{tipo_recorrido}', view=True)

# Creación del árbol
raiz = Nodo(1)
raiz.izquierda = Nodo(2)
raiz.derecha = Nodo(3)
raiz.izquierda.izquierda = Nodo(4)
raiz.izquierda.derecha = Nodo(5)
raiz.derecha.izquierda = Nodo(6)
raiz.derecha.derecha = Nodo(7)

# Graficar el árbol
graficar_arbol(raiz, 'Estructura')
