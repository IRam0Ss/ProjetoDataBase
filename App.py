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
st.markdown(
    """
    <style>
    [data-testid="stMetric"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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

# criar os graficos 2 por coluna

col_graf1, col_graf2 = st.columns(2)

# media salarial de acordo com nivel de experiencia
with col_graf1:
    if not df_filtered.empty:
        salary_by_experience = (
            df_filtered.groupby("experience_level")["salary_in_usd"]
            .mean()
            .sort_values(ascending=True)
            .reset_index()
        )
        fig_experience = px.bar(
            salary_by_experience,
            x="experience_level",
            y="salary_in_usd",
            title="Média Salarial Anual por Nível de Experiência",
            color="experience_level",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            labels={
                "experience_level": "Nível de Experiência",
                "salary_in_usd": "Salário (USD)",
            },
        )
        fig_experience.update_layout(
            showlegend=False,
            title_x=0.2,
            yaxis_title="Salário (USD)",
            xaxis_title="Nível de Experiência",
        )
        st.plotly_chart(fig_experience, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível para o filtro selecionado.")

# top 5 cargos que mais pagam
with col_graf2:
    if not df_filtered.empty:
        top_5_job_titles = (
            df_filtered.groupby("job_title")["salary_in_usd"]
            .mean()
            .sort_values(ascending=False)
            .head(5)
            .reset_index()
        )
        fig_top5_jobs = px.bar(
            top_5_job_titles,
            x="salary_in_usd",
            y="job_title",
            orientation="h",
            title="Top 5 cargos com maiores médias salariais",
            color="job_title",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            labels={
                "job_title": "Cargo",
                "salary_in_usd": "Salário (USD)",
            },
        )
        fig_top5_jobs.update_layout(
            showlegend=False,
            title_x=0.3,
            yaxis_title="",
            xaxis_title="Salário (USD)",
        )
        st.plotly_chart(fig_top5_jobs, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível para o filtro selecionado.")

col_graf3 = st.columns(1)

# destribuicao de salarios anuais
if not df_filtered.empty:
    fig_salary_distribution = px.histogram(
        df_filtered,
        x="salary_in_usd",
        nbins=10,
        title="Distribuição de Salários Anuais",
        color="work_year",
        color_discrete_sequence=px.colors.qualitative.Pastel,
        barmode="overlay",
        opacity=1,
        labels={
            "work_year": "Ano",
            "salary_in_usd": "Salário (USD)",
        },
    )
    fig_salary_distribution.update_layout(
        title_x=0.4,
        yaxis_title="Total de Registros",
        xaxis_title="Salário (USD)",
        showlegend=True,
        legend_title="Ano",
        legend_x=0.8,
        legend_y=1,
    )
    st.plotly_chart(fig_salary_distribution, use_container_width=True)
else:
    st.warning("Nenhum dado disponível para o filtro selecionado.")

# evolucao do salario de acordo com o tamanho da empresa
col_graf4, col_graf5 = st.columns(2)

with col_graf4:
    if not df_filtered.empty:
        salary_by_company_size = (
            df_filtered.groupby(["work_year", "company_size"])["salary_in_usd"]
            .mean()
            .reset_index()
        )
        fig_company_size = px.line(
            salary_by_company_size,
            x="work_year",
            y="salary_in_usd",
            title="Tendencia Salarial por Tamanho da Empresa",
            markers=True,
            color="company_size",
            color_discrete_sequence=px.colors.qualitative.Pastel,
            labels={
                "work_year": "Ano",
                "salary_in_usd": "Salário (USD)",
                "company_size": "Tamanho da Empresa",
            },
            template="plotly_white",
        )
        fig_company_size.update_layout(
            title_x=0.3,
            yaxis_title="Salário (USD)",
            xaxis_title="Ano",
            showlegend=True,
            legend_title="Tamanho da Empresa",
            legend_x=0.8,
            legend_y=1,
            hovermode="x unified",
            yaxis_tickformat=",.2f",
        )
        st.plotly_chart(fig_company_size, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível para o filtro selecionado.")

with col_graf5:
    if not df_filtered.empty:
        remote_count = df_filtered["remote_ratio"].value_counts().reset_index()
        remote_count.columns = ["remote_ratio", "count"]
        fig_remote_count = px.pie(
            remote_count,
            names="remote_ratio",
            values="count",
            title="Proporção de Trabalho Remoto",
            hole=0.5,
            color_discrete_sequence=px.colors.qualitative.Pastel,
            labels={
                "remote_ratio": "Modalidade de Trabalho",
                "count": "Quantidade de Registros",
            },
        )
        fig_remote_count.update_layout(
            title_x=0.3,
            yaxis_title="Quantidade de Registros",
            xaxis_title="Modalidade de Trabalho",
            showlegend=True,
            legend_title="Modalidade de Trabalho",
            legend_x=0.8,
            legend_y=1,
            hovermode="x unified",
            yaxis_tickformat=",.2f",
        )
        st.plotly_chart(fig_remote_count, use_container_width=True)
    else:
        st.warning("Nenhum dado disponível para o filtro selecionado.")

# mapa mundi do salario pela localizacao
if not df_filtered.empty:
    mean_salary_by_country = (
        df_filtered.groupby("employee_residence")["salary_in_usd"].mean().reset_index()
    )
    unique_jobs = sorted(df_filtered["job_title"].unique())

    # Lógica para definir titulo e dados de cargo para o hover
    if len(unique_jobs) == 1:
        title_map = f"Salário Médio por País - {unique_jobs[0]} por pais"
        mean_salary_by_country["Cargo"] = unique_jobs[0]
        label_cargo = "Cargo"
    else:
        if len(job_title_selected) < 1:
            title_map = "Salário Médio por País para todos os cargos"
        else:
            title_map = "Salário Médio por País (Cargos Selecionados)"

        # Identifica o cargo mais comum por país para mostrar no hover
        top_jobs = (
            df_filtered.groupby("employee_residence")["job_title"]
            .agg(lambda x: x.mode()[0])
            .reset_index()
        )
        top_jobs.columns = ["employee_residence", "Cargo"]
        mean_salary_by_country = pd.merge(
            mean_salary_by_country, top_jobs, on="employee_residence"
        )
        label_cargo = "Cargo (Mais Comum)"

    # gerando grafico
    map_graf = px.choropleth(
        mean_salary_by_country,
        locations="employee_residence",
        color="salary_in_usd",
        color_continuous_scale="Viridis",
        title=title_map,
        hover_data=["Cargo"],
        labels={
            "employee_residence": "País",
            "salary_in_usd": "Salário (USD)",
            "Cargo": label_cargo,
        },
    )
    map_graf.update_layout(
        title_x=0.3,
        yaxis_title="Salário (USD)",
        xaxis_title="País",
        showlegend=True,
        legend_title="País",
        legend_x=0.8,
        legend_y=1,
        hovermode="x unified",
        yaxis_tickformat=",.2f",
        margin={
            "r": 0,
            "t": 50,
            "l": 0,
            "b": 0,
        },  # Remove margens brancas inúteis no mapa
    )
    st.plotly_chart(map_graf, use_container_width=True)
else:
    st.warning("Nenhum dado disponível para o filtro selecionado.")
