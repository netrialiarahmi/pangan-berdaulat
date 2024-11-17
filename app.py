import streamlit as st

# Konfigurasi Halaman (Hanya di file utama)
st.set_page_config(
    page_title="Dashboard Data Pangan",
    page_icon="🍚",
    layout="wide",
)

# Sidebar Header
st.sidebar.header("📂 Menu")

# Konten Halaman Utama
st.title("📊 Dashboard Data Pangan")
st.markdown("""
Selamat datang di **Dashboard Data Pangan**!  
Dashboard ini menampilkan visualisasi interaktif dari:
- **Data rumah tangga**  
- **Data kemandirian pangan per rumah tangga**  
- **Data kemandirian pangan per dusun**  

Silakan pilih halaman dari menu di sidebar sebelah kiri.
""")

# Footer
st.markdown(
    """
    <hr>
    <div style='text-align: center;'>
        <small>© 2024 Dashboard Data Pangan. All rights reserved.</small>
    </div>
    """,
    unsafe_allow_html=True
)
