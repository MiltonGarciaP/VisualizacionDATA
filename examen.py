import pandas as pd
import matplotlib as plt
#1.Cargar el archivo 'netflix_title.csv'
data = pd.read_csv('netflix_titles.csv')


#2.Visualizar los primeros 10 registros del conjunto de datos
print("")
print("Los 10 primero registro")
print(data.head(10))
#3. Visualizar los últimos 15 registros del conjunto de datos
print("")
print("Los últimos 15 registros")
print(data.tail(15))


#4. Generar los estadísticos básicos
years = data[data['release_year'] >= 2010]
years = years['release_year']
years = years.values.tolist()
years = set(years)
years = list(years)
years.sort()

print(years)

#5. Completar todos los datos vacíos (na) con ceros (0)
print("Todos los datos vacíos remplazados por ceros ")
datanew = data.fillna(0)
print(datanew.to_string())

#6. Generar un gráfico de tipo barras que compare películas vs s
#desde el 2010 hasta el 2021. El resultado del grafico debe ser algo asi:
movie =  data[data['type'] == 'Movie']
movie = movie[movie['release_year'] >= 2010]

tv_show =  data[data['type'] == 'TV Show']
tv_show = tv_show[tv_show['release_year'] >= 2010]

movie = movie.groupby('release_year').size()
tv_show = tv_show.groupby('release_year').size()

print(movie)

df = pd.DataFrame({'Movies': movie, 'Tv Shows': tv_show}, index = years)

ax = df.plot.bar(rot=0)

plt.show()