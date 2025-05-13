import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Avian Flu Dashboard", layout="wide")
st.title("🦜 HPAI Outbreak Dashboard (Wild Birds, 2022–2023)")

# Load CSV
df = pd.read_csv("hpai-wild-birds-2022-2023.csv")

# Sidebar filters (optional)
species = st.sidebar.multiselect("Select Species", df["Species"].unique(), default=df["Species"].unique())
province = st.sidebar.multiselect("Select Province", df["Province"].unique(), default=df["Province"].unique())

# Filter Data
filtered_df = df[df["Species"].isin(species) & df["Province"].isin(province)]

# Top Species Chart
top_species = filtered_df["Species"].value_counts().head(10).reset_index()
top_species.columns = ["Species", "Cases"]
fig1 = px.bar(top_species, x="Cases", y="Species", orientation="h", title="Top 10 Species")

# Province Chart
top_province = filtered_df["Province"].value_counts().head(10).reset_index()
top_province.columns = ["Province", "Cases"]
fig2 = px.bar(top_province, x="Cases", y="Province", orientation="h", title="Top 10 Provinces")

# Layout
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    st.plotly_chart(fig2, use_container_width=True)
