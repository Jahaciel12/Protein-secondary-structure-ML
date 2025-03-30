import os
import requests


directorio = 'pdb_files_for_prediction'
os.makedirs(directorio, exist_ok=True)
url = "https://files.rcsb.org/download/"
pdb_ID = []

with open('pdb_ides.txt', 'r') as pdb_ids:
    for id in pdb_ids:
        id = id.strip()
        pdb_ID.append(id)

for ID in pdb_ID:
    fin_url = f'{url}{ID}.pdb'
    respuesta = requests.get(fin_url)
    if respuesta.status_code == 200:
        file_path = os.path.join(directorio, f"{ID}.pdb")
        with open(file_path, "w") as f:
            f.write(respuesta.text)
        print(f"Descargado: {file_path}")
    else:
        print(f"Error descargando {ID}: {respuesta.status_code}")
