import pandas as pd

df = pd.read_csv('Cleanclustered.csv')
aminoacidos = [
    'A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I',
    'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'
]
for seq in range(len(df['Estructura primaria'])):
    for aa in str(df.loc[seq + 1, 'Estructura primaria']):
        if aa not in aminoacidos:
            print(seq)