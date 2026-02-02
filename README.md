# 🎲 Dashboard de Análise de Salários na Área de Dados

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

Este projeto consiste em um dashboard interativo desenvolvido em Python para análise exploratória de dados salariais de profissionais da área de dados (Data Scientists, Analysts, Engineers, etc.) ao redor do mundo.

O objetivo é permitir que o usuário explore tendências de mercado, compare salários por nível de experiência, localização e tamanho da empresa através de uma interface dinâmica e intuitiva.

## 🚀 Demonstração Online

O dashboard está hospedado no Streamlit Cloud e pode ser acessado diretamente pelo navegador:

🔗 **[Clique aqui para acessar o Dashboard em Tempo Real](https://projetodatabase.streamlit.app/)**

---

## 📊 Funcionalidades do Projeto

O dashboard oferece filtros em tempo real (Barra Lateral) que atualizam automaticamente todas as métricas e gráficos:

### 🔎 Filtros Disponíveis:
- **Ano de referência**
- **Nível de Experiência** (Júnior, Pleno, Sênior, Expert)
- **Tipo de Contrato** (Full-time, Freelance, etc.)
- **Cargo** (Data Scientist, Data Engineer, ML Engineer, etc.)
- **Tamanho e Localização da Empresa**

### 📈 Visualizações e KPIs:
1.  **Métricas Rápidas:** Salário Médio, Máximo, Mediano, Cargo mais comum e Total de registros filtrados.
2.  **Média Salarial por Nível de Experiência:** Gráfico de barras comparativo.
3.  **Top 5 Cargos:** Ranking dos cargos com maiores médias salariais.
4.  **Distribuição de Salários:** Histograma para análise da dispersão salarial anual.
5.  **Tendência Salarial:** Gráfico de linha correlacionando ano e tamanho da empresa.
6.  **Modalidade de Trabalho:** Gráfico de pizza mostrando a proporção de trabalho Remoto, Híbrido e Presencial.
7.  **Mapa Global:** Mapa coroplético interativo mostrando a média salarial por país (conversão ISO-3 via `pycountry`).

---

## 🛠️ Tecnologias Utilizadas

* **Python:** Linguagem principal.
* **Streamlit:** Framework para construção da interface web interativa.
* **Plotly Express:** Biblioteca para criação dos gráficos dinâmicos e mapa interativo.
* **Pandas:** Manipulação e filtragem dos dados em memória.
* **Pycountry:** Utilizado no script de tratamento para padronização das siglas de países (ISO-3).

---

## 🗂️ Estrutura do Repositório

O projeto está organizado da seguinte forma:

- `App.py`: Código principal da aplicação Dashboard. Contém a lógica de interface, filtros e construção dos gráficos.
- `TratamentoDataFrame.py`: Script de ETL (Extração e Tratamento). Responsável por limpar a base original, traduzir siglas (Ex: "EN" -> "Junior") e converter códigos de países para ISO-3 para compatibilidade com o mapa.
- `requirements.txt`: Lista de dependências do projeto.
- `database/`: Pasta contendo o arquivo CSV tratado (`dataBase_salary.csv`).

---

## 💻 Como Rodar o Projeto Localmente

Se você deseja rodar este projeto na sua própria máquina, siga os passos abaixo:

#### 1. Clone o repositório
```bash
git clone [https://github.com/IRam0Ss/ProjetoDataBase.git](https://github.com/IRam0Ss/ProjetoDataBase.git)
cd ProjetoDataBase
```
#### 2. Crie um ambiente virtual (Opcional, mas recomendado)
```bash
##### Windows
python -m venv venv
.\venv\Scripts\activate
```
##### Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
```
#### 3. Instale as dependencias
```bash
pip install -r requirements.txt
```
#### 4. Execute a aplicacao
```bash
streamlit run App.py
```
# ✒️ Autor
Desenvolvido por Iury Ramos Sodre  
**Linkedin** = www.linkedin.com/in/iuryramossodre  
**GitHub** = https://github.com/IRam0Ss

---  
# 🎲 Data Science Salaries Dashboard

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

This project is an interactive dashboard built with Python to explore global salary data for data professionals (Data Scientists, Analysts, Engineers, etc.).

The goal is to allow users to explore market trends, compare salaries by experience level, location, and company size through a dynamic and intuitive interface.

## 🚀 Live Demo

The dashboard is hosted on Streamlit Cloud and can be accessed directly via the browser:

🔗 **[Click here to access the Dashboard](https://projetodatabase.streamlit.app/)**

---

## 📊 Features

The dashboard offers real-time filters (Sidebar) that automatically update all metrics and charts:

### 🔎 Available Filters:
- **Reference Year**
- **Experience Level** (Junior, Mid-level, Senior, Expert)
- **Employment Type** (Full-time, Freelance, etc.)
- **Job Title** (Data Scientist, Data Engineer, ML Engineer, etc.)
- **Company Size & Location**

### 📈 Visualizations & KPIs:
1.  **Quick Metrics:** Average Salary, Max Salary, Median Salary, Most Common Job, and Total Records.
2.  **Salary by Experience:** Comparative bar chart.
3.  **Top 5 Jobs:** Ranking of job titles with the highest average salaries.
4.  **Salary Distribution:** Histogram to analyze annual salary spread.
5.  **Salary Trends:** Line chart correlating year and company size.
6.  **Work Models:** Pie chart showing the ratio of Remote, Hybrid, and On-site work.
7.  **Global Map:** Interactive choropleth map showing average salary by country (ISO-3 conversion via `pycountry`).

---

## 🛠️ Tech Stack

* **Python:** Main language.
* **Streamlit:** Framework for building the interactive web interface.
* **Plotly Express:** Library for creating dynamic charts and maps.
* **Pandas:** In-memory data manipulation and filtering.
* **Pycountry:** Used in the ETL script to standardize country codes (ISO-3).

---

## 🗂️ Project Structure

The repository is organized as follows:

```text
├── database/
│   └── dataBase_salary.csv    # Processed data
├── App.py                     # Main Dashboard application
├── TratamentoDataFrame.py     # ETL Script (Cleaning & ISO-3 conversion)
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---  

## 💻 How to Run Locally

If you wish to run this project on your local machine, follow the steps below:

#### 1. Clone the repository
```bash
git clone [https://github.com/IRam0Ss/ProjetoDataBase.git](https://github.com/IRam0Ss/ProjetoDataBase.git)
cd ProjetoDataBase
```
#### 2. Create a Virtual Environment (Optional but recommended)

##### Windows
```bash
python -m venv venv
.\venv\Scripts\activate
```
###### Linux/Mac
```bash
python3 -m venv venv
source venv/bin/activate
```
#### 3. Install dependencies
``` bash
pip install -r requirements.txt
```
#### 4. Run the application
``` bash
streamlit run App.py
```

#✒️ Author

Developed by Iury Ramos Sodré

**Linkedin** = www.linkedin.com/in/iuryramossodre  
**GitHub** = https://github.com/IRam0Ss
