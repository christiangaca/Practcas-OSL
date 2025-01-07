import pandas as pd
import matplotlib.pyplot as plt

# Cargamos los datos desde un archivo CSV
datos = pd.read_csv('/home/christiangc/Practica Python/Ultimo_formato.csv')

# Seleccionamos la columna 'Nada' y eliminamos valores NaN
columna_g = datos['Nada'].dropna()

# Dividimos los términos separados por comas y aplanamos la lista de listas en una sola lista
todas_las_palabras = [palabra.strip() for sublist in columna_g.str.split(',') for palabra in sublist]

# Contamos la cantidad de 'Nada' y no 'Nada'
nada_count = len(columna_g[columna_g == 'Nada'])
not_nada_count = len(todas_las_palabras) - nada_count

# Crear gráfico circular que muestra el % de asignaturas que utilizan software libre
labels = ['No', 'Sí']
sizes = [nada_count, not_nada_count]
explode = (0.1, 0)  # solo "explota" la primer porción

plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  # iguala las longitudes de los ejes para que el gráfico sea circular
plt.title('¿Utiliza software libre?')
#plt.show()

# Guardamos la gráfica como un archivo de imagen
output_path = '/home/christiangc/Practica Python/porcentaje_utilizacion_sl.png'
plt.savefig(output_path)
plt.show()

# Contamos la frecuencia de cada palabra
conteo_palabras = pd.Series(todas_las_palabras).value_counts()

# Agrupamos las palabras que aparecen una sola vez en el grupo "Otros"
conteo_palabras['Otros'] = conteo_palabras[conteo_palabras == 1].sum()
conteo_palabras = conteo_palabras.drop(conteo_palabras[conteo_palabras == 1].index)

# Mostramos las palabras agrupadas por frecuencia en una gráfica de barras
plt.figure(figsize=(20, 14))
conteo_palabras.sort_values(ascending=False).plot(kind='bar', width=0.8)
plt.xlabel('Palabras', fontsize=14)
plt.ylabel('Frecuencia', fontsize=14)
plt.title('Software libre utilizado según sus apariciones', fontsize=16)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout(pad=3.0)

# Guardamos la gráfica como un archivo de imagen
output_path_1 = '/home/christiangc/Practica Python/frecuencia_palabras.png'
plt.savefig(output_path_1)
plt.show()