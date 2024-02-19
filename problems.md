# Subconjunto contiguo de suma más grande
```
Más conocido como: Largest Sum Contiguous Subarray
Algoritmo: Kadane’s Algorithm
Complejidad del tiempo: O(N)
Complejidad del espacio: O(1)
```

## Problema
Dada una matriz arr[] de tamaño N. La tarea es encontrar la suma de la submatriz contigua con la suma más grande.

## Ejemplo

```
Problema de la Subsecuencia Contigua de Suma Máxima

      +---+----+---+----+---+----+---+
      | 2 | -3 | 3 | -1 | 2 | -4 | 2 |
      +---+----+---+----+---+----+---+
        0   1    2    3   4    5   6

La subsecuencia que proporciona la suma máxima está indicada por corchetes y es la siguiente:

      +---+----+---+----+---+----+---+
      |   |    |[3]|[ -1]|[ 2]|    |   |
      +---+----+---+----+---+----+---+

El cálculo de la suma de esta subsecuencia es el siguiente:

3 + (-1) + 2 = 4

Por lo tanto, la Suma Máxima de una Subsecuencia Contigua es 4.
```

## Solución

Para resolver el problema del subconjunto contiguo de suma más grande, también conocido como el problema de la subsecuencia contigua de suma máxima, se puede utilizar el **algoritmo de Kadane**. Este algoritmo es eficiente y permite encontrar la máxima suma de una subsecuencia contigua en un arreglo en tiempo lineal.

Aquí te dejo una explicación del algoritmo seguido de un ejemplo de código en Python:

### Pseudocódigo
```
Inicio
    Si el arreglo está vacío:
        Devolver 0

    Definir max_hasta_ahora como el primer elemento del arreglo
    Definir max_termina_aqui como el primer elemento del arreglo

    Para cada elemento X en el arreglo empezando desde el segundo elemento:
        max_termina_aqui = max(X, max_termina_aqui + X)
        max_hasta_ahora = max(max_hasta_ahora, max_termina_aqui)

    Devolver max_hasta_ahora
Fin
```
### Implementación del Algoritmo de Kadane
```python
def maxSubArraySum(a):
    if not a:  # Si el arreglo está vacío
        return 0

    max_hasta_ahora = a[0]
    max_termina_aqui = a[0]
    
    for i in range(1, len(a)):
        max_termina_aqui = max(a[i], max_termina_aqui + a[i])
        max_hasta_ahora = max(max_hasta_ahora, max_termina_aqui)
        
    return max_hasta_ahora

# Ejemplo de uso
arr = [2, -3, 3, -1, 2, -4, 2]
print("La suma máxima de subsecuencia contigua es", maxSubArraySum(arr))
```

### Explicación Paso a Paso
- Inicio con el Primer Elemento: Tanto el pseudocódigo como la implementación de Python comienzan explícitamente con el primer elemento del arreglo para inicializar max_hasta_ahora y max_termina_aqui. Esto refleja un enfoque práctico para manejar arreglos que comienzan con valores negativos o positivos.

- Comparaciones Directas: La primera función `max` se utiliza para decidir si es mejor tomar el elemento actual por sí solo o agregarlo a la suma `max_termina_aqui` acumulada. Esta decisión se toma en cada paso del bucle.

- Actualización de Máximos: Continuamente actualizamos `max_hasta_ahora` con el máximo entre el valor actual de `max_hasta_ahora` y `max_termina_aqui`. Esto asegura que siempre tengamos la suma máxima encontrada hasta el momento.

## Tracing

Para complementar la explicación y hacer el concepto aún más claro, aquí tienes un diagrama ASCII que muestra la evolución de las sumas para el arreglo dado \([2, -3, 3, -1, 2, -4, 2]\), utilizando el algoritmo de Kadane. Este diagrama se presenta en forma de tabla para ilustrar cómo cambian `max_termina_aqui` y `max_hasta_ahora` a medida que avanzamos a través del arreglo.

| Índice | Elemento | max_termina_aqui | max_hasta_ahora |
|--------|----------|------------------|-----------------|
|   0    |    2     |        2         |        2        |
|   1    |   -3     |        2         |        2        |
|   2    |    3     |        3         |        3        |
|   3    |   -1     |        2         |        3        |
|   4    |    2     |        4         |        4        |
|   5    |   -4     |        0         |        4        |
|   6    |    2     |        2         |        4        |

### Explicación de la Tabla:
- **Índice**: La posición del elemento actual en el arreglo.
- **Elemento**: El valor del elemento en el arreglo en la posición actual.
- **max_termina_aqui**: La suma máxima de la subsecuencia contigua que termina en el elemento actual. Se calcula tomando el máximo entre el elemento actual y la suma de `max_termina_aqui` más el elemento actual. Si esta suma es menor que el elemento actual, se "reinicia" tomando el valor del elemento actual.
- **max_hasta_ahora**: La suma máxima encontrada en cualquier subsecuencia contigua hasta el momento. Se actualiza si `max_termina_aqui` es mayor que `max_hasta_ahora`.

Este diagrama ilustra cómo el algoritmo evalúa cada elemento del arreglo para determinar si contribuye a aumentar la suma de la subsecuencia contigua más grande encontrada hasta el momento, o si es más ventajoso "reiniciar" en el elemento actual debido a una suma negativa previa. La clave para entender este algoritmo es observar cómo se toman decisiones en cada paso para optimizar el resultado final, manteniendo la flexibilidad para adaptarse a los valores del arreglo.

## Complejidad

- `Complejidad del tiempo: O(N)`
  La complejidad del tiempo del algoritmo de Kadane es O(n), donde (n) es el número de elementos en el array de entrada. Esto se debe a que el algoritmo recorre el array una sola vez, calculando la suma máxima de subarrays contiguos en un paso lineal.

- `Complejidad del espacio: O(1)`
  En cuanto a la complejidad del espacio, el algoritmo de Kadane necesita un espacio constante O(1), ya que solo requiere un número fijo de variables para almacenar la suma máxima actual, la suma máxima final y posiblemente el inicio y el final de la subsecuencia.

En resumen, Kadane's es muy eficiente tanto en tiempo como en espacio, lo que lo hace ideal para problemas de suma de subarrays contiguos en la práctica.

### Nemotécnicos y Didácticos
- **Imagínate como un "recolector de tesoros"**: Al recorrer el arreglo, piensa en ti mismo como un explorador que recoge tesoros (valores positivos) y evita trampas (valores negativos). `max_termina_aqui` representa tu bolsa actual de tesoros, mientras que `max_hasta_ahora` es la mejor bolsa de tesoros que has logrado recoger en tu viaje.

- **El "reset" esencial**: La idea de resetear `max_termina_aqui` a 0 cuando se vuelve negativo es como tener la habilidad de "teletransportarte" fuera de una situación peligrosa (secuencia de números negativos) y empezar de nuevo desde una posición más favorable. Este "reset" asegura que solo conservamos la colección de tesoros que nos beneficia.

- **Visualización con "termómetros"**: Puedes visualizar `max_hasta_ahora` y `max_termina_aqui` como dos termómetros. `max_termina_aqui` sube o baja con cada elemento del arreglo, mientras que `max_hasta_ahora` solo registra la temperatura máxima alcanzada. Este enfoque ayuda a entender cómo seguimos la "temperatura" (suma de valores) más alta a lo largo del arreglo.

### Ideas
- **Aplicaciones en la vida real**: Imagina que estás invirtiendo en el mercado de valores, donde los números positivos representan ganancias y los negativos, pérdidas. Este algoritmo te ayudaría a identificar el período continuo en el que deberías haber invertido para maximizar tu retorno. Aquí, "comprar" al inicio de la subsecuencia máxima y "vender" al final.

- **Optimización de recursos**: En términos de optimización y gestión de recursos, el algoritmo de Kadane es un excelente ejemplo de cómo hacer más con menos. No necesitamos memorizar todo el arreglo ni recurrir a soluciones complejas; con un seguimiento sencillo y eficiente de los "picos" y "valles" en nuestros datos, podemos alcanzar una solución óptima.

### Anécdotas
- **Historia de Kadane**: Aunque el algoritmo lleva el nombre de Joseph Kadane, quien lo popularizó en la década de 1980, su concepto básico fue descrito por primera vez por Ulf Grenander de la Universidad de Brown en un seminario. Esto nos enseña cómo la colaboración y la comunicación en la comunidad científica pueden llevar a la evolución y mejora de las ideas.

- **Lección de humildad**: Este algoritmo también es un recordatorio de que, en la ciencia de la computación, las soluciones más poderosas a menudo provienen de ideas simples y elegantes. A veces, tendemos a complicar los problemas buscando soluciones sofisticadas cuando, de hecho, una aproximación más directa y sencilla podría ser suficiente.

