# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "networkx",
# ]
# ///

(edges := [ (line.split(":")[0], dest) for line in open(0).read().splitlines() for dest in line.split(":")[1].strip().split(" ") ], G := __import__("networkx").DiGraph(), G.add_edges_from(edges), print(len(list(__import__("networkx").all_simple_paths(G, "you", "out")))))


# (
#     edges := [ (line.split(":")[0], dest) for line in open(0).read().splitlines() for dest in line.split(":")[1].strip().split(" ") ],
#     G := __import__("networkx").DiGraph(),
#     G.add_edges_from(edges),
#     print(len(list(__import__("networkx").all_simple_paths(G, "you", "out"))))
# )


# import networkx as nx
#
# edges = [ (line.split(":")[0], dest) for line in open(0).read().splitlines() for dest in line.split(":")[1].strip().split(" ") ]
#
# G = nx.DiGraph()
# G.add_edges_from(edges)
# print(len(list(nx.all_simple_paths(G, "you", "out"))))
