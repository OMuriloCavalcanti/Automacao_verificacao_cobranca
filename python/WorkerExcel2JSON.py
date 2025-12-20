from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

excel_path = BASE_DIR / "excel" / "tabela_clientes.xlsx"
json_path = BASE_DIR / "json" / "clientes.json"

df = pd.read_excel(excel_path)

df = df.rename(columns={
    "Nome": "nome",
    "CPF": "cpf",
    "Rua": "rua",
    "Bairro": "bairro",
    "Cidade": "cidade",
    "Número da casa": "numeroCasa",
    "Complemento": "complemento",
    "CEP": "cep"
})

df = df.fillna("")

json_path.parent.mkdir(parents=True, exist_ok=True)

df.to_json(
    json_path,
    orient="records",
    force_ascii=False,
    indent=2
)

print("JSON gerado com sucesso!")
