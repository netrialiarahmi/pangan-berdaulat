import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(
    page_title="Dashboard Data Pangan",
    page_icon="🍚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with modern styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Main container styling */
    .main .block-container {
        padding: 2rem 2rem 4rem 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Typography */
    h1, h2, h3, .stMarkdown, .stButton {
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Header styling */
    h1 {
        color: #1a365d;
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        margin-bottom: 1.5rem !important;
        padding-bottom: 1rem;
        border-bottom: 3px solid #e2e8f0;
    }
    
    /* Card container */
    .css-card {
        background-color: #ffffff;
        border-radius: 1rem;
        padding: 2rem;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06);
        margin-bottom: 2rem;
    }
    
    /* Feature cards */
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin-top: 2rem;
    }
    
    .feature-card {
        background-color: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 0.75rem;
        padding: 1.5rem;
        transition: transform 0.2s;
    }
    
    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    /* Sidebar styling */
    .css-1offfwp.e1fqkh3o3 {
        background-color: #f1f5f9;
        padding: 2rem 1rem;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 0.5rem;
        padding: 0.75rem 1.5rem;
        font-weight: 500;
        border: none;
        transition: background-color 0.2s;
    }
    
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    
    /* Footer */
    .footer {
        margin-top: 4rem;
        padding-top: 2rem;
        border-top: 1px solid #e2e8f0;
        text-align: center;
        color: #64748b;
    }
    </style>
""", unsafe_allow_html=True)

# Main content
st.title('🍚 Dashboard Data Pangan')

# Welcome section with card styling
st.markdown("""
    <div class="css-card">
        <h2 style="color: #1a365d; margin-bottom: 1rem;">Selamat datang di Dashboard Data Pangan!</h2>
        <p style="color: #475569; font-size: 1.1rem; line-height: 1.6;">
            Dashboard ini menyediakan visualisasi interaktif untuk membantu Anda memahami data pangan 
            dengan lebih baik. Eksplorasi berbagai aspek data melalui tiga modul utama kami.
        </p>
    </div>
""", unsafe_allow_html=True)

# Feature cards
st.markdown("""
    <div class="feature-grid">
        <div class="feature-card">
            <h3 style="color: #1a365d; margin-bottom: 0.75rem;">🏠 Data Rumah Tangga</h3>
            <p style="color: #475569;">
                Analisis menyeluruh tentang data demografi dan karakteristik rumah tangga 
                dalam konteks ketahanan pangan.
            </p>
        </div>
        <div class="feature-card">
            <h3 style="color: #1a365d; margin-bottom: 0.75rem;">🍛 Kemandirian Pangan RT</h3>
            <p style="color: #475569;">
                Eksplorasi tingkat kemandirian pangan per rumah tangga dengan 
                visualisasi interaktif.
            </p>
        </div>
        <div class="feature-card">
            <h3 style="color: #1a365d; margin-bottom: 0.75rem;">🌾 Kemandirian Pangan Dusun</h3>
            <p style="color: #475569;">
                Analisis komprehensif kemandirian pangan di tingkat dusun dengan 
                pemetaan detail.
            </p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Quick start guide
st.markdown("""
    <div class="css-card" style="margin-top: 2rem;">
        <h2 style="color: #1a365d; margin-bottom: 1rem;">🚀 Cara Menggunakan Dashboard</h2>
        <ol style="color: #475569; font-size: 1.1rem; line-height: 1.6;">
            <li>Pilih modul yang ingin Anda eksplorasi dari menu navigasi di sebelah kiri</li>
            <li>Gunakan filter yang tersedia untuk menyaring data sesuai kebutuhan</li>
            <li>Interaksi dengan grafik untuk melihat detail lebih lanjut</li>
            <li>Unduh data atau grafik yang Anda butuhkan untuk analisis lebih lanjut</li>
        </ol>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>© 2024 Dashboard Data Pangan. All rights reserved.</p>
        <p style="font-size: 0.9rem; margin-top: 0.5rem;">
            Indonesia Emas 2045
        </p>
    </div>
""", unsafe_allow_html=True)
