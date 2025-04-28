import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")

df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

# 1. Contar cuántas películas ha dirigido cada director
conteo_directores = df_movies['directors'].value_counts()

# 2. Obtener los 10 directores más frecuentes
top_10_directors = conteo_directores.head(10)
print("\nTop 10 directores con más películas:")
print(top_10_directors)

# 3. Filtrar las películas
top_10_director_names = top_10_directors.index.tolist()
df_top_10 = df_movies[df_movies['directors'].isin(top_10_director_names)].copy()

# 4. Calcular el promedio
promedio_tomatometro_por_director = df_top_10.groupby('directors')['tomatometer_rating'].mean().sort_values(ascending=False)

# 5. Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(promedio_tomatometro_por_director.index, promedio_tomatometro_por_director.values, color='skyblue', edgecolor='black')
plt.title("Calificación Promedio (Tomatometer) de los Top 10 Directores Más Frecuentes")
plt.xlabel("Director")
plt.ylabel("Calificación Promedio")
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
