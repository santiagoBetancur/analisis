import pandas as pd
import matplotlib.pyplot as plt

# Usar barras invertidas dobles para la ruta del archivo
Arexel = 'C:\\Users\\mecho\\OneDrive\\Escritorio\\Nueva carpeta\\Book2.xlsx'

# Leer el archivo Excel
df = pd.read_excel(Arexel, sheet_name='Break Schedule')
print(df.head())

# Convertir la columna de tiempo a tipo datetime
df['End Time'] = pd.to_datetime(df['Start Time'])
print(1)

# Extraer la hora de la columna de tiempo
df['hour'] = df['End Time'].dt.hour

# Contar la frecuencia de cada hora
hourly_demand = df['hour'].value_counts().sort_index()

# Visualizar los resultados
plt.figure(figsize=(10, 6))
hourly_demand.plot(kind='bar')
plt.title('Frecuencia de demanda por hora')
plt.xlabel('Hora del día')
plt.ylabel('Número de demandas')
plt.xticks(range(24))
plt.grid(True)
plt.show()
