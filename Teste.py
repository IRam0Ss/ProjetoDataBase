import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/IRam0Ss/ProjetoDataBase/refs/heads/main/database/dataBase_salary.csv"
)

print(df.info())
