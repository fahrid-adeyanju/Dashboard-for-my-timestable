import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

st.title("SIMPLE DATA DASHBOARD")

uploaded_file = st.file_uploader("Choose a csv file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("file uploaded...")

    st.subheader("data preview")
    st.write(df.describe())

    st.subheader("data f")
    st.subheader(df.describe())

    st.subheader("Filter data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("select colunm to filter by", columns)
    unique_values = df[selected_columns].unique()
    selected_values = st.selectbox("select value", unique_values)

    filtered_df = df[df[selected_columns] == selected_values]
    st.write(filtered_df)

    st.subheader("plot data")
    x_column = st.selectbox("select x-axix column", columns)
    y_column = st.selectbox("select y-axix column", columns)