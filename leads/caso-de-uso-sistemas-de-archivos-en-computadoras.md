# Caso de Uso: Sistemas de Archivos en Computadoras

### Introducción:
Los sistemas de archivos son una parte esencial de los sistemas operativos, gestionando cómo se almacenan y recuperan los datos en los dispositivos de almacenamiento. Un sistema de archivos organiza estos datos en una estructura jerárquica, donde directorios y archivos se representan de manera que faciliten su acceso y gestión. Los árboles N-arios, donde cada nodo puede tener cualquier número de hijos, son ideales para modelar esta estructura jerárquica.

### Estructuras de Datos Nativas de Python:
Para representar un sistema de archivos usando árboles N-arios en Python, se puede emplear una clase que represente tanto los directorios (nodos) como los archivos (nodos hoja). Cada nodo en el árbol podría tener propiedades como nombre, tipo (directorio o archivo), y una lista de nodos hijos (para directorios).

```python
class FileSystemNode:
    def __init__(self, name, type="directory"):
        self.name = name
        self.type = type  # "directory" o "file"
        self.children = []  # Lista de FileSystemNode

    def add_child(self, child):
        self.children.append(child)
```

### Implementación de Árboles Simples:
Para construir un sistema de archivos, se crearían instancias de `FileSystemNode`, una para el directorio raíz y más para subdirectorios y archivos, reflejando la estructura jerárquica del sistema de archivos real.

```python
# Crear sistema de archivos
root = FileSystemNode("root")
documents = FileSystemNode("documents")
root.add_child(documents)
documents.add_child(FileSystemNode("resume.docx", "file"))
```

### Conclusión:
Los árboles N-arios son fundamentales en la implementación de sistemas de archivos debido a su capacidad para representar eficientemente estructuras jerárquicas complejas. Al utilizar árboles N-arios, los sistemas operativos pueden gestionar de manera eficaz y eficiente el almacenamiento, la recuperación y la organización de archivos y directorios, permitiendo operaciones como la creación, búsqueda, y eliminación de archivos y directorios de manera intuitiva y acorde con la estructura jerárquica del sistema de archivos.

### Ejercicios:
1. **Implementar Función de Búsqueda**: Escribe una función que, dado un nombre de archivo, busque en el sistema de archivos y devuelva la ruta completa si el archivo existe.
2. **Listar Directorio**: Implementa una función que liste todos los archivos y subdirectorios dentro de un directorio dado.

### Soluciones:
1. **Búsqueda de Archivo**:
```python
def buscar_archivo(nodo, nombre_archivo, ruta=""):
    if nodo.type == "file" and nodo.name == nombre_archivo:
        return ruta + "/" + nodo.name
    for child in nodo.children:
        resultado = buscar_archivo(child, nombre_archivo, ruta + "/" + nodo.name)
        if resultado:
            return resultado
    return None
```

2. **Listar Directorio**:
```python
def listar_directorio(nodo):
    for child in nodo.children:
        print("Tipo:", child.type, "- Nombre:", child.name)
        if child.type == "directory":
            listar_directorio(child)
```