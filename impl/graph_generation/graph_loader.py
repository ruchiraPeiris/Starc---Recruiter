import pickle
import networkx as nx
import os
from itertools import islice

G = {}


def similarity(category, a, b):
    try:
        return 1 - nx.dijkstra_path_length(G[category], a, b)
    except nx.NetworkXNoPath:
        return 0


if __name__ == '__main__':
    print(os.listdir('saved_objects/'))
    files = ['programming_frameworks', 'database', 'platforms', 'version_control', 'ide', 'combined_graph']
    for filename in files:
        G[filename] = nx.DiGraph(pickle.load(open("saved_objects/"+filename+".p", "rb")))

    print(similarity('combined_graph', 'java', 'python'))


