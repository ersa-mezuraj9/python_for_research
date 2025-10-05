import networkx as nx

G = nx.Graph()
G.add_node(1)
G.add_nodes_from([2,3])
G.add_nodes_from(["u","v"])
print(G.nodes())
G.add_edge(1,2)
G.add_edge("u","v")
G.add_edges_from([(1,3), (1,4), (1,5), (1,6)])
G.add_edge("u", "w")
print(G.edges())
G.remove_nodes_from([2,4,5])
G.remove_edges_from([(1,2),("u","w"),(1,3)])
G.number_of_edges()
G.number_of_nodes()

g = nx.karate_club_graph()

import matplotlib.pyplot as plt
nx.draw(g, with_labels=True, node_color="lightblue", edge_color="grey")
plt.show()
g.degree()
g.degree()[33]

print(g.degree(33) is g.degree()[33]) # True

# Implementing an ER model as Python function
from scipy.stats import bernoulli
bernoulli.rvs(p=0.2) # p represents the probability of success

def er_graph(N, p): 
    """ Generate an ER graph """
    # create empty graph
    G = nx.Graph()
    # add all N nodes in the graph
    G.add_nodes_from(range(N))
    # loop over all pairs of nodes
    for node1 in G.nodes():
        for node2 in G.nodes():
        # add an edge with probability p
            if node1 < node2 and bernoulli.rvs(p=p):
                G.add_edge(node1, node2)
    return G

nx.draw(er_graph(50, 0.8), node_size=40, node_color="gray")
plt.show()

def plot_degree_distribution(G):
    degree_sequence = [d for n, d in G.degree()]
    plt.hist(degree_sequence, histtype="step")
    plt.xlabel("Degree $k$")
    plt.ylabel("$P(k)$")
    plt.title("Degree distribution")
    

G1 = er_graph(500, 0.08)
plot_degree_distribution(G1)
G2 = er_graph(500, 0.08)
plot_degree_distribution(G2)
G3 = er_graph(500, 0.08)
plot_degree_distribution(G3)
plt.show()

import numpy as np
A1 = np.loadtxt("C:/Users/User/OneDrive/Desktop/python_for_research/data/adj_allVillageRelationships_vilno_1.csv", delimiter=",")
A2 = np.loadtxt("C:/Users/User/OneDrive/Desktop/python_for_research/data/adj_allVillageRelationships_vilno_2.csv", delimiter=",")

G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

def basic_net_stats(G):
    print("Number of nodes: %d" % G.number_of_nodes())
    print("Number of edges: %d" % G.number_of_edges())
    degree_sequence = [d for n, d in G.degree()]
    print("Average degree: %.2f" % np.mean(degree_sequence))

basic_net_stats(G1)
basic_net_stats(G2)

plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.show()

components = nx.connected_components(G1)
largest_component = max(components, key=len)
print(len(largest_component) / G1.number_of_nodes()) # percentage of nodes connected to the largest component
g1 = G1.subgraph(largest_component).copy()
nx.draw(g1, node_color="red", edge_color="gray", node_size=20)
plt.show()

components = nx.connected_components(G2)
largest_component = max(components, key=len)
print(len(largest_component) / G2.number_of_nodes())
g2 = G2.subgraph(largest_component).copy()
nx.draw(g2, node_color="green", edge_color="gray", node_size=20)
plt.show()