# 1. Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt


df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")
print(df_movies.head())

#primeras filas del DataFrame
print(df_movies.head())

#nombres de las columnas y sus tipos de datos
print("\nTipos de datos originales:")
print(df_movies.dtypes)

#Convertir la columna
df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

#conversión fue exitosa
print("\nTipos de datos después de conversión:")
print(df_movies.dtypes)

#Mostrar si hubo valores no convertidos (NaT)
missing_dates = df_movies['in_theaters_date'].isna().sum()
print(f"\nPelículas con fechas no reconocidas: {missing_dates}")