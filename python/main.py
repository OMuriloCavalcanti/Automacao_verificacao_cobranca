import subprocess

print("Rodando WORKER 1...")
subprocess.run(
    ["python", "python/WorkerExcel2JSON.py"],
    check=True
)

print("Rodando WORKER 2...")
subprocess.run(
    ["node", "js/WorkerVerificaDados.js"],
    check=True
)

print("Rodando WORKER 3...")
subprocess.run(
    ["python", "python/WorkerJSON2Excel.py"],
    check=True
)

print("Pipeline finalizado com sucesso!")