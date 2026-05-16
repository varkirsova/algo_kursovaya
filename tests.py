# test_graph.py
from bfs import bfs
from graph import Graph
from graph_generator import (
    generate_sparse_graph,
    generate_dense_graph
)


print("\nТест 1: Создание графа\n")

graph = Graph(
    directed=True,
    weighted=True
)

graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)

graph.add_edge(1, 2, 5)
graph.add_edge(2, 3, 10)
graph.add_edge(1, 3, 7)

graph.print_graph()

graph.print_switching_graph()

print("\nVertices:", graph.number_of_vertices())
print("Edges:", graph.number_of_edges())

print("\nVALID:", graph.validate_graph())



print("\nТест 2: Sparse граф\n")

sparse_graph = generate_sparse_graph(
    vertices=10,
    weighted=True
)

sparse_graph.print_graph()

print("\nVertices:", sparse_graph.number_of_vertices())
print("Edges:", sparse_graph.number_of_edges())

print("\nVALID:", sparse_graph.validate_graph())


print("\nТест 3: Dense граф\n")

dense_graph = generate_dense_graph(
    vertices=5,
    weighted=True
)

dense_graph.print_graph()

print("\nVertices:", dense_graph.number_of_vertices())
print("Edges:", dense_graph.number_of_edges())

print("\nVALID:", dense_graph.validate_graph())


# ---------------------------------------------------
# Тест 4 — get_neighbors
# ---------------------------------------------------

print("\nТест 4: get_neighbors\n")

neighbors = graph.get_neighbors(1)

print("Neighbors of 1:")
print(neighbors)


print("\nТест 5: Switching граф\n")

graph.print_switching_graph()



print("\nТест 6: bfs\n")

test_graph = Graph(
    directed=True,
    weighted=True
)

test_graph.add_edge(0, 1, 1)
test_graph.add_edge(0, 2, 1)
test_graph.add_edge(1, 3, 1)
test_graph.add_edge(2, 4, 1)

test_graph.print_graph()

traversal_order, distances = bfs(
    test_graph,
    0
)

print("\nBFS Traversal Order:")
print(traversal_order)

print("\nDistances:")
print(distances)