import streamlit as st
import pandas as pd

@st.cache_data
def load_data(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
    else:
        st.error('Format file tidak didukung.')
        return None
    return df

def extract_lat_lon(coord):
    try:
        # Mengasumsikan format 'Longitude, Latitude, Altitude, Accuracy'
        parts = coord.split(',')
        if len(parts) >= 2:
            longitude = float(parts[0].strip())
            latitude = float(parts[1].strip())
            return pd.Series({'Latitude': latitude, 'Longitude': longitude})
        else:
            return pd.Series({'Latitude': None, 'Longitude': None})
    except:
        return pd.Series({'Latitude': None, 'Longitude': None})
