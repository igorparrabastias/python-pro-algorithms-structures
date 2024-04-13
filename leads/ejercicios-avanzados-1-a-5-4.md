## Ejercicio Avanzado 1: Diccionario de Contadores con Clases

**Objetivo:** Utilizar clases para crear un contador personalizado que maneje un diccionario interno para contar ocurrencias de objetos.

**Descripción:**
1. Define una clase `Contador` que inicialice un diccionario vacío.
2. Añade un método `agregar` que incremente en uno la cuenta de un objeto dado.
3. Añade un método `obtener_cuenta` que devuelva la cuenta actual de un objeto.

**Código de Ejemplo:**
```python
class Contador:
    def __init__(self):
        self.items = {}
    
    def agregar(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1
    
    def obtener_cuenta(self, item):
        return self.items.get(item, 0)

# Uso de la clase
contador = Contador()
contador.agregar('manzana')
contador.agregar('manzana')
print(contador.obtener_cuenta('manzana'))  # Debería imprimir 2
print(contador.obtener_cuenta('banana'))  # Debería imprimir 0
```

## Ejercicio Avanzado 2: Fusionar Listas en Diccionarios Anidados

**Objetivo:** Fusionar múltiples diccionarios que contienen listas como valores, combinando listas con la misma clave.

**Descripción:**
1. Dado una lista de diccionarios, fusiona estos diccionarios para que las listas de valores con la misma clave se combinen en una sola lista.

**Código de Ejemplo:**
```python
diccs = [{'a': [1, 2]}, {'b': [3, 4]}, {'a': [5]}]
resultado = {}
for dicc in diccs:
    for clave, valor in dicc.items():
        if clave in resultado:
            resultado[clave].extend(valor)
        else:
            resultado[clave] = valor.copy()
print(resultado)  # Debería imprimir {'a': [1, 2, 5], 'b': [3, 4]}
```

## Ejercicio Avanzado 3: Diccionario con Valores Predeterminados

**Objetivo:** Crear un diccionario que automáticamente asigna una lista vacía a nuevas claves accedidas.

**Descripción:**
1. Usa `collections.defaultdict` para crear un diccionario que no requiera chequear si una clave existe antes de agregar un elemento a la lista de esa clave.

**Código de Ejemplo:**
```python
from collections import defaultdict

dicc = defaultdict(list)
dicc['frutas'].append('manzana')
dicc['frutas'].append('banana')
print(dicc['frutas'])  # Debería imprimir ['manzana', 'banana']
```

## Ejercicio Avanzado 4: Serialización Personalizada de Diccionarios

**Objetivo:** Implementar una función que serialize un diccionario a JSON, excluyendo aquellos pares clave-valor donde el valor sea `None`.

**Descripción:**
1. Define una función que tome un diccionario y devuelva una versión serializada en JSON excluyendo pares con valores `None`.

**Código de Ejemplo:**
```python
import json

def serialize(dicc):
    return json.dumps({clave: valor for clave, valor in dicc.items() if valor is not None})

dicc = {'nombre': 'Juan', 'edad': None}
print(serialize(dicc))  # Debería imprimir '{"nombre": "Juan"}'
```

## Ejercicio Avanzado 5: Aplicar Funciones a Claves Específicas

**Objetivo:** Aplicar una función específica a valores de claves específicas en un diccionario.

**Descripción:**
1. Define un diccionario que mapea nombres de claves a funciones.
2. Aplica estas funciones a un diccionario de entrada, modificando los valores de las claves especificadas.

**Código de Ejemplo:**
```python
def incrementar(x):
    return x + 1

def capitalizar(texto):
    return texto.capitalize()



transformaciones = {'edad': incrementar, 'nombre': capitalizar}
persona = {'nombre': 'juan', 'edad': 29}

for clave, func in transformaciones.items():
    if clave in persona:
        persona[clave] = func(persona[clave])

print(persona)  # Debería imprimir {'nombre': 'Juan', 'edad': 30}
```