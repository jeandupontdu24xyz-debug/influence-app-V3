import streamlit as st

st.set_page_config(page_title="SAC-Explorer", layout="wide")

st.title("SAC-Explorer - Système Anthropo-Cybernétique")
st.write("""
Bienvenue dans SAC-Explorer, outil interactif pour visualiser les concepts, actions et effets 
de la guerre cognitive et de l’influence stratégique.
""")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choisissez une page", ["Graphe", "Concepts", "Exemples"])

if page == "Graphe":
    st.write("➡️ Veuillez cliquer dans la barre de gauche sur 'Graphe' ou accéder à la page Graphe.")
elif page == "Concepts":
    st.write("➡️ Veuillez cliquer dans la barre de gauche sur 'Concepts' ou accéder à la page Concepts.")
elif page == "Exemples":
    st.write("➡️ Veuillez cliquer dans la barre de gauche sur 'Exemples' ou accéder à la page Exemples.")
