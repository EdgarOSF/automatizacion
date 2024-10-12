from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
# import psycopg2

#INPUT YOUR OWN CONNECTION STRING HERE
conn_string = "postgresql://desarrollo:salud2024@localhost:3000/departamento_inventario"

# Configurar pandas para mostrar todas las filas
# pd.set_option('display.max_rows', None)

# df = pd.read_excel('PADRON+CATALOGO  GENERAL JULIO 2024 CON SUSTITUCIONES.xlsx')

# Guardar el DataFrame como un archivo pickle
# df.to_pickle('padron.pkl', index=False, encoding='utf-8')

df = pd.read_pickle('padron.pkl')

# Tamaño del dt antes de la limpieza
# print(df.shape)

# Extraer solo una fila del dt por su index
# print(df.iloc[16227])

# Filtrar filas donde 'columna1' y 'columna3' tienen valores vacíos
filas_vacias = df[df[['fuente_financiamiento_id', 'numero_economico', 'numero_inventario', 'nombre_completo', 'numero_resguardo']].isnull().all(axis=1)]
# print(filas_vacias)

df_sin_vacios = df.drop(filas_vacias.index)

df_sin_vacios = df_sin_vacios.drop(126914)
df_sin_vacios = df_sin_vacios.drop(14648)
df_sin_vacios = df_sin_vacios.drop(127308)

# Agregar la columna "estatus" con valor 1 (entero)
df_sin_vacios['estatus'] = 1

# Agregar las columnas "fecha_captura" y "fecha_actualizacion" con valores estáticos de tipo datetime
fecha_captura = datetime(2024, 9, 1)  # Fecha válida de este año y mes (ejemplo: 1 de septiembre de 2024)
fecha_actualizacion = datetime(2024, 9, 1)  # Fecha válida de este año y mes (ejemplo: 2 de septiembre de 2024)

df_sin_vacios['fecha_captura'] = fecha_captura
df_sin_vacios['fecha_actualizacion'] = fecha_actualizacion

# Convertir la columna 'fecha' a formato datetime, forzando valores inválidos a NaT
df_sin_vacios['fecha_entrada'] = pd.to_datetime(df_sin_vacios['fecha_entrada'], errors='coerce')

#perform to_sql test and print result
db = create_engine(conn_string)
conn = db.connect()

df_sin_vacios.to_sql('BienFisico', con=conn, if_exists='append', index=False, chunksize=1000)

print('Listo!')

# Tamaño del dt despues de limpieza
# print(df_sin_vacios.shape)
