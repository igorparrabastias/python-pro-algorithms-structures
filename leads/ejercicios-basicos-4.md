# Ejercicios Básicos con Diccionarios en Python

## Ejercicio 1: Crear un Diccionario

Crea un diccionario llamado `persona` que contenga las siguientes claves y valores:
- `nombre`: tu nombre.
- `ciudad`: tu ciudad.
- `edad`: tu edad.

```python
persona = {
    'nombre': 'Tu Nombre',
    'ciudad': 'Tu Ciudad',
    'edad': Tu Edad
}
```

## Ejercicio 2: Acceder a Elementos

Accede al valor de la ciudad en el diccionario `persona` e imprímelo.

```python
print(persona['ciudad'])
```

## Ejercicio 3: Modificar Elementos

Modifica la edad en el diccionario `persona` sumándole 1.

```python
persona['edad'] += 1
print(persona['edad'])
```

## Ejercicio 4: Agregar Nuevos Elementos

Agrega una nueva clave `ocupacion` con el valor de tu ocupación al diccionario `persona`.

```python
persona['ocupacion'] = 'Tu Ocupación'
print(persona)
```

## Ejercicio 5: Eliminar Elementos

Elimina la clave `ciudad` del diccionario `persona` usando el método `pop`.

```python
persona.pop('ciudad', None)
print(persona)
```

## Ejercicio 6: Claves y Valores

Imprime todas las claves y todos los valores del diccionario `persona`.

```python
print("Claves:", persona.keys())
print("Valores:", persona.values())
```

## Ejercicio 7: Iterar en un Diccionario

Itera sobre el diccionario `persona`, imprimiendo todas las claves y sus respectivos valores.

```python
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

## Ejercicio 8: Diccionario de Cuadrados

Usa una comprensión de diccionarios para crear un diccionario donde las claves sean los números del 1 al 10 y los valores sean el cuadrado de las claves.

```python
cuadrados = {x: x ** 2 for x in range(1, 11)}
print(cuadrados)
```

## Ejercicio 9: Filtrar Diccionario

Crea un nuevo diccionario a partir del diccionario `cuadrados` que incluya solo los items donde el valor es mayor que 50.

```python
filtrados = {clave: valor for clave, valor in cuadrados.items() if valor > 50}
print(filtrados)
```

## Ejercicio 10: Combinar Diccionarios

Dado otro diccionario `adicional = {'hobby': 'fotografía', 'mascota': 'perro'}`, combina este diccionario con `persona` para expandir su información.

```python
persona.update(adicional)
print(persona)
```

## Ejercicio 11: Contar Ocurrencias

Dado una lista de palabras, crea un diccionario que cuente la cantidad de veces que cada palabra aparece en la lista.

```python
palabras = ['manzana', 'banana', 'cereza', 'manzana', 'durazno', 'cereza', 'manzana']
conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1
print(conteo)
```

## Ejercicio 12: Invertir un Diccionario

Crea un diccionario invertido donde las claves y los valores del diccionario original se intercambien.

```python
original = {'a': 1, 'b': 2, 'c': 3}
invertido = {valor: clave for clave, valor in original.items()}
print(invertido)
```

## Ejercicio 13: Sub-diccionarios

Dado un diccionario, crea sub-diccionarios basados en un conjunto específico de claves.

```python
dicc_total = {'nombre': 'Juan', 'edad': 25, 'ciudad': 'Santiago', 'profesion': 'Ingeniero'}
claves_sub = ['nombre', 'profesion']
sub_diccionario = {clave: dicc_total[clave] for clave in claves_sub}
print(sub_diccionario)
```

## Ejercicio 14: Diccionarios por Comprensión con Condicionales

Usa una comprensión de diccionarios para crear un diccionario con solo los items que tienen claves como números impares.

```python
dicc = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
dicc_impares = {clave: valor for clave, valor in dicc.items() if clave % 2 != 0}
print(dicc_impares)
```

## Ejercicio 15: Diccionario de Listas

Crea un diccionario donde cada clave es una letra y cada valor es una lista de palabras que comienzan con esa letra.

```python
palabras = ['apple', 'banana', 'cherry', 'apricot', 'blueberry']
dicc_por_letra = {}
for palabra in palabras:
    letra = palabra[0]
    if letra in dicc_por_letra:
        dicc_por_letra[letra].append(palabra)
    else:
        dicc_por_letra[letra] = [palabra]
print(dicc_por_letra)
```

## Ejercicio 16: Unión de Diccionarios con Prioridad

Dado dos diccionarios, une ambos pero da prioridad a los valores del segundo en caso de colisión de claves.

```python
dicc1 = {'a': 1, 'b': 2}
dicc2 = {'b': 3, 'c': 4}
union = {**dicc1, **dicc2}
print(union)
```

## Ejercicio 17: Diccionario de Frecuencias

Dado un texto, crea un diccionario que mapee cada palabra a su frecuencia de aparición en el texto.

```python
texto = "hola mundo hola todos"
palabras = texto.split()
frecuencias = {}
for palabra in palabras:
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
print(frecuencias)
```

## Ejercicio 18: Diccionario de Máximos

Crea un diccionario que contenga el valor máximo de cada lista asociada a cada clave.

```python
dicc_listas = {'a': [1, 2, 3], 'b': [7, 6, 5], 'c': [9, 8]}
maximos = {clave: max(valor) for clave, valor in dicc_listas.items()}
print(maximos)
```

## Ejercicio 19: Filtrar Diccionario por Valor

Crea un nuevo diccionario que contenga solo los items del diccionario original donde los valores sean mayores que 10.

```python
dicc_original = {'a': 5, 'b': 15, 'c': 20, 'd': 9}
filtrado = {clave: valor for clave, valor in dicc_original.items() if valor > 

10}
print(filtrado)
```

## Ejercicio 20: Mapeo Reverso

Dado un diccionario donde los valores son listas, crea un nuevo diccionario que asocie cada elemento de las listas a su clave original.

```python
dicc = {'a': [1, 2], 'b': [2, 3]}
mapeo_reverso = {}
for clave, lista in dicc.items():
    for elemento in lista:
        if elemento in mapeo_reverso:
            mapeo_reverso[elemento].append(clave)
        else:
            mapeo_reverso[elemento] = [clave]
print(mapeo_reverso)
```