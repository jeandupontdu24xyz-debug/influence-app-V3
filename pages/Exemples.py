import streamlit as st
import json

st.set_page_config(page_title="Exemples - SAC-Explorer", layout="wide")
st.title("Exemples opérationnels")

with open("data.json") as f:
    data = json.load(f)

exemples = [node['id'] for node in data['nodes'] if node.get('type') == 'exemple']
st.write("Exemples de campagnes et opérations :")
for ex in exemples:
    st.markdown(f"- {ex}")
