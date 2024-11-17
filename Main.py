import streamlit as st
import pandas as pd

# Konfigurasi Halaman (Hanya di file utama)
st.set_page_config(
    page_title="Dashboard Data Pangan",
    page_icon="🍚",
    layout="wide",
)

# Inisialisasi session_state
if "rumah_tangga_total" not in st.session_state:
    st.session_state["rumah_tangga_total"] = 0

if "kemandirian_tinggi" not in st.session_state:
    st.session_state["kemandirian_tinggi"] = 0

if "data_terbaru" not in st.session_state:
    st.session_state["data_terbaru"] = "Belum Ada Data"

# Sidebar Navigasi
st.sidebar.title("📂 Menu Navigasi")
PAGES = ["🏠 Home", "📊 Data Rumah Tangga", "🍛 Kemandirian Pangan RT", "🌾 Kemandirian Pangan Dusun"]
selected_page = st.sidebar.radio("", PAGES)

# Halaman Home
if selected_page == "🏠 Home":
    st.title("📊 Dashboard Data Pangan")
    st.markdown(
        """
        Selamat datang di **Dashboard Data Pangan**!  
        Dashboard ini menampilkan visualisasi interaktif dari:
        - **Data rumah tangga**
        - **Data kemandirian pangan per rumah tangga**
        - **Data kemandirian pangan per dusun**
        """
    )

    st.subheader("🔍 Statistik Utama")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Total Rumah Tangga",
            value=f"{st.session_state['rumah_tangga_total']} keluarga",
        )
    with col2:
        st.metric(
            label="Kemandirian Tinggi",
            value=f"{st.session_state['kemandirian_tinggi']}%",
        )
    with col3:
        st.metric(
            label="Data Terbaru",
            value=f"{st.session_state['data_terbaru']}",
        )

# Halaman Data Rumah Tangga
elif selected_page == "📊 Data Rumah Tangga":
    st.title("📊 Data Rumah Tangga")
    uploaded_file = st.file_uploader("Unggah file data rumah tangga (CSV):", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)
        st.session_state["rumah_tangga_total"] = len(data)
        st.success(f"Total rumah tangga diperbarui: {len(data)} keluarga.")
    else:
        st.info("Silakan unggah file.")

# Halaman Kemandirian Pangan RT
elif selected_page == "🍛 Kemandirian Pangan RT":
    st.title("🍛 Kemandirian Pangan Rumah Tangga")
    uploaded_file = st.file_uploader("Unggah file data kemandirian pangan RT (CSV):", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)
        if "Kemandirian (%)" in data.columns:
            kemandirian_tinggi = data["Kemandirian (%)"].mean()
            st.session_state["kemandirian_tinggi"] = round(kemandirian_tinggi, 2)
            st.success(f"Kemandirian tinggi diperbarui: {round(kemandirian_tinggi, 2)}%.")
        else:
            st.warning("Kolom 'Kemandirian (%)' tidak ditemukan.")
    else:
        st.info("Silakan unggah file.")

# Halaman Kemandirian Pangan Dusun
elif selected_page == "🌾 Kemandirian Pangan Desa":
    st.title("🌾 Kemandirian Pangan Dusun")
    uploaded_file = st.file_uploader("Unggah file data kemandirian pangan dusun (CSV):", type=["csv"])
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write(data)
        if "Tahun" in data.columns:
            data_terbaru = data["Tahun"].max()
            st.session_state["data_terbaru"] = str(data_terbaru)
            st.success(f"Data terbaru diperbarui: {data_terbaru}.")
        else:
            st.warning("Kolom 'Tahun' tidak ditemukan.")
    else:
        st.info("Silakan unggah file.")
