from fastapi import FastAPI
from app.routes import dispatch, patch, rastro, motorista, rota, cancelamento

app = FastAPI(title="Tout Courier API")

app.include_router(dispatch.router, prefix="/api")
app.include_router(patch.router, prefix="/api")
app.include_router(rastro.router, prefix="/api")
app.include_router(motorista.router, prefix="/api")
app.include_router(rota.router, prefix="/api")
app.include_router(cancelamento.router, prefix="/api")
