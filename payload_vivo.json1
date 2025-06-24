import json
from app.schemas.dispatch import DispatchToutbox

with open("payload_vivo.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

try:
    modelo = DispatchToutbox(**dados)
    print("✅ Payload validado com sucesso!")
except Exception as e:
    print("❌ Erro ao validar payload:")
    print(e)
