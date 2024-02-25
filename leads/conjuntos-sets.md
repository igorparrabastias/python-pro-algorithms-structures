# Conjuntos (Sets)

### Introducción:

Los conjuntos en Python, conocidos como `set`, son colecciones desordenadas de elementos únicos. Son particularmente útiles para operaciones que requieren elementos únicos, y para realizar operaciones matemáticas de conjuntos como unión, intersección y diferencia.

### Fundamentos de los Conjuntos:

### Creación de Conjuntos:

Un conjunto se puede crear utilizando la función `set()` o mediante llaves `{}`.

```python
mi_conjunto = set([1, 2, 3])
otro_conjunto = {4, 5, 6}
```

Los conjuntos automáticamente eliminan los elementos duplicados.

```python
conjunto_con_duplicados = {1, 2, 2, 3}  # {1, 2, 3}
```

### Operaciones Básicas:

- **Añadir Elementos**: Utiliza `add()` para añadir un elemento al conjunto.
    
```python
mi_conjunto.add(4)
```
    
- **Eliminar Elementos**: Utiliza `remove()` o `discard()` para eliminar elementos.
    
```python
mi_conjunto.remove(4)  # Lanza un KeyError si el elemento no existe
mi_conjunto.discard(5) # No lanza un error si el elemento no existe
```
    
- **Verificar Pertenencia**: Utiliza `in` para verificar si un elemento está en el conjunto.

```python
3 in mi_conjunto  # True
```

### Operaciones Matemáticas de Conjuntos:

- **Unión**: Utiliza `|` o `union()` para combinar dos conjuntos.

```python
union_conjuntos = mi_conjunto | otro_conjunto
```

- **Intersección**: Utiliza `&` o `intersection()` para obtener elementos comunes.

```python
interseccion_conjuntos = mi_conjunto & otro_conjunto
```

- **Diferencia**: Utiliza `` o `difference()` para obtener elementos de un conjunto que no están en otro.

```python
diferencia_conjuntos = mi_conjunto - otro_conjunto
```

- **Diferencia Simétrica**: Usa `^` o `symmetric_difference()` para obtener elementos que están en uno de los conjuntos, pero no en ambos.

```python
diferencia_simetrica = mi_conjunto ^ otro_conjunto
```

### Casos Prácticos en los que los Conjuntos son Útiles:

1. **Eliminar Duplicados de una Lista**: Convierte una lista en un conjunto para eliminar elementos duplicados.
    
```python
lista = [1, 2, 2, 3, 3, 4]
sin_duplicados = list(set(lista))
```
    
2. **Búsqueda Rápida de Elementos**: Los conjuntos ofrecen una búsqueda más rápida que las listas para determinar si un elemento está presente.
3. **Operaciones de Conjuntos en Análisis de Datos**: Útiles para comparar grupos de datos, como encontrar elementos comunes o diferentes entre conjuntos de datos.
4. **Aplicaciones en Matemáticas y Lógica**: Ideal para aplicaciones que involucran teoría de conjuntos y lógica matemática.

### Conclusión:

Los conjuntos en Python son herramientas poderosas y eficientes para manejar colecciones de elementos únicos y realizar operaciones de conjuntos. Su capacidad para eliminar duplicados automáticamente y realizar operaciones matemáticas de conjuntos de manera eficiente los hace indispensables en ciertas aplicaciones, especialmente aquellas relacionadas con el análisis de datos y la teoría de conjuntos. En la próxima clase, exploraremos en profundidad casos de estudio y ejemplos prácticos que demuestren la utilidad de los conjuntos en escenarios de programación reales.

<aside>
🙋‍♂️ Los set pueden contener cualquier tipo de elemento?
No, los sets en Python no pueden contener elementos mutables como listas, diccionarios o incluso otros sets. Pueden contener tipos inmutables como números, cadenas y tuplas.
</aside>

# Creando un set con diferentes tipos de elementos inmutables
```

```python
mi_set = {42, "Hola", (1, 2, 3)}
print(mi_set)  # Funciona bien
```

```markdown
# Intentando agregar un elemento mutable como una lista
```python

try:
    mi_set.add([4, 5, 6])  # Esto generará un error
except TypeError as e:
    print(e)  # Muestra el error porque las listas no se pueden agregar a un set
```