import pandas as pd

# Cargar el archivo airbnb.csv
df = pd.read_csv('/workspaces/PC05Python/data/airbnb.csv')

lisbon_properties = df[df['city'] == 'Lisbon']

affordable_properties = lisbon_properties[lisbon_properties['price'] <= 50]

# Dar preferencia a las habitaciones compartidas y ordenar por puntuación de mejor a peor
shared_rooms = affordable_properties[affordable_properties['room_type'] == 'Shared room']
sorted_shared_rooms = shared_rooms.sort_values(by=['overall_satisfaction'], ascending=False)

# Si hay menos de 10 habitaciones compartidas, completamos con las propiedades no compartidas
if len(sorted_shared_rooms) < 10:
    non_shared_rooms = affordable_properties[affordable_properties['room_type'] != 'Shared room']
    remaining = 10 - len(sorted_shared_rooms)
    top_properties = pd.concat([sorted_shared_rooms.head(remaining), non_shared_rooms.head(10 - remaining)])
else:
    top_properties = sorted_shared_rooms.head(10)

# Mostrar las 10 propiedades seleccionadas
print(top_properties[['room_id', 'neighborhood', 'price', 'overall_satisfaction', 'room_type']])