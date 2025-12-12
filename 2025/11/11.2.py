# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "networkx",
# ]
# ///

(edges := [ (line.split(":")[0], dest) for line in open(0).read().splitlines() for dest in line.split(":")[1].strip().split(" ") ], G := __import__("networkx").DiGraph(), G.add_edges_from(edges), topology := list(__import__("networkx").topological_sort(G)), paths_from := lambda node: (paths := {n: (1 if n == node else 0) for n in G}, [paths.__setitem__(v, paths[v] + paths[u]) for u in topology for v in G.successors(u)], paths)[-1], from_svr_to := paths_from("svr"), from_dac_to := paths_from("dac"), from_fft_to := paths_from("fft"), print(from_svr_to["dac"] * from_dac_to["fft"] * from_fft_to["out"] + from_svr_to["fft"] * from_fft_to["dac"] * from_dac_to["out"]))


# (
#     edges := [ (line.split(":")[0], dest) for line in open(0).read().splitlines() for dest in line.split(":")[1].strip().split(" ") ],
#     G := __import__("networkx").DiGraph(),
#     G.add_edges_from(edges),
#     topology := list(__import__("networkx").topological_sort(G)),
#     
#     paths_from := lambda node:
#         (
#             paths := {n: (1 if n == node else 0) for n in G},
#             [
#                 paths.__setitem__(v, paths[v] + paths[u])
#                 for u in topology
#                 for v in G.successors(u)
#             ],
#             paths
#         )[-1],
#     from_svr_to := paths_from("svr"),
#     from_dac_to := paths_from("dac"),
#     from_fft_to := paths_from("fft"),
#     print(
#         from_svr_to["dac"] * from_dac_to["fft"] * from_fft_to["out"]
#         + from_svr_to["fft"] * from_fft_to["dac"] * from_dac_to["out"]
#     )
# )


# import networkx as nx
#
# edges = [ (line.split(":")[0], dest) for line in open(0).read().splitlines() for dest in line.split(":")[1].strip().split(" ") ]
#
# G = nx.DiGraph()
# G.add_edges_from(edges)
#
# topology = list(nx.topological_sort(G))
#
# def paths_from(node):
#     paths = {n: (1 if n == node else 0) for n in G}
#     for u in topology:
#         for v in G.successors(u):
#             paths[v] += paths[u]
#     return paths
#
# from_svr_to = paths_from("svr")
# from_dac_to = paths_from("dac")
# from_fft_to = paths_from("fft")
#
# print(
#       from_svr_to["dac"] * from_dac_to["fft"] * from_fft_to["out"]
#     + from_svr_to["fft"] * from_fft_to["dac"] * from_dac_to["out"]
# )
