import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the pipeline and dataframe
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("Laptop Price Predictor")

# Sidebar for user input
st.header("Enter Laptop Features:")

company = st.selectbox('Brand', df['Company'].unique())
typename = st.selectbox('Type', df['TypeName'].unique())
ram = st.selectbox('RAM (GB)', sorted(df['Ram'].unique()))
weight = st.number_input('Weight (kg)', min_value=0.5, max_value=5.0, value=2.0, step=0.1)
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
ips = st.selectbox('IPS Display', ['No', 'Yes'])
ppi = st.number_input('PPI', min_value=50.0, max_value=400.0, value=150.0, step=1.0)
cpu = st.selectbox('CPU Brand', df['CpuBrand'].unique())
hdd = st.number_input('HDD (GB)', min_value=0, max_value=2000, value=0, step=128)
ssd = st.number_input('SSD (GB)', min_value=0, max_value=2000, value=256, step=128)
gpu = st.selectbox('GPU Brand', df['GpuBrand'].unique())
os = st.selectbox('Operating System', df['OpSys'].unique())

# Convert categorical Yes/No to 1/0
touchscreen = 1 if touchscreen == 'Yes' else 0
ips = 1 if ips == 'Yes' else 0

if st.button('Predict Price'):
    # Arrange input in the same order as model expects
    input_df = pd.DataFrame([[company, typename, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os]],
                            columns=['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'ips', 'ppi',
                                     'CpuBrand', 'HDD', 'SSD', 'GpuBrand', 'OpSys'])
    # Predict
    result = pipe.predict(input_df)[0]
    st.success(f"Predicted Laptop Price: ₹{int(result):,}")