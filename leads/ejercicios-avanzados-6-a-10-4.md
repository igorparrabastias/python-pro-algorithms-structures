## Ejercicio Avanzado 6: Diccionarios Como Matrices Dispersas

**Objetivo:** Usar diccionarios para simular una matriz dispersa donde la mayoría de los valores son cero o no existen.

**Descripción:**
1. Crea un diccionario para representar una matriz dispersa, donde las claves son tuplas que representan las coordenadas (i, j) y los valores son los elementos de la matriz.
2. Implementa una función para agregar un valor en una coordenada específica y otra para obtener un valor de una coordenada específica.

**Código de Ejemplo:**
```python
def agregar(matriz, i, j, valor):
    if valor != 0:
        matriz[(i, j)] = valor

def obtener(matriz, i, j):
    return matriz.get((i, j), 0)

matriz_dispersa = {}
agregar(matriz_dispersa, 1, 2, 5)
agregar(matriz_dispersa, 3, 1, 10)
print(obtener(matriz_dispersa, 1, 2))  # Debería imprimir 5
print(obtener(matriz_dispersa, 2, 2))  # Debería imprimir 0
```

## Ejercicio Avanzado 7: Construcción de un Índice Invertido

**Objetivo:** Crear un índice invertido a partir de documentos de texto para facilitar búsquedas rápidas.

**Descripción:**
1. Dado una lista de cadenas (documentos), crea un diccionario donde cada palabra clave apunta a un conjunto de números de documento en los que aparece esa palabra.

**Código de Ejemplo:**
```python
documentos = [
    "python y programación",
    "programación avanzada en python",
    "explorando estructuras de datos"
]

indice_invertido = {}
for i, doc in enumerate(documentos):
    palabras = set(doc.split())
    for palabra in palabras:
        if palabra not in indice_invertido:
            indice_invertido[palabra] = set()
        indice_invertido[palabra].add(i)

print(indice_invertido)
```

## Ejercicio Avanzado 8: Agregación de Datos de Diccionarios Anidados

**Objetivo:** Agregar datos numéricos contenidos en una lista de diccionarios anidados.

**Descripción:**
1. Dado una lista de diccionarios que contienen otros diccionarios con datos numéricos, calcula la suma total de un campo específico en todos los sub-diccionarios.

**Código de Ejemplo:**
```python
datos = [
    {'id': 1, 'atributos': {'a': 10, 'b': 20}},
    {'id': 2, 'atributos': {'a': 5, 'b': 15}},
    {'id': 3, 'atributos': {'a': 7, 'b': 17}}
]

total_a = sum(item['atributos']['a'] for item in datos)
print(total_a)  # Debería imprimir 22
```

## Ejercicio Avanzado 9: Diccionarios de Diccionarios

**Objetivo:** Trabajar con diccionarios de diccionarios para representar y manipular estructuras de datos complejas.

**Descripción:**
1. Crea un diccionario de usuarios, donde cada clave es un ID de usuario y cada valor es otro diccionario con información sobre el usuario (nombre, email, etc.).
2. Implementa una función para añadir un nuevo usuario y otra para modificar la información de un usuario existente.

**Código de Ejemplo:**
```python
usuarios = {
    1: {'nombre': 'Ana', 'email': 'ana@example.com'},
    2: {'nombre': 'Luis', 'email': 'luis@example.com'}
}

def añadir_usuario(usuarios, id, info):
    usuarios[id] = info

def modificar_usuario(usuarios, id, clave, valor):
    if id in usuarios:
        usuarios[id][clave] = valor

añadir_usuario(usuarios, 3, {'nombre': 'Carlos', 'email': 'carlos@example.com'})
modificar_usuario(usuarios, 1, 'email', 'nuevo_ana@example.com')
print(usuarios)
```

## Ejercicio Avanzado 10: Filtrado y Transformación de Diccionarios

**Objet

ivo:** Realizar operaciones complejas de filtrado y transformación sobre un diccionario grande para obtener datos específicos en un formato deseado.

**Descripción:**
1. Dado un diccionario grande con varios niveles de anidamiento, filtra y transforma este diccionario para obtener un resumen específico basado en ciertos criterios.

**Código de Ejemplo:**
```python
datos_grandes = {
    'categoria': {
        'subcat1': {'item1': 10, 'item2': 20},
        'subcat2': {'item3': 30, 'item4': 40},
        'subcat3': {'item5': 50, 'item6': 60}
    }
}

def resumen_datos(datos, categoria):
    resumen = {}
    if categoria in datos:
        for subcat, items in datos[categoria].items():
            for item, valor in items.items():
                resumen[item] = valor
    return resumen

print(resumen_datos(datos_grandes, 'categoria'))
```