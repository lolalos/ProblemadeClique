# UNIVERSIDAD NACIONAL DE SAN ANTONIO ABAD DEL CUSCO  
**ESCUELA PROFESIONAL DE INGENIERÍA INFORMÁTICA Y DE SISTEMAS**  

## PROBLEMA DE CLIQUE  
**TEORÍA DE LA COMPUTACIÓN**  

**Docente:**  
HECTOR EDUARDO UGARTE ROJAS  

**Estudiantes:**  
- CONDORI HUILLCA LIDER  
- MOREANO VILLENA MIGUEL ANGEL  
- VITORINO MARIN EFRAIN  

**Semestre:** 2025-I  
**Cusco, Perú**  
**7 Julio de 2025**

---

## Versión Simplificada del Solver de Cliques

Este proyecto implementa una **versión simplificada y eficiente** para el análisis de cliques máximos en el dataset DBLP, **sin dependencias externas** (excepto `matplotlib` para visualización opcional). El enfoque es completamente en consola, permitiendo cargar el grafo, analizar comunidades, ejecutar algoritmos exacto (fuerza bruta) y aproximado (greedy), y comparar resultados de manera interactiva.

---

## Índice

1. [Descripción General](#descripción-general)
2. [Estructura y Carga del Grafo](#estructura-y-carga-del-grafo)
3. [Algoritmos Implementados](#algoritmos-implementados)
    - [Greedy](#algoritmo-greedy)
    - [Fuerza Bruta](#algoritmo-fuerza-bruta)
4. [Análisis y Estadísticas](#análisis-y-estadísticas)
5. [Interfaz de Usuario y Ejecución](#interfaz-de-usuario-y-ejecución)
6. [Visualización de Resultados](#visualización-de-resultados)
7. [Referencias](#referencias)
8. [Estructura del Proyecto](#estructura-del-proyecto)
9. [Cómo Ejecutar el Proyecto](#cómo-ejecutar-el-proyecto)

---

## Descripción General

La herramienta permite:

- **Cargar el dataset DBLP** (`com-dblp.top5000.cmty.txt`) y construir el grafo de coautoría.
- **Analizar comunidades**: tamaño, distribución y comunidad más grande.
- **Ejecutar algoritmos**:
    - **Greedy**: rápido, encuentra cliques grandes en grafos grandes.
    - **Fuerza bruta**: exacto, limitado a subgrafos pequeños (≤15 nodos).
- **Comparar resultados** y graficar el desempeño de ambos algoritmos.
- **Interfaz de consola** interactiva y amigable.

---

## Estructura y Carga del Grafo

- El grafo se representa mediante un **diccionario de adyacencia** (`defaultdict(set)`).
- Cada línea del archivo de entrada representa una comunidad; todos los nodos de una comunidad se conectan entre sí.
- Se almacenan nodos, aristas y comunidades para análisis posterior.

**Carga del grafo:**
```python
solver = SimpleCliqueSolver()
solver.load_from_file("com-dblp.top5000.cmty.txt")
```
Muestra estadísticas: nodos, aristas, comunidades, grado promedio, densidad, etc.

---

## Algoritmos Implementados

### Algoritmo Greedy

- Selecciona iterativamente el nodo con más conexiones entre los candidatos restantes.
- Construye el clique añadiendo nodos compatibles.
- Muy eficiente para grafos grandes.

```python
clique, exec_time = solver.greedy_clique()
```

### Algoritmo Fuerza Bruta

- Prueba todos los subconjuntos de los nodos de mayor grado (limitado a 15 nodos).
- Garantiza encontrar el clique máximo en el subconjunto.
- Solo recomendable para subgrafos pequeños.

```python
clique, exec_time = solver.brute_force_clique()
```

---

## Análisis y Estadísticas

- **Estadísticas generales**: número de nodos, aristas, comunidades, grado promedio, densidad.
- **Análisis de comunidades**: tamaño promedio, máximo, mínimo, distribución de tamaños.
- **Resultados detallados**: tamaño del clique, tiempo de ejecución, validez, comparación con la comunidad más grande.

---

## Interfaz de Usuario y Ejecución

El programa ofrece un **menú interactivo** en consola:

1. Ejecutar algoritmo Greedy (rápido)
2. Ejecutar algoritmo Fuerza Bruta (lento, máx. 15 nodos)
3. Mostrar estadísticas nuevamente
4. Análisis de comunidades
5. Graficar comparación de resultados
6. Salir

**Ejemplo de uso:**
```bash
python backend/clique_simple.py
```
Sigue las instrucciones en pantalla para analizar el grafo y comparar algoritmos.

---

## Visualización de Resultados

- Se puede graficar la comparación de tamaño de clique y tiempo de ejecución entre algoritmos usando `matplotlib`.
- La gráfica muestra barras para el tamaño del clique y línea para el tiempo (ms).

---

## Referencias

1. Karp, R. M. (1972). Reducibility among combinatorial problems. In Complexity of Computer Computations (pp. 85-103). Springer.
2. Garey, M. R., & Johnson, D. S. (1979). Computers and Intractability: A Guide to the Theory of NP-Completeness. W. H. Freeman.
3. West, D. B. (2001). Introduction to Graph Theory (2nd ed.). Prentice Hall.
4. DBLP: Computer Science Bibliography. https://dblp.org/
5. Bron, C., & Kerbosch, J. (1973). Algorithm 457: finding all cliques of an undirected graph. Communications of the ACM, 16(9), 575-577.

---

## Estructura del Proyecto

```text
ProblemadeClique/
│
├── backend/
│   └── clique_simple.py      # Implementación principal (greedy y fuerza bruta)
│
├── com-dblp.top5000.cmty.txt # Dataset DBLP (entrada)
│
├── README.md                 # Documentación principal
│
└── test.bat                  # Script de automatización para Windows
```

---

## Cómo Ejecutar el Proyecto

1. **Automático (Windows):**
    ```bash
    test.bat
    ```
2. **Manual:**
    ```bash
    cd backend
    python clique_simple.py
    ```

---

**Fin del documento**
