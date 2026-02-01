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
years_options = sorted(df["work_year"].unique())
years_selected = st.sidebar.multiselect(
    "Anos", years_options, placeholder="Selecione os anos"
)

experience_level_options = sorted(df["experience_level"].unique())
experience_level_selected = st.sidebar.multiselect(
    "Nivel de experiencia",
    experience_level_options,
    placeholder="Selecione o nivel de experiencia",
)

employment_type_options = sorted(df["employment_type"].unique())
employment_type_selected = st.sidebar.multiselect(
    "Tipo de contrato",
    employment_type_options,
    placeholder="Selecione o tipo de contrato",
)

job_title_options = sorted(df["job_title"].unique())
job_title_selected = st.sidebar.multiselect(
    "Titulo do cargo",
    job_title_options,
    placeholder="Selecione o titulo do cargo",
)

company_size_options = sorted(df["company_size"].unique())
company_size_selected = st.sidebar.multiselect(
    "Tamanho da empresa",
    company_size_options,
    placeholder="Selecione o tamanho da empresa",
)

company_location_options = sorted(df["company_location"].dropna().unique())
company_location_selected = st.sidebar.multiselect(
    "Localizacao da empresa",
    company_location_options,
    placeholder="Selecione a localizacao da empresa",
)

# apply filters
df_filtered = df.copy()

filters = {
    "work_year": years_selected,
    "experience_level": experience_level_selected,
    "employment_type": employment_type_selected,
    "job_title": job_title_selected,
    "company_size": company_size_selected,
    "company_location": company_location_selected,
}

# aplica a logica de filtrar somente se a lista de valores nao estiver vazia
for column, selected_values in filters.items():
    if selected_values:
        df_filtered = df_filtered[df_filtered[column].isin(selected_values)]


# conteudo principal acesso rapido
st.markdown(
    "<h1 style='text-align: center;'>🎲 Análise de Salários na Área de Dados 🎲</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    """
    <div style='text-align: center;'>
        <h4>Explore os dados salariais da área de dados dos últimos anos.</h4>
        <p>Utilize os filtros do campo a esquerda para facilitar sua vizualização.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# principais metricas
st.subheader(":straight_ruler: *Principais Métricas*")

if not df_filtered.empty:
    mean_salary = df_filtered["salary_in_usd"].mean()
    max_salary = df_filtered["salary_in_usd"].max()
    median_salary = df_filtered["salary_in_usd"].median()
    total_registers = df_filtered.shape[0]
    most_common_job = df_filtered["job_title"].mode()[0]
else:
    mean_salary = 0
    max_salary = 0
    median_salary = 0
    total_registers = 0
    most_common_job = ""

# layout exibicao das metricas
# primeira linha de colunas de dados relacionados a salario
col1, col2, col3 = st.columns(3)

col1.metric("Salário Médio", f"${mean_salary:,.2f}")
col2.metric("Salário Máximo", f"${max_salary:,.2f}")
col3.metric("Salário Mediano", f"${median_salary:,.2f}")

# segunda linha de colunas de dados relacionados a quantidade de registros e cargo mais comum, centralizados
vazio_esq, col4, col5, vazio_dir = st.columns([1, 2, 2, 1])

with col4:
    col4.metric("Total de registros", total_registers)
with col5:
    col5.metric("Cargo mais comum", most_common_job)

st.markdown("---")

# criar os graficos
