# pip install streamlit
# streamlit hello
# streamlit run .\Streamlit_demo.py

import streamlit as st

# Inicjalizacja sesji
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        "Nauka Pythona",
        "Nauka Streamlit",
        "Tworzenie aplikacji webowych",
    ]
if "done" not in st.session_state:
    st.session_state.done = []

st.title("✅ Lista zadań")

st.subheader("🔧 Do zrobienia")

# Wprowadzanie nowego zadania
new_task = st.text_input("Nowe zadanie", placeholder="Dodaj nowe zadanie")
if st.button("Dodaj"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.rerun()

# Pętla po zadaniach
for task in st.session_state.tasks.copy():
    if st.checkbox(task, key=task):
        st.session_state.tasks.remove(task)
        st.session_state.done.append(task)
        st.rerun()

# Sekcja zrealizowanych
if st.session_state.done:
    st.subheader("🎉 Zrealizowane")
    for task in st.session_state.done:
        st.markdown(f"- ~~{task}~~")
