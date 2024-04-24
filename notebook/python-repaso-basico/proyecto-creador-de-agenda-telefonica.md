# Proyecto: **Creador de Agenda Telefónica**
- **Objetivo**: Construir una aplicación de consola en Python que permita a los usuarios agregar, eliminar, buscar y listar contactos almacenados en un diccionario.
- **Características**:
  - Uso de funciones para cada acción (agregar, eliminar, buscar, listar).
  - Implementación de excepciones para manejar errores como entradas inválidas o búsquedas de contactos que no existen.
  - Utilización de listas y diccionarios para almacenar la información de los contactos.
  - Aplicación de slicing en listas para visualizar partes de la agenda.
  - Uso del iterador "for" para iterar sobre estructuras de datos.
  - Creación de una función recursiva para menús o repetir acciones.

Para comenzar con el proyecto del **Creador de Agenda Telefónica**, primero definiremos un esqueleto básico de la aplicación en Python y luego integraremos las pruebas unitarias usando el módulo `unittest`.

### Esqueleto de la Aplicación

Vamos a estructurar la aplicación en un solo archivo para mantener la simplicidad, aunque en un proyecto real podrías querer modularizar el código en varios archivos.

**agenda_telefonica.py**

```python
class AgendaTelefonica:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
        else:
            raise ValueError("El contacto no existe")

    def buscar_contacto(self, nombre):
        try:
            return self.contactos[nombre]
        except KeyError:
            raise ValueError("El contacto no existe")

    def listar_contactos(self):
        return self.contactos


def main():
    agenda = AgendaTelefonica()
    # Aquí podrías incluir una interfaz de usuario de consola
    pass

if __name__ == "__main__":
    main()
```

### Pruebas Unitarias

Agregaremos pruebas unitarias utilizando `unittest`. Estas pruebas asegurarán que cada función de la clase `AgendaTelefonica` funcione como se espera.

**test_agenda_telefonica.py**

```python
import unittest
from agenda_telefonica import AgendaTelefonica

class TestAgendaTelefonica(unittest.TestCase):
    def setUp(self):
        self.agenda = AgendaTelefonica()
        self.agenda.agregar_contacto("Juan", "123456789")

    def test_agregar_contacto(self):
        self.agenda.agregar_contacto("Maria", "987654321")
        self.assertIn("Maria", self.agenda.contactos)
        self.assertEqual(self.agenda.contactos["Maria"], "987654321")

    def test_eliminar_contacto(self):
        self.agenda.eliminar_contacto("Juan")
        self.assertNotIn("Juan", self.agenda.contactos)

    def test_eliminar_contacto_no_existente(self):
        with self.assertRaises(ValueError):
            self.agenda.eliminar_contacto("No Existe")

    def test_buscar_contacto(self):
        telefono = self.agenda.buscar_contacto("Juan")
        self.assertEqual(telefono, "123456789")

    def test_buscar_contacto_no_existente(self):
        with self.assertRaises(ValueError):
            self.agenda.buscar_contacto("No Existe")

    def test_listar_contactos(self):
        contactos = self.agenda.listar_contactos()
        self.assertEqual(len(contactos), 1)
        self.assertIn("Juan", contactos)

if __name__ == '__main__':
    unittest.main()
```

### Uso de los Tests

Para ejecutar las pruebas unitarias, simplemente corre el script `test_agenda_telefonica.py`. Asegúrate de que ambos archivos (`agenda_telefonica.py` y `test_agenda_telefonica.py`) estén en el mismo directorio o maneja los imports adecuadamente si decides usar una estructura de directorio diferente.

Este esqueleto y las pruebas asociadas proporcionan una base sólida para comenzar el desarrollo del proyecto. Podemos expandir y ajustar las funcionalidades según sea necesario.