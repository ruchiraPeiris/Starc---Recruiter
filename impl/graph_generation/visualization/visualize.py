from pyvis.network import Network
import pandas as pd

net = Network()
got_net = Network(height="750px", width="100%", bgcolor="#000000", font_color="white")
got_net.show_buttons(filter_=['physics'])
# set the physics layout of the network
got_net.barnes_hut()
got_data = pd.read_csv('C:/Users/pc/Downloads/stack_network_links.csv')

df_nodes = pd.read_csv('C:/Users/pc/Downloads/stack_network_nodes.csv')
df_edges = pd.read_csv('C:/Users/pc/Downloads/stack_network_links.csv')


sources = got_data['source']
targets = got_data['target']
weights = got_data['value']

edge_data = zip(sources, targets, weights)

for e in edge_data:
    src = e[0]
    dst = e[1]
    w = e[2]

    got_net.add_node(src, src, title=src)
    got_net.add_node(dst, dst, title=dst)
    got_net.add_edge(src, dst, value=w)

neighbor_map = got_net.get_adj_list()

# add neighbor data to node hover data
for node in got_net.nodes:
    node["title"] += " Neighbors:<br>" + "<br>".join(neighbor_map[node["id"]])
    node["value"] = len(neighbor_map[node["id"]])

got_net.show("gameofthrones.html")