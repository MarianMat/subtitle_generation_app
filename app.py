import streamlit as st

st.set_page_config(page_title="Aplikacja Generowanie Napisów V1", page_icon="🎬")
st.title("🎬 Aplikacja Generowanie Napisów — V1")
st.subheader("V1 — przesłanie i wyświetlenie wideo")

uploaded_video = st.file_uploader(
    "Wybierz plik wideo",
    type=["mp4", "mov", "m4v", "webm", "avi"],
)

if uploaded_video:
    st.success(f"Załadowano: {uploaded_video.name}")
    st.video(uploaded_video)
    st.info("V1: użytkownik przesyła wideo, a aplikacja je wyświetla.")
else:
    st.write("Prześlij plik wideo, aby rozpocząć.")
