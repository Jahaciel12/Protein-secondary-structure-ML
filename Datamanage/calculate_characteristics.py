import pandas as pd
import Dictionaris_input_values

#from clustered data where we have primari structure and secondari, we calculate charge, polarity and size of aa
#also one hot encoding for prim and sec

df = pd.read_csv('Cleanclustered.csv')

#vamos a eliminar las X en las estructuras de prot
aminoacidos = [
    'A', 'R', 'N', 'D', 'C', 'E', 'Q', 'G', 'H', 'I',
    'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V'
]
def eliminarXs(dfprim, dfsec):
    listprim = []
    listsec = []

    for seq1 in dfprim:
        listprim.append(seq1)
    for seq2 in dfsec:
        listsec.append(seq2)

    listafinal1 = []
    listafinal2 = []
    for seqprim, seqsec in zip(listprim, listsec):
        nuevacad1 = ''
        nuevacad2 = ''
        for aa, st in zip(seqprim, seqsec):
            if aa in aminoacidos:
                nuevacad1 += aa
                nuevacad2 += st
        listafinal1.append(nuevacad1)
        listafinal2.append(nuevacad2)
    return listafinal1, listafinal2

#index_to_drop = df[df['ID'] == '4CAT'].index
#df = df.drop(index_to_drop)
#struc1, struc2 = eliminarXs(df['Estructura primaria'], df['Estructura dssp'])
#df['Estructura primaria'] = struc1
#df['Estructura dssp'] = struc2
#df = df.dropna()
#df.to_csv('Cleanclustered.csv', index=False)

#hacemos todos los inputs/outputs para el modelo
df['Isoelectric point'] = df['Estructura primaria'].apply(lambda seq: [Dictionaris_input_values.pi_scaled[aa] for aa in seq])
df['Atomic mass'] = df['Estructura primaria'].apply(lambda seq : [Dictionaris_input_values.mw_scaled[aa] for aa in seq])
df['Polarity'] = df['Estructura primaria'].apply(lambda seq : [Dictionaris_input_values.hydro_scaled[aa] for aa in seq])
df['One_hot_prim'] = df['Estructura primaria'].apply(lambda seq : [Dictionaris_input_values.one_hot_encoding[aa] for aa in seq])
df['One_hot_sec'] = df['Estructura dssp'].apply(lambda seq: [Dictionaris_input_values.dssp_one_hot[aa] for aa in seq])

df.to_csv('Alldatainout.csv', index=False)



