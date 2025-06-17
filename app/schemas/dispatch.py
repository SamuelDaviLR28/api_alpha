from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class Produto(BaseModel):
    Descricao: Optional[str] = None
    Preco: Optional[float] = None
    Quantidade: Optional[int] = None
    SKU: Optional[str] = None
    NumeroDeSerie: Optional[str] = None

class Transportadora(BaseModel):
    Id: Optional[str] = None
    Nome: Optional[str] = None
    NomeServico: Optional[str] = None
    IdServico: Optional[str] = None
    CodigoRastreio: Optional[str] = None
    ListaPostagem: Optional[str] = None
    Reversa: Optional[bool] = None
    Coleta: Optional[bool] = None
    Dispatch: Optional[bool] = None
    AlocacaoAutomatica: Optional[bool] = None
    ValorAR: Optional[float] = None
    ValorAverbadoPago: Optional[float] = None
    ValorDeclarado: Optional[float] = None
    ValorFrete: Optional[float] = None
    Prioridade: Optional[bool] = None

class Destinatario(BaseModel):
    Nome: Optional[str] = None
    CPFCNPJ: Optional[str] = None
    Telefone: Optional[str] = None
    TelefoneFixo: Optional[str] = None
    TelefoneAdicional: Optional[str] = None
    Email: Optional[EmailStr] = None
    Empresa: Optional[str] = None
    Endereco: Optional[str] = None
    Numero: Optional[str] = None
    Complemento: Optional[str] = None
    Bairro: Optional[str] = None
    Cidade: Optional[str] = None
    Estado: Optional[str] = None
    Pais: Optional[str] = None
    CEP: Optional[str] = None
    IE: Optional[str] = None

class Remetente(BaseModel):
    Nome: Optional[str] = None
    NomeCentroDistribuicao: Optional[str] = None
    CodigoCentroDistribuicao: Optional[str] = None
    Endereco: Optional[str] = None
    Numero: Optional[str] = None
    Complemento: Optional[str] = None
    Bairro: Optional[str] = None
    Cidade: Optional[str] = None
    Estado: Optional[str] = None
    Pais: Optional[str] = None
    CEP: Optional[str] = None
    IE: Optional[str] = None
    CPFCNPJ: Optional[str] = None

class Tomador(BaseModel):
    Nome: Optional[str] = None
    Endereco: Optional[str] = None
    Numero: Optional[str] = None
    Complemento: Optional[str] = None
    Bairro: Optional[str] = None
    Cidade: Optional[str] = None
    Estado: Optional[str] = None
    Pais: Optional[str] = None
    CEP: Optional[str] = None
    IE: Optional[str] = None
    CPFCNPJ: Optional[str] = None

class Frete(BaseModel):
    Transportadora: Optional[Transportadora] = None
    Destinatario: Optional[Destinatario] = None
    Remetente: Optional[Remetente] = None
    Tomador: Optional[Tomador] = None

class Item(BaseModel):
    IdUnico: Optional[str] = None
    QuantidadeProdutos: Optional[int] = None
    Volumes: Optional[int] = None
    Largura: Optional[float] = None
    Peso: Optional[float] = None
    Altura: Optional[float] = None
    Comprimento: Optional[float] = None
    Produtos: Optional[List[Produto]] = None
    Frete: Optional[Frete] = None

class CanalDeVenda(BaseModel):
    Id: Optional[str] = None
    Nome: Optional[str] = None

class NotaFiscal(BaseModel):
    DataEmissao: Optional[datetime] = None
    Numero: Optional[int] = None
    Serie: Optional[int] = None
    Chave: Optional[str] = None
    ValorTotal: Optional[float] = None
    ValorTotalProdutos: Optional[float] = None

class InfosAdicionais(BaseModel):
    EntregaAgendada: Optional[bool] = None
    Portabilidade: Optional[bool] = None

class Pedido(BaseModel):
    CriacaoPedido: Optional[datetime] = None
    NumeroPedido: Optional[str] = None
    NumeroPedidoMarketplace: Optional[str] = None
    NumeroPedidoErp: Optional[str] = None
    NumeroPedidoAux: Optional[str] = None
    CanalDeVenda: Optional[CanalDeVenda] = None
    Itens: Optional[List[Item]] = None
    NotaFiscal: Optional[NotaFiscal] = None
    InfosAdicionais: Optional[InfosAdicionais] = None

class DispatchToutbox(BaseModel):
    pedido: Pedido

class DispatchToutbox(BaseModel):
    pedidos: List[Pedido]
