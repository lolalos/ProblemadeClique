"""
Version simplificada del solver de cliques - Resultados en consola
Analisis completo del dataset DBLP sin dependencias externas
"""

import time
import itertools
from typing import List, Set, Dict, Tuple
from collections import defaultdict
import matplotlib.pyplot as plt

class SimpleCliqueSolver:
    """Implementa algoritmos de clique sin dependencias externas"""
    
    def __init__(self):
        self.adjacency_dict = defaultdict(set)
        self.nodes = set()
        self.edges = set()
        self.communities = []
    
    def load_from_file(self, filepath: str):
        """Cargar grafo desde archivo DBLP"""
        print("="*60)
        print("          CARGANDO DATASET DBLP")
        print("="*60)
        print(f"Archivo: {filepath}")
        
        start_time = time.time()
        
        try:
            with open(filepath, 'r') as file:
                for line_num, line in enumerate(file, 1):
                    if line.strip():
                        # Cada linea es una comunidad
                        community = list(map(int, line.strip().split()))
                        self.communities.append(community)
                        
                        # Agregar nodos
                        for node in community:
                            self.nodes.add(node)
                        
                        # Conectar todos los pares en la comunidad
                        for i, node1 in enumerate(community):
                            for j, node2 in enumerate(community):
                                if i != j:
                                    self.adjacency_dict[node1].add(node2)
                                    self.edges.add((min(node1, node2), max(node1, node2)))
                    
                    if line_num % 1000 == 0:
                        print(f"Procesadas {line_num:,} comunidades...")
        
        except FileNotFoundError:
            print(f"ERROR: No se encontro el archivo {filepath}")
            return False
        
        self.edges = list(set(self.edges))
        load_time = time.time() - start_time
        
        print(f"Grafo cargado exitosamente en {load_time:.2f} segundos")
        print(f"Estadisticas: {len(self.nodes):,} nodos, {len(self.edges):,} aristas, {len(self.communities):,} comunidades")
        return True
    
    def is_clique(self, vertices: List[int]) -> bool:
        """Verificar si un conjunto de vertices forma un clique"""
        if len(vertices) <= 1:
            return True
            
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                if vertices[j] not in self.adjacency_dict[vertices[i]]:
                    return False
        return True
    
    def greedy_clique(self) -> tuple[List[int], float]:
        """Algoritmo greedy para clique maximo"""
        print("\n" + "="*60)
        print("          EJECUTANDO ALGORITMO GREEDY")
        print("="*60)
        
        start_time = time.time()
        clique = []
        remaining = self.nodes.copy()
        iteration = 0
        
        print("Iniciando busqueda greedy...")
        
        while remaining:
            iteration += 1
            
            # Elegir vertice con mas conexiones
            best_vertex = max(remaining, 
                            key=lambda v: len(self.adjacency_dict[v] & remaining))
            
            connections = len(self.adjacency_dict[best_vertex] & remaining)
            clique.append(best_vertex)
            remaining &= self.adjacency_dict[best_vertex]
            
            if iteration <= 10 or iteration % 5 == 0:
                print(f"   Iteracion {iteration}: Agregado nodo {best_vertex} "
                      f"(conexiones: {connections}, restantes: {len(remaining)})")
        
        execution_time = time.time() - start_time
        print(f"Algoritmo completado en {execution_time:.3f} segundos")
        
        return clique, execution_time
    
    def brute_force_clique(self, max_nodes: int = 15) -> tuple[List[int], float]:
        """Algoritmo de fuerza bruta (limitado)"""
        print("\n" + "="*60)
        print("          EJECUTANDO ALGORITMO FUERZA BRUTA")
        print("="*60)
        print(f"Limitado a {max_nodes} nodos por complejidad exponencial")
        
        start_time = time.time()
        
        # Seleccionar nodos con mayor grado
        sorted_nodes = sorted(self.nodes, 
                            key=lambda n: len(self.adjacency_dict[n]), 
                            reverse=True)
        test_nodes = sorted_nodes[:max_nodes]
        
        print(f"Analizando {len(test_nodes)} nodos de mayor grado...")
        
        max_clique = []
        combinations_tested = 0
        
        # Probar todos los subconjuntos, empezando por los mas grandes
        for r in range(len(test_nodes), 0, -1):
            found = False
            for subset in itertools.combinations(test_nodes, r):
                combinations_tested += 1
                if self.is_clique(list(subset)):
                    max_clique = list(subset)
                    found = True
                    break
                
                if combinations_tested % 1000 == 0:
                    print(f"   Probadas {combinations_tested:,} combinaciones...")
            
            if found:
                break
        
        execution_time = time.time() - start_time
        print(f"Fuerza bruta completada en {execution_time:.3f} segundos")
        print(f"Combinaciones probadas: {combinations_tested:,}")
        
        return max_clique, execution_time
    
    def analyze_communities(self):
        """Analizar las comunidades originales"""
        print("\n" + "="*60)
        print("          ANALISIS DE COMUNIDADES")
        print("="*60)
        
        if not self.communities:
            print("No hay comunidades cargadas")
            return
        
        sizes = [len(community) for community in self.communities]
        
        print(f"Total de comunidades: {len(self.communities):,}")
        print(f"Tamanio promedio: {sum(sizes)/len(sizes):.2f}")
        print(f"Tamanio maximo: {max(sizes)}")
        print(f"Tamanio minimo: {min(sizes)}")
        
        # Mostrar la comunidad mas grande
        largest_community = max(self.communities, key=len)
        print(f"\nComunidad mas grande: {len(largest_community)} nodos")
        print(f"   Nodos: {largest_community[:10]}..." if len(largest_community) > 10 else f"   Nodos: {largest_community}")
        
        # Distribucion de tamanios
        print(f"\nDistribucion de tamanios:")
        size_counts = {}
        for size in sizes:
            size_counts[size] = size_counts.get(size, 0) + 1
        
        for size in sorted(size_counts.keys()):
            if size_counts[size] > 5:  # Solo mostrar tamanios frecuentes
                print(f"   Tamanio {size}: {size_counts[size]:,} comunidades")
    
    def get_detailed_stats(self) -> dict:
        """Obtener estadisticas detalladas del grafo"""
        if not self.nodes:
            return {}
        
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
    
    def display_results(self, instance_name: str, clique: List[int], algorithm: str, execution_time: float, exact_clique_size: int = None):
        """Mostrar resultados de manera detallada"""
        print("\n" + "="*60)
        print("               RESULTADOS")
        print("="*60)
        
        print(f"Instancia: {instance_name}")
        print(f"Algoritmo utilizado: {algorithm}")
        print(f"Tiempo de ejecucion: {execution_time*1000:.2f} ms")
        print(f"Tamanio del clique encontrado: {len(clique)} nodos")
        if exact_clique_size is not None:
            print(f"Tamanio del clique exacto: {exact_clique_size} nodos")
        print(f"Es un clique valido?: {'Si' if self.is_clique(clique) else 'No'}")
        
        if clique:
            print(f"\nNodos del clique:")
            if len(clique) <= 20:
                print(f"   {clique}")
            else:
                print(f"   Primeros 20: {clique[:20]}...")
                print(f"   Total: {len(clique)} nodos")
            
            # Calcular densidad del clique
            possible_edges = len(clique) * (len(clique) - 1) // 2
            print(f"\nAnalisis del clique:")
            print(f"   • Aristas internas: {possible_edges:,}")
            print(f"   • Densidad: 100% (clique completo)")
            
            # Comparar con la comunidad mas grande
            if self.communities:
                largest_community = max(self.communities, key=len)
                percentage = (len(clique) / len(largest_community)) * 100
                print(f"   • Comparacion con comunidad mas grande: {percentage:.1f}%")

def plot_comparison(results):
    """Graficar comparacion de resultados"""
    algorithms = [r['algorithm'] for r in results]
    sizes = [r['size'] for r in results]
    times = [r['time_ms'] for r in results]
    exact_size = None
    for r in results:
        if r.get('exact_size') is not None:
            exact_size = r['exact_size']
            break

    fig, ax1 = plt.subplots(figsize=(8,5))
    color = 'tab:blue'
    ax1.set_xlabel('Algoritmo')
    ax1.set_ylabel('Tamanio del clique', color=color)
    bars = ax1.bar(algorithms, sizes, color=color, alpha=0.7, label='Tamanio clique')
    if exact_size is not None:
        ax1.axhline(exact_size, color='tab:green', linestyle='--', label='Clique exacto')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.legend(loc='upper left')

    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Tiempo (ms)', color=color)
    ax2.plot(algorithms, times, color=color, marker='o', label='Tiempo (ms)')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.legend(loc='upper right')

    plt.title('Comparacion de algoritmos de clique')
    plt.tight_layout()
    plt.show()

def main():
    """Funcion principal con interfaz mejorada"""
    print("🔷" * 20)
    print("     ANALISIS DE CLIQUES - DATASET DBLP")
    print("     Problema de Clique Maximo")
    print("🔷" * 20)
    
    solver = SimpleCliqueSolver()
    instance_file = "../com-dblp.top5000.cmty.txt"
    
    # Cargar datos
    if not solver.load_from_file(instance_file):
        print("\nNo se pudo cargar el dataset. Verifica que el archivo existe.")
        input("\nPresiona Enter para salir...")
        return
    
    # Mostrar estadisticas generales
    print("\n" + "="*60)
    print("          ESTADISTICAS DEL GRAFO")
    print("="*60)
    
    stats = solver.get_detailed_stats()
    print(f"Nodos totales: {stats['nodes']:,}")
    print(f"Aristas totales: {stats['edges']:,}")
    print(f"Comunidades: {stats['communities']:,}")
    print(f"Grado promedio: {stats['avg_degree']:.2f}")
    print(f"Grado maximo: {stats['max_degree']:,}")
    print(f"Grado minimo: {stats['min_degree']:,}")
    print(f"Densidad del grafo: {stats['density']*100:.6f}%")
    
    # Analizar comunidades
    solver.analyze_communities()
    
    # Resultados para graficar
    comparison_results = []
    exact_clique_size = None
    
    # Menu de opciones
    while True:
        print("\n" + "="*60)
        print("                   MENU")
        print("="*60)
        print("1. Ejecutar algoritmo Greedy (rapido)")
        print("2. Ejecutar algoritmo Fuerza Bruta (lento, max 15 nodos)")
        print("3. Mostrar estadisticas nuevamente")
        print("4. Analisis de comunidades")
        print("5. Graficar comparacion de resultados")
        print("6. Salir")
        
        choice = input("\nSelecciona una opcion (1-6): ").strip()
        
        if choice == "1":
            clique, exec_time = solver.greedy_clique()
            solver.display_results(instance_file, clique, "Greedy", exec_time, exact_clique_size)
            comparison_results.append({
                'algorithm': 'Greedy',
                'size': len(clique),
                'time_ms': exec_time * 1000,
                'exact_size': exact_clique_size
            })
            
        elif choice == "2":
            confirm = input("\nFuerza bruta puede ser lento. Continuar? (s/n): ").lower()
            if confirm == 's':
                clique, exec_time = solver.brute_force_clique()
                exact_clique_size = len(clique)
                solver.display_results(instance_file, clique, "Fuerza Bruta", exec_time, exact_clique_size)
                comparison_results.append({
                    'algorithm': 'Fuerza Bruta',
                    'size': len(clique),
                    'time_ms': exec_time * 1000,
                    'exact_size': exact_clique_size
                })
            
        elif choice == "3":
            stats = solver.get_detailed_stats()
            print("\nEstadisticas actualizadas:")
            for key, value in stats.items():
                if isinstance(value, float):
                    print(f"   {key}: {value:.4f}")
                else:
                    print(f"   {key}: {value:,}")
            
        elif choice == "4":
            solver.analyze_communities()
        
        elif choice == "5":
            if not comparison_results:
                print("\nNo hay resultados para graficar. Ejecuta primero algun algoritmo.")
            else:
                plot_comparison(comparison_results)
        
        elif choice == "6":
            print("\nGracias por usar el analizador de cliques!")
            break
            
        else:
            print("\nOpcion no valida. Intenta de nuevo.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
