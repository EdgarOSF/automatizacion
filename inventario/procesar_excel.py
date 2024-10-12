import pandas as pd

# Import .csv file
df = pd.read_excel('./PADRON+CATALOGO  GENERAL JULIO 2024-sin-duplicidad.xlsx')
# Guardar el DataFrame como un archivo pickle
df.to_pickle('padron.pkl')
# Leer archivo
df = pd.read_pickle('padron.pkl')

# Eliminar varias columnas
df.drop(columns=[
    'NUM.',
    'NOMBRE DE LA PARTIDA',
    'NUM DE UBICACIÓN FINAL',
    'UNIDAD DE SALIDA',
    'UNIDAD A CARGO',
    'APELLIDO PATERNO',
    'APELLIDO MATERNO',
    'NOMBRES',
    'RFC',
    'CURP'
], inplace=True)

print(df.head())
