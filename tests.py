# # test_graph.py
#
# from graph import Graph
# from graph_generator import (
#     generate_sparse_graph,
#     generate_dense_graph
# )
#
#
# # ---------------------------------------------------
# # Тест 1 — создание графа
# # ---------------------------------------------------
#
# print("\n===== TEST 1: CREATE GRAPH =====\n")
#
# graph = Graph(
#     directed=True,
#     weighted=True
# )
#
# graph.add_vertex(1)
# graph.add_vertex(2)
# graph.add_vertex(3)
#
# graph.add_edge(1, 2, 5)
# graph.add_edge(2, 3, 10)
# graph.add_edge(1, 3, 7)
#
# graph.print_graph()
#
# graph.print_switching_graph()
#
# print("\nVertices:", graph.number_of_vertices())
# print("Edges:", graph.number_of_edges())
#
# print("\nVALID:", graph.validate_graph())
#
#
# # ---------------------------------------------------
# # Тест 2 — sparse graph
# # ---------------------------------------------------
#
# print("\n===== TEST 2: SPARSE GRAPH =====\n")
#
# sparse_graph = generate_sparse_graph(
#     vertices=10,
#     weighted=True
# )
#
# sparse_graph.print_graph()
#
# print("\nVertices:", sparse_graph.number_of_vertices())
# print("Edges:", sparse_graph.number_of_edges())
#
# print("\nVALID:", sparse_graph.validate_graph())
#
#
# # ---------------------------------------------------
# # Тест 3 — dense graph
# # ---------------------------------------------------
#
# print("\n===== TEST 3: DENSE GRAPH =====\n")
#
# dense_graph = generate_dense_graph(
#     vertices=5,
#     weighted=True
# )
#
# dense_graph.print_graph()
#
# print("\nVertices:", dense_graph.number_of_vertices())
# print("Edges:", dense_graph.number_of_edges())
#
# print("\nVALID:", dense_graph.validate_graph())
#
#
# # ---------------------------------------------------
# # Тест 4 — get_neighbors
# # ---------------------------------------------------
#
# print("\n===== TEST 4: GET NEIGHBORS =====\n")
#
# neighbors = graph.get_neighbors(1)
#
# print("Neighbors of 1:")
# print(neighbors)
#
#
# # ---------------------------------------------------
# # Тест 5 — switching graph
# # ---------------------------------------------------
#
# print("\n===== TEST 5: SWITCHING GRAPH =====\n")
#
# graph.print_switching_graph()