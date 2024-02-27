# Listas Enlazadas (Linked Lists)

Implementar una lista enlazada en Python es un excelente ejercicio para comprender mejor las estructuras de datos. Vamos a crear una lista enlazada simple, donde cada nodo tiene un valor y una referencia al siguiente nodo. Aquí está el código con los métodos básicos:

1. **Definición de la Clase Nodo**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

1. **Definición de la Clase Lista Enlazada**

```python
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """ Agrega un nuevo nodo al final de la lista. """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """ Agrega un nuevo nodo al inicio de la lista. """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        """ Inserta un nuevo nodo después de un nodo dado. """
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        """ Elimina el nodo con el valor 'key'. """
        curr_node = self.head

        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return

        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return

        prev.next = curr_node.next
        curr_node = None

    def print_list(self):
        """ Imprime todos los elementos de la lista. """
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print("None")
```

1. **Uso de la Lista Enlazada**

```python
# Creando la lista enlazada y añadiendo elementos
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.prepend("0")
llist.insert_after_node(llist.head.next, "C")

# Eliminando un elemento
llist.delete_node("B")

# Imprimiendo la lista
llist.print_list()

```

Este código define una lista enlazada simple con métodos para agregar, insertar y eliminar nodos, así como para imprimir la lista. Puedes expandir esta implementación para incluir más funcionalidades según tus necesidades.