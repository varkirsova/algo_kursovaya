from collections import deque


def bfs(graph, start_vertex):

    # посещённые вершины
    visited = set()

    # очередь BFS
    queue = deque()

    # порядок обхода
    traversal_order = []

    # расстояния от стартовой вершины
    distances = {}

    # стартовая вершина
    visited.add(start_vertex)
    queue.append(start_vertex)

    distances[start_vertex] = 0

    while queue:

        # берём вершину из очереди
        current_vertex = queue.popleft()

        traversal_order.append(current_vertex)

        # соседи вершины
        neighbors = graph.get_neighbors(current_vertex)

        for neighbor, weight in neighbors:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)

                distances[neighbor] = (
                    distances[current_vertex] + 1
                )

    return traversal_order, distances