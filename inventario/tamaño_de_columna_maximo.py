import pandas as pd

# Configurar pandas para mostrar todas las filas
pd.set_option('display.max_rows', None)

df = pd.read_excel('PADRON+CATALOGO  GENERAL JULIO 2024 CON SUSTITUCIONES.xlsx')

# Reemplazar los caracteres no deseados en todas las columnas de tipo string (object)
for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = df[column].str.replace('_x000D_', '', regex=False).str.replace('_x0002_', '', regex=False).replace('S/N', None, regex=False).replace('S/N-', None, regex=False).replace('SIN NUMERO', None, regex=False).str.strip()

# Guardar el DataFrame como un archivo pickle
df.to_pickle('padron.pkl')

# Crear un DataFrame de ejemplo
df = pd.read_pickle('padron.pkl')

# Crear un DataFrame que contendrá los valores con más caracteres por cada columna
max_lenght_values = {}

# Iterar sobre cada columna
for column in df.columns:
    if df[column].dtype == 'object':  # Solo aplicar a columnas de tipo cadena
        # Obtener el valor con más caracteres en la columna
        max_length_index = df[column].str.strip().str.len().idxmax()  # Encuentra el índice del valor con más caracteres
        max_lenght_values[column] = df.loc[max_length_index, column]  # Obtiene el valor correspondiente
    

for i in max_lenght_values:
    print(f'columna: {i}, valor: {max_lenght_values[i]}, long: {len(max_lenght_values[i])}')
# Convertir el resultado a un DataFrame
# df_max_values = pd.DataFrame([max_lenght_values])


# print(df_max_values)
