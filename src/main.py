import tkinter as tk
from tkinter import filedialog, messagebox
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import random
import os

canvas = None
pos = None
file_label = None
G = None
num_clusters = 1

def open_file():
    global file_label, G

    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            process_content(content)
            visualize_graph()

        # Update file label
        file_name = os.path.basename(file_path)
        file_label.config(text="File: " + file_name)

def add_node():
    global G
    
    node_name = node_entry.get()
    neighbors = neighbor_entry.get()
    weights = weight_entry.get()

    try:
        neighbors = [int(x) for x in neighbors.strip().split()]
        weights = [int(x) for x in weights.strip().split()]
    except ValueError:
        messagebox.showerror("Error", "Invalid input.")
        return

    if len(neighbors) != len(weights):
        messagebox.showerror("Error", "Number of neighbors must match the number of weights.")
        return

    G.add_node(node_name)
    for neighbor, weight in zip(neighbors, weights):
        G.add_edge(node_name, neighbor, weight=weight)

    visualize_graph()

def remove_node():
    global G
    
    try:
        node_index = int(remove_node_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input.")
        return

    if G.has_node(node_index):
        G.remove_node(node_index)
        visualize_graph()
    else:
        messagebox.showerror("Error", "Node does not exist.")

def solve():
    global canvas, G, num_clusters

    algorithm = algorithm_var.get()

    if algorithm == "Kruskal":
        minimum_spanning_tree = nx.minimum_spanning_tree(G)
    elif algorithm == "Prim":
        minimum_spanning_tree = nx.minimum_spanning_tree(G, algorithm="prim")
    else:
        messagebox.showerror("Error", "Invalid algorithm selected.")
        return

    if num_clusters is None:
        messagebox.showerror("Error", "Number of clusters is not set.")
        return

    clusters = perform_mst_clustering(G, num_clusters)

    if canvas is not None:
        canvas.get_tk_widget().destroy()

    fig, ax = plt.subplots(figsize=(8, 6))

    nx.draw_networkx(G, pos=pos, with_labels=True, node_color='lightblue', node_size=500, ax=ax)
    nx.draw_networkx_edges(minimum_spanning_tree, pos=pos, edge_color='red', width=2, ax=ax)

    # Color nodes based on clusters
    cluster_colors = get_cluster_colors(num_clusters)
    for cluster, color in zip(clusters.values(), cluster_colors):
        nx.draw_networkx_nodes(G, pos=pos, nodelist=cluster, node_color=color, node_size=500, ax=ax)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, ax=ax)
    ax.set_title("Minimum Spanning Tree Clustering")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


def perform_mst_clustering(graph, num_clusters):
    clusters = {}

    mst = nx.minimum_spanning_tree(graph)

    sorted_edges = sorted(mst.edges(data=True), key=lambda x: x[2]['weight'])

    for node in graph.nodes:
        clusters[node] = [node]

    for edge in sorted_edges:
        u, v, weight = edge

        if len(clusters) <= num_clusters:
            break

        if any(u in cluster and v in cluster for cluster in clusters.values()):
            continue

        for cluster in clusters.values():
            if u in cluster:
                if v not in cluster:
                    cluster.extend(clusters[v])
                    del clusters[v]
                break

    return clusters



def get_cluster_colors(num_clusters):
    colors = []
    for _ in range(num_clusters):
        color = '#' + ''.join(random.choices('0123456789ABCDEF', k=6))
        colors.append(color)
    return colors

def visualize_graph():
    global canvas, pos, G

    if canvas is not None:
        canvas.get_tk_widget().destroy()

    pos = nx.spring_layout(G)

    fig, ax = plt.subplots(figsize=(8, 6))

    nx.draw_networkx(G, pos=pos, with_labels=True, node_color='lightblue', node_size=500, ax=ax)
    ax.set_title("Graph")
    ax.axis("off")

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


def process_content(content):
    global G

    lines = content.strip().split("\n")
    adjacency_matrix = []
    for line in lines:
        row = [int(x) for x in line.strip().split()]
        adjacency_matrix.append(row)

    G = nx.Graph()
    num_nodes = len(adjacency_matrix)
    for i in range(num_nodes):
        G.add_node(i + 1)

    for i in range(num_nodes):
        for j in range(i+1, num_nodes):
            weight = adjacency_matrix[i][j]
            if weight != 0:
                G.add_edge(i + 1, j + 1, weight=weight)

def set_clusters():
    global num_clusters
    try:
        num_clusters = int(cluster_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input.")
        return

window = tk.Tk()
window.title("Minimum Spanning Tree Visualizer")
window.configure(bg='black')

frame = tk.Frame(window, width=600, height=500, highlightbackground='blue', highlightthickness=1)
frame.grid(row=0, column=1, rowspan=10, padx=10, pady=10, sticky="nsew")

solve_button = tk.Button(window, text="Solve", command=solve, bg='lightblue', fg='black')
solve_button.grid(row=4, column=0, padx=10, pady=10, sticky="w")

algorithm_var = tk.StringVar()
algorithm_var.set("Kruskal")

algorithm_label = tk.Label(window, text="Select Algorithm:", bg='black', fg='white')
algorithm_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

algorithm_menu = tk.OptionMenu(window, algorithm_var, "Kruskal", "Prim")
algorithm_menu.configure(bg='lightblue')
algorithm_menu.grid(row=3, column=0, padx=10, pady=10, sticky="w")

open_button = tk.Button(window, text="Open File", command=open_file, bg='lightblue', fg='black')
open_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

file_label = tk.Label(window, text="File:", bg='black', fg='white')
file_label.grid(row=1, column=0, padx=10, pady=0, sticky="w")

node_label = tk.Label(window, text="Add Node:", bg='black', fg='white')
node_label.grid(row=0, column=2, padx=10, pady=10, sticky="w")

node_entry = tk.Entry(window)
node_entry.grid(row=0, column=3, padx=10, pady=10, sticky="w")

neighbor_label = tk.Label(window, text="Neighbors:", bg='black', fg='white')
neighbor_label.grid(row=1, column=2, padx=10, pady=10, sticky="w")

neighbor_entry = tk.Entry(window)
neighbor_entry.grid(row=1, column=3, padx=10, pady=10, sticky="w")

weight_label = tk.Label(window, text="Weights:", bg='black', fg='white')
weight_label.grid(row=2, column=2, padx=10, pady=10, sticky="w")

weight_entry = tk.Entry(window)
weight_entry.grid(row=2, column=3, padx=10, pady=10, sticky="w")

add_button = tk.Button(window, text="Add Node", command=add_node, bg='lightblue', fg='black')
add_button.grid(row=3, column=2, padx=10, pady=10, sticky="w")

remove_node_label = tk.Label(window, text="Remove Node:", bg='black', fg='white')
remove_node_label.grid(row=4, column=2, padx=10, pady=10, sticky="w")

remove_node_entry = tk.Entry(window)
remove_node_entry.grid(row=4, column=3, padx=10, pady=10, sticky="w")

remove_button = tk.Button(window, text="Remove Node", command=remove_node, bg='lightblue', fg='black')
remove_button.grid(row=5, column=2, padx=10, pady=10, sticky="w")

cluster_label = tk.Label(window, text="Number of Clusters:", bg='black', fg='white')
cluster_label.grid(row=6, column=2, padx=10, pady=10, sticky="w")

cluster_entry = tk.Entry(window)
cluster_entry.grid(row=6, column=3, padx=10, pady=10, sticky="w")

cluster_button = tk.Button(window, text="Set Clusters", command=set_clusters, bg='lightblue', fg='black')
cluster_button.grid(row=7, column=2, padx=10, pady=10, sticky="w")

window.iconphoto(True, tk.PhotoImage(file="src/icon.png"))
window.resizable(width=False, height=False)
window.mainloop()
