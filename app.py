
import streamlit as st

st.set_page_config(page_title="Jeu de déduction magique", page_icon="🔮")

st.title("🔮 Jeu de déduction magique")

# Initialisation de l'étape
if "etape" not in st.session_state:
    st.session_state.etape = 1

# Étape 1 : Demander le nom
if st.session_state.etape == 1:
    nom = st.text_input("Quel est votre nom ?")
    if nom:
        st.session_state.nom = nom
        st.session_state.etape = 2
        st.experimental_rerun()

# Étape 2 : Choix du nombre
elif st.session_state.etape == 2:
    st.write(f"Bonjour {st.session_state.nom} 👋")
    st.write("Imaginez que vous avez choisi un *nombre entier non nul*.")
    st.write("Ne me le dites pas, gardez ce nombre secret dans votre tête.")
    if st.button("✅ J'ai choisi un nombre dans ma tête"):
        st.session_state.etape = 3
        st.experimental_rerun()

# Étape 3 : Addition
elif st.session_state.etape == 3:
    st.write("Additionnez ce nombre avec lui-même.")
    if st.button("✅ J'ai effectué l'addition"):
        st.session_state.etape = 4
        st.experimental_rerun()

# Étape 4 : Multiplication
elif st.session_state.etape == 4:
    st.write("Multipliez maintenant le résultat par un nombre entre 1 et 10.")
    n = st.slider("Choisissez ce nombre :", 1, 10)
    st.session_state.n = n
    if st.button("✅ J'ai effectué la multiplication"):
        st.session_state.etape = 5
        st.experimental_rerun()

# Étape 5 : Division
elif st.session_state.etape == 5:
    st.write("Divisez maintenant le résultat par le nombre que vous aviez choisi au début.")
    if st.button("✅ J'ai effectué la division"):
        st.session_state.etape = 6
        st.experimental_rerun()

# Étape 6 : Révélation
elif st.session_state.etape == 6:
    resultat = st.session_state.n * 2
    st.success(f"Je devine que le résultat est : *{resultat}* 🎯")
