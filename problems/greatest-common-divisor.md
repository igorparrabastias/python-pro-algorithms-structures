# Máximo Común Divisor

> Más conocido como: Greatest Common Divisor (GCD)  
Algoritmo: Algoritmo de Euclides  
Complejidad del tiempo: O(log(min(a, b)))  
Complejidad del espacio: O(1)  

## Problema
El objetivo es encontrar el mayor número que divide a dos números enteros sin dejar residuo.

## Ejemplo
<pre>
Encuentra el Máximo Común Divisor de 48 y 18

    +----+----+
    | 48 | 18 |
    +----+----+

Aplicando el algoritmo de Euclides:

- Paso 1: 48 / 18 = 2, residuo = 12
- Paso 2: 18 / 12 = 1, residuo = 6
- Paso 3: 12 / 6 = 2, residuo = 0

El MCD es 6.
</pre>

## Solución
La solución utiliza el algoritmo de Euclides, que se basa en el principio de que el MCD de dos números también divide su diferencia.

### Pseudocódigo
<pre>
Inicio
   función gcd(a, b)
   mientras b ≠ 0
       temporal = b
       b = a mod b
       a = temporal
   fin mientras
   retornar a
Fin
</pre>

### Implementación
```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Ejemplo de uso
print("El MCD de 48 y 18 es", gcd(48, 18))
```

### Explicación Paso a Paso
- **Inicialización**: Comenzamos con dos números, `a` y `b`.
- **Iteración**: Repetimos el proceso de tomar el residuo de `a` dividido por `b`, y luego asignamos `a` a `b` y el residuo a `a`.
- **Conclusión**: El algoritmo termina cuando `b` se convierte en 0. El valor actual de `a` es el MCD.

### Tracing
| Paso | a   | b   | Residuo |
| ---- | --- | --- | ------- |
| 1    | 48  | 18  | 12      |
| 2    | 18  | 12  | 6       |
| 3    | 12  | 6   | 0       |

## Puntos clave
- El algoritmo de Euclides es eficiente y efectivo para encontrar el MCD de dos números.
- La complejidad temporal es logarítmica, lo que hace que este algoritmo sea muy rápido incluso para números grandes.

## Complejidad
- **Complejidad del tiempo:** O(log(min(a, b))) debido a que el algoritmo de Euclides reduce el problema de manera significativa en cada paso mediante la aplicación del residuo.
- **Complejidad del espacio:** O(1) ya que solo se necesitan un número limitado de variables temporales, independientemente del tamaño de la entrada.

## Nemotécnicos
- **"Divide y Vencerás"**: Puedes recordar el algoritmo de Euclides con la frase "divide y vencerás", ya que el proceso implica dividir repetidamente los números hasta encontrar el divisor común.

## Ideas
- **Extensión a múltiples números**: Este método se puede extender para encontrar el MCD de más de dos números, aplicándolo iterativamente entre el resultado de los dos primeros números y el siguiente número en la secuencia.

## Anécdotas
- **Historia del Algoritmo de Euclides**: Este algoritmo lleva el nombre de Euclides de Alejandría, el matemático griego que lo describió en su obra "Elementos" alrededor del 300 a.C. Es uno de los algoritmos más antiguos que se utilizan en la práctica hasta el día de hoy.

## Resúmen
El Máximo Común Divisor (MCD) de dos números se puede encontrar de manera eficiente utilizando el algoritmo de Euclides. Este método iterativo reduce el tamaño del problema en cada paso hasta que el divisor se convierte en 0, momento en el cual el otro número representa el MCD. Este algoritmo es notablemente eficiente tanto en términos de tiempo como de espacio, lo que lo hace adecuado para aplicaciones prácticas incluso con números muy grandes.

## Temas de estudio
- Explorar variantes del algoritmo de Euclides, como el algoritmo de Euclides extendido, que además de encontrar el MCD, también encuentra los coeficientes enteros que satisfacen la identidad de Bézout.
- Estudiar la aplicación del MCD en problemas de teoría de números, como simplificación de fracciones, determinación de la coprimalidad entre números, y en algoritmos de cifrado como RSA.