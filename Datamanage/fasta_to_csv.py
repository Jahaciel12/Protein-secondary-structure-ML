import pandas as pd
from Bio import SeqIO


def fasta_to_csv(fasta_file):
    ides = []
    seqs = []
    for res in SeqIO.parse(fasta_file, 'fasta'):
        ides.append(res.id)
        seqs.append(res.seq)

    ide_cad = []
    ide = []
    cad = []
    for i in ides:
        ide_cad.append(i.split('_'))
    for j in ide_cad:
        ide.append(j[0])
        cad.append(j[1])

    df = pd.read_csv('Rawdata.csv', delimiter= ';', on_bad_lines='skip')
    data = {
        'ID': ide,
        'Cadena': cad
    }
    df_combin = pd.DataFrame(data)
    df_resultado = pd.merge(df, df_combin, on=['ID', 'Cadena'], how='inner')
    #df_resultado.to_csv('Clustered.csv')
    print(len(ide))



fasta_to_csv('clustered.fasta')



