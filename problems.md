# Subconjunto contiguo de suma más grande (algoritmo de Kadane)

Dada una matriz arr[] de tamaño N. La tarea es encontrar la suma de la submatriz contigua dentro de una arr[] con la suma más grande.

Para resolver el problema del subconjunto contiguo de suma más grande, también conocido como el problema de la subsecuencia contigua de suma máxima, se puede utilizar el algoritmo de Kadane. Este algoritmo es eficiente y permite encontrar la máxima suma de una subsecuencia contigua en un arreglo en tiempo lineal.

Aquí te dejo una explicación del algoritmo seguido de un ejemplo de código en Python bien comentado:

### Pseudocódigo
```
Inicio
    Definir max_hasta_ahora = -infinito
    Definir max_termina_aqui = 0

    Para cada elemento X en el arreglo:
        max_termina_aqui = max_termina_aqui + X
        Si max_hasta_ahora < max_termina_aqui:
            max_hasta_ahora = max_termina_aqui
        Si max_termina_aqui < 0:
            max_termina_aqui = 0
    Devolver max_hasta_ahora
Fin
```

### Explicación
- `max_hasta_ahora` guarda la máxima suma encontrada hasta el momento.
- `max_termina_aqui` guarda la suma de la subsecuencia contigua que termina en el índice actual.
- Se recorre el arreglo una sola vez, y en cada paso, se actualiza `max_termina_aqui` añadiendo el valor del elemento actual del arreglo.
- Si `max_termina_aqui` supera a `max_hasta_ahora`, entonces se actualiza `max_hasta_ahora` con el valor de `max_termina_aqui`.
- Si `max_termina_aqui` se vuelve negativo (lo que significa que no es beneficioso seguir sumando los elementos anteriores), se resetea a 0.

### Código en Python
```python
def maxSubArraySum(arr):
    # Inicialización de variables
    max_hasta_ahora = float('-inf')
    max_termina_aqui = 0

    # Recorrido del arreglo
    for x in arr:
        max_termina_aqui += x
        if max_hasta_ahora < max_termina_aqui:
            max_hasta_ahora = max_termina_aqui
        if max_termina_aqui < 0:
            max_termina_aqui = 0
    return max_hasta_ahora

# Ejemplo de uso
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print("La suma máxima de subsecuencia contigua es", maxSubArraySum(arr))
```

Este código retorna la suma del subconjunto contiguo más grande de `arr`. En el ejemplo dado, la salida sería `7`, ya que el subconjunto de suma máxima es `[4, -1, -2, 1, 5]`.

---

Para proporcionar una explicación visual que complemente la comprensión del algoritmo de Kadane, vamos a utilizar un diagrama ASCII. Este diagrama representará cómo evolucionan `max_termina_aqui` y `max_hasta_ahora` a medida que recorremos el arreglo.

Considera el siguiente arreglo como ejemplo:
```
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
```

A continuación, un diagrama ASCII que muestra la evolución de las sumas:

```
Índice    Elemento    max_termina_aqui    max_hasta_ahora    Visualización
0         -2          0                   -inf               |          
1         -3          0                   -inf               |          
2          4          4                    4                |****
3         -1          3                    4                |***
4         -2          1                    4                |*
5          1          2                    4                |**
6          5          7                    7                |*******
7         -3          4                    7                |****
```

### Visualización
- `|` marca el inicio de cada visualización.
- `*` representa la unidad de suma en `max_termina_aqui`.

Esta representación ayuda a visualizar cómo `max_termina_aqui` se ajusta con cada nuevo elemento del arreglo, incrementándose o reseteándose a 0 si la suma se vuelve negativa. Mientras tanto, `max_hasta_ahora` solo cambia cuando encontramos una nueva "bolsa de tesoros" que supera el récord anterior.

### Clave de comprensión:
- **Inicio con negativos**: Los primeros dos pasos muestran cómo, al empezar con números negativos, `max_termina_aqui` se resetea a 0 porque llevar esos "tesoros" no es beneficioso.
- **Encuentro con un positivo**: Al llegar al `4`, inmediatamente vemos un aumento significativo en nuestra "colección", lo que nos lleva a un nuevo máximo.
- **Fluctuaciones**: A medida que avanzamos, las fluctuaciones representan las decisiones de "recoger o dejar" valores basadas en su impacto en la suma total.
- **Pico máximo**: El pico cuando `max_termina_aqui` alcanza 7 es nuestro momento óptimo, mostrando la mejor secuencia para "invertir".

Este tipo de diagrama no solo es útil para entender cómo funciona el algoritmo de Kadane, sino también para enseñar conceptos básicos de optimización y toma de decisiones en tiempo real, aplicables en diversas áreas de la informática y la vida real.

---

Para complementar lo ya explicado y hacer más comprensible y memorable la solución del algoritmo de Kadane, vamos a agregar algunos comentarios nemotécnicos, didácticos, ideas y anécdotas:

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

Con estos comentarios adicionales, espero que la solución no solo sea más fácil de entender, sino también más memorable y aplicable en diferentes contextos. ¿Hay algo más en lo que te pueda ayudar?