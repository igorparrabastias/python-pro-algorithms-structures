La búsqueda en anchura (BFS, Breadth-First Search) es otro algoritmo utilizado para recorrer y explorar todos los nodos de un grafo, pero a diferencia de DFS, BFS explora los nodos vecinos antes de moverse hacia los nodos más profundos. Aquí te muestro cómo implementar BFS en un grafo representado mediante una matriz de adyacencia en Python:

### Implementación de Búsqueda en Anchura (BFS) en un Grafo

```python
from collections import deque

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

    def breadth_first_search(self, start_vertex):
        """
        Realiza una búsqueda en anchura (BFS) comenzando desde el vértice de inicio.
        """
        if 0 <= start_vertex < self.num_vertices:
            queue = deque()
            queue.append(start_vertex)
            self.visited[start_vertex] = True

            while queue:
                current_vertex = queue.popleft()
                print(current_vertex, end=' ')

                # Obtener todos los vértices adyacentes no visitados
                for i in range(self.num_vertices):
                    if self.adj_matrix[current_vertex][i] == 1 and not self.visited[i]:
                        queue.append(i)
                        self.visited[i] = True

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

print("Recorrido en Anchura (BFS):")
g.breadth_first_search(0)  # Comenzar desde el vértice 0
print("\\n")

# Reiniciar la lista de nodos visitados
g.reset_visited()

# Realizar BFS desde otro vértice
print("Recorrido en Anchura desde vértice 3:")
g.breadth_first_search(3)  # Comenzar desde el vértice 3

```

En esta implementación:

- La función `breadth_first_search` inicia el recorrido BFS desde un vértice específico.
- Utilizamos una cola (deque) para mantener un seguimiento de los vértices que se deben visitar en el próximo nivel.
- La lista `visited` se utiliza para llevar un registro de los nodos visitados durante el recorrido.
- El método `reset_visited` reinicia la lista de nodos visitados para futuros recorridos.

Este código realizará un recorrido en anchura BFS en el grafo y mostrará los vértices visitados en orden. Puedes comenzar el recorrido desde cualquier vértice del grafo.