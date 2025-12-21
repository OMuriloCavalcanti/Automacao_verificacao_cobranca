from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent

json_path = BASE_DIR / "json" / "json_clientes.json"
excel_path = BASE_DIR / "excel" / "tabela_clientes_tratados.xlsx"

df = pd.read_json(json_path)

df = df.rename(columns={
    "nome": "Nome",
    "cpf": "CPF",
    "rua": "Rua",
    "bairro": "Bairro",
    "cidade": "Cidade",
    "numeroCasa": "Número da casa",
    "complemento": "Complemento",
    "cep": "CEP"
})

excel_path.parent.mkdir(parents=True, exist_ok=True)

df.to_excel(
    excel_path,
    index=False
)

print("Excel gerado com sucesso!")
