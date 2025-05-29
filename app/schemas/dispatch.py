from pydantic import BaseModel
from typing import List, Optional, Dict

class Marketplace(BaseModel):
    Id: str
    Nome: str

class Marca(BaseModel):
    Id: str
    Nome: str

class Seller(BaseModel):
    Id: str
    RazaoSocial: str
    NomeFantasia: str
    CNPJ: str
    Contato: str
    Email: str
    Endereco: str
    Numero: str
    Complemento: str
    Bairro: str
    Cidade: str
    Estado: str
    Pais: str
    CEP: str

class Produto(BaseModel):
    Descricao: str
    Altura: float
    Comprimento: float
    Largura: float
    Peso: float
    Preco: float
    Quantidade: int
    SKU: str

class Transportadora(BaseModel):
    id: str
    Nome: str
    NomeServico: str
    IdServico: str
    CodigoRastreio: str
    ListaPostagem: str
    CNPJ: str
    Reversa: bool
    CodigoAutorizacao: str
    Coleta: bool
    EntregaAgendada: bool
    DataPrometida: str
    PrazoDiasUteis: int
    PrevisaoDeEntrega: str
    ValorAR: float
    ValorAverbadoPago: float
    ValorDeclarado: float
    ValorFrete: float

class Pessoa(BaseModel):
    Nome: str
    CPFCNPJ: str
    IE: str
    Telefone: Optional[str] = None
    Email: Optional[str] = None
    Empresa: Optional[str] = None
    Endereco: str
    Numero: str
    Complemento: str
    Bairro: str
    Cidade: str
    Estado: str
    Pais: str
    CEP: str

class Remetente(BaseModel):
    Loja: bool
    NomeCentroDistribuicao: str
    CodigoCentroDistribuicao: str
    CPFCNPJ: str
    IE: str
    Endereco: str
    Numero: str
    Complemento: str
    Bairro: str
    Cidade: str
    Estado: str
    Pais: str
    CEP: str

class Frete(BaseModel):
    Transportadora: Transportadora
    Destinatario: Pessoa
    Tomador: Pessoa
    Remetente: Remetente

class Item(BaseModel):
    IdUnico: str
    Volumes: str
    Largura: float
    Peso: float
    Altura: float
    Comprimento: float
    Formato: str
    Produtos: List[Produto]
    Frete: Frete

class NotaFiscal(BaseModel):
    Numero: str
    Serie: str
    Cfop: str
    Chave: str
    DataEmissao: str
    ValorTotal: float
    ValorTotalProdutos: float
    InfosAdicionais: Dict[str, str]

class DispatchToutbox(BaseModel):
    CriacaoPedido: str
    DataPagamento: Optional[str]
    NumeroPedido: str
    NumeroPedidomarketplace: str
    NumeroPedidoErp: str
    Marketplace: Marketplace
    Marca: Marca
    Seller: Seller
    Itens: List[Item]
    NotaFiscal: NotaFiscal
