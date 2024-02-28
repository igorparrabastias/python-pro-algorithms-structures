## Clase: Árbol de Segmentos

### Introducción:
Los árboles de segmentos son una estructura de datos esencial para manejar de manera eficiente consultas de rango y actualizaciones en arreglos. Son especialmente útiles en contextos donde los datos cambian dinámicamente y se requieren respuestas rápidas a consultas como la suma, el mínimo o el máximo en un rango específico del arreglo. Su poder reside en la capacidad de dividir el problema en segmentos más pequeños, permitiendo operaciones en tiempo logarítmico.

### Árboles de Segmentos:
Un árbol de segmentos se construye a partir de un arreglo, donde cada nodo representa un segmento o rango del arreglo. La raíz del árbol representa el rango completo del arreglo, y cada hoja representa un solo elemento. Los nodos internos representan la unión de los segmentos de sus hijos. Esta estructura permite realizar operaciones de actualización y consulta en rangos específicos de manera eficiente.

#### Construcción:
La construcción de un árbol de segmentos comienza con la raíz representando el rango completo del arreglo. Se divide el arreglo en dos mitades, creando dos nodos hijos para la raíz, cada uno representando una mitad del arreglo. Este proceso se repite recursivamente hasta que cada elemento del arreglo es representado por una hoja del árbol.

Para ilustrar la construcción de un árbol de segmentos con un diagrama ASCII, tomemos como ejemplo el arreglo `[1, 3, 5, 7, 9, 11]`. La construcción del árbol de segmentos para este arreglo, considerando una operación de suma de rango, resultaría en algo como esto:

<pre>
                        [0, 5, 36]
                    /           \
            [0, 2, 9]             [3, 5, 27]
            /      \               /       \
        [0, 1, 4]   [2, 2, 5]   [3, 4, 16]   [5, 5, 11]
        /    \                      /    \
    [0, 0, 1] [1, 1, 3]        [3, 3, 7] [4, 4, 9]
</pre>

Este diagrama muestra la estructura del árbol de segmentos, donde cada nodo está representado como `[inicio, fin, suma]`. `inicio` y `fin` son los índices del segmento del arreglo que el nodo representa, y `suma` es la suma de los elementos en ese segmento (o el valor del elemento, en el caso de las hojas).

- La raíz del árbol representa la suma de todos los elementos en el arreglo, cubriendo el rango completo de índices de `0` a `5`.
- Cada nivel del árbol divide el rango del arreglo en segmentos más pequeños, hasta llegar a los nodos hoja, que representan un solo elemento del arreglo.
- Los nodos internos representan la suma de sus nodos hijos, permitiendo consultas de suma de rango eficientes.

Este árbol de segmentos permite realizar consultas de suma en un rango específico, así como actualizar los valores del arreglo original, manteniendo la estructura del árbol actualizada para reflejar estos cambios.


#### Consultas:
Para realizar una consulta en un rango, el árbol se recorre desde la raíz, dividiendo el rango de la consulta entre los nodos hijos hasta que se encuentren los segmentos exactos o parciales que cubren el rango deseado. La respuesta a la consulta es la combinación de los resultados de estos segmentos.

Para ilustrar cómo se realizan las consultas en un árbol de segmentos, utilizaremos el mismo árbol de segmentos construido para el arreglo `[1, 3, 5, 7, 9, 11]` y mostraremos cómo se consulta la suma del rango de índices 2 a 5.

El árbol de segmentos es el siguiente:

<pre>
                    [0, 5, 36]
                   /           \
          [0, 2, 9]             [3, 5, 27]
          /      \               /       \
    [0, 1, 4]   [2, 2, 5]   [3, 4, 16]   [5, 5, 11]
    /    \                      /    \
[0, 0, 1] [1, 1, 3]        [3, 3, 7] [4, 4, 9]
</pre>

Para realizar una consulta de suma para el rango de índices 2 a 5, el proceso es el siguiente:

1. Comenzamos en la raíz del árbol que cubre todo el arreglo `[0, 5]`.
2. Dividimos la búsqueda entre los nodos hijos, buscando aquellos que se intersecten con nuestro rango de consulta `[2, 5]`.

El proceso de consulta se desglosa así:

- **Nodo `[0, 5, 36]`**: Cubre el rango completo de la consulta, así que continuamos hacia sus hijos.
  - **Nodo `[0, 2, 9]`**: Parcialmente cubre el rango de consulta (hasta el índice 2). Necesitamos considerar solo el segmento que se intersecta, que es `[2, 2, 5]`.
  - **Nodo `[3, 5, 27]`**: Cubre completamente el resto del rango de consulta. Como cubre completamente parte de nuestro rango de interés, podemos tomar su suma directamente sin necesidad de descomponerlo más.

<pre>
Consulta: Suma de rango [2, 5]

                    [0, 5, 36]
                   /           \
          [0, 2, 9]             [3, 5, 27]  <--- Tomamos esta suma completamente
          /      \               /       \
    [0, 1, 4]   [2, 2, 5] <--- Parcial   [3, 4, 16]   [5, 5, 11]
                      \                      /    \
                   Tomamos esta suma    [3, 3, 7] [4, 4, 9]

</pre>

Para obtener la suma del rango `[2, 5]`, sumamos los valores de los nodos `[2, 2, 5]` y `[3, 5, 27]`, que son `5` y `27` respectivamente, dando un total de `32`.

Este método permite realizar consultas de suma de rango de manera eficiente, utilizando la estructura del árbol para dividir y conquistar el problema, reduciendo significativamente el número de operaciones requeridas en comparación con una suma iterativa directa sobre el arreglo.

#### Actualizaciones:
Las actualizaciones se realizan modificando los valores de las hojas correspondientes y actualizando todos los nodos padres hasta la raíz para reflejar el cambio. Esto asegura que las consultas posteriores consideren la actualización.


Para ilustrar cómo se realizan las actualizaciones en un árbol de segmentos, tomaremos el mismo árbol de segmentos construido para el arreglo `[1, 3, 5, 7, 9, 11]` y mostraremos cómo se actualiza el valor del elemento en el índice 4 a 10. Esto implica cambiar el valor de `9` a `10` en el arreglo, y luego actualizar el árbol de segmentos para reflejar este cambio.

El árbol de segmentos original es el siguiente:

<pre>
                    [0, 5, 36]
                   /           \
          [0, 2, 9]             [3, 5, 27]
          /      \               /       \
    [0, 1, 4]   [2, 2, 5]   [3, 4, 16]   [5, 5, 11]
    /    \                      /    \
[0, 0, 1] [1, 1, 3]        [3, 3, 7] [4, 4, 9]

</pre>

La actualización del elemento en el índice 4 del arreglo a `10` afecta al nodo hoja `[4, 4, 9]`, cambiando su valor a `[4, 4, 10]`. A continuación, necesitamos actualizar los nodos padres para reflejar este cambio en el árbol.

El proceso de actualización se desglosa así:

1. **Actualizar el nodo hoja `[4, 4, 9]` a `[4, 4, 10]`**.
2. **Actualizar el nodo padre `[3, 4, 16]` a `[3, 4, 17]`**, sumando la diferencia de la actualización al valor existente.
3. **Actualizar el nodo padre `[3, 5, 27]` a `[3, 5, 28]`**, nuevamente sumando la diferencia.
4. **Finalmente, actualizar la raíz `[0, 5, 36]` a `[0, 5, 37]`**.

Aquí está el diagrama ASCII del árbol de segmentos después de la actualización:

<pre>
                    [0, 5, 37]
                   /           \
          [0, 2, 9]             [3, 5, 28]
          /      \               /       \
    [0, 1, 4]   [2, 2, 5]   [3, 4, 17]   [5, 5, 11]
    /    \                      /    \
[0, 0, 1] [1, 1, 3]        [3, 3, 7] [4, 4, 10]
                                          \
                                       Actualizado
                                       
</pre>

Para realizar la actualización en el árbol de segmentos:

1. Localizamos el nodo hoja correspondiente al índice que estamos actualizando.
2. Cambiamos el valor en el nodo hoja.
3. Recorremos el camino de regreso a la raíz, actualizando el valor de cada nodo padre para reflejar el cambio en el nodo hoja.

Este método asegura que todas las consultas posteriores al árbol de segmentos reflejen correctamente el arreglo actualizado, manteniendo la eficiencia de las operaciones de consulta de rango.

### Ejercicios:
1. **Construir un Árbol de Segmentos**: Dado un arreglo `[1, 3, 5, 7, 9, 11]`, construye un árbol de segmentos que permita consultas de suma de rango.
2. **Consulta de Suma de Rango**: Utilizando el árbol de segmentos construido, realiza una consulta para obtener la suma de los elementos en el rango de índices 2 a 5.
3. **Actualizar un Elemento**: Actualiza el valor del elemento en el índice 4 a 10 y muestra cómo se actualiza el árbol de segmentos.
4. **Consulta de Mínimo de Rango**: Modifica el árbol de segmentos para que soporte consultas de mínimo de rango. Realiza una consulta para encontrar el valor mínimo en el rango de índices 1 a 3.
5. **Optimización de Memoria**: Propone una estrategia para reducir el uso de memoria del árbol de segmentos sin comprometer la eficiencia de las operaciones.

### Conclusión:
Los árboles de segmentos son una herramienta poderosa para tratar con consultas y actualizaciones de rango en arreglos. Su capacidad para dividir el problema y manejarlo en segmentos hace que las operaciones sean eficientes, lo cual es crucial en aplicaciones que requieren respuestas rápidas a consultas dinámicas. En la próxima clase, exploraremos otras estructuras de datos avanzadas que permiten manejar diferentes tipos de consultas de manera eficiente.

---

### Soluciones:

#### Ejercicio 1: Construir un Árbol de Segmentos
```python
def construir_segment_tree(arr, inicio, fin, segment_tree, indice):
    if inicio == fin:
        segment_tree[indice] = arr[inicio]
        return arr[inicio]
    mid = (inicio + fin) // 2
    segment_tree[indice] = construir_segment_tree(arr, inicio, mid, segment_tree, 2 * indice + 1) + construir_segment_tree(arr, mid + 1, fin, segment_tree, 2 * indice + 2)
    return segment_tree[indice]

arr = [1, 3, 5, 7, 9, 11]
n = len(arr)
segment_tree = [0] * (4 * n)  # Tamaño suficiente para almacenar el árbol
construir_segment_tree(arr, 0, n-1, segment_tree, 0)
print(segment_tree)
```

#### Ejercicio 2: Consulta de Suma de Rango
```python
def suma_rango(segment_tree, rango_inicio, rango_fin, inicio, fin, indice):
    if rango_inicio <= inicio and rango_fin >= fin:
        return segment_tree[indice]
    if fin < rango_inicio or inicio > rango_fin:
        return 0
    mid = (inicio + fin) // 2
    return suma_rango(segment_tree, rango_inicio, rango_fin, inicio, mid, 2 * indice + 1) + suma_rango(segment_tree, rango_inicio, rango_fin, mid + 1, fin, 2 * indice + 2)

print(suma_rango(segment_tree, 2, 5, 0, n-1, 0))
```

#### Ejercicio 3: Actualizar un Elemento
```python
def actualizar_elemento(segment_tree, arr_index, nuevo_valor, inicio, fin, indice):
    if inicio == fin:
        segment_tree[indice] = nuevo_valor
    else:
        mid = (inicio + fin) // 2
        if inicio <= arr_index <= mid:
            actualizar_elemento(segment_tree, arr_index, nuevo_valor, inicio, mid, 2 * indice + 1)
        else:
            actualizar_elemento(segment_tree, arr_index, nuevo_valor, mid + 1, fin, 2 * indice + 2)
        segment_tree[indice] = segment_tree[2 * indice + 1] + segment_tree[2 * indice + 2]

actualizar_elemento(segment_tree, 4, 10, 0, n-1, 0)
print(segment_tree)
```

#### Ejercicio 4: Consulta de Mínimo de Rango
Para este ejercicio, se necesitaría modificar la función de construcción y consulta del árbol de segmentos para operar con el mínimo en lugar de la suma. Este ajuste implicaría cambiar la lógica de combinación de resultados en los nodos para seleccionar el mínimo de los hijos en lugar de sumarlos.

#### Ejercicio 5: Optimización de Memoria
Una estrategia para reducir el uso de memoria en un árbol de segmentos es utilizar una representación de árbol basada en un arreglo dinámico (como un `vector` en C++ o una lista en Python

) en lugar de nodos de objeto explícitos. Además, se puede implementar el árbol de segmentos como un árbol implícito sin almacenar explícitamente los nodos hoja NIL, reduciendo aún más el uso de memoria.