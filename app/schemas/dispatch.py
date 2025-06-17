from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class Produto(BaseModel):
    Descricao: str
    Preco: float
    Quantidade: int
    SKU: str
    NumeroDeSerie: str

class Transportadora(BaseModel):
    Id: str
    Nome: str
    NomeServico: str
    IdServico: str
    CodigoRastreio: str
    ListaPostagem: str
    Reversa: bool
    Coleta: bool
    Dispatch: bool
    AlocacaoAutomatica: bool
    ValorAR: float
    ValorAverbadoPago: float
    ValorDeclarado: float
    ValorFrete: float
    Prioridade: bool

class Destinatario(BaseModel):
    Nome: str
    CPFCNPJ: str
    Telefone: str
    TelefoneFixo: str
    TelefoneAdicional: str
    Email: EmailStr
    Empresa: str
    Endereco: str
    Numero: str
    Complemento: str
    Bairro: str
    Cidade: str
    Estado: str
    Pais: str
    CEP: str
    IE: str

class Remetente(BaseModel):
    Nome: str
    NomeCentroDistribuicao: str
    CodigoCentroDistribuicao: str
    Endereco: str
    Numero: str
    Complemento: str
    Bairro: str
    Cidade: str
    Estado: str
    Pais: str
    CEP: str
    IE: str
    CPFCNPJ: str

class Tomador(BaseModel):
    Nome: str
    Endereco: str
    Numero: str
    Complemento: str
    Bairro: str
    Cidade: str
    Estado: str
    Pais: str
    CEP: str
    IE: Optional[str] = None
    CPFCNPJ: str

class Frete(BaseModel):
    Transportadora: Transportadora
    Destinatario: Destinatario
    Remetente: Remetente
    Tomador: Tomador

class Item(BaseModel):
    IdUnico: str
    QuantidadeProdutos: int
    Volumes: int
    Largura: float
    Peso: float
    Altura: float
    Comprimento: float
    Produtos: List[Produto]
    Frete: Frete

class CanalDeVenda(BaseModel):
    Id: str
    Nome: str

class NotaFiscal(BaseModel):
    DataEmissao: datetime
    Numero: int
    Serie: int
    Chave: str
    ValorTotal: float
    ValorTotalProdutos: float

class InfosAdicionais(BaseModel):
    EntregaAgendada: bool
    Portabilidade: bool

class Pedido(BaseModel):
    CriacaoPedido: datetime
    NumeroPedido: str
    NumeroPedidoMarketplace: str
    NumeroPedidoErp: str
    NumeroPedidoAux: str
    CanalDeVenda: CanalDeVenda
    Itens: List[Item]
    NotaFiscal: NotaFiscal
    InfosAdicionais: InfosAdicionais
