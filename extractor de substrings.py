import pandas as pd
import re
df = pd.read_csv("calles1.csv", index_col="Id", encoding="latin-1", sep=";") #DataFrame donde está la celda con las substrings a extraer
df2 = pd.read_excel("direcciones.xlsx") #DataFrame que se utiliza como direccionario para la comparación con el primer DataFrame
a = df["Direccion"].to_list()
b = df2["Descripción"].to_list()
c = df2.Descripción.str.extractall(f"({'|'.join(df['Direccion'])})").unstack() #Función que extrae las substrings provistas el df2, compara cada ROW con el df2
c.to_csv("calles.csv") #Guarda en csv las substrings extraidas. 
