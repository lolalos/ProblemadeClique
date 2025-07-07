"""
Versión simplificada del solver de cliques - Resultados en consola
Análisis completo del dataset DBLP sin dependencias externas
"""

import time
import itertools
from typing import List, Set, Dict
from collections import defaultdict

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
        print(f"📂 Archivo: {filepath}")
        
        start_time = time.time()
        
        try:
            with open(filepath, 'r') as file:
                for line_num, line in enumerate(file, 1):
                    if line.strip():
                        # Cada línea es una comunidad
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
                        print(f"📊 Procesadas {line_num:,} comunidades...")
        
        except FileNotFoundError:
            print(f"❌ ERROR: No se encontró el archivo {filepath}")
            return False
        
        self.edges = list(set(self.edges))
        load_time = time.time() - start_time
        
        print(f"✅ Grafo cargado exitosamente en {load_time:.2f} segundos")
        print(f"📈 Estadísticas: {len(self.nodes):,} nodos, {len(self.edges):,} aristas, {len(self.communities):,} comunidades")
        return True
    
    def is_clique(self, vertices: List[int]) -> bool:
        """Verificar si un conjunto de vértices forma un clique"""
        if len(vertices) <= 1:
            return True
            
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                if vertices[j] not in self.adjacency_dict[vertices[i]]:
                    return False
        return True
    
    def greedy_clique(self) -> List[int]:
        """Algoritmo greedy para clique máximo"""
        print("\n" + "="*60)
        print("          EJECUTANDO ALGORITMO GREEDY")
        print("="*60)
        
        start_time = time.time()
        clique = []
        remaining = self.nodes.copy()
        iteration = 0
        
        print("🔄 Iniciando búsqueda greedy...")
        
        while remaining:
            iteration += 1
            
            # Elegir vértice con más conexiones
            best_vertex = max(remaining, 
                            key=lambda v: len(self.adjacency_dict[v] & remaining))
            
            connections = len(self.adjacency_dict[best_vertex] & remaining)
            clique.append(best_vertex)
            remaining &= self.adjacency_dict[best_vertex]
            
            if iteration <= 10 or iteration % 5 == 0:
                print(f"   Iteración {iteration}: Agregado nodo {best_vertex} "
                      f"(conexiones: {connections}, restantes: {len(remaining)})")
        
        execution_time = time.time() - start_time
        print(f"✅ Algoritmo completado en {execution_time:.3f} segundos")
        
        return clique
    
    def brute_force_clique(self, max_nodes: int = 15) -> List[int]:
        """Algoritmo de fuerza bruta (limitado)"""
        print("\n" + "="*60)
        print("          EJECUTANDO ALGORITMO FUERZA BRUTA")
        print("="*60)
        print(f"⚠️  Limitado a {max_nodes} nodos por complejidad exponencial")
        
        start_time = time.time()
        
        # Seleccionar nodos con mayor grado
        sorted_nodes = sorted(self.nodes, 
                            key=lambda n: len(self.adjacency_dict[n]), 
                            reverse=True)
        test_nodes = sorted_nodes[:max_nodes]
        
        print(f"🔍 Analizando {len(test_nodes)} nodos de mayor grado...")
        
        max_clique = []
        combinations_tested = 0
        
        # Probar todos los subconjuntos, empezando por los más grandes
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
        print(f"✅ Fuerza bruta completada en {execution_time:.3f} segundos")
        print(f"📊 Combinaciones probadas: {combinations_tested:,}")
        
        return max_clique
    
    def analyze_communities(self):
        """Analizar las comunidades originales"""
        print("\n" + "="*60)
        print("          ANÁLISIS DE COMUNIDADES")
        print("="*60)
        
        if not self.communities:
            print("❌ No hay comunidades cargadas")
            return
        
        sizes = [len(community) for community in self.communities]
        
        print(f"📊 Total de comunidades: {len(self.communities):,}")
        print(f"📏 Tamaño promedio: {sum(sizes)/len(sizes):.2f}")
        print(f"📈 Tamaño máximo: {max(sizes)}")
        print(f"📉 Tamaño mínimo: {min(sizes)}")
        
        # Mostrar la comunidad más grande
        largest_community = max(self.communities, key=len)
        print(f"\n🏆 Comunidad más grande: {len(largest_community)} nodos")
        print(f"   Nodos: {largest_community[:10]}..." if len(largest_community) > 10 else f"   Nodos: {largest_community}")
        
        # Distribución de tamaños
        print(f"\n📈 Distribución de tamaños:")
        size_counts = {}
        for size in sizes:
            size_counts[size] = size_counts.get(size, 0) + 1
        
        for size in sorted(size_counts.keys()):
            if size_counts[size] > 5:  # Solo mostrar tamaños frecuentes
                print(f"   Tamaño {size}: {size_counts[size]:,} comunidades")
    
    def get_detailed_stats(self) -> dict:
        """Obtener estadísticas detalladas del grafo"""
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
    
    def display_results(self, clique: List[int], algorithm: str, execution_time: float):
        """Mostrar resultados de manera detallada"""
        print("\n" + "="*60)
        print("               RESULTADOS")
        print("="*60)
        
        print(f"🔬 Algoritmo utilizado: {algorithm}")
        print(f"⏱️  Tiempo de ejecución: {execution_time:.4f} segundos")
        print(f"🎯 Tamaño del clique: {len(clique)} nodos")
        print(f"✅ ¿Es un clique válido?: {'Sí' if self.is_clique(clique) else 'No'}")
        
        if clique:
            print(f"\n📋 Nodos del clique:")
            if len(clique) <= 20:
                print(f"   {clique}")
            else:
                print(f"   Primeros 20: {clique[:20]}...")
                print(f"   Total: {len(clique)} nodos")
            
            # Calcular densidad del clique
            possible_edges = len(clique) * (len(clique) - 1) // 2
            print(f"\n📊 Análisis del clique:")
            print(f"   • Aristas internas: {possible_edges:,}")
            print(f"   • Densidad: 100% (clique completo)")
            
            # Comparar con la comunidad más grande
            if self.communities:
                largest_community = max(self.communities, key=len)
                percentage = (len(clique) / len(largest_community)) * 100
                print(f"   • Comparación con comunidad más grande: {percentage:.1f}%")

def main():
    """Función principal con interfaz mejorada"""
    print("🔷" * 20)
    print("     ANÁLISIS DE CLIQUES - DATASET DBLP")
    print("     Problema de Clique Máximo")
    print("🔷" * 20)
    
    solver = SimpleCliqueSolver()
    
    # Cargar datos
    if not solver.load_from_file("../com-dblp.top5000.cmty.txt"):
        print("\n❌ No se pudo cargar el dataset. Verifica que el archivo existe.")
        input("\nPresiona Enter para salir...")
        return
    
    # Mostrar estadísticas generales
    print("\n" + "="*60)
    print("          ESTADÍSTICAS DEL GRAFO")
    print("="*60)
    
    stats = solver.get_detailed_stats()
    print(f"📊 Nodos totales: {stats['nodes']:,}")
    print(f"🔗 Aristas totales: {stats['edges']:,}")
    print(f"👥 Comunidades: {stats['communities']:,}")
    print(f"📈 Grado promedio: {stats['avg_degree']:.2f}")
    print(f"🔝 Grado máximo: {stats['max_degree']:,}")
    print(f"🔻 Grado mínimo: {stats['min_degree']:,}")
    print(f"🕸️ Densidad del grafo: {stats['density']*100:.6f}%")
    
    # Analizar comunidades
    solver.analyze_communities()
    
    # Menú de opciones
    while True:
        print("\n" + "="*60)
        print("                   MENÚ")
        print("="*60)
        print("1. 🚀 Ejecutar algoritmo Greedy (rápido)")
        print("2. 🔍 Ejecutar algoritmo Fuerza Bruta (lento, max 15 nodos)")
        print("3. 📊 Mostrar estadísticas nuevamente")
        print("4. 👥 Análisis de comunidades")
        print("5. ❌ Salir")
        
        choice = input("\n🔘 Selecciona una opción (1-5): ").strip()
        
        if choice == "1":
            start_time = time.time()
            clique = solver.greedy_clique()
            end_time = time.time()
            solver.display_results(clique, "Greedy", end_time - start_time)
            
        elif choice == "2":
            confirm = input("\n⚠️  Fuerza bruta puede ser lento. ¿Continuar? (s/n): ").lower()
            if confirm == 's':
                start_time = time.time()
                clique = solver.brute_force_clique()
                end_time = time.time()
                solver.display_results(clique, "Fuerza Bruta", end_time - start_time)
            
        elif choice == "3":
            stats = solver.get_detailed_stats()
            print("\n📊 Estadísticas actualizadas:")
            for key, value in stats.items():
                if isinstance(value, float):
                    print(f"   {key}: {value:.4f}")
                else:
                    print(f"   {key}: {value:,}")
            
        elif choice == "4":
            solver.analyze_communities()
            
        elif choice == "5":
            print("\n👋 ¡Gracias por usar el analizador de cliques!")
            break
            
        else:
            print("\n❌ Opción no válida. Intenta de nuevo.")
        
        input("\n⏸️  Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
