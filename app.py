import streamlit as st
import json
from pyvis.network import Network
import networkx as nx
import tempfile

# --- Chargement des données ---
with open("data.json") as f:
    data = json.load(f)

nodes = data['nodes']
links = data['links']

# --- Création du graphe NetworkX ---
G = nx.DiGraph()
for node in nodes:
    G.add_node(node['id'], label=node['id'], type=node.get('type', ''), champ=node.get('champ', ''))

for link in links:
    G.add_edge(link['source'], link['target'], relation=link['relation'])

# --- Création du graphe PyVis ---
nt = Network(height="600px", width="100%", directed=True)
nt.from_nx(G)

# Ajouter des labels pour les arêtes
for edge in nt.edges:
    edge['title'] = G.edges[edge['from'], edge['to']]['relation']

# Style nodes selon type
color_map = {
    "concept": "lightblue",
    "action": "orange",
    "EFR": "green",
    "outil": "purple",
    "exemple": "red",
    "doctrine": "yellow"
}

for node in nt.nodes:
    ntype = G.nodes[node['id']].get('type', '')
    node['color'] = color_map.get(ntype, "grey")

# --- Affichage avec Streamlit ---
st.title("SAC-Explorer - Système Anthropo-Cybernétique")
st.write("Graphe interactif des concepts, actions et effets de la guerre cognitive et de l’influence stratégique.")

# PyVis + Streamlit workaround
with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp_file:
    path = tmp_file.name
    nt.save_graph(path)
    st.components.v1.html(open(path, 'r', encoding='utf-8').read(), height=650)
