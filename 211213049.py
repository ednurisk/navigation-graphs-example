with open("graf.txt") as f:
    lines = f.readlines()

adjacency_matrix = [list(map(int, line.strip().split())) for line in lines]

for i in range(len(adjacency_matrix)):
    neighbors = [j for j in range(len(adjacency_matrix)) if adjacency_matrix[i][j] == 1]
    print(f"{i}: {', '.join(map(str, neighbors))}")


graph = {i: [] for i in range(len(adjacency_matrix))}
for i in range(len(adjacency_matrix)):
    for j in range(len(adjacency_matrix)):
        if adjacency_matrix[i][j] == 1:
            graph[i].append(j)


def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

    print()

dfs(graph, 0)
