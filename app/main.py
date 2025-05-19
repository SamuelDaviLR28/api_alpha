from fastapi import FastAPI
from app.routes import dispatch, patch, rastro, motorista, rota, cancelamento

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API rodando online com sucesso!"}

# Inclui as rotas existentes
app.include_router(dispatch.router)
app.include_router(patch.router)
app.include_router(rastro.router)
app.include_router(motorista.router)
app.include_router(rota.router)
app.include_router(cancelamento.router)
