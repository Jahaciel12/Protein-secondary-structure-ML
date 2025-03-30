import subprocess


def cd_hit_run(fasta_in, fasta_out, identity=0.9):

    comando = [
        "cd-hit",  # Asegúrate de que cd-hit esté en tu PATH
        "-i", fasta_in,  # Archivo de entrada
        "-o", fasta_out,  # Archivo de salida
        "-c", str(identity),
    ]

    resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
    print('cluster con exito')


cd_hit_run('forcluster.fasta', 'clustered.fasta')
