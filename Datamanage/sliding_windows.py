import pandas as pd

csv_file = 'Alldatainout.csv'

df = pd.read_csv(csv_file)

def break_windows(n, df):
    for entry in df:
        ide = entry['ID']
        windows_prim = []
        windows_sec = []
        for aa in range(len(entry['One_hot_prim'])):
            win = entry['One_hot_prim'][0+aa, n+aa]
            windows_prim.append(win)
        for aa in range(len(entry['One_hot_sec'])):
            win = entry['One_hot_sec'][0+aa, n+aa]
            windows_sec.append(win)
#hay que hacer las listas que correspondan a las filas del nuevo data frame.
