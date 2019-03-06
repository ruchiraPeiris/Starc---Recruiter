import csv
from decimal import  Decimal
import matplotlib.pyplot as plt
import networkx as nx
import pickle

global_graph = nx.DiGraph()


def generate_graph_for_file(filename):
    global global_graph

    with open('outputs/'+filename) as csvfile:
        G = nx.DiGraph()

        for line in csvfile:
            print(line)
            row = line.split(',')
            skill_a = str(row[0]).strip()
            skill_b = str(row[1]).strip()
            weight = 1 - Decimal(row[2].strip())
            G.add_node(skill_a)
            G.add_node(skill_b)
            G.add_edge(skill_a, skill_b, weight=weight)

            # print(skill_a, skill_b, weight)

        # nx.draw()

        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
        esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]

        pos = nx.spring_layout(G)  # positions for all nodes
        # nodes
        nx.draw_networkx_nodes(G, pos, node_size=700)

        # edges
        nx.draw_networkx_edges(G, pos, edgelist=elarge,
                               width=6)
        nx.draw_networkx_edges(G, pos, edgelist=esmall,
                               width=6, alpha=0.5, edge_color='b', style='dashed')

        # label

        nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

        # for drawing networkx graph
        # plt.axis('off')
        # plt.savefig('weighted_graph_'+ filename + '.png')  # save as png
        # plt.show()  # display
        pickle.dump(G, open('saved_objects/'+filename[:-4] + '.p', 'wb'))

        global_graph = nx.compose(G, global_graph)

        print(filename + ' complete')


if __name__ == '__main__':
    files = ['programming_frameworks', 'database', 'frameworks', 'platforms', 'version_control', 'ide']
    for filename in files:
        print('Generating for ' + filename)
        generate_graph_for_file(filename + '.txt')

    pickle.dump(global_graph, open('saved_objects/combined_graph.p', 'wb'))

