import pandas as pd

df = pd.read_pickle('padron.pkl')

'''
0       FED-107003   [51314, 126914]
1       IFO-012223    [14624, 14648]
2       PEF-042542  [126621, 127308]
'''

print(f'Numero economico: FED-107003 {df.iloc[51314]}')
print(f'Numero economico: FED-107003 {df.iloc[126914]}')
print(f'Numero economico: IFO-012223 {df.iloc[14624]}')
print(f'Numero economico: IFO-012223 {df.iloc[14648]}')
print(f'Numero economico: PEF-042542 {df.iloc[126621]}')
print(f'Numero economico: PEF-042542 {df.iloc[127308]}')