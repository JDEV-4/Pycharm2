import pandas as pd
import matplotlib.pyplot as plt

df_movies = pd.read_csv("Data/Rotten Tomatoes Movies.csv")
print(df_movies.head())

# 1. Convertir la columna
df_movies['in_theaters_date'] = pd.to_datetime(df_movies['in_theaters_date'], errors='coerce')

# 2. Cuántas películas hay en total?
total_peliculas = len(df_movies)
print(f"\nNúmero total de películas: {total_peliculas}")

# 3. Cómo se distribuyen las calificaciones?
calificaciones = df_movies['tomatometer_status'].value_counts()
print("\nDistribución de calificaciones del tomatómetro:")
print(calificaciones)

# 4. Gráfico circular
plt.figure(figsize=(8, 6))
plt.pie(calificaciones, labels=calificaciones.index, autopct='%1.1f%%', startangle=90, colors=['#66c2a5', '#fc8d62', '#8da0cb'])
plt.title("Distribución de calificaciones del tomatómetro")
plt.axis('equal')  # Para que sea un círculo
plt.show()
