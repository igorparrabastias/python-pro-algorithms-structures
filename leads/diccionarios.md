# Diccionarios en Python

## ¿Qué es un Diccionario?

Los diccionarios en Python son estructuras de datos que funcionan como mapas de clave-valor. Son colecciones desordenadas, lo que significa que no tienen un orden establecido ni están indexados. En Python, los diccionarios son mutables, lo que permite modificar los datos después de haber sido creados.

## Creación de Diccionarios

Para comenzar con diccionarios, veamos cómo podemos crearlos y qué sintaxis utilizar.

### Creando un Diccionario Vacío

```python
diccionario_vacio = {}
print(diccionario_vacio)
```

### Creando un Diccionario con Elementos Iniciales

```python
diccionario_con_datos = {'nombre': 'Ana', 'edad': 28, 'ciudad': 'Santiago'}
print(diccionario_con_datos)
```

## Acceso a los Elementos

Los elementos de los diccionarios se pueden acceder utilizando sus claves.

### Accediendo a un Elemento por su Clave

```python
nombre = diccionario_con_datos['nombre']
print("Nombre:", nombre)
```

### Utilizando el Método `get`

El método `get` es una forma segura de acceder a los elementos, ya que permite especificar un valor predeterminado si la clave no existe.

```python
profesion = diccionario_con_datos.get('profesion', 'No especificado')
print("Profesión:", profesion)
```

## Modificación de Elementos

Una vez que tienes un diccionario, puedes modificarlo agregando nuevos elementos o cambiando el valor de los existentes.

### Agregando un Nuevo Elemento

```python
diccionario_con_datos['profesion'] = 'Ingeniero'
print(diccionario_con_datos)
```

### Modificando un Elemento Existente

```python
diccionario_con_datos['edad'] = 29
print(diccionario_con_datos)
```

## Eliminación de Elementos

Podemos eliminar elementos de un diccionario utilizando diversas funciones.

### Eliminar un Elemento Específico

```python
del diccionario_con_datos['ciudad']
print(diccionario_con_datos)
```

### Utilizando el Método `pop`

El método `pop` elimina el elemento con la clave dada y devuelve el valor del elemento eliminado.

```python
edad = diccionario_con_datos.pop('edad')
print("Edad eliminada:", edad)
print(diccionario_con_datos)
```

## Métodos Útiles para Diccionarios

Python proporciona varios métodos útiles que facilitan la manipulación de diccionarios.

### Claves, Valores y Elementos

```python
# Claves
claves = diccionario_con_datos.keys()
print("Claves:", list(claves))

# Valores
valores = diccionario_con_datos.values()
print("Valores:", list(valores))

# Elementos (clave-valor)
elementos = diccionario_con_datos.items()
print("Elementos:", list(elementos))
```

### Limpiar un Diccionario

Para eliminar todos los elementos de un diccionario, utilizamos el método `clear`.

```python
diccionario_con_datos.clear()
print("Diccionario después de limpiar:", diccionario_con_datos)
```

## Conclusión

En este cuaderno hemos aprendido cómo trabajar con diccionarios en Python, incluyendo cómo crearlos, acceder a sus elementos, modificarlos y eliminarlos. Los diccionarios son herramientas poderosas y flexibles en Python, ideales para manejar datos de forma dinámica.