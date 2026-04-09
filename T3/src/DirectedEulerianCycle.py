import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Digraph import EdgeWeightedDigraph as Digraph
from DirectedEdge import DirectedEdge

class DirectedEulerianCycle:
    def __init__(self, G, outdegree, indegree):
        self.cycle = []
        self.total_cost = 0.0

        if G.E == 0:
            return

        for v in range(G.V):
            if outdegree[v] != indegree[v]:
                return

        adj = [[] for _ in range(G.V)]
        for v in range(G.V):
            # Iterate through the Bag items using iteration
            for e in G.adj[v]:
                adj[v].append(e)

        start_vertex = 0
        for v in range(G.V):
            if len(adj[v]) > 0:
                start_vertex = v
                break

        path = []
        path.append(start_vertex)
        
        print("\n--- INICIANDO BUSCA DE CAMINHOS (Método de Hierholzer) ---")
        while len(path) > 0:
            v = path[-1]
            if len(adj[v]) > 0:
                e = adj[v].pop()
                w = e.To()
                self.total_cost += e.weight
                print(f"📍 Mapeando caminho: {chr(v + ord('a'))} -> {chr(w + ord('a'))} | Custo da aresta: {e.weight} | Custo Total Acumulado: {self.total_cost:.1f}")
                path.append(w)
            else:
                finished_vertex = path.pop()
                print(f"🔒 Beco sem saída atingido em '{chr(finished_vertex + ord('a'))}'. Fechando esse nó para o sub-circuito final.")
                self.cycle.append(finished_vertex)
                
        print("----------------------------------------------------------")
        self.cycle.reverse()
        
        # Verify if all edges were used (otherwise graph must be disconnected)
        if len(self.cycle) != G.E + 1:
            self.cycle = []
            self.total_cost = 0.0

    def has_eulerian_cycle(self):
        return len(self.cycle) > 0

    def get_cycle(self):
        return self.cycle

    def get_cost(self):
        return self.total_cost
