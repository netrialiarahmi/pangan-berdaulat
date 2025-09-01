# 🍚 Food Security Analysis Dashboard

This project is an interactive, multi-page web dashboard built with Streamlit for analyzing and visualizing food security and household data. The application allows users to upload their own datasets (CSV or Excel) and explore various socio-economic, agricultural, and consumption patterns through dynamic charts and maps.

The dashboard is structured into three main modules:

1.  **Household Data Analysis**: A deep dive into household demographics, income, expenses, production, and more.
2.  **Household Food Self-Sufficiency**: Analysis of food self-sufficiency at the individual household level.
3.  **Hamlet Food Self-Sufficiency**: A higher-level view of food self-sufficiency aggregated by hamlet.

## ✨ Key Features

### General

  - **Multi-Page Interface**: A clean, navigable application with a main homepage and separate pages for each analysis module.
  - **File Uploader**: Supports uploading `.csv` and `.xlsx` files for each module.
  - **Modern UI**: Features a custom, modern design with responsive layouts and interactive elements.
  - **Data Caching**: Uses Streamlit's caching for improved performance when loading data.

### 🏠 Household Data Page

  - **Dynamic Filtering**: Filter the entire dashboard view by **Hamlet** (Dusun), **Village** (Desa/Kelurahan), or **Sub-district** (Kecamatan).
  - **Geospatial Mapping**: Visualizes the geographic distribution of households on an interactive map using GPS coordinates.
  - **Demographic Insights**:
      - Histogram of monthly income distribution.
      - Pie chart of family size distribution.
  - **Comprehensive Analytics**: Generates dynamic bar and pie charts for various categories, including:
      - **Production**: Carbohydrates, cooking oil, spices, etc.
      - **Consumption**: Food, beverages, fuel, etc.
      - **Agricultural Inputs**: Proportions of expenses on fertilizer, pesticides, seeds, etc.
      - **Livestock & Fisheries**: Total ownership and production/consumption analysis.
      - **Waste Management**: Analysis of waste sources and processing methods.
      - **Education**: Breakdown of education-related expenses.

### 🍛 Household Self-Sufficiency Page

  - **Individual Analysis**: Bar chart visualizing the food self-sufficiency percentage for each household.
  - **Top Performers**: Displays a table highlighting the **Top 5** households with the highest food self-sufficiency.

### 🌾 Hamlet Self-Sufficiency Page

  - **Aggregated View**: A treemap visualization to compare food self-sufficiency levels across different hamlets.
  - **Overall Average**: Calculates and displays the average self-sufficiency percentage for the entire dataset.

-----

## 🛠️ Tech Stack

  - **Web Framework**: [Streamlit](https://streamlit.io/)
  - **Data Manipulation**: [Pandas](https://pandas.pydata.org/)
  - **Data Visualization**: [Plotly Express](https://plotly.com/python/plotly-express/)

-----

## 📂 Project Structure

For the Streamlit multi-page feature to work correctly, the project should be organized as follows:

```
your-repo-name/
│
├── main.py                 # The main landing page script
├── utils.py                # Helper functions (e.g., load_data)
├── requirements.txt        # List of dependencies
│
└── pages/                  # Directory for other pages
    ├── 1_🏠_Data_Rumah_Tangga.py
    ├── 2_🍛_Kemandirian_Pangan_Rumah_Tangga.py
    └── 3_🌾_Kemandirian_Pangan_Dusun.py
```

-----

## 🖥️ Setup and Installation

To run this application locally, follow these steps.

1.  **Clone the Repository**

    ```bash
    git clone https://your-repository-url.git
    cd your-repository-directory
    ```

2.  **Create and Install Dependencies**
    Create a `requirements.txt` file with the following content:

    ```
    streamlit
    pandas
    plotly
    openpyxl
    ```

    Then, install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Application**
    Execute the following command in your terminal:

    ```bash
    streamlit run main.py
    ```

    The application will open in your default web browser.

-----

## 📊 Data Requirements

The application expects specific file formats and column names to function correctly. **All data files (CSV or Excel) must have their headers on the second row.**

  - **Household Data File (`Data_Rumah_Tangga`)**:

      - **Filtering Columns**: `Dusun`, `Desa/Kelurahan`, `Kecamatan`
      - **Demographic Columns**: `Pendapatan Bulanan (Rp.)`, `Jumlah Anggota Keluarga (jiwa)`
      - **Mapping Column**: `Koordinat GPS` (in the format `"longitude, latitude, ..."`)
      - **Analysis Columns**: Various columns related to production, consumption, livestock, etc. The app is robust and will only display charts for the columns it finds.

  - **Household Self-Sufficiency File (`Kemandirian_Pangan_Rumah_Tangga`)**:

      - `Data`: The name of the head of the household.
      - `Rata-rata`: The self-sufficiency percentage (e.g., `85%` or `85`).

  - **Hamlet Self-Sufficiency File (`Kemandirian_Pangan_Dusun`)**:

      - `Data`: The name of the hamlet (Dusun).
      - `Rata-rata`: The aggregated self-sufficiency percentage for that hamlet.
