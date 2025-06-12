from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
from app.database import Base

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
