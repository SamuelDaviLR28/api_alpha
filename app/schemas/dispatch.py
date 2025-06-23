from typing import List, Optional, Union
from pydantic import BaseModel


class Produto(BaseModel):
    Descricao: Optional[str]
    Altura: Optional[float]
    Comprimento: Optional[float]
    Largura: Optional[float]
    Peso: Optional[float]
    Preco: Optional[float]
    Quantidade: Optional[int]
    SKU: Optional[str]
    CodigoProduto: Optional[str]
    NumeroDeSerie: Optional[str]
    TipoProduto: Optional[str]
    Fabricante: Optional[str]


class Pessoa(BaseModel):
    Nome: Optional[str]
    CPFCNPJ: Optional[str]
    IE: Optional[str]
    Telefone: Optional[str]
    TelefoneFixo: Optional[str]
    TelefoneAdicional: Optional[str]
    Email: Optional[Union[str, None]]
    Empresa: Optional[str]
    Endereco: Optional[str]
    Numero: Optional[str]
    Complemento: Optional[str]
    Bairro: Optional[str]
    Cidade: Optional[str]
    Estado: Optional[str]
    Pais: Optional[str]
    CEP: Optional[str]
    Loja: Optional[Union[bool, str]]
    NomeCentroDistribuicao: Optional[str]
    CodigoCentroDistribuicao: Optional[str]


class Transportadora(BaseModel):
    Id: Optional[str]
    id: Optional[str]  
    Nome: Optional[str]
    NomeServico: Optional[str]
    IdServico: Optional[str]
    CodigoRastreio: Optional[str]
    ListaPostagem: Optional[str]
    CNPJ: Optional[str]
    Reversa: Optional[bool]
    Coleta: Optional[bool]
    Dispatch: Optional[bool]
    AlocacaoAutomatica: Optional[bool]
    CodigoAutorizacao: Optional[str]
    PrazoDiasUteis: Optional[int]
    PrazoEntregaFinal: Optional[str]
    DataPrometida: Optional[str]
    PrevisaoDeEntrega: Optional[str]
    ValorAR: Optional[float]
    ValorAverbadoPago: Optional[float]
    ValorDeclarado: Optional[float]
    ValorFrete: Optional[float]
    EntregaAgendada: Optional[bool]
    Prioridade: Optional[bool]


class Frete(BaseModel):
    Transportadora: Optional[Transportadora]
    Destinatario: Optional[Pessoa]
    Remetente: Optional[Pessoa]
    Tomador: Optional[Pessoa]


class InfosAdicionaisNota(BaseModel):
    Chave: Optional[str]


class NotaFiscal(BaseModel):
    Numero: Optional[Union[str, int]]
    Serie: Optional[Union[str, int]]
    Cfop: Optional[str]
    Chave: Optional[str]
    DataEmissao: Optional[str]
    ValorTotal: Optional[float]
    ValorTotalProdutos: Optional[float]
    InfosAdicionais: Optional[InfosAdicionaisNota]


class ProdutoItem(BaseModel):
    Descricao: Optional[str]
    Altura: Optional[float]
    Comprimento: Optional[float]
    Largura: Optional[float]
    Peso: Optional[float]
    Preco: Optional[float]
    Quantidade: Optional[int]
    SKU: Optional[str]


class Item(BaseModel):
    IdUnico: Optional[str]
    QuantidadeProdutos: Optional[int]
    Volumes: Optional[Union[int, str]]
    Largura: Optional[float]
    Peso: Optional[float]
    Altura: Optional[float]
    Comprimento: Optional[float]
    Formato: Optional[str]
    Produtos: Optional[List[ProdutoItem]]
    Frete: Optional[Frete]


class Marketplace(BaseModel):
    Id: Optional[str]
    Nome: Optional[str]


class Marca(BaseModel):
    Id: Optional[str]
    Nome: Optional[str]


class Seller(BaseModel):
    Id: Optional[str]
    RazaoSocial: Optional[str]
    NomeFantasia: Optional[str]
    CNPJ: Optional[str]
    Contato: Optional[str]
    Email: Optional[str]
    Endereco: Optional[str]
    Numero: Optional[str]
    Complemento: Optional[str]
    Bairro: Optional[str]
    Cidade: Optional[str]
    Estado: Optional[str]
    Pais: Optional[str]
    CEP: Optional[str]


class DispatchToutbox(BaseModel):
    CriacaoPedido: Optional[str]
    DataPagamento: Optional[str]
    NumeroPedido: Optional[str]
    NumeroPedidomarketplace: Optional[str]
    NumeroPedidoMarketplace: Optional[str]
    NumeroPedidoErp: Optional[str]
    NumeroPedidoAux: Optional[str]
    IdsAuxiliares: Optional[str]
    CanalDeVenda: Optional[dict]

    Marketplace: Optional[Marketplace]
    Marca: Optional[Marca]
    Seller: Optional[Seller]

    Itens: Optional[List[Item]]
    NotaFiscal: Optional[NotaFiscal]
    InfosAdicionais: Optional[dict]

    class Config:
        extra = "allow"  
