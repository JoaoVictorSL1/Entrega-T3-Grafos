# Trabalho Prático 3 - Problema do Carteiro Chinês

## Eulerização do Grafo Oficial

A eulerização manual do grafo oficial requer o balanceamento dos vértices com graus de entrada e saída diferentes.
A partir do grafo fornecido (`imgs/graph.png`), foram obtidos os seguintes graus:
- a (0): Entrada=1, Saída=2 (Desbalanceado: delta=+1) -> Precisa de +1 grau de entrada
- b (1): Entrada=1, Saída=2 (Desbalanceado: delta=+1) -> Precisa de +1 grau de entrada
- c (2): Entrada=2, Saída=2 (Balanceado: delta=0)
- d (3): Entrada=2, Saída=2 (Balanceado: delta=0)
- e (4): Entrada=3, Saída=2 (Desbalanceado: delta=-1) -> Precisa de +1 grau de saída
- f (5): Entrada=2, Saída=1 (Desbalanceado: delta=-1) -> Precisa de +1 grau de saída

Para balancear, emparelhamos os vértices `e` e `f` com `a` e `b` buscando os caminhos de menor custo:
- Caminho de **e** para **a** (peso 12) -> aresta `e -> a`
- Caminho de **f** para **b** (peso 69) -> caminho `f -> c -> d -> e -> a -> b`

Os caminhos adicionados em nossa abstração do método Húngaro/Floyd-Warshall somaram custo de 81.
Arestas repetidas:
- `e -> a` (peso 12)
- `f -> c` (peso 22)
- `c -> d` (peso 20)
- `d -> e` (peso 5)
- `e -> a` (peso 12) (aparece novamente no caminho estendido)
- `a -> b` (peso 10)

Após essa duplicação, o grafo tornou-se equilibrado para a execução do circuito.

## Como o Programa Produz o Resultado (Método de Hierholzer)

1. **Leitura e Validação:** Primeiro o script (`Main.py`) lê a lista de adjacências e confirma o balanceamento (entradas iguais a saídas para todos os vértices).
2. **Exploração de Caminhos:** O algoritmo de Hierholzer, implementado na classe `DirectedEulerianCycle`, inicializa uma pilha de caminhos e insere o vértice inicial (por exemplo, `a`, que tem ID `0`).
3. **Mergulho em Profundidade:** Sempre que o vértice no topo da pilha tiver arestas não visitadas de saída, o programa empilha o vértice destino da aresta e retira essa aresta do grafo. Ao mesmo tempo, ele aproveita essa passagem para somar o peso (custo) da respectiva aresta na variável `total_cost`.
4. **Fechamento de Sub-circuitos:** Quando o topo da pilha atinge um "beco sem saída" onde todas as arestas partindo dele já foram caminhadas, isso quer dizer que o algoritmo fechou um sub-ciclo completo. O algoritmo remove esse vértice do caminho temporário e o coloca no circuito Euleriano definitivo (`cycle.append()`).
5. **Reversão:** Devido ao mecanismo de pilha (LIFO), os sub-circuitos são salvos de trás para frente. No final do processamento, a lista total do ciclo é revertida para obter a ordem correta cronológica em que o carteiro andou.
6. **Resultado Final:** Em `Main.py`, se o tamanho final do ciclo corresponde de fato a todas as arestas mais o nó de retorno, mostramos o arranjo de vértices transcrevendo os Inteiros localizados para seus nomes reais (`chr(v + ord('a'))`) e expomos o custo computado.

## Instruções de Execução

O projeto implementa o **Método de Hierholzer** em Python visando encontrar o percurso sobre o grafo balanceado.

1. **Requisitos**: É necessário ter Python instalado na máquina. Nenhuma biblioteca externa é necessária, uma vez que as dependências (`bag.py`, `Digraph.py` e `DirectedEdge.py`) estão importadas diretamente na pasta `src/`.
2. **Como rodar**: Execute o arquivo `Main.py` via linha de comando (preferência partindo do diretório raiz) e informando o arquivo com o grafo eulerizado.

```bash
python src/Main.py dados/entrada_eulerizada.txt
```

A saída exibirá o carregamento atestando o balanceamento de vértices (`Entrada == Saída`), a ordem de passagem pelas ruas da cidade (ex: `a c d e ...`) e o custo mínimo calculado (que fechará em **276.0**).

## Vídeo Explicação
Aqui deve ser preenchido o link do vídeo de apresentação da modelagem e do código em pleno funcionamento:
[(https://youtu.be/a_zeOX2mIrg)]
