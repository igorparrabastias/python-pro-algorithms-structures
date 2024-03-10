# Árboles Y Algoritmos de Operaciones

 Seguiremos un orden que asegura una progresión lógica, desde lo más fundamental a lo más avanzado, permitiendo a los estudiantes construir una base sólida antes de abordar estructuras más complejas.

## Fundamentales

- :bookmark_tabs: [Árboles](../notebook/arboles-y-algoritmos-de-operaciones/tipos-de-arboles.ipynb)
  - :page_with_curl: [Algoritmos Relacionados con Árboles](../notebook/arboles-y-algoritmos-de-operaciones/algoritmos-relacionados-con-arboles.ipynb)
  - :page_with_curl: [Introducción](/notebook/implementacion-de-arboles/introduccion.ipynb)
  - :page_with_curl: [Introducción algoritmos](/notebook/algoritmos-de-arboles/introduccion.ipynb)  

- :bookmark_tabs: [Árboles Binarios](../notebook/arboles/arbol-binario.ipynb) Concepto básico sobre árboles, introduce la idea de nodos y estructura jerárquica.
  - :page_with_curl: [Implementación básica](/notebook/implementacion-de-arboles/trees-metodos-basicos.ipynb)  
  - :page_with_curl: [Búsqueda y Eliminación](/notebook/implementacion-de-arboles/trees-busqueda-y-eliminacion.ipynb)  
  - :page_with_curl: [Altura: Determinar la altura del árbol](/notebook/implementacion-de-arboles/altura-determinar-la-altura-del-arbol.ipynb)  
  - :page_with_curl: [Nivel de un Nodo: Encontrar el nivel de un nodo dado en el árbol](/notebook/implementacion-de-arboles/nivel-de-un-nodo-encontrar-el-nivel-de-un-nodo-dado-en-el-arbol.ipynb)  
  - :page_with_curl: [Tamaño del Árbol: Contar el número total de nodos en el árbol](/notebook/implementacion-de-arboles/tamanno-del-arbol-contar-el-numero-total-de-nodos-en-el-arbol.ipynb)  

- :bookmark_tabs: [Árboles Binarios de Búsqueda (ABB)](../notebook/arboles/arbol-binario-de-busqueda-abb.ipynb)  Evolución del árbol binario, introduce la idea de ordenamiento y eficiencia en la búsqueda.
  - :page_with_curl: [Definición y recorridos (preorden, inorden, postorden)](/notebook/implementacion-de-arboles/arboles-binarios-definicion-y-recorridos-preorden-inorden-postorden.ipynb)  
  - :page_with_curl: [Recorridos en Árboles Binarios](/notebook/algoritmos-de-arboles/recorridos-en-arboles-binarios.ipynb)  
  - :page_with_curl: [Implementación de Árboles Binarios de Búsqueda (ABB)](/notebook/algoritmos-de-arboles-arboles-binarios-de-busqueda/implementacion-de-arboles-binarios-de-busqueda-abb.ipynb)  
  - :page_with_curl: [Árboles Binarios](/notebook/algoritmos-de-arboles/arboles-binarios.ipynb)  
  - :page_with_curl: [Verificación de Árbol Binario de Búsqueda: Comprobar si un árbol binario cumple las propiedades de un BST](/notebook/implementacion-de-arboles/verificacion-de-arbol-binario-de-busqueda-comprobar-si-un-arbol-binario-cumple-las-propiedades-de-un-bst.ipynb)  

- :bookmark_tabs: [Árbol AVL](../notebook/arboles/arbol-avl.ipynb)  Introduce los árboles balanceados y las operaciones de rotación para mantener el equilibrio.
  - :page_with_curl: [Balanceo de Árboles: Introducción a los Árboles AVL](/notebook/algoritmos-de-arboles-arboles-binarios-de-busqueda/balanceo-de-arboles-introduccion-a-los-arboles-av.ipynb)  
  - :page_with_curl: [Balanceo del Árbol: En árboles AVL, implementar rotaciones para mantener el árbol balanceado](/notebook/implementacion-de-arboles/balanceo-del-arbol-en-arboles-avl-implementar-rotaciones-para-mantener-el-arbol-balanceado.ipynb)  

- :bookmark_tabs: [Árbol Rojo-Negro](../notebook/arboles/arbol-rojo-negro.ipynb) : Otro tipo de árbol balanceado, introduce un mecanismo diferente para mantener el balance.
  - :page_with_curl: [Conceptos Básicos de Árboles Rojo-Negro](/notebook/algoritmos-de-arboles-arboles-especializados/conceptos-basicos-de-arboles-rojo-negro.ipynb)  
  - :page_with_curl: [Árboles Rojo-Negro](/notebook/implementacion-de-arboles/arboles-rojo-negro.ipynb)  

- :bookmark_tabs: [Árbol Splay](../notebook/arboles/arbol-splay.ipynb) Presenta una estrategia de autoajuste para optimizar las búsquedas secuenciales.

---

A continuación los árboles **B**, **B+** y **n-arios**, aún siendo estructuras de árbol fundamentales son más complejas y avanzadas, diseñadas para casos de uso específicos, especialmente en sistemas de bases de datos y sistemas de archivos, donde se manejan grandes volúmenes de datos. Estos árboles están optimizados para minimizar el acceso a disco y mejorar la eficiencia en la búsqueda, inserción y eliminación de datos en contextos donde el rendimiento es crítico. Los árboles binarios, en cambio, sí se consideran estructuras básicas y fundamentales en el estudio de estructuras de datos.

- :bookmark_tabs: [Árbol B](../notebook/arboles/arbol-b.ipynb) Es una estructura de datos de búsqueda balanceada, diseñada para almacenar información en sistemas de bases de datos y archivos, optimizando las operaciones de lectura y escritura en disco mediante la minimización de accesos. 
- :bookmark_tabs: [Árbol B+](../notebook/arboles/arbol-b+.ipynb) Es una variante del árbol B que mejora el acceso secuencial y la eficiencia en la búsqueda al almacenar todos los elementos en las hojas y mantener un enlace entre ellas, siendo ampliamente utilizado en bases de datos y sistemas de archivos.
- :bookmark_tabs: [Árbol n-ario](../notebook/arboles/arbol-n-ario.ipynb) Generalización de árboles con más de dos hijos, útil para entender la base de árboles B y B+. Esta característica los hace especialmente útiles para representar estructuras más complejas que los árboles binarios y son esenciales en varias aplicaciones como bases de datos y sistemas de archivos.
  - :page_with_curl: [Caso de uso: Sistemas de Gestión de Bases de Datos (SGBD)](/notebook/estructuras-de-datos-avanzadas/caso-de-uso-sistemas-de-gestion-de-bases-de-datos-sgbd.ipynb)  
  - :page_with_curl: [Caso de uso: Sistemas de archivos en computadoras](/notebook/estructuras-de-datos-avanzadas/caso-de-uso-sistemas-de-archivos-en-computadoras.ipynb)  - 


## Especializados

- :bookmark_tabs: [Árbol Trie](../notebook/arboles/arbol-trie.ipynb)  Especializado para manejo de cadenas, útil en búsquedas de texto.
  - :page_with_curl: [Caso de uso: Autocompletado](/notebook/estructuras-de-datos-avanzadas/caso-de-uso-autocompletado.ipynb)  
  - :page_with_curl: [Caso de uso: Encontrar palabras con un prefijo común](/notebook/estructuras-de-datos-avanzadas/encontrar-palabras-con-un-prefijo-comun.ipynb)  
  - :page_with_curl: [Caso de uso: Verificación Ortográfica](/notebook/estructuras-de-datos-avanzadas/caso-de-uso-verificacion-ortografica.ipynb)  
  - :page_with_curl: [Caso de uso: Sistemas de Enrutamiento](/notebook/estructuras-de-datos-avanzadas/caso-de-uso-sistemas-de-enrutamiento.ipynb)

Los árboles de **segmentos** y los árboles de **Fenwick**, también conocidos como Binary Indexed Trees (BIT), son estructuras de datos avanzadas que se utilizan ampliamente en el contexto de algoritmos y programación competitiva, especialmente para resolver eficientemente problemas que involucran consultas y actualizaciones de rangos en un arreglo de números. Permitiendo resolver problemas complejos dentro de límites de tiempo estrictos.

- :bookmark_tabs: [Árbol de Segmentos](../notebook/arboles/arbol-de-segmentos.ipynb)  Es una estructura de datos que permite realizar eficientemente consultas y actualizaciones de rangos, siendo esencial para operaciones como la suma o el mínimo en un segmento.
  - :page_with_curl: [Árboles de Segmentos](/notebook/implementacion-de-arboles/arboles-de-segmentos.ipynb) (merge)  
  - :page_with_curl: [Árboles de Segmentos: Ejercicios](/notebook/implementacion-de-arboles/arboles-de-segmentos-ejercicios.ipynb)  
  - :page_with_curl: [Caso de uso: Sistema de Contabilidad en Tiempo Real](/notebook/estructuras-de-datos-avanzadas/caso-de-uso-sistema-de-contabilidad-en-tiempo-real.ipynb)  

- :bookmark_tabs: [Árbol de Fenwick o Binary Indexed Tree (BIT)](../notebook/arboles/arbol-de-fenwick-o-binary-indexed-tree-bit.ipynb) Proporciona una forma compacta y eficiente de realizar sumas acumulativas y actualizaciones, ideal para escenarios donde estas operaciones se realizan frecuentemente.

A continuación, los árboles de **expresión** y **decisión** son estructuras fundamentales en el campo de la inteligencia artificial y el aprendizaje automático. Los árboles de expresión representan una forma de organizar y evaluar expresiones matemáticas de manera jerárquica, lo que los hace útiles en la optimización de operaciones aritméticas complejas. Por otro lado, los árboles de decisión son herramientas poderosas para la toma de decisiones basadas en condiciones lógicas, donde cada nodo representa una pregunta y cada rama una posible respuesta. Ambos tipos de árboles son ampliamente utilizados en una variedad de aplicaciones, desde la clasificación de datos hasta la optimización de algoritmos.

- :bookmark_tabs: [Árbol de Expresión](../notebook/arboles/arbol-de-expresion.ipynb) Introduce árboles en el contexto de expresiones matemáticas o lógicas.
- :bookmark_tabs: [Árbol de Decisión](../notebook/arboles/arbol-de-decision.ipynb) Aplica los conceptos de árboles en un contexto de aprendizaje automático o toma de decisiones.

## Avanzados

- :bookmark_tabs: [Árbol de Van Emde Boas](../notebook/arboles/arbol-de-van-emde-boas.ipynb)  Introduce conceptos avanzados para manejo de universos pequeños y operaciones muy eficientes.
- :bookmark_tabs: [Árbol de Merkle](../notebook/arboles/arbol-de-merkle.ipynb)  Aplicado en criptografía y sistemas distribuidos, muestra un uso especializado de los árboles.