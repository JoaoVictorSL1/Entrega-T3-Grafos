import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Digraph import EdgeWeightedDigraph as Digraph
from DirectedEulerianCycle import DirectedEulerianCycle

def main():
    if len(sys.argv) < 2:
        # Tenta carregar o arquivo oficial por padrão caso o usuário não passe argumentos
        filename = os.path.join('dados', 'entrada_eulerizada.txt')
        if not os.path.exists(filename):
            print("Uso: python Main.py <arquivo_entrada>")
            print(f"Erro: Arquivo padrão '{filename}' não encontrado.")
            sys.exit(1)
        print(f"--- Nenhum arquivo fornecido. Carregando padrão: {filename} ---\n")
    else:
        filename = sys.argv[1]
    
    with open(filename, 'r') as f:
        graph = Digraph(file=f)
        
    print(f"Grafo carregado de '{filename}':\n")
    # print(graph) # Opcional: imprimir o grafo completo
    
    indegree = [0] * graph.V
    outdegree = [0] * graph.V
    
    for v in range(graph.V):
        for e in graph.adj[v]:
            outdegree[v] += 1
            indegree[e.To()] += 1
            
    print("Graus dos Vértices:")
    is_balanced = True
    for v in range(graph.V):
        print(f"  Vértice {v}: Entrada = {indegree[v]}, Saída = {outdegree[v]}")
        if indegree[v] != outdegree[v]:
            is_balanced = False
            
    if is_balanced:
        print("\nO grafo está balanceado (Eulerizado).")
    else:
        print("\nO grafo NÃO está balanceado.")
        
    eulerian = DirectedEulerianCycle(graph, outdegree, indegree)
    
    if eulerian.has_eulerian_cycle():
        cycle = eulerian.get_cycle()
        print("\nCircuito Euleriano Encontrado (sequência de vértices):")
        print(" ".join(chr(v + ord('a')) for v in cycle))
        print(f"\nCusto total do circuito: {eulerian.get_cost():.1f}")
    else:
        print("\nNão foi possível encontrar um circuito euleriano.")

if __name__ == '__main__':
    main()
