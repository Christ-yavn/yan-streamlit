import streamlit as st

st.set_page_config(page_title="Jeu de déduction magique", page_icon="🔮")

st.title("🔮 Jeu de déduction magique")

# Initialisation des variables
if "etape" not in st.session_state:
    st.session_state.etape = 1
if "nom" not in st.session_state:
    st.session_state.nom = ""
if "n" not in st.session_state:
    st.session_state.n = 2

# Étape 1 : salutation + nom
if st.session_state.etape == 1:
    st.write("Bonjour Mr/Mme. Heureux de vous rencontrer !")
    st.session_state.nom = st.text_input("Quel est votre nom ?")
    if st.session_state.nom and st.button("Continuer"):
        st.session_state.etape = 2

# Étape 2 : choix du nombre
elif st.session_state.etape == 2:
    st.write(f"Bonjour {st.session_state.nom} 👋")
    st.write("Imaginez que vous avez choisi un *nombre entier non nul*.")
    st.write("Ne me le dites pas, gardez ce nombre secret dans votre tête.")
    if st.button("✅ J'ai choisi un nombre dans ma tête"):
        st.session_state.etape = 3

# Étape 3 : addition
elif st.session_state.etape == 3:
    st.write("Additionnez ce nombre avec lui-même.")
    if st.button("✅ J'ai effectué l'addition"):
        st.session_state.etape = 4

# Étape 4 : multiplication
elif st.session_state.etape == 4:
    st.write("Multipliez maintenant le résultat de l'addition par un nombre entier entre 1 et 10.")
    st.session_state.n = st.slider("Choisissez ce nombre :", 1, 10)
    if st.button("✅ J'ai effectué la multiplication"):
        st.session_state.etape = 5

# Étape 5 : division
elif st.session_state.etape == 5:
    st.write("Divisez maintenant le résultat obtenu par le nombre que vous aviez choisi au début.")
    if st.button("✅ J'ai effectué la division"):
        st.session_state.etape = 6

# Étape 6 : révélation
elif st.session_state.etape == 6:
    nombre_devine = st.session_state.n * 2
    st.success(f"Je devine que le résultat est : *{nombre_devine}* 🎯")
