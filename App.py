# DashBoard para analise de dados

import pandas as pd
import streamlit as st
import plotly.express as px

# page config
st.set_page_config(
    page_title="Dashboard: Salarios da Área de Dados",
    layout="wide",
    page_icon=":bar_chart:",
)

# get data
df = pd.read_csv(
    "https://raw.githubusercontent.com/IRam0Ss/ProjetoDataBase/refs/heads/main/database/dataBase_salary.csv"
)

# side bar
st.sidebar.header(":material/filter_list: Filtros")

# filtros
years_options = df["work_year"].unique().tolist()
years_selected = st.sidebar.multiselect(
    "Anos", years_options, placeholder="Selecione os anos"
)

experience_level_options = df["experience_level"].unique().tolist()
experience_level_selected = st.sidebar.multiselect(
    "Nivel de experiencia",
    experience_level_options,
    placeholder="Selecione o nivel de experiencia",
)

employment_type_options = df["employment_type"].unique().tolist()
employment_type_selected = st.sidebar.multiselect(
    "Tipo de contrato",
    employment_type_options,
    placeholder="Selecione o tipo de contrato",
)

job_title_options = df["job_title"].unique().tolist()
job_title_selected = st.sidebar.multiselect(
    "Titulo do cargo",
    job_title_options,
    placeholder="Selecione o titulo do cargo",
)

company_size_options = df["company_size"].unique().tolist()
company_size_selected = st.sidebar.multiselect(
    "Tamanho da empresa",
    company_size_options,
    placeholder="Selecione o tamanho da empresa",
)
