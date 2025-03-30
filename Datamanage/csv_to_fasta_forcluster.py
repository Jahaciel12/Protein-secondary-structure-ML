import pandas as pd
import csv


def csv_a_fasta(name_csv, name_fasta):
    df = pd.read_csv(name_csv, delimiter= ';', on_bad_lines='skip')
    with open(name_fasta, 'w') as fasta:
        for seq, id, cadena in zip(df['Estructura primaria'], df['ID'], df['Cadena']):
            fasta.write(f'>{id}_{cadena}\n')
            fasta.write(seq + '\n')


csv_a_fasta('Rawdata.csv', 'forcluster.fasta')
