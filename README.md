# Problema de Clique
____________________________________________________
## Algoritmos Computacionales  
**Tarea 2**

El **problema de la clique** es un problema clásico de la teoría de la complejidad computacional, clasificado como NP-completo.

---

## Descripción del Problema

Dado un grafo no dirigido $G = (V, E)$ y un número natural $k$, determinar si $G$ posee un clique de tamaño $k$.

- **Clique:** Un conjunto $C$ de vértices tal que todo par de vértices en $C$ está conectado por una arista en $G$ (es decir, $C$ es un subgrafo completo).
- **Problema de decisión:** ¿Existe una clique de tamaño $k$ en el grafo?
- **Problema de optimización:** Encontrar una clique de tamaño máximo en el grafo.

Verificar si un conjunto de vértices forma una clique es trivial, lo que hace que el problema pertenezca a NP.

---

## ¿Qué es un clique?

El término "clique" proviene del inglés y se refiere a un grupo de personas con intereses comunes. En grafos, los vértices representan personas y las aristas, intereses compartidos. Un clique es un subconjunto de vértices donde todos están conectados entre sí.

---

## Ejemplo

Suponga el siguiente grafo $G$:

- Cliques de tamaño 3: $\{1,2,5\}$ y $\{1,4,5\}$
- Cliques de tamaño 2: $\{2,3\}$ y $\{3,4\}$

---

## Aplicaciones

- **Link Farm:** Grupos de sitios web que se enlazan entre sí para manipular la relevancia en motores de búsqueda.
- **Segmentación de imágenes y reconocimiento de patrones:** Identificación de regiones o patrones en imágenes mediante cliques máximas.
- **Cálculo de probabilidades condicionales:** En redes bayesianas, el agrupamiento en "árboles de cliques" facilita el cálculo eficiente.
- **Biología:** Análisis de redes de expresión génica y estructuras de proteínas mediante la identificación de cliques.

---

## Algoritmos para Resolver el Problema

### Fuerza Bruta

- Lista todos los subconjuntos de vértices y verifica si forman una clique.
- Complejidad exponencial: $O(n^k)$.

### Bron-Kerbosch

- Construye cliques a partir de vértices individuales y las expande recursivamente.
- Complejidad en el peor caso: $O(3^{n/3})$.
- Más eficiente que fuerza bruta.

---

## Reducción SAT

Para más detalles sobre la reducción del problema de clique a SAT, consulte el documento PDF adjunto.

---

## Bibliografía

- [Problema de Clique Máximo](#)
- [Clasificación de problemas](#)
- [Clique problem - Wikipedia](https://en.wikipedia.org/wiki/Clique_problem)
- [Problema de la clique - Wikipedia](https://es.wikipedia.org/wiki/Problema_de_la_clique)
- [Complejidad computacional](#)
- [Cliques and a bit of biology](#)

---

Publicado por Unknown a las 22:00
