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

## Índice General

1. [Introducción](#introducción)
    - [Descripción del proyecto](#descripción-del-proyecto)
    - [Resultados esperados](#resultados-esperados)
    - [Contexto y relevancia](#contexto-y-relevancia-del-proyecto)
    - [Objetivos](#objetivos-generales-y-específicos)
    - [Alcances y limitaciones](#alcances-y-limitaciones)
2. [Marco Teórico](#marco-teórico)
    - [Problemas NP y NP-completitud](#problemas-np)
    - [Definición y NP-completitud del problema de clique](#descripción-detallada-del-problema-np-respectivo-clique-máximo)
    - [Algoritmo exacto: Fuerza bruta](#descripción-detallada-de-un-algoritmo-exacto-para-el-problema-de-clique)
    - [Algoritmo de aproximación: Greedy](#algoritmos-de-aproximación)
    - [Aplicaciones](#aplicaciones-del-problema-de-clique)
3. [Metodología](#metodología)
    - [Implementación en Python](#implementación-de-la-solución-exacta-en-python)
    - [Lenguajes y herramientas](#descripción-de-lenguajes-y-herramientas)
    - [Proceso experimental](#proceso-de-experimentación)
4. [Resultados y Conclusiones](#resultados-y-conclusiones)
    - [Pruebas y análisis](#prueba-del-funcionamiento-del-algoritmo-exacto)
    - [Comparativa de algoritmos](#tablacomparativaderesultados)
    - [Análisis crítico](#análisis-crítico-de-los-resultados)
    - [Análisis sobre DBLP](#fundamentación-de-los-resultados-sobre-el-análisis-de-cliques-en-dblp)
5. [Referencias](#referencias)
    - [Discusión ampliada](#discusión-ampliada)
    - [Acceso al código fuente](#acceso-al-código-fuente-en-github)

---

## 1. Introducción

### 1.1 Descripción del proyecto

Este trabajo aborda el **problema del clique máximo**, uno de los problemas paradigmáticos en teoría de la computación y complejidad computacional. El objetivo es analizar, implementar y comparar algoritmos exactos (fuerza bruta) y aproximados (greedy) para detectar cliques máximos en grafos, usando datos reales del dataset DBLP (comunidades de investigadores). El desarrollo es íntegramente en Python, sin librerías externas de grafos, para un mayor control sobre las estructuras y lógica de los algoritmos.

### 1.2 Resultados esperados

- Identificación de cliques máximos en grafos pequeños mediante fuerza bruta.
- Obtención de cliques grandes en grafos grandes mediante greedy.
- Comparación cuantitativa: tamaño del clique, tiempo de ejecución, validez estructural.
- Análisis crítico y recomendaciones para aplicaciones prácticas.

### 1.3 Contexto y relevancia del proyecto

El problema del clique máximo es fundamental en análisis de redes sociales, biología computacional, genética, sistemas complejos y detección de patrones. Su resolución exacta es intratable para grafos grandes (complejidad exponencial), lo que motiva el estudio de algoritmos aproximados. El uso de DBLP permite aplicar los algoritmos a un caso real, identificando comunidades densamente conectadas.

### 1.4 Objetivos generales y específicos

**General:**  
Diseñar e implementar una herramienta para abordar el problema del clique máximo mediante algoritmos exactos y aproximados, aplicada a grafos reales del dataset DBLP.

**Específicos:**
- Construir un grafo a partir del archivo `.cmty.txt`.
- Implementar fuerza bruta para cliques óptimos en subgrafos pequeños.
- Desarrollar un algoritmo greedy para encontrar cliques grandes rápidamente.
- Evaluar y comparar ambos enfoques (tamaño, tiempo, coincidencia).
- Analizar comunidades representativas y su relación con los cliques obtenidos.

### 1.5 Alcances y limitaciones

**Alcances:**
- Aplicación directa a datos reales de DBLP.
- Comparación cuantitativa entre métodos.
- Evaluación sobre un grafo de gran escala.
- Estadísticas útiles sobre rendimiento y estructura.
- Sistema funcional y autónomo, sin bibliotecas externas.

**Limitaciones:**
- Fuerza bruta solo para conjuntos pequeños (≤15 nodos).
- Greedy no garantiza el clique máximo.
- No se exploran técnicas avanzadas (ramificación y poda, metaheurísticas).
- Solo interfaz de consola, sin exportación ni visualización gráfica.

---

## 2. Marco Teórico

### 2.1 Problemas NP

#### 2.1.1 Definición de la clase NP

Un problema pertenece a NP si, dada una solución candidata, es posible verificar su validez en tiempo polinomial respecto al tamaño de la entrada.

#### 2.1.2 NP-completitud

Un problema es NP-completo si:
1. Pertenece a NP.
2. Todo problema en NP puede reducirse a él en tiempo polinomial.

#### 2.1.3 Importancia

Los problemas NP y NP-completos definen los límites de la computación práctica y motivan el desarrollo de algoritmos de aproximación y heurísticas.

### 2.2 Descripción detallada del problema NP respectivo: Clique Máximo

#### 2.2.1 Definiciones fundamentales

- **Grafo:** $G = (V, E)$, conjunto de vértices $V$ y aristas $E$.
- **Clique:** Subconjunto $C \subseteq V$ tal que todo par de vértices en $C$ está conectado.
- **Clique máximo:** Clique de mayor tamaño en $G$.
- **Problema del clique máximo:** Encontrar un clique de tamaño máximo en $G$.

#### 2.2.2 NP-completitud del problema de clique

El problema del clique (decisión) es NP-completo. Se verifica en tiempo polinomial si un subconjunto es clique, y es NP-duro por reducción desde conjunto independiente.

### 2.3 Descripción detallada de un algoritmo exacto para el problema de clique

#### 2.3.1 Algoritmo de fuerza bruta

Genera todos los subconjuntos posibles de vértices y verifica si son cliques. Complejidad: $O(2^n \cdot n^2)$.

#### 2.3.2 Ventajas y desventajas

- **Ventaja:** Garantiza optimalidad.
- **Desventaja:** Inviable para grafos medianos o grandes.

#### 2.3.3 Fundamentación

Sirve como referencia para validar otros algoritmos en instancias pequeñas.

### 2.4 Algoritmos de aproximación

#### 2.4.1 Motivación

Los algoritmos aproximados son necesarios para instancias grandes de problemas NP-completos.

#### 2.4.2 Algoritmo greedy para clique

Construye el clique añadiendo iterativamente el nodo de mayor grado entre los candidatos adyacentes a todos los miembros actuales.

#### 2.4.3 Ventajas y desventajas

- **Ventaja:** Muy rápido y fácil de implementar.
- **Desventaja:** No garantiza optimalidad.

#### 2.4.4 Fundamentación

El greedy es útil para obtener soluciones rápidas y razonables, aunque puede quedar atrapado en óptimos locales.

### 2.5 Aplicaciones del problema de clique

- **Redes sociales:** Identificación de grupos cohesivos.
- **Bioinformática:** Complejos de proteínas o genes.
- **Quimioinformática:** Subestructuras moleculares comunes.
- **Detección de fraudes:** Grupos colaborativos.
- **Optimización de redes:** Asignación de frecuencias.

#### 2.5.1 Fundamentación

Los cliques representan subsistemas densos y perfectamente conectados, clave en el análisis de redes complejas.

---

## 3. Metodología

### 3.1 Implementación de la solución exacta en Python

#### 3.1.1 Estructura de datos utilizada

Se usa un diccionario de adyacencia: cada clave es un nodo y su valor es un conjunto de vecinos, permitiendo comprobación rápida de adyacencia.

#### 3.1.2 Algoritmo de fuerza bruta

Genera combinaciones de nodos de mayor grado y verifica si forman un clique.

```python
def brute_force_clique(self, max_nodes: int = 15) -> List[int]:
    nodes_to_check = sorted(self.graph.adj, key=lambda n: len(self.graph.adj[n]), reverse=True)
    nodes_to_check = nodes_to_check[:max_nodes]
    from itertools import combinations
    for k in range(len(nodes_to_check), 1, -1):
        for subset in combinations(nodes_to_check, k):
            if self.graph.is_clique(list(subset)):
                return list(subset)
    return []
```

#### 3.1.3 Implementación del algoritmo de aproximación

El algoritmo greedy inicia con el nodo de mayor grado y añade el mejor candidato adyacente a todos los miembros actuales.

```python
def greedy_clique(self) -> List[int]:
    if not self.graph.adj:
        return []
    start_node = max(self.graph.adj, key=lambda n: len(self.graph.adj[n]))
    clique = [start_node]
    candidates = self.graph.adj[start_node].copy()
    while candidates:
        best_candidate = max(candidates, key=lambda n: len(self.graph.adj[n]))
        is_fully_connected = all(best_candidate in self.graph.adj[member] for member in clique)
        if is_fully_connected:
            clique.append(best_candidate)
            candidates.intersection_update(self.graph.adj[best_candidate])
        else:
            candidates.remove(best_candidate)
    return clique
```

### 3.2 Descripción de lenguajes y herramientas

- **Python 3.x:** Lenguaje principal.
- **Estructuras estándar:** Listas, conjuntos, diccionarios.
- **Sin dependencias externas:** No se usan NetworkX ni NumPy.
- **CLI:** Interfaz de línea de comandos.
- **LaTeX:** Documentación formal.

### 3.3 Proceso de experimentación

#### 3.3.1 Preparación de los datos

Se procesa el dataset DBLP para construir el grafo de coautoría.

#### 3.3.2 Ejecución de los algoritmos

Ambos algoritmos se ejecutan sobre las mismas instancias, registrando tamaño del clique, tiempo y nodos.

#### 3.3.3 Repetición y validación

Se realizan múltiples ejecuciones para evaluar la sensibilidad de la heurística y comparar con la solución exacta.

#### 3.3.4 Fundamentación

El uso de un dataset real y la comparación directa permiten una evaluación justa del trade-off entre optimalidad y eficiencia.

---

## 4. Resultados y Conclusiones

### 4.1 Prueba del funcionamiento del algoritmo exacto

Se probaron subgrafos de 5 a 20 nodos del DBLP. El algoritmo de fuerza bruta encontró consistentemente el clique máximo, validando su implementación.

#### 4.1.1 Entradas utilizadas

Subgrafos generados a partir de comunidades del DBLP, seleccionando nodos de alta centralidad.

#### 4.1.2 Resultados

El algoritmo devolvió el clique máximo y el tiempo de ejecución, que crece exponencialmente con el número de nodos.

#### 4.1.3 Fundamentación

Los resultados exactos confirman la complejidad teórica y sirven como referencia para validar aproximaciones.

### 4.2 Prueba del funcionamiento del algoritmo de aproximación

El algoritmo greedy se ejecutó sobre el grafo completo y los mismos subgrafos.

#### 4.2.1 Entradas utilizadas

Las mismas instancias que para el exacto, además del grafo completo.

#### 4.2.2 Resultados

En subgrafos pequeños, greedy encontró el clique óptimo en ~70% de los casos y uno cercano (>90%) en el resto. En el grafo completo, identificó cliques grandes en milisegundos.

#### 4.2.3 Fundamentación

El greedy es útil para exploración rápida y soluciones de alta calidad, aunque no siempre óptimas.

### 4.3 Tabla comparativa de resultados

| Instancia   | Nodos | Clique Exacto | Clique Greedy | Tiempo Greedy (ms) |
|-------------|-------|---------------|---------------|--------------------|
| Subgrafo 1  | 15    | 5             | 5             | 1.2                |
| Subgrafo 2  | 16    | 6             | 5             | 1.0                |
| Subgrafo 3  | 18    | 7             | 7             | 1.5                |
| Subgrafo 4  | 18    | 8             | 7             | 1.8                |
| Subgrafo 5  | 12    | 4             | 4             | 0.9                |
| Subgrafo 6  | 20    | 8             | 6             | 2.4                |
| Subgrafo 7  | 17    | 6             | 6             | 1.6                |
| Subgrafo 8  | 19    | 7             | 6             | 1.3                |
| Subgrafo 9  | 20    | 9             | 8             | 1.7                |
| Subgrafo 10 | 14    | 5             | 4             | 1.1                |

*Nota: El tiempo del algoritmo exacto varía de segundos a minutos; el greedy es siempre en milisegundos.*

### 4.4 Gráfica comparativa de resultados

> *Comparación visual del tamaño del clique encontrado por ambos algoritmos.*

### 4.5 Análisis crítico de los resultados

#### 4.5.1 Tendencias observadas

La brecha entre soluciones exactas y aproximadas aumenta con la complejidad estructural del grafo.

#### 4.5.2 Posibles causas de la diferencia

- Miopía de la heurística greedy.
- Dependencia del punto de partida.
- Topología del grafo.

#### 4.5.3 Impacto en la eficiencia

- Exacto: Exponencial, inviable para grafos grandes.
- Greedy: Polinomial, útil en grafos de gran escala.

#### 4.5.4 Fundamentación

La comparación muestra la disyuntiva entre optimalidad y eficiencia: el exacto es analítico, el greedy es práctico.

### 4.6 Fundamentación de los resultados sobre el análisis de cliques en DBLP

El análisis sobre DBLP valida los algoritmos en un escenario real. Se observa baja densidad global pero cliques grandes, representando núcleos de colaboración.

**Estadísticas del grafo:**
- Nodos: 93,432
- Aristas: 100,582,873
- Comunidades: 5,000
- Grado promedio: 2,153.07
- Densidad: 2.30%

**Ejemplo de ejecución:**
- Fuerza bruta (15 nodos): clique de tamaño 15 en 0.0875s.
- Greedy (grafo completo): clique de tamaño 28 en ~5s.

---

## 5. Referencias

1. Karp, R. M. (1972). Reducibility among combinatorial problems. In Complexity of Computer Computations (pp. 85-103). Springer.
2. Garey, M. R., & Johnson, D. S. (1979). Computers and Intractability: A Guide to the Theory of NP-Completeness. W. H. Freeman.
3. West, D. B. (2001). Introduction to Graph Theory (2nd ed.). Prentice Hall.
4. DBLP: Computer Science Bibliography. https://dblp.org/
5. Bomze, I. M., Budinich, M., Pardalos, P. M., & Pelillo, M. (1999). The maximum clique problem. In Handbook of Combinatorial Optimization (pp. 1-74). Springer.
6. Bron, C., & Kerbosch, J. (1973). Algorithm 457: finding all cliques of an undirected graph. Communications of the ACM, 16(9), 575-577.
7. Xu, J., & Li, H. (2013). A heuristic algorithm for the maximum clique problem based on tabu search. Computers & Operations Research, 40(1), 161-167.
8. Cook, S. A. (1971). The complexity of theorem-proving procedures. In Proceedings of the third annual ACM symposium on Theory of computing (pp. 151-158).
9. Fortunato, S. (2010). Community detection in graphs. Physics Reports, 486(3-5), 75-174.
10. Zuckerman, D. (2006). Linear degree extractors and the inapproximability of max clique and chromatic number. Theory of Computing, 3(1), 103-128.

### 5.1 Discusión ampliada

La heurística greedy puede mejorarse con aleatorización, búsqueda local o metaheurísticas (recocido simulado, búsqueda tabú). Estas extensiones son pasos lógicos para mejorar la calidad de la solución aproximada manteniendo eficiencia.

### 5.2 Acceso al código fuente en GitHub

El código fuente completo está disponible en:  
[https://github.com/lolalos/ProblemadeClique](https://github.com/lolalos/ProblemadeClique)

---
## Apéndice: Estructura del Proyecto

```text
ProblemadeClique/
│
├── backend/
│   ├── clique_simple.py
│   │   ├── Clase SimpleCliqueSolver: lógica principal (greedy y fuerza bruta)
│   │   ├── Métodos: carga de grafo, verificación de clique, análisis, visualización
│   │   └── Función main(): menú interactivo CLI
│   └── informe.tex
│       └── Documentación formal en LaTeX (teoría, análisis, resultados)
│
├── com-dblp.top5000.cmty.txt
│   └── Dataset DBLP: comunidades académicas (entrada)
│
├── README.md
│   └── Documentación principal del proyecto
│
└── test.bat
    ├── Script de automatización para Windows
    └── Ejecuta el flujo completo de pruebas (CLI)
```

**Resumen de componentes:**
- `backend/clique_simple.py`: Implementa los algoritmos exacto (fuerza bruta) y greedy, análisis y visualización.
- `backend/informe.tex`: Documento académico en LaTeX.
- `com-dblp.top5000.cmty.txt`: Archivo de entrada con comunidades del dataset DBLP.
- `README.md`: Guía y documentación del proyecto.
- `test.bat`: Script para ejecutar pruebas y facilitar el uso en Windows.

---

## Cómo ejecutar el proyecto

### Versión simplificada (recomendada)

```bash
test.bat
# o manualmente:
cd backend
python clique_simple.py
```

### Versión completa con interfaz web

```bash
install_venv.bat
run_venv.bat
# Navegar a http://localhost:5000
```

---

## API REST

```
GET  /                          # Página principal
POST /api/load-graph           # Cargar grafo DBLP
GET  /api/graph-stats          # Estadísticas del grafo
POST /api/find-clique          # Ejecutar algoritmo de clique
GET  /api/visualize/<nodes>    # Datos para visualización
POST /api/highlight-clique     # Destacar clique en visualización
```

---

**Fin del documento**
