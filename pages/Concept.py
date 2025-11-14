import streamlit as st
import json

st.set_page_config(page_title="Concepts - SAC-Explorer", layout="wide")
st.title("Lexique des Concepts")

with open("data.json") as f:
    data = json.load(f)

st.write("Liste des concepts, actions, outils, doctrines et EFR :")
for node in data['nodes']:
    st.markdown(f"- **{node['id']}** | Type: {node.get('type','')} | Champ: {node.get('champ','')}")
