# :file_folder: Árboles Y Algoritmos de Operaciones

Seguiremos un orden que asegura una progresión lógica, desde lo más **fundamental** a lo más **avanzado**, permitiendo construir una base sólida antes de abordar estructuras más complejas.  
- :file_folder: Repása esta página de principio a fin para tener una visión global sobre la **estructura de datos** de tipo **árbol**.
- :ledger: Después de eso sigue cada link en el primer nivel  en forma secuencial para aprender sobre cada tipo.   
- :page_with_curl: Y al final, una vez hayas revisado todos los tipos, avanza a los link anidados para profundizar más, teniendo ya muy claro el contexto general.

## Fundamentales

Entre ellos, los **árboles binarios** son aquellos en los que cada nodo tiene como máximo dos hijos, lo que facilita la implementación y manipulación de datos. Por otro lado, los **árboles de búsqueda binaria** son una variante especializada en la que cada nodo cumple con una regla de ordenamiento, permitiendo búsquedas eficientes y rápidas en conjuntos de datos ordenados. Estas estructuras son esenciales en la programación y la gestión de datos, siendo ampliamente utilizadas en aplicaciones como bases de datos, algoritmos de búsqueda y optimización.

- :ledger: [Arboles](../notebook/arboles/introduccion.ipynb) Introducción general a árboles. Terminología y consideraciones de implementación.
  - :page_with_curl: [Tipos de Árboles](../notebook/arboles/tipos-de-arboles.ipynb) Tipos principales y su categorización según su estructura y propósito.
  - :page_with_curl: [Algoritmos Relacionados con Árboles](../notebook/arboles/algoritmos-relacionados-con-arboles.ipynb)
  - :page_with_curl: [Ejemplo de Algoritmo en Sistemas de Recomendación](../notebook/arboles/ejemplo-de-algoritmo-en-sistemas-de-recomendacion.ipynb)
  - :page_with_curl: [Ejemplo de Algoritmo par Procesamiento del Lenguaje Natural](../notebook/arboles/ejemplo-de-algoritmo-par-procesamiento-del-lenguaje-natural.ipynb)
  - :page_with_curl: [Ejemplo de Algoritmo en Bioinformática](../notebook/arboles/ejemplo-de-algoritmo-en-bioinformatica.ipynb)
  - :page_with_curl: [Implementación Básica](/notebook/arboles/tree-elemental.ipynb)  
  - :page_with_curl: [Ejercicios](/notebook/arboles/ejercicios.ipynb)  

- :ledger: [Árboles Binarios](../notebook/arboles/arbol-binario.ipynb) Concepto básico y recorridos.
  - :page_with_curl: [Aplicaciones de Árboles Binarios](/notebook/arboles/aplicaciones-arboles-binarios.ipynb)
  - :page_with_curl: [Consideraciones al implementar un árbol binario](/notebook/arboles/consideraciones-al-implementar-un-arbol-binario.ipynb)
  - **Métodos Elementales**
    - :page_with_curl: [Inserción manual](/notebook/arboles/insercion-manual.ipynb)  
    - :page_with_curl: [Inserción automática](/notebook/arboles/insercion-automatica.ipynb)  
    - :page_with_curl: [Búsqueda recursiva](/notebook/arboles/busqueda-recursiva.ipynb)  
    - :page_with_curl: [Eliminación de nodos](/notebook/arboles/eliminacion-de-nodos.ipynb)  
  - **Métodos de Recorrido**
    - :page_with_curl: [preorder (DFS)](/notebook/arboles/implementacion-preorder.ipynb)
    - :page_with_curl: [inorder (DFS)](/notebook/arboles/implementacion-inorder.ipynb)
    - :page_with_curl: [postorder (DFS)](/notebook/arboles/implementacion-postorder.ipynb)
    - :page_with_curl: [level_order (BFS)](/notebook/arboles/implementacion-level_order.ipynb)
  - **Métodos de Utilidad**
    - :page_with_curl: [height](/notebook/arboles/implementacion-height.ipynb)
    - :page_with_curl: [size](/notebook/arboles/implementacion-size.ipynb)
    - :page_with_curl: [is_balanced](/notebook/arboles/implementacion-is_balanced.ipynb)
  - **Métodos Avanzados**
    - :page_with_curl: [mirror](/notebook/arboles/implementacion-mirror.ipynb)
    - :page_with_curl: [is_tree](/notebook/arboles/implementacion-is_tree.ipynb)
    - :page_with_curl: [convert_to_linked_list](/notebook/arboles/implementacion-convert_to_linked_list.ipynb)
    - :page_with_curl: [serialize_deserialize](/notebook/arboles/implementacion-serialize_deserialize.ipynb)

---

- :ledger: [Árboles Binarios de Búsqueda ( BST)](../notebook/arboles/arbol-binario-de-busqueda-bst.ipynb)  Evolución del árbol binario, introduce la idea de ordenamiento y eficiencia en la búsqueda.
  - :page_with_curl: [Consideraciones al implementar métodos para BST](/notebook/arboles/consideraciones-al-implementar-metodos-para-bst.ipynb)
  - **Métodos de Utilidad**
    - :page_with_curl: [get_successor](/notebook/arboles/implementacion-get_successor.ipynb)
    - :page_with_curl: [get_predecessor](/notebook/arboles/implementacion-get_predecessor.ipynb)
    - :page_with_curl: [lowest_common_ancestor](/notebook/arboles/implementacion-lowest_common_ancestor.ipynb)
  - **Métodos Avanzados**
    - :page_with_curl: [find_level](/notebook/arboles/implementacion-find_level.ipynb)
    - :page_with_curl: [is_subtree](/notebook/arboles/implementacion-is_subtree.ipynb)
    - :page_with_curl: [convert_bst_to_linked_list](/notebook/arboles/implementacion-convert_bst_to_linked_list.ipynb)
    - :page_with_curl: [bst_serialize_deserialize](/notebook/arboles/implementacion-bst_serialize_deserialize.ipynb)- 


  - :page_with_curl: [Definición y recorridos (preorden, inorden, postorden)](/notebook/implementacion-de-arboles/arboles-binarios-definicion-y-recorridos-preorden-inorden-postorden.ipynb)  
  - :page_with_curl: [Recorridos en Árboles Binarios](/notebook/algoritmos-de-arboles/recorridos-en-arboles-binarios.ipynb)  
  - :page_with_curl: [Implementación de Árboles Binarios de Búsqueda (ABB)](/notebook/algoritmos-de-arboles-arboles-binarios-de-busqueda/implementacion-de-arboles-binarios-de-busqueda-abb.ipynb)  
  - :page_with_curl: [Árboles Binarios](/notebook/algoritmos-de-arboles/arboles-binarios.ipynb)  
  - :page_with_curl: [Verificación de Árbol Binario de Búsqueda: Comprobar si un árbol binario cumple las propiedades de un BST](/notebook/implementacion-de-arboles/verificacion-de-arbol-binario-de-busqueda-comprobar-si-un-arbol-binario-cumple-las-propiedades-de-un-bst.ipynb)  

Los árboles **AVL**, **rojo-negro** y **splay** son variantes avanzadas de los **árboles binarios de búsqueda**, diseñadas para mejorar el rendimiento en operaciones de inserción, eliminación y búsqueda. Los **árboles AVL** mantienen un equilibrio óptimo, asegurando que la diferencia de altura entre subárboles no supere un valor específico, lo que garantiza tiempos de búsqueda consistentes. Los **árboles rojo-negro**, por otro lado, aplican reglas de coloración para mantener un equilibrio relajado, lo que los hace más eficientes en operaciones de inserción y eliminación. Mientras tanto, los **árboles splay** utilizan rotaciones y reorganizaciones dinámicas para llevar a los nodos más accesibles a la raíz, optimizando las operaciones de búsqueda. Estas estructuras son cruciales en aplicaciones donde se requiere un rendimiento óptimo en la gestión y manipulación de datos, como bases de datos, sistemas de archivos y algoritmos de búsqueda.

- :ledger: [Árbol AVL](../notebook/arboles/arbol-avl.ipynb)  Introduce los árboles balanceados y las operaciones de rotación para mantener el equilibrio.
  - :page_with_curl: [Balanceo de Árboles: Introducción a los Árboles AVL](/notebook/algoritmos-de-arboles-arboles-binarios-de-busqueda/balanceo-de-arboles-introduccion-a-los-arboles-av.ipynb)  
  - :page_with_curl: [Balanceo del Árbol: En árboles AVL, implementar rotaciones para mantener el árbol balanceado](/notebook/implementacion-de-arboles/balanceo-del-arbol-en-arboles-avl-implementar-rotaciones-para-mantener-el-arbol-balanceado.ipynb)  

- :ledger: [Árbol Rojo-Negro](../notebook/arboles/arbol-rojo-negro.ipynb) : Otro tipo de árbol balanceado, introduce un mecanismo diferente para mantener el balance.
  - :page_with_curl: [Conceptos Básicos de Árboles Rojo-Negro](/notebook/algoritmos-de-arboles-arboles-especializados/conceptos-basicos-de-arboles-rojo-negro.ipynb)  
  - :page_with_curl: [Árboles Rojo-Negro](/notebook/implementacion-de-arboles/arboles-rojo-negro.ipynb)  

- :ledger: [Árbol Splay](../notebook/arboles/arbol-splay.ipynb) Presenta una estrategia de autoajuste para optimizar las búsquedas secuenciales.

---

A continuación los árboles **B**, **B+** y **n-arios**, aún siendo estructuras de árbol fundamentales son más complejas y avanzadas, diseñadas para casos de uso específicos, especialmente en sistemas de bases de datos y sistemas de archivos, donde se manejan grandes volúmenes de datos. Estos árboles están optimizados para minimizar el acceso a disco y mejorar la eficiencia en la búsqueda, inserción y eliminación de datos en contextos donde el rendimiento es crítico.

- :ledger: [Árbol B](../notebook/arboles/arbol-b.ipynb) Es una estructura de datos de búsqueda balanceada, diseñada para almacenar información en sistemas de bases de datos y archivos, optimizando las operaciones de lectura y escritura en disco mediante la minimización de accesos. 
- :ledger: [Árbol B+](../notebook/arboles/arbol-b+.ipynb) Es una variante del árbol B que mejora el acceso secuencial y la eficiencia en la búsqueda al almacenar todos los elementos en las hojas y mantener un enlace entre ellas, siendo ampliamente utilizado en bases de datos y sistemas de archivos.
- :ledger: [Árbol n-ario](../notebook/arboles/arbol-n-ario.ipynb) Generalización de árboles con más de dos hijos. Esta característica los hace especialmente útiles para representar estructuras más complejas que los árboles binarios y son esenciales en varias aplicaciones como bases de datos y sistemas de archivos.
  - :page_with_curl: [Caso de uso: Sistemas de Gestión de Bases de Datos (SGBD)](/notebook/estructuras-de-datos-avanzadas/caso-de-uso-sistemas-de-gestion-de-bases-de-datos-sgbd.ipynb)  
  - :page_with_curl: [Caso de uso: Sistemas de archivos en computadoras](/notebook/estructuras-de-datos-avanzadas/caso-de-uso-sistemas-de-archivos-en-computadoras.ipynb)  - 


## Especializados

- :ledger: [Árbol Trie](../notebook/arboles/arbol-trie.ipynb)  Especializado para manejo de cadenas, útil en búsquedas de texto.
  - :page_with_curl: [Caso de uso: Autocompletado](/notebook/estructuras-de-datos-avanzadas/caso-de-uso-autocompletado.ipynb)  
  - :page_with_curl: [Caso de uso: Encontrar palabras con un prefijo común](/notebook/estructuras-de-datos-avanzadas/encontrar-palabras-con-un-prefijo-comun.ipynb)  
  - :page_with_curl: [Caso de uso: Verificación Ortográfica](/notebook/estructuras-de-datos-avanzadas/caso-de-uso-verificacion-ortografica.ipynb)  
  - :page_with_curl: [Caso de uso: Sistemas de Enrutamiento](/notebook/estructuras-de-datos-avanzadas/caso-de-uso-sistemas-de-enrutamiento.ipynb)

---

Los árboles de **segmentos** y los árboles de **Fenwick**, también conocidos como Binary Indexed Trees (**BIT**), son estructuras de datos avanzadas que se utilizan ampliamente en el contexto de algoritmos y programación competitiva, especialmente para resolver eficientemente problemas que involucran consultas y actualizaciones de rangos en un arreglo de números. Permitiendo resolver problemas complejos dentro de límites de tiempo estrictos.

- :ledger: [Árbol de Segmentos](../notebook/arboles/arbol-de-segmentos.ipynb)  Es una estructura de datos que permite realizar eficientemente consultas y actualizaciones de rangos, siendo esencial para operaciones como la suma o el mínimo en un segmento.
  - :page_with_curl: [Árboles de Segmentos](/notebook/implementacion-de-arboles/arboles-de-segmentos.ipynb) (merge)  
  - :page_with_curl: [Árboles de Segmentos: Ejercicios](/notebook/implementacion-de-arboles/arboles-de-segmentos-ejercicios.ipynb)  
  - :page_with_curl: [Caso de uso: Sistema de Contabilidad en Tiempo Real](/notebook/estructuras-de-datos-avanzadas/caso-de-uso-sistema-de-contabilidad-en-tiempo-real.ipynb)  

- :ledger: [Árbol de Fenwick o Binary Indexed Tree (BIT)](../notebook/arboles/arbol-de-fenwick-o-binary-indexed-tree-bit.ipynb) Proporciona una forma compacta y eficiente de realizar sumas acumulativas y actualizaciones, ideal para escenarios donde estas operaciones se realizan frecuentemente.

---

A continuación, los árboles de **expresión** y **decisión** son estructuras fundamentales en el campo de la inteligencia artificial y el aprendizaje automático. Los **árboles de expresión** representan una forma de organizar y evaluar expresiones matemáticas de manera jerárquica, lo que los hace útiles en la optimización de operaciones aritméticas complejas. Por otro lado, los **árboles de decisión** son herramientas poderosas para la toma de decisiones basadas en condiciones lógicas, donde cada nodo representa una pregunta y cada rama una posible respuesta. Ambos tipos de árboles son ampliamente utilizados en una variedad de aplicaciones, desde la clasificación de datos hasta la optimización de algoritmos.

- :ledger: [Árbol de Expresión](../notebook/arboles/arbol-de-expresion.ipynb) Introduce árboles en el contexto de expresiones matemáticas o lógicas.
- :ledger: [Árbol de Decisión](../notebook/arboles/arbol-de-decision.ipynb) Aplica los conceptos de árboles en un contexto de aprendizaje automático o toma de decisiones.

## Avanzados

- :ledger: [Árbol de Van Emde Boas](../notebook/arboles/arbol-de-van-emde-boas.ipynb)  Introduce conceptos avanzados para manejo de universos pequeños y operaciones muy eficientes.
- :ledger: [Árbol de Merkle](../notebook/arboles/arbol-de-merkle.ipynb)  Aplicado en criptografía y sistemas distribuidos, muestra un uso especializado de los árboles.