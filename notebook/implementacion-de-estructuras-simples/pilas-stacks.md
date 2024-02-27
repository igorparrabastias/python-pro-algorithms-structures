# Pilas (Stacks)

Una pila (stack) es una estructura de datos que sigue el principio de "último en entrar, primero en salir" (LIFO, Last In First Out). En Python, puedes implementar una pila utilizando listas, ya que estas proporcionan métodos para simular el comportamiento de una pila. A continuación, te muestro cómo implementar una pila con sus operaciones básicas:

1. **Definición de la Clase Pila**

```python
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """ Verifica si la pila está vacía. """
        return len(self.items) == 0

    def push(self, item):
        """ Agrega un elemento al tope de la pila. """
        self.items.append(item)

    def pop(self):
        """ Remueve y retorna el elemento del tope de la pila. """
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        """ Retorna el elemento del tope sin removerlo. """
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        """ Retorna el tamaño de la pila. """
        return len(self.items)

    def print_stack(self):
        """ Imprime los elementos de la pila. """
        for item in reversed(self.items):
            print(item)
```

1. **Uso de la Pila**

```python
# Creando una pila
stack = Stack()

# Agregando elementos
stack.push("Apple")
stack.push("Banana")
stack.push("Cherry")

# Imprimiendo la pila
stack.print_stack()

# Verificando el elemento superior
print("Top item:", stack.peek())

# Removiendo elementos
print("Popped:", stack.pop())
print("Popped:", stack.pop())

# Imprimiendo la pila después de las eliminaciones
stack.print_stack()

```

En este código, `push` agrega un elemento al final de la lista (el tope de la pila), `pop` elimina el último elemento y lo devuelve, `peek` devuelve el último elemento sin removerlo, y `is_empty` verifica si la pila está vacía. `print_stack` es un método auxiliar para visualizar los elementos de la pila. Esta es una manera sencilla y efectiva de implementar una pila en Python aprovechando las características de las listas.