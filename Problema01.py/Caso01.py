import pandas as pd

# Cargar el archivo airbnb.csv
df = pd.read_csv('/workspaces/PC05Python/data/airbnb.csv')

# Filtrar las habitaciones
filtered_df = df[(df['reviews'] > 10) & (df['overall_satisfaction'] > 4) & (df['bedrooms'] >= 2)]

# Ordenar las habitaciones de mejor a peor puntuación y luego por cantidad de críticas
sorted_df = filtered_df.sort_values(by=['overall_satisfaction', 'reviews'], ascending=[False, False])

# Seleccionar las 3 mejores opciones
top_3_options = sorted_df.head(3)

# Mostrar las opciones seleccionadas
print(top_3_options[['room_id', 'neighborhood', 'overall_satisfaction', 'reviews']])