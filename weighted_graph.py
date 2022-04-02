import networkx as nx
import matplotlib.pyplot as plt

file = "edges.txt"
G = nx.Graph()
G = nx.read_edgelist(file, nodetype = str, data = (("weight", int),))
Gc = sorted(nx.connected_components(G), key=len, reverse=True)
Gl = G.subgraph(Gc[0])

# minimum spanning tree
mst = nx.minimum_spanning_tree(Gl)
nx.draw_planar(mst, with_labels = True, font_size = 8, node_color = "#F0E68C")
plt.show()

# centroid
centroid = nx.barycenter(mst)
print("Centroid: ", centroid)
print("")

# prufer code
nmst = nx.convert_node_labels_to_integers(mst)
nx.draw_planar(nmst, with_labels = True, font_size = 8, node_color = "#F0E68C")
plt.show()
pruferCode = nx.to_prufer_sequence(nmst)
print("Prufer code: ", pruferCode)