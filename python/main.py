import subprocess

print("Rodando Python...")
subprocess.run(
    ["python", "python/WorkerExcel2JSON.py"],
    check=True
)

print("Rodando JavaScript...")
subprocess.run(
    ["node", "js/WorkerVerificaDados.js"],
    check=True
)

print("Pipeline finalizado com sucesso!")