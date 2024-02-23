# Estructuras de Datos Básicas

## Introducción:
En esta sección abordaremos los fundamentos de Python centrados en listas, tuplas, secuencias y el uso de la función `range()`. Estas estructuras de datos son esenciales para la manipulación de colecciones de valores en Python y son fundamentales para cualquier desarrollador que busque dominar el lenguaje.

### Listas:
Las listas en Python son estructuras de datos dinámicas que pueden contener elementos de diferentes tipos. Se definen entre corchetes `[]` y permiten almacenar, modificar y acceder a secuencias de datos de manera ordenada.

- **Definición y uso básico**:
  ```python
  mi_lista = [1, 2, 3, 'Python', True]
  print(mi_lista[3])  # Acceso al cuarto elemento: 'Python'
  ```

- **Operaciones comunes**:
  - Añadir elementos: `mi_lista.append('nuevo elemento')`
  - Eliminar elementos: `mi_lista.remove(2)`
  - Acceder por índice: `elemento = mi_lista[0]`

### Tuplas:
Las tuplas son similares a las listas, pero son inmutables. Esto significa que una vez definida, no se pueden modificar sus elementos. Las tuplas se definen entre paréntesis `()`.

- **Definición y uso básico**:
  ```python
  mi_tupla = (1, 2, 3, 'Python', True)
  print(mi_tupla[3])  # Acceso al cuarto elemento: 'Python'
  ```

- **Características**:
  - Inmutables: no se pueden añadir o eliminar elementos después de su creación.
  - Útiles para datos fijos o para devolver múltiples valores desde funciones.

### Secuencias:
En Python, las secuencias son una colección ordenada de elementos. Las listas y tuplas son ejemplos de secuencias, lo que significa que comparten operaciones comunes como indexación, slicing (rebanado), y la iteración con bucles `for`.

- **Operaciones comunes en secuencias**:
  - Slicing: `mi_lista[1:3]` devuelve una lista que contiene desde el segundo hasta el tercer elemento.
  - Iteración: `for elemento in mi_lista:` para recorrer cada elemento en la lista.

### Rango (`range()`):
La función `range()` genera una secuencia inmutable de números enteros, útil para iterar en bucles `for`.

- **Uso básico**:
  ```python
  for i in range(5):  # Genera números de 0 a 4
      print(i)
  ```

- **Características**:
  - Útil para generar secuencias numéricas.
  - Puede especificar el inicio, fin y el paso: `range(inicio, fin, paso)`.

## Conclusión:
Las listas, tuplas, secuencias y la función `range()` constituyen la base sobre la cual se construye la manipulación de datos en Python. Entender estas estructuras es esencial para avanzar en la programación con Python, permitiendo al desarrollador manejar de forma eficiente colecciones de datos.