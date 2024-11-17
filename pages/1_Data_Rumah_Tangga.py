# 🏠 Data Rumah Tangga

import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, extract_lat_lon

st.title('🏠 Data Rumah Tangga')

# Upload dan tampilkan data_rumah_tangga
data_rumah_tangga_file = st.file_uploader('Upload Data Rumah Tangga (CSV atau Excel)', type=['csv', 'xlsx'], key='data_rumah_tangga')
if data_rumah_tangga_file is not None:
    data_rumah_tangga = load_data(data_rumah_tangga_file)
    if data_rumah_tangga is not None:
        with st.expander("🔍 Lihat Data Rumah Tangga"):
            st.write(data_rumah_tangga)
        
        # Opsi Filter
        st.subheader('📍 Filter Data')
        filter_option = st.selectbox('Pilih Opsi Filter', ['Semua Data', 'Dusun', 'Desa/Kelurahan', 'Kecamatan'])
        if filter_option == 'Dusun':
            if 'Dusun' in data_rumah_tangga.columns:
                dusun_list = data_rumah_tangga['Dusun'].dropna().unique()
                selected_dusun = st.multiselect('Pilih Dusun', options=dusun_list, default=dusun_list)
                filtered_data = data_rumah_tangga[data_rumah_tangga['Dusun'].isin(selected_dusun)]
            else:
                st.warning('Kolom "Dusun" tidak ditemukan dalam data.')
                filtered_data = data_rumah_tangga
        elif filter_option == 'Desa/Kelurahan':
            if 'Desa/Kelurahan' in data_rumah_tangga.columns:
                desa_list = data_rumah_tangga['Desa/Kelurahan'].dropna().unique()
                selected_desa = st.multiselect('Pilih Desa/Kelurahan', options=desa_list, default=desa_list)
                filtered_data = data_rumah_tangga[data_rumah_tangga['Desa/Kelurahan'].isin(selected_desa)]
            else:
                st.warning('Kolom "Desa/Kelurahan" tidak ditemukan dalam data.')
                filtered_data = data_rumah_tangga
        elif filter_option == 'Kecamatan':
            if 'Kecamatan' in data_rumah_tangga.columns:
                kecamatan_list = data_rumah_tangga['Kecamatan'].dropna().unique()
                selected_kecamatan = st.multiselect('Pilih Kecamatan', options=kecamatan_list, default=kecamatan_list)
                filtered_data = data_rumah_tangga[data_rumah_tangga['Kecamatan'].isin(selected_kecamatan)]
            else:
                st.warning('Kolom "Kecamatan" tidak ditemukan dalam data.')
                filtered_data = data_rumah_tangga
        else:
            filtered_data = data_rumah_tangga

        # 1. Visualisasi Data Rumah Tangga
        st.subheader('1️⃣ Visualisasi Data Rumah Tangga')
        col1, col2 = st.columns(2)
        with col1:
            if 'Pendapatan Bulanan (Rp.)' in filtered_data.columns:
                st.markdown('**Distribusi Pendapatan Bulanan**')
                # Mengonversi kolom 'Pendapatan Bulanan (Rp.)' menjadi numerik
                filtered_data['Pendapatan Bulanan (Rp.)'] = pd.to_numeric(filtered_data['Pendapatan Bulanan (Rp.)'], errors='coerce')
                fig = px.histogram(filtered_data, x='Pendapatan Bulanan (Rp.)', nbins=20, color_discrete_sequence=['#1ABC9C'])
                fig.update_layout(title='Distribusi Pendapatan Bulanan', xaxis_title='Pendapatan Bulanan (Rp.)', yaxis_title='Jumlah Rumah Tangga')
                st.plotly_chart(fig, use_container_width=True)
        with col2:
            if 'Jumlah Anggota Keluarga (jiwa)' in filtered_data.columns:
                st.markdown('**Distribusi Jumlah Anggota Keluarga**')
                filtered_data['Jumlah Anggota Keluarga (jiwa)'] = pd.to_numeric(filtered_data['Jumlah Anggota Keluarga (jiwa)'], errors='coerce')
                fig = px.pie(filtered_data, names='Jumlah Anggota Keluarga (jiwa)', color_discrete_sequence=px.colors.sequential.RdBu)
                fig.update_traces(textposition='inside', textinfo='percent+label')
                fig.update_layout(title='Persentase Jumlah Anggota Keluarga')
                st.plotly_chart(fig, use_container_width=True)

        # 2. Peta Sebaran Rumah Tangga
        st.subheader('2️⃣ Peta Sebaran Rumah Tangga')
        if 'Koordinat GPS' in filtered_data.columns:
            # Memisahkan latitude dan longitude
            coords = filtered_data['Koordinat GPS'].apply(extract_lat_lon)
            filtered_data = filtered_data.join(coords)
            filtered_data = filtered_data.dropna(subset=['Latitude', 'Longitude'])
            
            fig = px.scatter_mapbox(
                filtered_data,
                lat='Latitude',
                lon='Longitude',
                hover_name='Nama Kepala Keluarga',
                zoom=12,
                height=500,
                mapbox_style='open-street-map',
                color_discrete_sequence=['#FF5733']
            )
            fig.update_layout(title='Peta Sebaran Rumah Tangga')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning('Kolom "Koordinat GPS" tidak ditemukan dalam data.')

        # 3. 🍚 Analisis Produksi
        st.subheader('3️⃣ 🍚 Analisis Produksi')
        produksi_cols = {
            'Produksi Karbohidrat': ['Beras Lokal (Sawah/Ladang dalam Kg)', 'Singkong', 'Jagung Lokal', 'Jagung Hibrida', 'Umbi-umbian lain', 'Sorgum', 'Jewawut/Weteng'],
            'Produksi Pertanian': ['Nama Tanaman', 'Jenis Pangan', 'Varietas', 'Luas Lahan', 'Produktivitas'],
            'Minyak Masak': ['Minyak Masak', 'Minyak Kelapa'],
            'Bumbu dan Rempah': ['Cabai Besar', 'Cabai Kecil', 'Kemiri', 'Kunyit', 'Jahe', 'Sereh', 'Lengkuas', 'Jeruk Nipis', 'Mete', 'Lain-lain']
        }
        for category, cols in produksi_cols.items():
            available_cols = [col for col in cols if col in filtered_data.columns]
            if available_cols:
                st.markdown(f'**{category}**')
                for col in available_cols:
                    filtered_data[col] = pd.to_numeric(filtered_data[col], errors='coerce')
                total_produksi = filtered_data[available_cols].sum()
                produksi_df = total_produksi.reset_index()
                produksi_df.columns = ['Komoditas', 'Jumlah']
                fig = px.bar(produksi_df, x='Komoditas', y='Jumlah', color='Jumlah', color_continuous_scale='Viridis')
                fig.update_layout(title=f'Produksi {category}', xaxis_title='Komoditas', yaxis_title='Jumlah')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning(f'Tidak ada data untuk {category}.')

        # 4. Analisis Konsumsi Pangan
        st.subheader('4️⃣ Analisis Konsumsi Pangan')
        konsumsi_cols = {
            'Konsumsi Karbohidrat': ['Beras Lokal (Sawah/Ladang)', 'Singkong.1', 'Jagung Lokal.1', 'Jagung Hibrida.1', 'Umbi-umbian lain.1', 'Sorgum.1', 'Jewawut/Weteng.1'],
            'Konsumsi Pertanian': ['Nama Tanaman', 'Jenis Pangan', 'Varietas', 'Luas Lahan', 'Produktivitas'],
            'Minyak Masak': ['Minyak Masak.1', 'Minyak Kelapa.1'],
            'Bumbu dan Rempah': ['Cabai Besar.1', 'Cabai Kecil.1', 'Kemiri.1', 'Kunyit.1', 'Jahe.1', 'Sereh.1', 'Lengkuas.1', 'Jeruk Nipis.1', 'Mete.1', 'Lain-lain.1'],
            'Konsumsi Sayur dan Buah': ['Daun Ubi', 'Kangkung', 'Kubis', 'Sawi', 'Bayam', 'Brokoli', 'Wortel', 'Jantung Pisang', 'Kelor', 'Bunga dan Daun Pepaya', 'Pakis/Paku', 'Rebung', 'Mangga', 'Alpukat', 'Jeruk', 'Anggur', 'Buah Naga', 'Mete', 'Pisang', 'Rambutan', 'Nanas', 'Salak', 'Pepaya', 'Kelapa', 'Tomat', 'Timun', 'Labu', 'Kemangi'],
            'Makanan dan Minuman Olahan': ['Susu (Bubuk/UHT)', 'Kental Manis', 'Minuman Kemasan', 'Minuman Fermentasi', 'Gula Pasir', 'Kopi', 'Teh', 'Mie Instan', 'Biskuit/Roti/Kue Kemasan'],
            'Konsumsi Lain-lain': ['Rokok Kemasan', 'Tembakau', 'Pinang', 'Daun Sirih'],
            'Bahan Bakar': ['Minyak Tanah', 'Gas', 'Biaya Listrik', 'BBM']
        }
        for category, cols in konsumsi_cols.items():
            available_cols = [col for col in cols if col in filtered_data.columns]
            if available_cols:
                st.markdown(f'**{category}**')
                for col in available_cols:
                    filtered_data[col] = pd.to_numeric(filtered_data[col], errors='coerce')
                total_konsumsi = filtered_data[available_cols].sum()
                konsumsi_df = total_konsumsi.reset_index()
                konsumsi_df.columns = ['Komoditas', 'Jumlah']
                fig = px.bar(konsumsi_df, x='Komoditas', y='Jumlah', color='Jumlah', color_continuous_scale='Cividis')
                fig.update_layout(title=f'Konsumsi {category}', xaxis_title='Komoditas', yaxis_title='Jumlah')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning(f'Tidak ada data untuk {category}.')

        # 5. Analisis Input Pertanian
        st.subheader('5️⃣ Analisis Input Pertanian')
        input_pertanian_cols = ['Pupuk', 'Pestisida/Herbisida/Fungisida', 'Benih', 'Upah Buruh', 'Sewa Alat dan Mesin Pertanian']
        available_input_cols = [col for col in input_pertanian_cols if col in filtered_data.columns]
        if available_input_cols:
            for col in available_input_cols:
                filtered_data[col] = pd.to_numeric(filtered_data[col], errors='coerce')
            total_input = filtered_data[available_input_cols].sum()
            input_df = total_input.reset_index()
            input_df.columns = ['Input Pertanian', 'Jumlah']
            fig = px.pie(input_df, names='Input Pertanian', values='Jumlah', color_discrete_sequence=px.colors.sequential.Blues)
            fig.update_layout(title='Proporsi Penggunaan Input Pertanian')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning('Tidak ada data untuk Input Pertanian.')

            # 6. Analisis Peternakan
            st.subheader('6️⃣ Analisis Peternakan')
            
            # Inisialisasi ternak_cols sebagai list kosong
            ternak_cols = []
            
            # Periksa apakah kolom "Jenis Ternak" dan "Kuda" ada dalam dataset
            if 'Jenis Ternak' in filtered_data.columns and 'Kuda' in filtered_data.columns:
                jenis_ternak_index = filtered_data.columns.get_loc('Jenis Ternak')
                kuda_index = filtered_data.columns.get_loc('Kuda')
            
                # Pastikan urutan indeks benar
                if jenis_ternak_index < kuda_index:
                    # Ambil kolom dari "Jenis Ternak" hingga "Kuda" secara inklusif
                    ternak_cols = filtered_data.columns[jenis_ternak_index:kuda_index+1].tolist()
                else:
                    st.warning('Kolom "Jenis Ternak" harus berada sebelum kolom "Kuda" dalam dataset.')
            else:
                st.warning('Kolom "Jenis Ternak" atau "Kuda" tidak ditemukan dalam dataset.')
            
            # Pastikan ternak_cols adalah list dan tidak kosong sebelum melanjutkan
            if isinstance(ternak_cols, list) and len(ternak_cols) > 0:
                # Filter data yang hanya relevan untuk peternakan
                peternakan_data = filtered_data[ternak_cols].copy()
            
                # Bersihkan data menjadi angka
                for col in ternak_cols[1:]:  # Lewati kolom "Jenis Ternak"
                    peternakan_data[col] = pd.to_numeric(peternakan_data[col], errors='coerce').fillna(0)
            
                # Hitung total jumlah ternak berdasarkan jenis
                total_peternakan = peternakan_data[ternak_cols[1:]].sum(axis=0)
                peternakan_summary = pd.DataFrame({
                    'Jenis Ternak': total_peternakan.index,
                    'Jumlah': total_peternakan.values
                })
            
                # Visualisasi data total peternakan
                fig_peternakan = px.bar(
                    peternakan_summary,
                    x='Jenis Ternak',
                    y='Jumlah',
                    color='Jumlah',
                    color_continuous_scale='OrRd',
                    title='Total Kepemilikan Ternak Berdasarkan Jenis'
                )
                fig_peternakan.update_layout(xaxis_title='Jenis Ternak', yaxis_title='Jumlah')
                st.plotly_chart(fig_peternakan, use_container_width=True)
            else:
                st.warning('Kolom ternak tidak ditemukan atau urutan kolom tidak sesuai.')

            # 7. Analisis Perikanan
            st.subheader('7️⃣ Analisis Perikanan')
            
            # Definisikan kolom untuk Produksi dan Konsumsi Perikanan
            produksi_perikanan_cols = ['Ikan dan Boga Laut Segar', 'Ikan dan Boga Laut Kering', 'Jumlah Hasil']
            konsumsi_perikanan_cols = ['Ikan dan Boga Laut Segar.1', 'Ikan dan Boga Laut Kering.1']
            
            # Analisis Produksi Perikanan
            available_produksi_cols = [col for col in produksi_perikanan_cols if col in filtered_data.columns]
            if len(available_produksi_cols) > 0:
                # Proses data produksi
                produksi_data = filtered_data[available_produksi_cols].copy()
                for col in available_produksi_cols:
                    produksi_data[col] = pd.to_numeric(produksi_data[col], errors='coerce').fillna(0)
                total_produksi = produksi_data.sum()
                produksi_df = total_produksi.reset_index()
                produksi_df.columns = ['Komoditas Perikanan', 'Jumlah']
                # Visualisasi
                fig_produksi = px.bar(
                    produksi_df,
                    x='Komoditas Perikanan',
                    y='Jumlah',
                    color='Jumlah',
                    color_continuous_scale='Teal',
                    title='Total Produksi Perikanan'
                )
                fig_produksi.update_layout(xaxis_title='Komoditas Perikanan', yaxis_title='Jumlah')
                st.plotly_chart(fig_produksi, use_container_width=True)
            else:
                st.warning('Tidak ada data untuk Produksi Perikanan.')
            
            # Analisis Konsumsi Perikanan
            available_konsumsi_cols = [col for col in konsumsi_perikanan_cols if col in filtered_data.columns]
            if len(available_konsumsi_cols) > 0:
                # Proses data konsumsi
                konsumsi_data = filtered_data[available_konsumsi_cols].copy()
                for col in available_konsumsi_cols:
                    konsumsi_data[col] = pd.to_numeric(konsumsi_data[col], errors='coerce').fillna(0)
                total_konsumsi = konsumsi_data.sum()
                konsumsi_df = total_konsumsi.reset_index()
                konsumsi_df.columns = ['Komoditas Perikanan', 'Jumlah']
                # Visualisasi
                fig_konsumsi = px.bar(
                    konsumsi_df,
                    x='Komoditas Perikanan',
                    y='Jumlah',
                    color='Jumlah',
                    color_continuous_scale='Blues',
                    title='Total Konsumsi Perikanan'
                )
                fig_konsumsi.update_layout(xaxis_title='Komoditas Perikanan', yaxis_title='Jumlah')
                st.plotly_chart(fig_konsumsi, use_container_width=True)
            else:
                st.warning('Tidak ada data untuk Konsumsi Perikanan.')
            
            # 8. Analisis Limbah
            st.subheader('8️⃣ Analisis Limbah')
            limbah_cols = ['Sumber Limbah', 'Pengolahan', 'Hasil Daur Ulang']
            
            if set(limbah_cols).issubset(filtered_data.columns):
                limbah_data = filtered_data[limbah_cols].copy()
                
                # Preprocessing Data Limbah
                limbah_data = limbah_data.fillna('')  # Isi nilai kosong dengan string kosong
                limbah_data['Sumber Limbah'] = limbah_data['Sumber Limbah'].astype(str).str.strip().str.capitalize()
                limbah_data['Pengolahan'] = limbah_data['Pengolahan'].astype(str).str.strip().str.capitalize().replace({'Tidak ada': 'Tidak diolah'})
                limbah_data['Hasil Daur Ulang'] = limbah_data['Hasil Daur Ulang'].astype(str).str.strip().str.capitalize().replace(
                    {'': 'Dibakar', 'Di buang': 'Dibakar', '0': 'Dibakar', 'Nan': 'Dibakar'}
                )
            
                # Pastikan tidak ada nilai numerik atau anonim
                def clean_numeric_values(value, default):
                    try:
                        float(value)  # Jika nilai numerik, ganti dengan default
                        return default
                    except ValueError:
                        return value
            
                limbah_data['Sumber Limbah'] = limbah_data['Sumber Limbah'].apply(lambda x: clean_numeric_values(x, 'Tidak diketahui'))
                limbah_data['Pengolahan'] = limbah_data['Pengolahan'].apply(lambda x: clean_numeric_values(x, 'Tidak diolah'))
                limbah_data['Hasil Daur Ulang'] = limbah_data['Hasil Daur Ulang'].apply(lambda x: clean_numeric_values(x, 'Dibakar'))
            
                # Visualisasi Sumber Limbah
                st.markdown('**Distribusi Sumber Limbah**')
                sumber_counts = limbah_data['Sumber Limbah'].value_counts().reset_index()
                sumber_counts.columns = ['Sumber Limbah', 'Jumlah']
                fig_sumber = px.pie(
                    sumber_counts, 
                    names='Sumber Limbah', 
                    values='Jumlah', 
                    hole=0.5, 
                    color_discrete_sequence=px.colors.sequential.RdBu
                )
                fig_sumber.update_traces(textposition='inside', textinfo='percent+label')
                fig_sumber.update_layout(title='Distribusi Sumber Limbah')
                st.plotly_chart(fig_sumber, use_container_width=True)
            
                # Visualisasi Pengolahan Limbah
                st.markdown('**Distribusi Pengolahan Limbah**')
                pengolahan_counts = limbah_data['Pengolahan'].value_counts().reset_index()
                pengolahan_counts.columns = ['Pengolahan', 'Jumlah']
                fig_pengolahan = px.pie(
                    pengolahan_counts, 
                    names='Pengolahan', 
                    values='Jumlah', 
                    hole=0.5, 
                    color_discrete_sequence=px.colors.sequential.Viridis
                )
                fig_pengolahan.update_traces(textposition='inside', textinfo='percent+label')
                fig_pengolahan.update_layout(title='Distribusi Pengolahan Limbah')
                st.plotly_chart(fig_pengolahan, use_container_width=True)
            
                # Visualisasi Hasil Daur Ulang
                st.markdown('**Distribusi Hasil Daur Ulang**')
                hasil_counts = limbah_data['Hasil Daur Ulang'].value_counts().reset_index()
                hasil_counts.columns = ['Hasil Daur Ulang', 'Jumlah']
                fig_hasil = px.pie(
                    hasil_counts, 
                    names='Hasil Daur Ulang', 
                    values='Jumlah', 
                    hole=0.5, 
                    color_discrete_sequence=px.colors.sequential.Plasma
                )
                fig_hasil.update_traces(textposition='inside', textinfo='percent+label')
                fig_hasil.update_layout(title='Distribusi Hasil Daur Ulang')
                st.plotly_chart(fig_hasil, use_container_width=True)
            
                # Menampilkan Data Limbah dalam tabel
                st.markdown('**Detail Data Limbah**')
                st.dataframe(limbah_data)
            else:
                st.warning('Tidak ada data untuk Limbah.')

        # 9. Analisis Pendidikan
        st.subheader('9️⃣ Analisis Pendidikan')
        pendidikan_cols = ['SPP (Iuran Sekolah)', 'Peralatan Sekolah/ATK', 'Transportasi/Kos/Jajan']
        available_pendidikan_cols = [col for col in pendidikan_cols if col in filtered_data.columns]
        if available_pendidikan_cols:
            for col in available_pendidikan_cols:
                filtered_data[col] = pd.to_numeric(filtered_data[col], errors='coerce')
            total_pendidikan = filtered_data[available_pendidikan_cols].sum()
            pendidikan_df = total_pendidikan.reset_index()
            pendidikan_df.columns = ['Pengeluaran Pendidikan', 'Jumlah']
            fig = px.bar(pendidikan_df, x='Pengeluaran Pendidikan', y='Jumlah', color='Jumlah', color_continuous_scale='Purples')
            fig.update_layout(title='Total Pengeluaran Pendidikan', xaxis_title='Jenis Pengeluaran', yaxis_title='Jumlah')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning('Tidak ada data untuk Pendidikan.')

    else:
        st.error('Gagal memuat data. Pastikan format file benar dan sesuai.')
else:
    st.info('Silakan upload file **Data Rumah Tangga** pada halaman ini.')
