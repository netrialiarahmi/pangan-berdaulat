# 🍛 Kemandirian Pangan Rumah Tangga

import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data

st.title('🍛 Data Kemandirian Pangan Per Rumah Tangga')

data_kemandirian_rumah_tangga_file = st.file_uploader('Upload Data Kemandirian Pangan Per Rumah Tangga (CSV atau Excel)', type=['csv', 'xlsx'], key='data_kemandirian_rumah_tangga')
if data_kemandirian_rumah_tangga_file is not None:
    data_kemandirian_rumah_tangga = load_data(data_kemandirian_rumah_tangga_file)
    if data_kemandirian_rumah_tangga is not None:
        # Membersihkan kolom 'Rata-rata'
        if 'Rata-rata' in data_kemandirian_rumah_tangga.columns:
            data_kemandirian_rumah_tangga['Rata-rata'] = data_kemandirian_rumah_tangga['Rata-rata'].astype(str).str.replace('%', '').str.strip()
            data_kemandirian_rumah_tangga['Rata-rata'] = pd.to_numeric(data_kemandirian_rumah_tangga['Rata-rata'], errors='coerce')
        with st.expander("🔍 Lihat Data Kemandirian Pangan Per Rumah Tangga"):
            st.write(data_kemandirian_rumah_tangga)
        
        # Visualisasi
        if 'Data' in data_kemandirian_rumah_tangga.columns and 'Rata-rata' in data_kemandirian_rumah_tangga.columns:
            st.subheader('🌟 Kemandirian Pangan Per Rumah Tangga')
            fig = px.bar(data_kemandirian_rumah_tangga, x='Data', y='Rata-rata', color='Rata-rata', color_continuous_scale='Blues')
            fig.update_layout(title='Kemandirian Pangan Per Rumah Tangga', xaxis_title='Nama Kepala Keluarga', yaxis_title='Rata-rata Kemandirian Pangan (%)')
            fig.update_xaxes(tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)
            
            # Top 5 Keluarga dengan Kemandirian Tertinggi
            top5 = data_kemandirian_rumah_tangga.nlargest(5, 'Rata-rata')
            st.markdown('**🏆 Top 5 Keluarga dengan Kemandirian Pangan Tertinggi**')
            st.table(top5[['Data', 'Rata-rata']])
        else:
            st.warning('Kolom "Data" atau "Rata-rata" tidak ditemukan dalam data.')
    else:
        st.error('Gagal memuat data. Pastikan format file benar dan sesuai.')
else:
    st.info('Silakan upload file **Data Kemandirian Pangan Per Rumah Tangga** pada halaman ini.')
