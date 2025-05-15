from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    cliente = Column(String, index=True)
    destino = Column(String)
    data_criacao = Column(DateTime, default=datetime.utcnow)

    patches = relationship("Patch", back_populates="pedido")
    ocorrencias = relationship("Ocorrencia", back_populates="pedido")
    motoristas = relationship("Motorista", back_populates="pedido")
    cancelamentos_suspensoes = relationship("CancelamentoSuspensao", back_populates="pedido")
    rotas = relationship("Rota", back_populates="pedido")

class Patch(Base):
    __tablename__ = "patches"
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), index=True)
    valor = Column(Float)
    prazo = Column(String)

    pedido = relationship("Pedido", back_populates="patches")

class Ocorrencia(Base):
    __tablename__ = "ocorrencias"
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), index=True)
    status = Column(String)
    descricao = Column(String)
    data_registro = Column(DateTime, default=datetime.utcnow)

    pedido = relationship("Pedido", back_populates="ocorrencias")

class Motorista(Base):
    __tablename__ = "motoristas"
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), index=True)
    nome = Column(String)
    documento = Column(String)

    pedido = relationship("Pedido", back_populates="motoristas")
    rotas = relationship("Rota", back_populates="motorista")

class Rota(Base):
    __tablename__ = "rotas"
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), index=True)
    motorista_id = Column(Integer, ForeignKey("motoristas.id"), index=True)

    pedido = relationship("Pedido", back_populates="rotas")
    motorista = relationship("Motorista", back_populates="rotas")
    coordenadas = relationship("Coordenada", back_populates="rota")

class Coordenada(Base):
    __tablename__ = "coordenadas"
    id = Column(Integer, primary_key=True, index=True)
    rota_id = Column(Integer, ForeignKey("rotas.id"), index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    timestamp = Column(DateTime)

    rota = relationship("Rota", back_populates="coordenadas")

class CancelamentoSuspensao(Base):
    __tablename__ = "cancelamentos_suspensoes"
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), index=True)
    acao = Column(String)
    motivo = Column(String)
    data_solicitacao = Column(DateTime, default=datetime.utcnow)

    pedido = relationship("Pedido", back_populates="cancelamentos_suspensoes")
