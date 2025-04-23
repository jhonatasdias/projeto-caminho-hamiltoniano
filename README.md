# Projeto Caminho Hamiltoniano

O **Projeto Caminho Hamiltoniano** implementa um algoritmo de **backtracking** para determinar se existe um caminho que visite cada vértice exatamente uma vez em um grafo orientado ou não-orientado, e o constrói quando possível.

---

## Descrição do Projeto

O objetivo deste projeto é encontrar um **Caminho Hamiltoniano** em um grafo representado como um dicionário de adjacências. Utiliza-se recursão e backtracking para explorar todas as possíveis sequências de vértices, garantindo que cada vértice seja visitado apenas uma vez. Caso um caminho completo seja descoberto, ele é retornado; caso contrário, conclui-se que não existe Caminho Hamiltoniano.

### Lógica do Código (linha a linha)

#### Função `hamiltonian_path_util(graph, path, visited, total_vertices)`

- **Parâmetros:**  
  - `graph` : dicionário de listas de adjacência.  
  - `path` : lista que guarda a sequência de vértices do caminho atual.  
  - `visited` : conjunto de vértices já incluídos em `path`.  
  - `total_vertices` : número total de vértices no grafo.  
- Verifica se `len(path) == total_vertices`; se sim, retorna `True` indicando que o caminho é completo.  
- Obtém o `current_vertex` como último elemento de `path`.  
- Para cada `neighbor` em `graph.get(current_vertex, [])`:  
  - Se `neighbor` não estiver em `visited`:  
    - Adiciona `neighbor` a `visited` e a `path`.  
    - Chama recursivamente a si mesma; se retornar `True`, propaga `True`.  
    - Caso contrário, faz **backtracking**: remove `neighbor` de `path` e de `visited`.  
- Se nenhum vizinho levar à solução, retorna `False`.

#### Função `find_hamiltonian_path(graph)`

- **Parâmetros:**  
  - `graph` : dicionário de listas de adjacência.  
- Calcula `total_vertices = len(graph)`.  
- Para cada `starting_vertex` em `graph`:  
  - Inicializa `path = [starting_vertex]` e `visited = {starting_vertex}`.  
  - Chama `hamiltonian_path_util`; se retornar `True`, retorna `path`.  
- Se nenhum ponto de partida produzir um caminho completo, retorna `None`.

#### Bloco principal (`if __name__ == '__main__'`)

- Define um **exemplo de grafo** (orientado ou não-orientado).  
- Chama `find_hamiltonian_path(graph)`.  
- Exibe no terminal se encontrou o caminho ou não.

---

## Como Executar o Projeto

### Requisitos

- Python 3.6 ou superior  
- Nenhuma dependência externa

### Passos

1. Clone ou copie o arquivo `hamiltonian_path.py` para seu computador.  
2. No terminal, execute:

    ```bash
    python nome_do_arquivo.py
    ```

> Substitua `nome_do_arquivo.py` pelo nome do arquivo caso seja diferente.

### Exemplo de Saída

```plaintext
Caminho Hamiltoniano encontrado:
A -> B -> D -> C
```

ou

```plaintext
Caminho Hamiltoniano não existe no grafo fornecido.
```

---

## Relatório Técnico

### Análise do Algoritmo

- Explora recursivamente todas as sequências possíveis de vértices até encontrar um caminho completo ou esgotar as opções.  
- Executa **backtracking** para desfazer escolhas que não levam à solução, evitando seguir caminhos inviáveis até o fim.

### Complexidade Assintótica

- **Melhor caso:** quando o caminho é encontrado rapidamente, pode explorar poucas ramificações, ainda que em geral exponencial.  
- **Pior caso:** O(n!) — fatoriais de permutações de vértices.  
- **Complexidade temporal:** O(n!)  
- **Complexidade espacial:** O(n) em profundidade de recursão (pilha de chamadas).

### Vantagens

- Implementação simples e direta.  
- Garante encontrar o caminho real, se existir.  
- Permite ser adaptado para grafos direcionados ou não-direcionados.

---

### Análise da complexidade pela aplicação do Teorema Mestre

```plaintext
O algoritmo de backtracking para Caminho Hamiltoniano não se enquadra na forma 
T(n) = a T(n/b) + f(n) do Teorema Mestre, pois a recusão se ramifica de modo 
variável (não há divisão em subproblemas de tamanho fixo). Logo, sua complexidade 
é de natureza exponencial (O(n!)) e não pode ser analisada via Teorema Mestre.
```

---

## Licença

Este projeto está licenciado sob a **Licença MIT**.