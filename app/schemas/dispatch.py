from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional, Dict

app = FastAPI()

class Marketplace(BaseModel):
    Id: str
    Nome: str

class Warehouse(BaseModel):
    Id: str
    Nome: str

class Produto(BaseModel):
    Descricao: str
    Preco: float
    Quantidade: int
    SKU: str
    NumeroDeSerie: str
    Altura: Optional[float] = None
    Peso: Optional[float] = None
    Comprimento: Optional[float] = None
    Largura: Optional[float] = None

class Transportadora(BaseModel):
    Id: str
    Nome: str
    NomeServico: Optional[str] = None
    IdServico: Optional[str] = None
    CodigoRastreio: Optional[str] = None

class Pessoa(BaseModel):
    Nome: str
    CPFCNPJ: str
    Telefone: Optional[str] = None
    Email: Optional[str] = None
    Endereco: Optional[str] = None
    Numero: Optional[str] = None
    Complemento: Optional[str] = None
    Bairro: Optional[str] = None
    Cidade: Optional[str] = None
    Estado: Optional[str] = None
    Pais: Optional[str] = None
    CEP: Optional[str] = None

class Frete(BaseModel):
    Transportadora: Transportadora
    Destinatario: Pessoa

class Item(BaseModel):
    IdUnico: str
    Volumes: int
    Largura: float
    Peso: float
    Altura: float
    Comprimento: float
    Produtos: List[Produto]
    Frete: Frete

class NotaFiscal(BaseModel):
    DataEmissao: str
    Numero: str
    Serie: str
    Chave: str
    ValorTotal: float

class Pedido(BaseModel):
    CriacaoPedido: str
    NumeroPedido: str
    NumeroPedidoMarketplace: str
    NumeroPedidoErp: str
    NumeroPedidoAux: str
    CanalDeVenda: Marketplace
    Warehouse: Warehouse
    Itens: List[Item]
    NotaFiscal: NotaFiscal

@app.post("/criar-pedido")
async def criar_pedido(pedido: Pedido):
    return {"message": "✅ Pedido recebido com sucesso!", "dados": pedido.dict()}
