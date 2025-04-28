import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")

print(df_movies.head())

# 1. Convertir la columna 'in_theaters_date' a datetime
df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

# 2. Promedio de valoración del tomatómetr
promedio_criticos = df_movies['tomatometer_rating'].mean()

# 3. Promedio de valoración del publico
promedio_audiencia = df_movies['audience_rating'].mean()

# 4. Mostrar resultados
print(f"\nPromedio de valoración por críticos: {promedio_criticos:.2f}")
print(f"Promedio de valoración por audiencia: {promedio_audiencia:.2f}")

# 5. (audiencia - críticos)
df_movies['rating_diff'] = df_movies['audience_rating'] - df_movies['tomatometer_rating']

# 6. Mostrar algunas filas para ver la nueva columna
print("\nPrimeras filas con diferencia de valoraciones:")
print(df_movies[['movie_title', 'audience_rating', 'tomatometer_rating', 'rating_diff']].head())

# 7. Histograma de la diferencia entre valoración de audiencia y críticos
plt.figure(figsize=(8, 6))
plt.hist(df_movies['rating_diff'].dropna(), bins=30, color='skyblue', edgecolor='black')
plt.title("Histograma de la diferencia entre valoración de audiencia y críticos")
plt.xlabel("Diferencia (audiencia - críticos)")
plt.ylabel("Cantidad de películas")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
