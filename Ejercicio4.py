import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")

print(df_movies.head())

# 1. Convertir 'in_theaters_date' a datetime
df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

# 2. Crear una copia
df_movies_copy = df_movies.copy()

# 3. Separar los géneros en listas y expandir filas
df_genres_exploded = df_movies_copy.assign(
    genre=df_movies_copy['genre'].str.split(',')
).explode('genre')

# Eliminar espacios en blanco en los género
df_genres_exploded['genre'] = df_genres_exploded['genre'].str.strip()

# 4. Calcular el promedio de audience_rating
promedios_genero = df_genres_exploded.groupby('genre')['audience_rating'].mean().sort_values(ascending=False)

# Mostrar los 10 géneros con mejor promedio
print("\nTop 10 géneros con mejor promedio de audiencia:")
print(promedios_genero.head(10))

# 5. Gráfico circular
top_10_generos = promedios_genero.head(10)

plt.figure(figsize=(8, 8))
plt.pie(top_10_generos, labels=top_10_generos.index, autopct='%1.1f%%', startangle=90, colors=plt.cm.tab10.colors)
plt.title("Top 10 géneros con mejor calificación de audiencia")
plt.axis('equal')  # Para que sea un círculo perfecto
plt.show()