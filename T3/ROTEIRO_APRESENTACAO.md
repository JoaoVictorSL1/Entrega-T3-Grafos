# 🎤 Roteiro de Apresentação Detalhado - Trabalho Prático 3

## Problema do Carteiro Chinês (Dígrafos Ponderados)

Este roteiro fornece falas sugeridas e detalhes técnicos para uma apresentação de alto nível.

---

### 👤 Pessoa 1: Fundamentos, Teoria e Modelagem Manual

**Objetivo:** Estabelecer a base do problema e mostrar o trabalho "braçal" de análise.

- **Abertura e Contexto:**
  - "Olá, nosso grupo vai apresentar a resolução do Problema do Carteiro Chinês. Imagine um carteiro que precisa passar por todas as ruas de um bairro. Ele quer fazer isso sem deixar nenhuma rua para trás e gastando o mínimo de combustível possível. Modelamos esse bairro como um **dígrafo (grafo orientado) ponderado**, onde os vértices são os cruzamentos e as arestas são as ruas com seus respectivos sentidos e comprimentos."
- **O Desafio Matemático:**
  - "O problema central é que nem todo grafo permite um caminho perfeito (Euleriano). Para que o carteiro não precise repetir ruas desnecessariamente, o grafo deve ser **conexo** e todos os vértices devem estar **balanceados** (Grau de Entrada = Grau de Saída)."
- **A Eulerização Manual (O Coração do Trabalho):**
  - "No nosso projeto, analisamos o grafo oficial do trabalho. Identificamos que os vértices **'e'** e **'f'** tinham deficiência de saída, enquanto **'a'** e **'b'** tinham deficiência de entrada."
  - "Para resolver isso sem precisar implementar algoritmos complexos como o Método Húngaro ou Floyd-Warshall (conforme as restrições do T3), realizamos o balanceamento manual: identificamos os caminhos mínimos e adicionamos as arestas repetidas necessárias no arquivo `entrada_eulerizada.txt` para que o custo total fosse o menor possível."

---

### 👤 Pessoa 2: Arquitetura de Software e Representação de Dados

**Objetivo:** Mostrar o domínio técnico sobre a implementação e as classes utilizadas.

- **Estrutura Orientada a Objetos:**
  - "Para a implementação, utilizamos a linguagem **Python** seguindo os padrões da biblioteca `algs4`. Nosso código está organizado na pasta `src/`, separando as responsabilidades."
- **Modelagem no Código (`Digraph` e `Edge`):**
  - "Utilizamos a classe `Digraph.py`, que representa o grafo através de uma **Lista de Adjacências**. Em vez de uma matriz (que ocuparia muito espaço desnecessário), cada vértice possui um 'Bag' de objetos do tipo `DirectedEdge`."
  - "Cada `DirectedEdge` armazena três informações críticas: o vértice de origem, o de destino e o **peso (custo)** da aresta. Isso permite que nosso algoritmo de busca consulte rapidamente quais ruas saem de um cruzamento e qual o custo de cada uma."
- **Leitura de Arquivos:**
  - "O programa foi projetado para ser dinâmico. O `Main.py` lê o número de vértices, o número de arestas e, em seguida, popula o grafo. Antes de qualquer cálculo, o sistema varre todos os vértices e imprime no console os graus de entrada e saída, garantindo que a entrada fornecida é de fato um grafo pronto para o Método de Hierholzer."

---

### 👤 Pessoa 3: Algoritmo de Hierholzer, Execução e Resultados

**Objetivo:** Demonstrar o funcionamento do algoritmo, resultados e a parte visual.

- **Lógica do Método de Hierholzer:**
  - "Com o grafo balanceado, usamos o **Método de Hierholzer**. A lógica dele é elegante e eficiente: ele utiliza uma **Pilha (Stack)** para explorar o grafo. Ele vai 'entrando' nos caminhos e, quando encontra um vértice que não tem mais arestas de saída disponíveis, ele entende que fechou um ciclo e move esse vértice para o circuito final."
  - "Diferente de uma busca simples, ele garante que 100% das arestas sejam visitadas. Adaptamos a classe original para que, durante essa travessia, ela acumule os pesos das arestas, resultando no **Custo Total Final**."
- **Demonstração Prática:**
  - "No terminal, ao rodar `python src/Main.py`, vemos o algoritmo identificando o caminho. No nosso caso oficial, o custo resultou em **276.0 unidades**."
- **O Diferencial Visual (O Frontend):**
  - "Para tornar a explicação mais didática, desenvolvemos um **Frontend animado em HTML/JavaScript**. (Mostre o visualizador aqui). Ele renderiza o grafo dinamicamente e mostra o percurso sendo traçado em tempo real, com um console que imita o log do sistema. Isso prova que o carteiro realmente visitou cada rua do mapa original atendendo à demanda do problema."

---

### 🏁 Conclusão do Grupo

- "Concluímos que a separação entre a análise teórica (eulerização manual) e a automação (método de Hierholzer) nos permitiu entender profundamente como o balanceamento de um grafo afeta a logística de rotas. O código final é robusto e capaz de processar desde grafos pequenos até instâncias colossais com centenas de arestas."
