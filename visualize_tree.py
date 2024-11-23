import torch
import networkx as nx
import matplotlib.pyplot as plt

# Load graph data
graph_data = torch.load("demo_tree.pt")
successors = graph_data["Successors"]

# Convert Successors to edge tuples
edges = [
    (parent, child)
    for parent, children in enumerate(successors)
    for child in children
]

# Create a directed graph
graph = nx.DiGraph()
graph.add_edges_from(edges)

# Use a hierarchical layout for visualization
pos = nx.nx_agraph.graphviz_layout(graph, prog="dot")  # Use 'dot' for hierarchical layout

# Plot the graph
plt.figure(figsize=(10, 8))
nx.draw(graph, pos, with_labels=True, node_color="lightblue", node_size=1500, font_size=10)
plt.title("Graph from .pt File with Hierarchical Layout")
plt.savefig("tree.png", format="png", dpi=300)  # Save as PNG with high resolution
plt.close()

print("Graph saved as tree.png")
