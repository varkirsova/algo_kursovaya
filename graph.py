from collections import defaultdict

class Graph:
    def __init__(self, directed=True, weighted=False):
        # directed  ориентированный граф
        # weighted  взвешенный граф

        self.directed = directed
        self.weighted = weighted

        # adjacency list
        # vertex -> [(neighbor, weight)]
        self.adjacency_list = defaultdict(list)

        # switching graph representation
        # edge_id -> (from, to, weight)
        self.switching_graph = {}

        self.vertices = set()
        self.edge_count = 0

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.add(vertex)
            self.adjacency_list[vertex] = []

    def add_edge(self, source, destination, weight=1):
        self.add_vertex(source)
        self.add_vertex(destination)

        # adjacency list
        self.adjacency_list[source].append((destination, weight))

        # switching graph
        self.switching_graph[self.edge_count] = (
            source,
            destination,
            weight
        )

        self.edge_count += 1

        # если граф неориентированный
        if not self.directed:
            self.adjacency_list[destination].append((source, weight))

            self.switching_graph[self.edge_count] = (
                destination,
                source,
                weight
            )

            self.edge_count += 1

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def number_of_vertices(self):
        return len(self.vertices)

    def number_of_edges(self):
        return self.edge_count


    def validate_graph(self):
        for vertex in self.vertices:

            if vertex not in self.adjacency_list:
                return False

            for neighbor, weight in self.adjacency_list[vertex]:

                if neighbor not in self.vertices:
                    return False

                if self.weighted and not isinstance(weight, (int, float)):
                    return False

        return True

    def print_graph(self):

        print("Adjacency List:\n")

        for vertex in self.adjacency_list:
            print(f"{vertex} -> {self.adjacency_list[vertex]}")

    def print_switching_graph(self):

        print("\nSwitching Graph:\n")

        for edge_id, edge_data in self.switching_graph.items():
            print(f"{edge_id}: {edge_data}")


