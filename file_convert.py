import pandas as pd

df_datos = pd.read_csv('OpenBootCamp\example.csv')
df_datos.to_excel('OpenBootCamp\example.xlsx', index=False)