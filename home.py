import streamlit as st
import pandas as pd
import webbrowser
from datetime import datetime


if "data" not in st.session_state:
    df_data = pd.read_csv("dataset/CLEAN_FIFA23_official_data.csv", index_col=0, encoding='utf-8')
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data
    
    
    df_22 = pd.read_csv("dataset/CLEAN_FIFA22_official_data.csv", index_col=0, encoding='utf-8')
    df_22 = df_22[df_22["Contract Valid Until"] >= datetime.today().year]
    df_22 = df_22[df_22["Value(£)"] > 0]
    df_22 = df_22.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_22
    
st.write("# Teste aparece")
st.sidebar.markdown("Acesse já https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

btn = st.button("Acesse os dados kaggle")
if btn: 
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
   
 
    
    
    
    
    
    