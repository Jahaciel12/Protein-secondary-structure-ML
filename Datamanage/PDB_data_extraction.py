from Bio.PDB import PDBParser, DSSP
import pandas as pd
import os

def lista_archivos_pdb(dir_archiv):
    lista_files = []
    for f in os.listdir(dir_archiv):
        lista_files.append(f)
    return lista_files


# extrae de un pdb, la sequencia primaria y estructura secundaria por cadenas
def prim_sec_struct(pdbfile):
    parser = PDBParser()
    structure = parser.get_structure('PDB_ID', pdbfile)
    model = structure[0]
    dssp = DSSP(model, pdbfile)
    id = pdbfile.strip('.pdb')
#iteramos sobre el objeto dssp que es un diccionario
    dic_result_cadenas = {}

    for key in dssp.keys():
        cadena = key[0]
        if cadena not in dic_result_cadenas:
            dic_result_cadenas[cadena] = {'prim': [], 'sec': []}

        result = dssp[key]
        dic_result_cadenas[cadena]['prim'].append(result[1])
        if result[2] == '-':
            dic_result_cadenas[cadena]['sec'].append('C')
        else:
            dic_result_cadenas[cadena]['sec'].append(result[2])

    lista_resulatdos = []
    for llave in dic_result_cadenas:
        lista_resulatdos.append((''.join(dic_result_cadenas[llave]['prim']), ''.join(dic_result_cadenas[llave]['sec']), id, llave))


    #devuelve una lista de tuplas, cada tupla contiene la prim, la sec, el id y la cadena
    return lista_resulatdos


def tupla_a_csv(prim, sec, id, cadena):
    data = {
        'ID': id,
        'Cadena': cadena,
        'Estructura primaria': prim,
        'Estructura dssp': sec
    }
    df = pd.DataFrame(data)
    df.to_csv('Rawdata.csv', index = False)
    print('csv creado con exito')


if __name__ == '__main__':
    #sacamos lista de todos los pdbs que tenemos en el directorio
    list_archiv = lista_archivos_pdb(r'C:\Users\jahac_1jki8d0\PycharmProjects\SecondaryStructurePred\pdb_files_for_prediction')

    #lista con todas las tuplas (prim, sec, id, chain)
    list_tuplas = []
    for archiv in list_archiv:
        path_archivo = os.path.join(r'C:\Users\jahac_1jki8d0\PycharmProjects\SecondaryStructurePred\pdb_files_for_prediction', archiv)
        try:
            list_tuplas.extend(prim_sec_struct(path_archivo))
        except Exception as e:
            print(f'Error procesar archivo {e}')
    #lista de cada parte del csv extraido de las tuplas
    prim = [a[0] for a in list_tuplas]
    sec = [a[1] for a in list_tuplas]
    id = [a[2] for a in list_tuplas]
    chain = [a[3] for a in list_tuplas]

    tupla_a_csv(prim, sec, id, chain)
