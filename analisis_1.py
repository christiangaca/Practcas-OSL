import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
datos = pd.read_csv('/home/christiangc/Practica Python/Ultimo_formato.csv')

# Procesar la columna 'g'
conteo_g = datos['g'].value_counts()
conteo_g['Otros'] = conteo_g[conteo_g == 1].sum()
conteo_g = conteo_g.drop(conteo_g[conteo_g == 1].index)

# Crear la gráfica de barras
plt.figure(figsize=(20, 14))
conteo_g.sort_values(ascending=False).plot(kind='bar', width=0.8)
plt.xlabel('Elementos', fontsize=14)
plt.ylabel('Frecuencia', fontsize=14)
plt.title('Gráfica de frecuencia agrupando elementos que aparecen una sola vez en "Otros"', fontsize=16)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout(pad=3.0)

# Guardar la gráfica como un archivo de imagen
output_path = '/home/christiangc/Practica Python/frecuencia_g.png'
plt.savefig(output_path)
plt.show()