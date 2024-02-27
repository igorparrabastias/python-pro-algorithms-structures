# Colas (Queues)

Las colas (queues) son estructuras de datos que siguen el principio FIFO (First In, First Out), donde el primer elemento añadido es el primero en ser removido. En Python, puedes implementar colas utilizando la clase `deque` del módulo `collections`, que es una implementación de una cola de doble extremo y ofrece un rendimiento óptimo para este propósito.

A continuación, te muestro cómo implementar una cola con sus operaciones básicas:

1. **Definición de la Clase Cola**

```python
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        """ Verifica si la cola está vacía. """
        return len(self.queue) == 0

    def enqueue(self, item):
        """ Agrega un elemento al final de la cola. """
        self.queue.append(item)

    def dequeue(self):
        """ Remueve y retorna el primer elemento de la cola. """
        if not self.is_empty():
            return self.queue.popleft()
        return None

    def size(self):
        """ Retorna el tamaño de la cola. """
        return len(self.queue)

    def front(self):
        """ Retorna el primer elemento de la cola sin removerlo. """
        if not self.is_empty():
            return self.queue[0]
        return None

    def print_queue(self):
        """ Imprime los elementos de la cola. """
        for item in self.queue:
            print(item, end=" -> ")
        print("None")

```

1. **Uso de la Cola**

```python
# Creando una cola
queue = Queue()

# Agregando elementos
queue.enqueue("Apple")
queue.enqueue("Banana")
queue.enqueue("Cherry")

# Imprimiendo la cola
queue.print_queue()

# Verificando el primer elemento
print("Front item:", queue.front())

# Removiendo elementos
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())

# Imprimiendo la cola después de las eliminaciones
queue.print_queue()

```

En este código, `enqueue` agrega un elemento al final de la cola, `dequeue` elimina el primer elemento y lo devuelve, `front` devuelve el primer elemento sin removerlo, y `is_empty` verifica si la cola está vacía. `print_queue` es un método auxiliar para visualizar los elementos de la cola. Usando `deque` de `collections`, se logra una implementación eficiente de la cola en Python.