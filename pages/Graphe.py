import streamlit as st
import json
from pyvis.network import Network
import networkx as nx
import tempfile

st.set_page_config(page_title="Graphe - SAC-Explorer", layout="wide")
st.title("Graphe interactif")

# Charger les données
with open("data.json") as f:
    data = json.load(f)

nodes = data['nodes']
links = data['links']

G = nx.DiGraph()
for node in nodes:
    G.add_node(node['id'], label=node['id'], type=node.get('type',''), champ=node.get('champ',''))

for link in links:
    G.add_edge(link['source'], link['target'], relation=link['relation'])

# PyVis
nt = Network(height="700px", width="100%", directed=True)
nt.from_nx(G)

for edge in nt.edges:
    edge['title'] = G.edges[edge['from'], edge['to']]['relation']

color_map = {
    "concept": "lightblue",
    "action": "orange",
    "EFR": "green",
    "outil": "purple",
    "exemple": "red",
    "doctrine": "yellow"
}

for node in nt.nodes:
    ntype = G.nodes[node['id']].get('type','')
    node['color'] = color_map.get(ntype, "grey")

with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp_file:
    path = tmp_file.name
    nt.save_graph(path)
    st.components.v1.html(open(path, 'r', encoding='utf-8').read(), height=700)
