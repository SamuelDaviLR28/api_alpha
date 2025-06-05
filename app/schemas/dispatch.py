from pydantic import BaseModel
from typing import List, Optional, Dict

class Marketplace(BaseModel):
    Id: Optional[str] = None
    Nome: Optional[str] = None

class Marca(BaseModel):
    Id: Optional[str] = None
    Nome: Optional[str] = None

class Seller(BaseModel):
    Id: Optional[str] = None
    RazaoSocial: Optional[str] = None
    NomeFantasia: Optional[str] = None
    CNPJ: Optional[str] = None
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

class Produto(BaseModel):
    Descricao: Optional[str] = None
    Altura: Optional[float] = None
    Comprimento: Optional[float] = None
    Largura: Optional[float] = None
    Peso: Optional[float] = None
    Preco: Optional[float] = None
    Quantidade: Optional[int] = None
    SKU: Optional[str] = None

class Transportadora(BaseModel):
    id: Optional[str] = None
    Nome: Optional[str] = None
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
    ValorAR: Optional[float] = None
    ValorAverbadoPago: Optional[float] = None
    ValorDeclarado: Optional[float] = None
    ValorFrete: Optional[float] = None

class Pessoa(BaseModel):
    Nome: Optional[str] = None
    CPFCNPJ: Optional[str] = None
    IE: Optional[str] = None
    Telefone: Optional[str] = None
    Email: Optional[str] = None
    Empresa: Optional[str] = None
    Endereco: Optional[str] = None
    Numero: Optional[str] = None
    Complemento: Optional[str] = None
    Bairro: Optional[str] = None
    Cidade: Optional[str] = None
    Estado: Optional[str] = None
    Pais: Optional[str] = None
    CEP: Optional[str] = None

class Remetente(BaseModel):
    Loja: Optional[bool] = None
    NomeCentroDistribuicao: Optional[str] = None
    CodigoCentroDistribuicao: Optional[str] = None
    CPFCNPJ: Optional[str] = None
    IE: Optional[str] = None
    Endereco: Optional[str] = None
    Numero: Optional[str] = None
    Complemento: Optional[str] = None
    Bairro: Optional[str] = None
    Cidade: Optional[str] = None
    Estado: Optional[str] = None
    Pais: Optional[str] = None
    CEP: Optional[str] = None

class Frete(BaseModel):
    Transportadora: Optional[Transportadora] = None
    Destinatario: Optional[Pessoa] = None
    Tomador: Optional[Pessoa] = None
    Remetente: Optional[Remetente] = None

class Item(BaseModel):
    IdUnico: Optional[str] = None
    Volumes: Optional[str] = None
    Largura: Optional[float] = None
    Peso: Optional[float] = None
    Altura: Optional[float] = None
    Comprimento: Optional[float] = None
    Formato: Optional[str] = None
    Produtos: Optional[List[Produto]] = None
    Frete: Optional[Frete] = None

class NotaFiscal(BaseModel):
    Numero: Optional[str] = None
    Serie: Optional[str] = None
    Cfop: Optional[str] = None
    Chave: Optional[str] = None
    DataEmissao: Optional[str] = None
    ValorTotal: Optional[float] = None
    ValorTotalProdutos: Optional[float] = None
    InfosAdicionais: Optional[Dict[str, str]] = None

class DispatchToutbox(BaseModel):
    CriacaoPedido: Optional[str] = None
    DataPagamento: Optional[str] = None
    NumeroPedido: Optional[str] = None
    NumeroPedidomarketplace: Optional[str] = None
    NumeroPedidoErp: Optional[str] = None
    Marketplace: Optional[Marketplace] = None
    Marca: Optional[Marca] = None
    Seller: Optional[Seller] = None
    Itens: Optional[List[Item]] = None
    NotaFiscal: Optional[NotaFiscal] = None
