from app.database import Base, engine
from app.models import models  
from datetime import datetime


print("Criando tabelas no banco de dados...")
Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!")


from sqlalchemy import Column, Integer, String, DateTime, JSON
from app.database import Base
from datetime import datetime

class Dispatch(Base):
    __tablename__ = "dispatch"
    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String)
    remetente = Column(String)
    destinatario = Column(String)
    data_criacao = Column(DateTime, default=datetime.utcnow)

class Motorista(Base):
    __tablename__ = "motoristas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cpf = Column(String)
    telefone = Column(String)
    cnh = Column(String)
    criado_em = Column(DateTime, default=datetime.utcnow)

class Rastro(Base):
    __tablename__ = "rastro"
    id = Column(Integer, primary_key=True, index=True)
    codigo_pedido = Column(String)
    status = Column(String)
    descricao = Column(String)
    data_evento = Column(DateTime)
    recebido_em = Column(DateTime, default=datetime.utcnow)

class Rota(Base):
    __tablename__ = "rota"
    id = Column(Integer, primary_key=True, index=True)
    codigo_rota = Column(String)
    origem = Column(String)
    destino = Column(String)
    status = Column(String)
    recebido_em = Column(DateTime, default=datetime.utcnow)

class Cancelamento(Base):
    __tablename__ = "cancelamento"
    id = Column(Integer, primary_key=True, index=True)
    codigo_pedido = Column(String)
    motivo = Column(String)
    tipo = Column(String)
    recebido_em = Column(DateTime, default=datetime.utcnow)

class PatchFretePrazo(Base):
    __tablename__ = "patch_frete_prazo"
    id = Column(Integer, primary_key=True, index=True)
    codigo_pedido = Column(String)
    valor_frete = Column(String)
    prazo = Column(String)
    recebido_em = Column(DateTime, default=datetime.utcnow)


class MotoristaCreate(BaseModel):
    nome: str
    cpf: str
    telefone: str
    cnh: str


class RastroCreate(BaseModel):
    codigo_pedido: str
    status: str
    descricao: str
    data_evento: datetime


from pydantic import BaseModel

class RotaCreate(BaseModel):
    codigo_rota: str
    origem: str
    destino: str
    status: str


from pydantic import BaseModel

class CancelamentoCreate(BaseModel):
    codigo_pedido: str
    motivo: str
    tipo: str


from pydantic import BaseModel

class PatchFretePrazoCreate(BaseModel):
    codigo_pedido: str
    valor_frete: str
    prazo: str