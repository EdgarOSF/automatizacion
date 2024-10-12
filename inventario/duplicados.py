import pandas as pd


# df = pd.read_excel('PADRON_CATALOGO.xlsx', usecols=['numero_economico'])
df = pd.read_pickle('padron.pkl')

# Quitar celdas con datos vacios
# df = df.apply(lambda x: pd.Series(x.dropna().values))

# Extraemos los datos duplicados
duplicados = df[df.duplicated(subset=['numero_economico'], keep=False)]  # Incluye todos los duplicados
# Agrupamos los datos duplicados y se realiza conteo de cuantas veces se repiten
conteo_duplicados = duplicados.groupby('numero_economico').size().reset_index(name='conteo')
# print(conteo_duplicados)
print(conteo_duplicados)