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

> **Fragmento de código:**
```python
class SimpleCliqueSolver:
    """Implementa algoritmos de clique sin dependencias externas"""
    def __init__(self):
        self.adjacency_dict = defaultdict(set)
        self.nodes = set()
        self.edges = set()
        self.communities = []
```

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

> **Fragmento de código:**
```python
"""
Version simplificada del solver de cliques - Resultados en consola
Analisis completo del dataset DBLP sin dependencias externas
"""
import time
import itertools
from typing import List, Set, Dict, Tuple
from collections import defaultdict
import matplotlib.pyplot as plt
```

---

## Estructura y Carga del Grafo

- El grafo se representa mediante un **diccionario de adyacencia** (`defaultdict(set)`).
- Cada línea del archivo de entrada representa una comunidad; todos los nodos de una comunidad se conectan entre sí.
- Se almacenan nodos, aristas y comunidades para análisis posterior.

**Carga del grafo:**
```python
def load_from_file(self, filepath: str):
    """Cargar grafo desde archivo DBLP"""
    with open(filepath, 'r') as file:
        for line in file:
            if line.strip():
                community = list(map(int, line.strip().split()))
                self.communities.append(community)
                for node in community:
                    self.nodes.add(node)
                for i, node1 in enumerate(community):
                    for j, node2 in enumerate(community):
                        if i != j:
                            self.adjacency_dict[node1].add(node2)
                            self.edges.add((min(node1, node2), max(node1, node2)))
```

---

## Algoritmos Implementados

### Algoritmo Greedy

- Selecciona iterativamente el nodo con más conexiones entre los candidatos restantes.
- Construye el clique añadiendo nodos compatibles.
- Muy eficiente para grafos grandes.

```python
def greedy_clique(self) -> tuple[list[int], float]:
    """Algoritmo greedy para clique maximo"""
    clique = []
    remaining = self.nodes.copy()
    while remaining:
        best_vertex = max(remaining, key=lambda v: len(self.adjacency_dict[v] & remaining))
        clique.append(best_vertex)
        remaining &= self.adjacency_dict[best_vertex]
    return clique, execution_time
```

### Algoritmo Fuerza Bruta

- Prueba todos los subconjuntos de los nodos de mayor grado (limitado a 15 nodos).
- Garantiza encontrar el clique máximo en el subconjunto.
- Solo recomendable para subgrafos pequeños.

```python
def brute_force_clique(self, max_nodes: int = 15) -> tuple[list[int], float]:
    """Algoritmo de fuerza bruta (limitado)"""
    sorted_nodes = sorted(self.nodes, key=lambda n: len(self.adjacency_dict[n]), reverse=True)
    test_nodes = sorted_nodes[:max_nodes]
    for r in range(len(test_nodes), 0, -1):
        for subset in itertools.combinations(test_nodes, r):
            if self.is_clique(list(subset)):
                return list(subset), execution_time
```

---

## Análisis y Estadísticas

- **Estadísticas generales**: número de nodos, aristas, comunidades, grado promedio, densidad.
- **Análisis de comunidades**: tamaño promedio, máximo, mínimo, distribución de tamaños.
- **Resultados detallados**: tamaño del clique, tiempo de ejecución, validez, comparación con la comunidad más grande.

```python
def get_detailed_stats(self) -> dict:
    """Obtener estadisticas detalladas del grafo"""
    degrees = [len(self.adjacency_dict[node]) for node in self.nodes]
    return {
        'nodes': len(self.nodes),
        'edges': len(self.edges),
        'communities': len(self.communities),
        'avg_degree': sum(degrees) / len(degrees),
        'max_degree': max(degrees),
        'min_degree': min(degrees),
        'density': (sum(degrees) / len(degrees)) / (len(self.nodes) - 1) if len(self.nodes) > 1 else 0
    }
```

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

> **Fragmento de código del menú principal:**
```python
def main():
    solver = SimpleCliqueSolver()
    instance_file = "../com-dblp.top5000.cmty.txt"
    if not solver.load_from_file(instance_file):
        return
    while True:
        print("1. Ejecutar algoritmo Greedy (rapido)")
        print("2. Ejecutar algoritmo Fuerza Bruta (lento, max 15 nodos)")
        print("3. Mostrar estadisticas nuevamente")
        print("4. Analisis de comunidades")
        print("5. Graficar comparacion de resultados")
        print("6. Salir")
        choice = input("Selecciona una opcion (1-6): ").strip()
        # ... lógica de opciones ...
```

---

## Visualización de Resultados

- Se puede graficar la comparación de tamaño de clique y tiempo de ejecución entre algoritmos usando `matplotlib`.
- La gráfica muestra barras para el tamaño del clique y línea para el tiempo (ms).

```python
def plot_comparison(results):
    """Graficar comparacion de resultados"""
    algorithms = [r['algorithm'] for r in results]
    sizes = [r['size'] for r in results]
    times = [r['time_ms'] for r in results]
    fig, ax1 = plt.subplots(figsize=(8,5))
    ax1.bar(algorithms, sizes, color='tab:blue', alpha=0.7)
    ax2 = ax1.twinx()
    ax2.plot(algorithms, times, color='tab:red', marker='o')
    plt.title('Comparacion de algoritmos de clique')
    plt.tight_layout()
    plt.show()
```

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
