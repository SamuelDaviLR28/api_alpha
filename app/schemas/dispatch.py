from pydantic import BaseModel
from typing import List
from datetime import datetime


class Produto(BaseModel):
    Descricao: str | None = None
    Preco: float | None = None
    Quantidade: int | None = None
    SKU: str | None = None
    NumeroDeSerie: str | None = None

    model_config = {
        "extra": "allow"
    }


class Transportadora(BaseModel):
    Id: str | None = None
    Nome: str | None = None
    NomeServico: str | None = None
    IdServico: str | None = None
    CodigoRastreio: str | None = None
    ListaPostagem: str | None = None
    Reversa: bool | None = None
    Coleta: bool | None = None
    Dispatch: bool | None = None
    AlocacaoAutomatica: bool | None = None
    ValorAR: float | None = None
    ValorAverbadoPago: float | None = None
    ValorDeclarado: float | None = None
    ValorFrete: float | None = None
    Prioridade: bool | None = None

    model_config = {
        "extra": "allow"
    }


class Destinatario(BaseModel):
    Nome: str | None = None
    CPFCNPJ: str | None = None
    Telefone: str | None = None
    TelefoneFixo: str | None = None
    TelefoneAdicional: str | None = None
    Email: str | None = None  
    Empresa: str | None = None
    Endereco: str | None = None
    Numero: str | None = None
    Complemento: str | None = None
    Bairro: str | None = None
    Cidade: str | None = None
    Estado: str | None = None
    Pais: str | None = None
    CEP: str | None = None
    IE: str | None = None

    model_config = {
        "extra": "allow"
    }


class Remetente(BaseModel):
    Nome: str | None = None
    NomeCentroDistribuicao: str | None = None
    CodigoCentroDistribuicao: str | None = None
    Endereco: str | None = None
    Numero: str | None = None
    Complemento: str | None = None
    Bairro: str | None = None
    Cidade: str | None = None
    Estado: str | None = None
    Pais: str | None = None
    CEP: str | None = None
    IE: str | None = None
    CPFCNPJ: str | None = None

    model_config = {
        "extra": "allow"
    }


class Tomador(BaseModel):
    Nome: str | None = None
    Endereco: str | None = None
    Numero: str | None = None
    Complemento: str | None = None
    Bairro: str | None = None
    Cidade: str | None = None
    Estado: str | None = None
    Pais: str | None = None
    CEP: str | None = None
    IE: str | None = None
    CPFCNPJ: str | None = None

    model_config = {
        "extra": "allow"
    }


class Frete(BaseModel):
    Transportadora: Transportadora | None = None
    Destinatario: Destinatario | None = None
    Remetente: Remetente | None = None
    Tomador: Tomador | None = None

    model_config = {
        "extra": "allow"
    }


class Item(BaseModel):
    IdUnico: str | None = None
    QuantidadeProdutos: int | None = None
    Volumes: int | None = None
    Largura: float | None = None
    Peso: float | None = None
    Altura: float | None = None
    Comprimento: float | None = None
    Produtos: List[Produto] | None = None
    Frete: Frete | None = None

    model_config = {
        "extra": "allow"
    }


class CanalDeVenda(BaseModel):
    Id: str | None = None
    Nome: str | None = None

    model_config = {
        "extra": "allow"
    }


class NotaFiscal(BaseModel):
    DataEmissao: datetime | None = None
    Numero: int | None = None
    Serie: int | None = None
    Chave: str | None = None
    ValorTotal: float | None = None
    ValorTotalProdutos: float | None = None

    model_config = {
        "extra": "allow"
    }


class InfosAdicionais(BaseModel):
    EntregaAgendada: bool | None = None
    Portabilidade: bool | None = None

    model_config = {
        "extra": "allow"
    }


class DispatchToutbox(BaseModel):
    CriacaoPedido: datetime | None = None
    NumeroPedido: str | None = None
    NumeroPedidoMarketplace: str | None = None
    NumeroPedidoErp: str | None = None
    NumeroPedidoAux: str | None = None
    CanalDeVenda: CanalDeVenda | None = None
    Itens: List[Item] | None = None
    NotaFiscal: NotaFiscal | None = None
    InfosAdicionais: InfosAdicionais | None = None

    model_config = {
        "extra": "allow"
    }
