import streamlit as st
import pandas as pd
import plotly.express as px

# Konfigurasi Halaman
st.set_page_config(page_title="Dashboard Data Pangan", page_icon="📊", layout="wide")

# CSS Kustom untuk Styling
st.markdown(
    """
    <style>
    /* Global Style */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f8f9fa;
    }
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }

    /* Header Navigation */
    .nav-buttons {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-bottom: 20px;
    }
    .nav-buttons button {
        background-color: #007bff;
        color: white;
        padding: 0.5rem 1rem;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }
    .nav-buttons button:hover {
        background-color: #0056b3;
    }

    /* Metric Cards */
    .metric-container {
        display: flex;
        justify-content: space-between;
        gap: 15px;
        margin: 20px 0;
    }
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        flex: 1;
        text-align: center;
    }
    .metric-title {
        font-size: 18px;
        font-weight: bold;
        color: #007bff;
    }
    .metric-value {
        font-size: 28px;
        font-weight: bold;
        color: #333;
    }
    .metric-subtitle {
        font-size: 14px;
        color: #777;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Navigasi Halaman
PAGES = ["🏠 Home", "📊 Data Rumah Tangga", "🍛 Kemandirian Pangan RT", "🌾 Kemandirian Pangan Dusun"]
selected_page = st.sidebar.radio("📂 Menu Navigasi", PAGES)

# Halaman Utama
if selected_page == "🏠 Home":
    st.title("📊 Dashboard Data Pangan")
    st.markdown(
        """
        Selamat datang di **Dashboard Data Pangan**!  
        Dashboard ini menampilkan visualisasi interaktif dari:
        - **Data rumah tangga**
        - **Data kemandirian pangan per rumah tangga**
        - **Data kemandirian pangan per dusun**
        
        Silakan pilih halaman dari menu navigasi di sidebar.
        """
    )

    # Metric Dashboard
    st.markdown("<div class='metric-container'>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='metric-card'>
            <div class='metric-title'>Rumah Tangga Terdata</div>
            <div class='metric-value'>12,345</div>
            <div class='metric-subtitle'>Dari 50 dusun</div>
        </div>
        <div class='metric-card'>
            <div class='metric-title'>Kemandirian Tinggi</div>
            <div class='metric-value'>80%</div>
            <div class='metric-subtitle'>Rumah tangga dengan swasembada pangan</div>
        </div>
        <div class='metric-card'>
            <div class='metric-title'>Data Terbaru</div>
            <div class='metric-value'>2024</div>
            <div class='metric-subtitle'>Pembaruan terakhir</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# Halaman Data Rumah Tangga
elif selected_page == "📊 Data Rumah Tangga":
    st.title("📊 Data Rumah Tangga")
    st.markdown(
        """
        Halaman ini menampilkan data rumah tangga.  
        Anda dapat mengunggah data, memfilter, dan melihat visualisasi interaktif.
        """
    )

    # File Uploader
    uploaded_file = st.file_uploader("Unggah file data rumah tangga (CSV atau Excel):", type=["csv", "xlsx"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write(data)
        # Visualisasi Contoh
        st.plotly_chart(
            px.histogram(data, x=data.columns[0], title="Histogram Data Rumah Tangga"),
            use_container_width=True,
        )
    else:
        st.info("Silakan unggah file untuk melihat konten.")

# Halaman Kemandirian Pangan RT
elif selected_page == "🍛 Kemandirian Pangan RT":
    st.title("🍛 Kemandirian Pangan Rumah Tangga")
    st.markdown(
        """
        Halaman ini menampilkan data kemandirian pangan rumah tangga.  
        Unggah file Anda untuk melihat analisis.
        """
    )

    # File Uploader
    uploaded_file = st.file_uploader("Unggah file data kemandirian pangan rumah tangga (CSV atau Excel):", type=["csv", "xlsx"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write(data)
        # Visualisasi Contoh
        st.plotly_chart(
            px.bar(data, x=data.columns[0], y=data.columns[1], title="Kemandirian Pangan RT"),
            use_container_width=True,
        )
    else:
        st.info("Silakan unggah file untuk melihat konten.")

# Halaman Kemandirian Pangan Dusun
elif selected_page == "🌾 Kemandirian Pangan Dusun":
    st.title("🌾 Kemandirian Pangan Dusun")
    st.markdown(
        """
        Halaman ini menampilkan data kemandirian pangan dusun.  
        Unggah file Anda untuk melihat analisis.
        """
    )

    # File Uploader
    uploaded_file = st.file_uploader("Unggah file data kemandirian pangan dusun (CSV atau Excel):", type=["csv", "xlsx"])
    if uploaded_file:
        data = pd.read_csv(uploaded_file)
        st.write(data)
        # Visualisasi Contoh
        st.plotly_chart(
            px.treemap(data, path=[data.columns[0]], values=data.columns[1], title="Treemap Kemandirian Pangan Dusun"),
            use_container_width=True,
        )
    else:
        st.info("Silakan unggah file untuk melihat konten.")
