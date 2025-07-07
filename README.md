# Problema de Clique

## Algoritmos Computacionales  
**Tarea 2**

El **problema de la clique** es un problema clásico de la teoría de la complejidad computacional, clasificado como NP-completo.



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

## Implementación del Proyecto

### Estructura de Archivos

```
ProblemadeClique/
├── backend/                    # Código Python
│   ├── clique_simple.py       # ⭐ Versión simplificada (sin dependencias)
│   ├── main.py                # Servidor web completo (Flask)
│   ├── clique_solver.py       # Algoritmos avanzados
│   ├── graph_loader.py        # Procesador de datos
│   ├── visualizer.py          # Generador de visualizaciones
│   └── requirements.txt       # Dependencias para versión web
├── frontend/                   # Interfaz web (solo para versión completa)
│   ├── index.html             # Página principal
│   └── static/                # CSS/JavaScript
├── com-dblp.top5000.cmty.txt # Dataset DBLP (5000 comunidades)
├── test.bat                   # ⭐ Ejecutar versión simplificada
├── install_venv.bat           # Instalar versión completa
└── run_venv.bat              # Ejecutar versión completa
```

### Tecnologías Utilizadas

**Backend (Python):**
- **Flask**: Servidor web y API REST
- **NetworkX**: Procesamiento y análisis de grafos
- **NumPy**: Cálculos numéricos eficientes

**Frontend (Web):**
- **HTML5/CSS3/JavaScript**: Interfaz de usuario
- **Bootstrap 5**: Framework CSS responsivo
- **Vis.js**: Visualización interactiva de grafos
- **Chart.js**: Gráficos estadísticos

### Algoritmos Implementados

#### 1. **Algoritmo Greedy**
- **Complejidad**: O(n²)
- **Características**: Rápido, aproximación
- **Uso**: Grafos grandes, resultado rápido

#### 2. **Algoritmo Bron-Kerbosch**
- **Complejidad**: O(3^(n/3))
- **Características**: Exacto, encuentra todos los cliques maximales
- **Uso**: Solución óptima garantizada

#### 3. **Algoritmo Fuerza Bruta**
- **Complejidad**: O(2^n)
- **Características**: Exacto pero muy lento
- **Uso**: Solo para grafos muy pequeños (< 20 nodos)

### Cómo Ejecutar el Proyecto

#### **Opción 1: Versión Simplificada (Recomendada)**
```bash
# Ejecutar directamente sin instalaciones
test.bat

# O manualmente:
cd backend
python simple_solver.py
```

#### **Opción 2: Versión Completa con Interfaz Web**
```bash
# 1. Instalar con entorno virtual
install_venv.bat

# 2. Ejecutar aplicación web
run_venv.bat

# 3. Abrir navegador en: http://localhost:5000
```

#### **Opción 3: Instalación Tradicional**
```bash
# 1. Instalar dependencias
install.bat

# 2. Ejecutar servidor
run.bat
```

### Características de la Versión Simplificada

#### **🎯 Resultados en Consola:**
- **Análisis completo** del dataset DBLP
- **Interfaz interactiva** con menú de opciones
- **Estadísticas detalladas** del grafo
- **Múltiples algoritmos** (Greedy y Fuerza Bruta)
- **Análisis de comunidades** originales

#### **📊 Lo que Obtienes:**
- Clique máximo encontrado con detalles
- Tiempo de ejecución de cada algoritmo
- Estadísticas del grafo (nodos, aristas, densidad)
- Análisis de las comunidades de DBLP
- Validación de resultados

#### **🚀 Ventajas:**
- **Sin instalaciones** complejas
- **Funciona inmediatamente** con Python estándar
- **Resultados completos** y detallados
- **Interfaz amigable** en consola

### Dataset DBLP

El archivo `com-dblp.top5000.cmty.txt` contiene:
- **5,000 comunidades** de coautoría científica
- Cada línea = una comunidad (grupo de autores que colaboran)
- Los números son IDs únicos de investigadores
- Representa colaboraciones en ciencias de la computación

**Ejemplo de interpretación:**
```
105653 105654 210737 210738
```
Significa que estos 4 investigadores han colaborado entre sí en publicaciones científicas.

### API REST Disponible

```
GET  /                          # Página principal
POST /api/load-graph           # Cargar grafo DBLP
GET  /api/graph-stats          # Estadísticas del grafo
POST /api/find-clique          # Ejecutar algoritmo de clique
GET  /api/visualize/<nodes>    # Datos para visualización
POST /api/highlight-clique     # Destacar clique en visualización
```
