from pydantic import BaseModel, validator
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
    Contato: Optional[str] = None
    Email: Optional[str] = None
    Endereco: Optional[str] = None
    Numero: Optional[str] = None
    Complemento: Optional[str] = None
    Bairro: Optional[str] = None
    Cidade: Optional[str] = None
    Estado: Optional[str] = None
    Pais: Optional[str] = None
    CEP: Optional[str] = None

    @validator("CNPJ")
    def validar_cnpj(cls, value):
        if value and not value.replace(".", "").replace("/", "").replace("-", "").isdigit():
            raise ValueError("CNPJ inválido")
        return value


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
    Id: str
    Nome: str
    NomeServico: Optional[str] = None
    IdServico: Optional[str] = None
    CodigoRastreio: Optional[str] = None
    ListaPostagem: Optional[str] = None
    CNPJ: Optional[str] = None
    Reversa: Optional[bool] = None
    CodigoAutorizacao: Optional[str] = None
    Coleta: Optional[bool] = None
    EntregaAgendada: Optional[bool] = None
    DataPrometida: Optional[str] = None
    PrazoDiasUteis: Optional[int] = None
    PrevisaoDeEntrega: Optional[str] = None
    ValorDeclarado: Optional[float] = None
    ValorFrete: Optional[float] = None


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

    @validator("CPFCNPJ")
    def validar_cpf_cnpj(cls, value):
        if value and not value.replace(".", "").replace("/", "").replace("-", "").isdigit():
            raise ValueError("CPF/CNPJ inválido")
        return value


class Remetente(BaseModel):
    NomeCentroDistribuicao: str
    CodigoCentroDistribuicao: str
    CPFCNPJ: str
    Endereco: str
    Numero: str
    Complemento: Optional[str] = None
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
    Volumes: Optional[str] = None
    Largura: float
    Peso: float
    Altura: float
    Comprimento: float
    Formato: Optional[str] = None
    Produtos: List[Produto] = []
    Frete: Frete


class NotaFiscal(BaseModel):
    Numero: str
    Serie: Optional[str] = None
    Cfop: Optional[str] = None
    Chave: Optional[str] = None
    DataEmissao: str
    ValorTotal: float
    ValorTotalProdutos: float
    InfosAdicionais: Optional[Dict[str, str]] = None


class DispatchToutbox(BaseModel):
    CriacaoPedido: str
    DataPagamento: Optional[str] = None
    NumeroPedido: str
    NumeroPedidomarketplace: Optional[str] = None
    NumeroPedidoErp: Optional[str] = None
    Marketplace: Marketplace
    Marca: Marca
    Seller: Seller
    Itens: List[Item] = []
    NotaFiscal: NotaFiscal
