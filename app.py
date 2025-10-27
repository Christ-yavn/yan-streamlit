
import streamlit as st

st.title("🔮 Jeu de déduction magique")

st.write("Bonjour Mr/Mn. Heureux de vous rencontrer !")

nom = st.text_input("Quel est votre nom ?", "")
if nom:
    st.success(f"Bonjour {nom} 👋")

st.write("Imaginez que vous avez choisi un *nombre entier non nul*.")
st.write("Ne me le dites pas, gardez ce nombre secret dans votre tête.")

choix = st.radio("Avez-vous choisi un nombre dans votre tête ?", ["oui", "non"])
if choix == "non":
    st.warning("Prenez le temps de choisir un nombre, puis relancez l'application.")
    st.stop()

addition = st.radio("Avez-vous effectué l'addition (nombre + lui-même) ?", ["oui", "non"])
if addition == "non":
    st.warning("Faites l'addition mentalement, puis relancez.")
    st.stop()

n = st.slider("Choisissez un nombre entier entre 1 et 10 pour multiplier :", 1, 10)

multiplication = st.radio("Avez-vous effectué la multiplication ?", ["oui", "non"])
if multiplication == "non":
    st.warning("Faites la multiplication mentalement, puis relancez.")
    st.stop()

division = st.radio("Avez-vous effectué la division par le nombre initial ?", ["oui", "non"])
if division == "non":
    st.warning("Faites la division mentalement, puis relancez.")
    st.stop()

if st.button("🔍 Deviner le résultat"):
    resultat = n * 2
    st.success(f"Je devine que le résultat est : *{resultat}* 🎯")
