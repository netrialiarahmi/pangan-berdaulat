# 🌾 Kemandirian Pangan Dusun

import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data

st.title('🌾 Data Kemandirian Pangan Per Dusun')

data_kemandirian_dusun_file = st.file_uploader('Upload Data Kemandirian Pangan Per Dusun (CSV atau Excel)', type=['csv', 'xlsx'], key='data_kemandirian_dusun')
if data_kemandirian_dusun_file is not None:
    data_kemandirian_dusun = load_data(data_kemandirian_dusun_file)
    if data_kemandirian_dusun is not None:
        # Membersihkan kolom 'Rata-rata'
        if 'Rata-rata' in data_kemandirian_dusun.columns:
            data_kemandirian_dusun['Rata-rata'] = data_kemandirian_dusun['Rata-rata'].astype(str).str.replace('%', '').str.strip()
            data_kemandirian_dusun['Rata-rata'] = pd.to_numeric(data_kemandirian_dusun['Rata-rata'], errors='coerce')
        with st.expander("🔍 Lihat Data Kemandirian Pangan Per Dusun"):
            st.write(data_kemandirian_dusun)
        
        # Visualisasi
        if 'Data' in data_kemandirian_dusun.columns and 'Rata-rata' in data_kemandirian_dusun.columns:
            st.subheader('🌾 Kemandirian Pangan Per Dusun')
            fig = px.treemap(data_kemandirian_dusun, path=['Data'], values='Rata-rata', color='Rata-rata', color_continuous_scale='Viridis')
            fig.update_layout(title='Kemandirian Pangan Per Dusun')
            st.plotly_chart(fig, use_container_width=True)
            
            # Rata-rata Kemandirian Pangan
            avg_kemandirian = data_kemandirian_dusun['Rata-rata'].mean()
            st.markdown(f'**📊 Rata-rata Kemandirian Pangan:** {avg_kemandirian:.2f}%')
        else:
            st.warning('Kolom "Data" atau "Rata-rata" tidak ditemukan dalam data.')
    else:
        st.error('Gagal memuat data. Pastikan format file benar dan sesuai.')
else:
    st.info('Silakan upload file **Data Kemandirian Pangan Per Dusun** pada halaman ini.')
