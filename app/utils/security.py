from fastapi import Header, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

security = HTTPBasic()

API_KEYS = ["minha-api-key-secreta"]
VALID_USERS = {"admin": "senha123"}

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key not in API_KEYS:
        raise HTTPException(status_code=403, detail="API Key inválida")
    return x_api_key

def verify_basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "admin")
    correct_password = secrets.compare_digest(credentials.password, VALID_USERS.get(credentials.username, ""))
    if not (correct_username and correct_password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return credentials.username
