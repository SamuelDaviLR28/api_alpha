from __future__ import annotations
from typing import List, Optional, Union
from pydantic import BaseModel

# PRODUTO
class Produto(BaseModel):
    Descricao: Optional[str] = None
    Altura: Optional[float] = None
    Comprimento: Optional[float] = None
    Largura: Optional[float] = None
    Peso: Optional[float] = None
    Preco: Optional[float] = None
    Quantidade: Optional[int] = None
    SKU: Optional[str] = None
    CodigoProduto: Optional[str] = None
    NumeroDeSerie: Optional[str] = None
    TipoProduto: Optional[str] = None
    Fabricante: Optional[str] = None
    model_config = {"extra": "allow"}

# TRANSPORTADORA
class Transportadora(BaseModel):
    Id: Optional[str] = None
    Nome: Optional[str] = None
    NomeServico: Optional[str] = None
    IdServico: Optional[str] = None
    CodigoRastreio: Optional[str] = None
    ListaPostagem: Optional[str] = None
    CNPJ: Optional[str] = None
    Reversa: Optional[bool] = None
    Coleta: Optional[bool] = None
    Dispatch: Optional[bool] = None
    AlocacaoAutomatica: Optional[bool] = None
    CodigoAutorizacao: Optional[str] = None
    PrazoDiasUteis: Optional[int] = None
    PrazoEntregaFinal: Optional[str] = None
    DataPrometida: Optional[str] = None
    PrevisaoDeEntrega: Optional[str] = None
    ValorAR: Optional[float] = None
    ValorAverbadoPago: Optional[float] = None
    ValorDeclarado: Optional[float] = None
    ValorFrete: Optional[float] = None
    Prioridade: Optional[bool] = None
    EntregaAgendada: Optional[bool] = None
    ResponsavelRecebimento: Optional[str] = None
    SenhaVerificacao: Optional[str] = None
    TipoOperacao: Optional[str] = None
    TipoDevolucao: Optional[str] = None
    MotivoDevolucao: Optional[str] = None
    TipoPrioridade: Optional[str] = None
    ServicosAdicionais: Optional[str] = None
    model_config = {"extra": "allow"}

# PESSOA
class Pessoa(BaseModel):
    Nome: Optional[str] = None
    CPFCNPJ: Optional[str] = None
    Telefone: Optional[str] = None
    TelefoneFixo: Optional[str] = None
    TelefoneAdicional: Optional[str] = None
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
    IE: Optional[str] = None
    Loja: Optional[Union[bool, str]] = None
    NomeCentroDistribuicao: Optional[str] = None
    CodigoCentroDistribuicao: Optional[str] = None
    Lat: Optional[str] = None
    Long: Optional[str] = None
    Referencia: Optional[str] = None
    model_config = {"extra": "allow"}

class Tomador(Pessoa):
    pass

# FRETE
class Frete(BaseModel):
    Transportadora: Optional[Transportadora] = None
    Destinatario: Optional[Pessoa] = None
    Remetente: Optional[Pessoa] = None
    Tomador: Optional[Tomador] = None
    model_config = {"extra": "allow"}

# ITEM
class Item(BaseModel):
    IdUnico: Optional[str] = None
    QuantidadeProdutos: Optional[int] = None
    Volumes: Optional[Union[int, str]] = None
    Largura: Optional[float] = None
    Peso: Optional[float] = None
    Altura: Optional[float] = None
    Comprimento: Optional[float] = None
    Formato: Optional[str] = None
    Produtos: Optional[List[Produto]] = None
    Frete: Optional[Frete] = None
    model_config = {"extra": "allow"}

# INFOS ADICIONAIS
class InfosAdicionais(BaseModel):
    CartaoPostagem: Optional[str] = None
    CodigoAdmnistrativo: Optional[str] = None
    ContratoCorreios: Optional[str] = None
    EntregaAgendada: Optional[bool] = None
    DataAgendamento: Optional[str] = None
    PeriodoEntregaAgendamento: Optional[str] = None
    Cluster: Optional[str] = None
    TecnologiaDeAcesso: Optional[str] = None
    Acronimo: Optional[str] = None
    IdCliente: Optional[str] = None
    IdDestinatario: Optional[str] = None
    Portabilidade: Optional[bool] = None
    SegmentoCliente: Optional[str] = None
    model_config = {"extra": "allow"}

# NOTA FISCAL
class NotaFiscal(BaseModel):
    Numero: Optional[Union[int, str]] = None
    Serie: Optional[Union[int, str]] = None
    Cfop: Optional[str] = None
    Chave: Optional[str] = None
    DataEmissao: Optional[str] = None
    ValorTotal: Optional[float] = None
    ValorTotalProdutos: Optional[float] = None
    StringXML: Optional[str] = None
    InfosAdicionais: Optional[Union[InfosAdicionais, dict]] = None
    model_config = {"extra": "allow"}

# OUTROS OBJETOS
class Marketplace(BaseModel):
    Id: Optional[str] = None
    Nome: Optional[str] = None
    model_config = {"extra": "allow"}

class Marca(BaseModel):
    Id: Optional[str] = None
    Nome: Optional[str] = None
    model_config = {"extra": "allow"}

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
    model_config = {"extra": "allow"}

class CanalDeVenda(BaseModel):
    Id: Optional[str] = None
    Nome: Optional[str] = None
    model_config = {"extra": "allow"}

# ✅ SCHEMA PRINCIPAL
class DispatchToutbox(BaseModel):
    CriacaoPedido: Optional[str] = None
    DataPagamento: Optional[str] = None
    NumeroPedido: Optional[str] = None
    NumeroPedidomarketplace: Optional[str] = None
    NumeroPedidoMarketplace: Optional[str] = None
    NumeroPedidoErp: Optional[str] = None
    NumeroPedidoAux: Optional[str] = None
    IdsAuxiliares: Optional[str] = None

    Marketplace: Optional[Marketplace] = None
    Marca: Optional[Marca] = None
    Seller: Optional[Seller] = None
    CanalDeVenda: Optional[CanalDeVenda] = None
    Warehouse: Optional[str] = None
    UnidadeDeNegocio: Optional[str] = None
    Rede: Optional[str] = None
    Campanha: Optional[str] = None

    Itens: Optional[List[Item]] = None
    NotaFiscal: Optional[NotaFiscal] = None
    InfosAdicionais: Optional[InfosAdicionais] = None

    VersaoSchema: Optional[str] = "v2.11.3"  # ⬅️ Campo sentinela aqui

    model_config = {"extra": "allow"}

# (Se usar herança em outro schema)
class RotaPayload(DispatchToutbox):
    pass
