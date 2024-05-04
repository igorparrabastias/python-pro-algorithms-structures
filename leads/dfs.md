La búsqueda en profundidad (DFS, Depth-First Search) es un algoritmo utilizado para recorrer y explorar todos los nodos de un grafo. Puede ser implementado de manera recursiva o utilizando una pila (stack). A continuación, te mostraré cómo implementar la búsqueda en profundidad en un grafo representado mediante una matriz de adyacencia en Python:

### Implementación de Búsqueda en Profundidad (DFS) en un Grafo

```python
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.visited = [False] * num_vertices

    def add_edge(self, start_vertex, end_vertex):
        # Asumiendo que es un grafo no dirigido
        if 0 <= start_vertex < self.num_vertices and 0 <= end_vertex < self.num_vertices:
            self.adj_matrix[start_vertex][end_vertex] = 1
            self.adj_matrix[end_vertex][start_vertex] = 1

    def depth_first_search(self, start_vertex):
        """
        Realiza una búsqueda en profundidad (DFS) comenzando desde el vértice de inicio.
        """
        if 0 <= start_vertex < self.num_vertices:
            self._dfs_recursive(start_vertex)

    def _dfs_recursive(self, vertex):
        """
        Función auxiliar recursiva para DFS.
        """
        print(vertex, end=' ')  # Imprimir el vértice actual
        self.visited[vertex] = True

        # Recorrer todos los vértices adyacentes no visitados
        for i in range(self.num_vertices):
            if self.adj_matrix[vertex][i] == 1 and not self.visited[i]:
                self._dfs_recursive(i)

    def reset_visited(self):
        """
        Reinicia la lista de nodos visitados para futuros recorridos.
        """
        self.visited = [False] * self.num_vertices

# Ejemplo de uso
g = Graph(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)

print("Recorrido en Profundidad (DFS):")
g.depth_first_search(0)  # Comenzar desde el vértice 0
print("\\n")

# Reiniciar la lista de nodos visitados
g.reset_visited()

# Realizar DFS desde otro vértice
print("Recorrido en Profundidad desde vértice 3:")
g.depth_first_search(3)  # Comenzar desde el vértice 3

```

En esta implementación:

- La función `depth_first_search` inicia el recorrido DFS desde un vértice específico.
- La función `_dfs_recursive` es una función auxiliar que realiza la exploración de manera recursiva.
- La lista `visited` se utiliza para llevar un registro de los nodos visitados durante el recorrido.
- El método `reset_visited` reinicia la lista de nodos visitados para futuros recorridos.

Este código realizará un recorrido en profundidad DFS en el grafo y mostrará los vértices visitados en orden. Puedes comenzar el recorrido desde cualquier vértice del grafo.