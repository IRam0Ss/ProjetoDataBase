import pandas as pd
import pycountry

df = pd.read_csv(
    "https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv"
)

# traducao das siglas
map_experience_level = {
    "SE": "Senior",
    "MI": "Mid-level",
    "EN": "Junior",
    "EX": "Expert",
}
df["experience_level"] = df["experience_level"].map(map_experience_level)

map_employment_type = {
    "FT": "Full-time",
    "PT": "Part-time",
    "FL": "Freelance",
    "CT": "Contract",
}
df["employment_type"] = df["employment_type"].map(map_employment_type)

map_company_size = {
    "S": "Small",
    "M": "Medium",
    "L": "Large",
}
df["company_size"] = df["company_size"].map(map_company_size)

map_remote_ratio = {
    0: "On-site",
    50: "Hybrid",
    100: "Remote",
}
df["remote_ratio"] = df["remote_ratio"].map(map_remote_ratio)

# remocao das linhas nulas, remocao pois a quantidade de nulos eh muito pequena em comparacao ao tamanho do df
df_limpo = df.dropna()

# conversao de tipo, ano tem que ser int64
df_limpo = df_limpo.assign(work_year=df_limpo["work_year"].astype("int64"))


# corecao do pais
def convert_iso2_to_iso3(iso2):
    try:
        return pycountry.countries.get(alpha_2=iso2).alpha_3
    except:  # noqa: E722
        return None


# converte as siglas para iso3
df_limpo = df_limpo.assign(
    employee_residence=convert_iso2_to_iso3(df_limpo["employee_residence"])
)
df_limpo = df_limpo.assign(
    company_location=convert_iso2_to_iso3(df_limpo["company_location"])
)

# exporta para cvs a database tratada
df_limpo.to_csv("dataBase_salary.csv", index=False)
