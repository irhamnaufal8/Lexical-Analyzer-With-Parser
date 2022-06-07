import streamlit as st

st.write("""
# Lexical Analyzer | Kelompok 6
Aplikasi yang mengecek susunan grammar bahasa sederhana
""")

kata1 = st.text_input("Masukkan Kata Pertama", "")
kata2 = st.text_input("Masukkan Kata Kedua", "")
kata3 = st.text_input("Masukkan Kata Ketiga", "")
valid = st.button("Cek Hasil")

if valid:
    st.success(f"Kalimat '" + kata1 + " " + kata2 + " " + kata3 + "' merupakan valid")
    st.balloons()
