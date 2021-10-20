import pandas as pd
import re
df = pd.read_csv("calles1.csv", index_col="Id", encoding="latin-1", sep=";")
df2 = pd.read_excel("direcciones.xlsx")
a = df["Direccion"].to_list()
b = df2["Descripción"].to_list()
pd.set_option("display.max_rows", None, "display.max_columns", None)
c = df2.Descripción.str.extractall(f"({'|'.join(df['Direccion'])})").unstack()
c.to_csv("colles.csv")
