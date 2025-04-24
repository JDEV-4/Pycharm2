# 1. Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt

# 2. Definir la ruta al archivo CSV (no es Excel)
file_path = "C:/Users/Usuario/PycharmProjects/Pycharm2/Data/Rotten Tomatoes Movies.csv"


# 3. Leer el archivo CSV
df_movies = pd.read_csv(file_path)

# 4. Mostrar las primeras filas del DataFrame
print(df_movies.head())

# 5. Verificar los nombres de las columnas y sus tipos de datos
print("\nTipos de datos originales:")
print(df_movies.dtypes)

# 6. Convertir la columna 'in_theaters_date' al tipo datetime
df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

# 7. Verificar que la conversión fue exitosa
print("\nTipos de datos después de conversión:")
print(df_movies.dtypes)

# 8. Mostrar si hubo valores no convertidos (NaT)
missing_dates = df_movies['in_theaters_date'].isna().sum()
print(f"\nPelículas con fechas no reconocidas: {missing_dates}")
