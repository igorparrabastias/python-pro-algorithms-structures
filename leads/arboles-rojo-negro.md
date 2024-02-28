## Clase: Árboles Rojo-Negro

### Introducción:

Los árboles Rojo-Negro son una forma elegante de mantener los árboles binarios de búsqueda equilibrados. Este tipo de estructura de datos es fundamental para entender cómo ciertos contenedores en lenguajes de programación, como los mapas y sets en C++, mantienen su eficiencia en operaciones como inserción, borrado y búsqueda. La clave de su eficiencia radica en cómo se equilibran a sí mismos mediante reglas específicas y recoloreamiento de nodos.

### Árboles Rojo-Negro:

Los árboles Rojo-Negro son una categoría especial de árboles binarios de búsqueda que siguen ciertas reglas para asegurar el balanceo del árbol. Cada nodo en el árbol tiene un color asignado, rojo o negro, y el árbol debe cumplir con las siguientes propiedades:

- **Propiedad 1**: Cada nodo es rojo o negro.
- **Propiedad 2**: La raíz siempre es negra.
- **Propiedad 3**: Todos los nodos hoja (NIL) son negros.
- **Propiedad 4**: Si un nodo es rojo, entonces ambos hijos son negros (no pueden haber dos nodos rojos consecutivos en cualquier camino desde la raíz a una hoja).
- **Propiedad 5**: Para cada nodo, todos los caminos desde el nodo a sus hojas descendientes contienen el mismo número de nodos negros.

Estas reglas aseguran que el árbol permanezca aproximadamente balanceado, con la altura máxima siendo solo el doble del logaritmo en base dos del número de nodos, lo que garantiza operaciones de búsqueda, inserción y borrado en tiempo logarítmico.

#### Ejemplos:
- **Inserción**: Al insertar un nuevo nodo, este se colorea de rojo. Luego, se realizan ajustes en el árbol (rotaciones y recoloreo) para asegurar que se mantengan las propiedades de los árboles Rojo-Negro.
- **Borrado**: El borrado puede ser más complejo ya que al remover un nodo, se pueden violar las propiedades del árbol. Se utilizan técnicas de recoloreo y rotación para restablecer el equilibrio.

### Ejercicios:
1. **Implementar la Inserción en un Árbol Rojo-Negro**: Escribe un algoritmo de inserción que inserte nodos manteniendo el árbol balanceado según las reglas de los árboles Rojo-Negro.
2. **Búsqueda en un Árbol Rojo-Negro**: Implementa una función de búsqueda que eficientemente encuentre un valor dado en un árbol Rojo-Negro.
3. **Eliminar un Nodo**: Desarrolla un algoritmo para eliminar un nodo en un árbol Rojo-Negro, asegurando que el árbol se reequilibre y mantenga sus propiedades.
4. **Contar Nodos Negros**: Escribe una función que cuente el número de nodos negros en cualquier camino desde la raíz hasta las hojas.
5. **Verificar Propiedades de Árbol Rojo-Negro**: Implementa una función que verifique si un árbol binario cumple con las propiedades de un árbol Rojo-Negro.

### Conclusión:
Los árboles Rojo-Negro son una herramienta poderosa para mantener estructuras de datos balanceadas. Al seguir sus reglas específicas, podemos asegurar que las operaciones de inserción, búsqueda y borrado se mantengan eficientes, lo cual es crucial para el rendimiento de muchas aplicaciones de software. En la próxima clase, exploraremos otra estructura de datos avanzada, ampliando así nuestro repertorio de herramientas algorítmicas.

---

### Soluciones:

#### Ejercicio 1: Implementar la Inserción en un Árbol Rojo-Negro

```python
class NodoRN:
    def __init__(self, valor, color="rojo", izquierda=None, derecha=None, padre=None):
        self.valor = valor
        self.color = color
        self.izquierda = izquierda
        self.derecha = derecha
        self.padre = padre

# Supongamos que ya tenemos definida la clase ÁrbolRN con métodos para mantener las propiedades Rojo-Negro.

def insertar(arbol, valor):
    # Este es un pseudocódigo. La implementación completa requeriría manejar las rotaciones y recoloreo.
    nuevo_nodo = NodoRN(valor)
    if arbol.raiz is None:
        arbol.raiz = nuevo_nodo
    else:
        # Insertar el nodo en el árbol como en un BST
        # Luego, ajustar el árbol para mantener las propiedades Rojo-Negro
        pass
```

#### Ejercicio 2: Búsqueda en un Árbol Rojo-Negro

```python
def buscar(arbol, valor):
    return buscar_nodo(arbol.raiz, valor)

def buscar_nodo(nodo, valor):
    if nodo is None or valor == nodo.valor:
        return nodo
    if valor < nodo.valor:
        return buscar_nodo(nodo.izquierda, valor)
    else:
        return buscar_nodo(nodo.derecha, valor)
```

#### Ejercicio 3: Eliminar un Nodo

```python
# La eliminación en un árbol Rojo-Negro es más compleja debido a la necesidad de mantener el árbol balanceado.
# Este pseudocódigo muestra un enfoque simplificado.
def eliminar(arbol, valor):
    # Encontrar el nodo a eliminar
    # Reemplazar el nodo por su sucesor si es necesario
    # Ajustar el árbol para mantener las propiedades Rojo-Negro
    pass
```

#### Ejercicio 4: Contar Nodos Negros

```python
def contar_nodos_negros(nodo):
    if nodo is None:
        return 1  # Los nodos NIL se consideran negros
    else:
        izquierda = contar_nodos_negros(nodo.izquierda)
        derecha = contar_nodos_negros(nodo.derecha)
        return izquierda + (nodo.color == "negro")
```

#### Ejercicio 5: Verificar Propiedades de Árbol Rojo-Negro

```python
def verificar_propiedades(arbol):
    # Verificar las cinco propiedades de los árboles Rojo-Negro
    pass
```