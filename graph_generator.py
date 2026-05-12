import random
from graph import Graph


# разреженный граф
def generate_sparse_graph(
        vertices,
        weighted=False,
        directed=True
):
    graph = Graph(
        directed=directed,
        weighted=weighted
    )

    edges = vertices

    used_edges = set()

    while len(used_edges) < edges:

        source = random.randint(0, vertices - 1)
        destination = random.randint(0, vertices - 1)

        # без петель
        if source == destination:
            continue

        # без дубликатов
        if (source, destination) in used_edges:
            continue

        used_edges.add((source, destination))

        weight = 1

        if weighted:
            weight = random.randint(1, 20)

        graph.add_edge(source, destination, weight)

    return graph



# плотный граф


def generate_dense_graph(
        vertices,
        weighted=False,
        directed=True
):
    graph = Graph(
        directed=directed,
        weighted=weighted
    )

    for source in range(vertices):

        for destination in range(vertices):

            # без петель
            if source == destination:
                continue

            weight = 1

            if weighted:
                weight = random.randint(1, 20)

            graph.add_edge(source, destination, weight)

    return graph

def test_sparse_graph():

    graph = generate_sparse_graph(
        vertices=10,
        weighted=True
    )

    print("\nSPARSE GRAPH\n")

    graph.print_graph()

    print("\nVALID:", graph.validate_graph())

    print("Vertices:", graph.number_of_vertices())
    print("Edges:", graph.number_of_edges())


def test_dense_graph():

    graph = generate_dense_graph(
        vertices=5,
        weighted=True
    )

    print("\nDENSE GRAPH\n")

    graph.print_graph()

    print("\nVALID:", graph.validate_graph())

    print("Vertices:", graph.number_of_vertices())
    print("Edges:", graph.number_of_edges())


# def generate_test_graphs():
#
#     sizes = [100, 1000, 5000]
#
#     graphs = []
#
#     for size in sizes:
#
#         sparse = generate_sparse_graph(
#             vertices=size,
#             weighted=True
#         )
#
#         dense = generate_dense_graph(
#             vertices=min(size, 200),
#             weighted=True
#         )
#
#         graphs.append((sparse, dense))
#
#         print(f"\nGenerated graphs for size {size}")
#
#     return graphs
