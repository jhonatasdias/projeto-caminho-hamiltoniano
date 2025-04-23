def hamiltonian_path_util(graph, path, visited, total_vertices):
    # Se o caminho contém todos os vértices, temos um caminho Hamiltoniano
    if len(path) == total_vertices:
        return True

    # O vértice atual é o último adicionado no caminho
    current_vertex = path[-1]

    # Para cada vértice adjacente ao vértice atual
    for neighbor in graph.get(current_vertex, []):
        if neighbor not in visited:
            # Adiciona o vizinho ao caminho e marca como visitado
            visited.add(neighbor)
            path.append(neighbor)

            # Tenta completar o caminho recursivamente
            if hamiltonian_path_util(graph, path, visited, total_vertices):
                return True

            # Se a adição de neighbor não levou à solução, realiza o backtracking
            path.pop()
            visited.remove(neighbor)

    # Se nenhum caminho válido foi encontrado a partir do vértice atual, retorna False
    return False

def find_hamiltonian_path(graph):
    total_vertices = len(graph)

    # Tenta encontrar o caminho a partir de cada vértice do grafo
    for starting_vertex in graph:
        path = [starting_vertex]
        visited = set([starting_vertex])

        if hamiltonian_path_util(graph, path, visited, total_vertices):
            return path

    # Se nenhum caminho Hamiltoniano existir, retorna None
    return None

# Exemplo de uso:
if __name__ == "__main__":
    # Definindo um grafo como dicionário.
    # Exemplo de grafo não-orientado (para cada aresta, adicionamos as conexões nos dois sentidos)
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D"],
        "D": ["B", "C"]
    }

    # Caso seja um grafo orientado, a estrutura pode ser definida sem duplicar as conexões.
    # Exemplo para grafo direcionado:
    # graph = {
    #     "A": ["B", "C"],
    #     "B": ["C", "D"],
    #     "C": ["D"],
    #     "D": []
    # }

    caminho = find_hamiltonian_path(graph)

    if caminho:
        print("Caminho Hamiltoniano encontrado:")
        print(" -> ".join(caminho))
    else:
        print("Caminho Hamiltoniano não existe no grafo fornecido.")
