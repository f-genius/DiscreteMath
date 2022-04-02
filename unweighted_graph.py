import networkx as nx
import matplotlib.pyplot as plt

# (а) Draw3 G* with the minimum number of intersecting edges
G = nx.read_adjlist("adj.txt", nodetype=str, delimiter = ',')
nx.draw_planar(G, with_labels = True, font_size = 8, node_color = "#F0E68C")
plt.show()

# (b) |V |, |E|, δ (G), Δ(G), rad(G), diam(G), girth(G), center(G)

Gc = sorted(nx.connected_components(G), key=len, reverse=True)
Gl = G.subgraph(Gc[0]) # the largest connected component 

print("nodes ", Gl.number_of_nodes()) # количество вершин
print("edges ", Gl.number_of_edges()) # количество ребер

print(Gl.edges())

# find δ (G), Δ(G)
minim = float("inf")
maxim = float("-inf")
for i in Gl:
    if (Gl.degree(i) < minim):
        minim = Gl.degree(i)
    if (Gl.degree(i) > maxim):
        maxim = Gl.degree(i)
print(minim, " ", maxim)


print("rad ", nx.radius(Gl))  # rad(G)
print("diam ", nx.diameter(Gl))  # diam(G)

# find girth 
minCycle = float("inf")
cycles = nx.minimum_cycle_basis(Gl)
for c in cycles:
    if (len(c) < minCycle):
        minCycle = len(c)
print("girth ", minCycle)  # girth

print("center ", nx.center(Gl))  # center(G)
print("")

# (c) Find the minimum vertex coloring Z
color = nx.greedy_color(Gl)
print("List of countries and colors: ")
for c in color:
    print(c, ' ', color[c])
print("")

# (е) Find the maximum clique Q
sizeClique = float("-inf")
cliques = list(nx.find_cliques(Gl))
for c in cliques:
    if (len(c) > sizeClique):
        sizeClique = len(c)
        maxClique = c

print("Size of the maximum cluque: ", sizeClique)
print("Vertices: ", maxClique)
print("")

# (f) Find the maximum stable set
maxStableSet = nx.algorithms.approximation.maximum_independent_set(Gl)
print("The maximum stable set: ")
print("Vertices: ", maxStableSet)
print("Size: ", len(maxStableSet))
print("")

# (g) Find the maximum matching M
maxim = nx.max_weight_matching(Gl)
print("The maximum matching: ")
print("Vertices: ", maxim)
print("Size: ", len(maxim))
print("")

# (h) Find the minimum vertex cover R
minim = nx.algorithms.approximation.min_weighted_vertex_cover(Gl)
print("The minimum vertex cover: ")
print("Vertices: ", minim)
print("Size: ", len(minim))
print("")

# (i) Find the minimum edge cover F
minim = nx.min_edge_cover(Gl)
print("The minimum edge cover: ")
print("Vertices: ", minim)
print("Size: ", len(minim))
print("")

# (j) find the shortest closed walk that visits every vertex of G.
shortestWalk = nx.approximation.traveling_salesman_problem(Gl)
print("The shortest vertice walk:")
print(shortestWalk)

# (k) find the shortest closed walk that visits every edge of G.
nGl = nx.convert_node_labels_to_integers(Gl)
print("Integer edges\n ", nGl.edges())

# (l) Find all biconnected components (blocks) and draw the block-cut tree of G
s = [G.subgraph(c).copy() for c in nx.biconnected_components(G)]
print("all biconnected components (blocks): ")
for i in s:
    print(i)
    nx.draw_planar(i, with_labels = True, font_size = 8, node_color = "#F0E68C")
    plt.show()

print("")

B = nx.Graph()
nodes = ["b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "c1", "c2", "c3", "c4", "c5"]
B.add_nodes_from(nodes)
B.add_edges_from([("b7", "c1"), ("c1", "b6"), ("b6", "c2"), ("c2", "b5"), ("c2", "b8"), ("b8", "c5"), ("c5", "b3"), ("c5", "b2"), ("b8", "c4"),
("c4", "b4"), ("b8", "c3"), ("c3", "b1")])

nx.draw(B, with_labels = True, node_color = "#F0E68C")
plt.show()

# (m) Find all 2-edge-connected components of G
connect = nx.k_edge_subgraphs(G, 2)
print("all 2-edge-connected components of G")
for i in connect:
    print(i)
print("")
