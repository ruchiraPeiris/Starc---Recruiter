from pyvis.network import Network
import networkx as nx
import pickle

nxg = nx.complete_graph(10)
skill_graph = nx.DiGraph(pickle.load(open('../saved_objects/combined_graph.p', 'rb')))
G = Network(height='100%', width='100%')
G.barnes_hut()
G.from_nx(skill_graph)
G.show_buttons(filter_=['physics'])

G.show("mygraph.html")