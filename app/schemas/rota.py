from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Produto(BaseModel):
    Descricao: str
    Preco: float
    Quantidade: int
    SKU: str
    NumeroDeSerie: str


class FreteTransportadora(BaseModel):
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


class PessoaEndereco(BaseModel):
    Nome: str
    CPFCNPJ: str
    Telefone: str
    TelefoneFixo: str
    TelefoneAdicional: str
    Email: str
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


class Frete(BaseModel):
    Transportadora: FreteTransportadora
    Destinatario: PessoaEndereco
    Remetente: PessoaEndereco
    Tomador: PessoaEndereco


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


class RotaPayload(BaseModel):
    CriacaoPedido: datetime
    NumeroPedido: str
    NumeroPedidoMarketplace: str
    NumeroPedidoErp: str
    NumeroPedidoAux: str
    CanalDeVenda: CanalDeVenda
    Itens: List[Item]
    NotaFiscal: NotaFiscal
    InfosAdicionais: InfosAdicionais
