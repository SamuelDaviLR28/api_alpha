from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel



class Produto(BaseModel):
    Descricao:             Optional[str] = None
    Altura:                Optional[float] = None
    Comprimento:           Optional[float] = None
    Largura:               Optional[float] = None
    Peso:                  Optional[float] = None
    Preco:                 Optional[float] = None
    Quantidade:            Optional[int]   = None
    SKU:                   Optional[str]  = None
    CodigoProduto:         Optional[str]  = None
    NumeroDeSerie:         Optional[str]  = None
    TipoProduto:           Optional[str]  = None
    Fabricante:            Optional[str]  = None


class Transportadora(BaseModel):
    PrevisaoDeEntrega:     Optional[str] = None
    DataPrometida:         Optional[str] = None
    Id:                    Optional[str] = None
    Nome:                  Optional[str] = None
    NomeServico:           Optional[str] = None
    IdServico:             Optional[str] = None
    CodigoRastreio:        Optional[str] = None
    ListaPostagem:         Optional[str] = None
    Reversa:               Optional[bool] = None
    Coleta:                Optional[bool] = None
    Dispatch:              Optional[bool] = None
    AlocacaoAutomatica:    Optional[bool] = None
    CodigoAutorizacao:     Optional[str] = None
    PrazoDiasUteis:        Optional[int]  = None
    PrazoEntregaFinal:     Optional[str] = None
    ValorAR:               Optional[float] = None
    ValorAverbadoPago:     Optional[float] = None
    ValorDeclarado:        Optional[float] = None
    ValorFrete:            Optional[float] = None
    CNPJ:                  Optional[str] = None
    ResponsavelRecebimento:Optional[str] = None
    SenhaVerificacao:      Optional[str] = None
    TipoOperacao:          Optional[str] = None
    TipoDevolucao:         Optional[str] = None
    MotivoDevolucao:       Optional[str] = None
    Prioridade:            Optional[bool] = None
    TipoPrioridade:        Optional[str] = None
    ServicosAdicionais:    Optional[str] = None


class Pessoa(BaseModel):
    Nome:                  Optional[str] = None
    CPFCNPJ:               Optional[str] = None
    Telefone:              Optional[str] = None
    TelefoneFixo:          Optional[str] = None
    TelefoneAdicional:     Optional[str] = None
    Email:                 Optional[str] = None
    Empresa:               Optional[str] = None
    Endereco:              Optional[str] = None
    Numero:                Optional[str] = None
    Complemento:           Optional[str] = None
    Bairro:                Optional[str] = None
    Cidade:                Optional[str] = None
    Estado:                Optional[str] = None
    Pais:                  Optional[str] = None
    CEP:                   Optional[str] = None
    IE:                    Optional[str] = None
    Lat:                   Optional[float] = None
    Long:                  Optional[float] = None
    Referencia:            Optional[str] = None
    Loja:                  Optional[str] = None
    NomeCentroDistribuicao:Optional[str] = None
    CodigoCentroDistribuicao:Optional[str] = None


class Tomador(BaseModel):
    Nome:        Optional[str] = None
    Endereco:    Optional[str] = None
    Numero:      Optional[str] = None
    Complemento: Optional[str] = None
    Bairro:      Optional[str] = None
    Cidade:      Optional[str] = None
    Estado:      Optional[str] = None
    Pais:        Optional[str] = None
    CEP:         Optional[str] = None
    IE:          Optional[str] = None
    CPFCNPJ:     Optional[str] = None



class Frete(BaseModel):
    Transportadora: Optional[Transportadora] = None
    Destinatario:   Optional[Pessoa]         = None
    Remetente:      Optional[Pessoa]         = None
    Tomador:        Optional[Tomador]        = None


class Item(BaseModel):
    IdUnico:             Optional[str] = None
    QuantidadeProdutos:  Optional[int]  = None
    Volumes:             Optional[int]  = None
    Largura:             Optional[float] = None
    Peso:                Optional[float] = None
    Altura:              Optional[float] = None
    Comprimento:         Optional[float] = None
    Formato:             Optional[str] = None
    Produtos:            Optional[List[Produto]] = None
    Frete:               Optional[Frete] = None


class NotaFiscal(BaseModel):
    DataEmissao:         Optional[str]  = None
    Numero:              Optional[int]  = None
    Serie:               Optional[int]  = None
    Cfop:                Optional[str]  = None
    Chave:               Optional[str]  = None
    ValorTotal:          Optional[float] = None
    ValorTotalProdutos:  Optional[float] = None
    StringXML:           Optional[str]  = None


class InfosAdicionais(BaseModel):
    CartaoPostagem:      Optional[str] = None
    CodigoAdmnistrativo: Optional[str] = None
    ContratoCorreios:    Optional[str] = None
    EntregaAgendada:     Optional[bool] = None
    DataAgendamento:     Optional[str] = None
    PeriodoEntregaAgendamento: Optional[str] = None
    Cluster:             Optional[str] = None
    TecnologiaDeAcesso:  Optional[str] = None
    Acronimo:            Optional[str] = None
    IdCliente:           Optional[str] = None
    IdDestinatario:      Optional[str] = None
    Portabilidade:       Optional[bool] = None
    SegmentoCliente:     Optional[str] = None


class DispatchToutbox(BaseModel):
    CriacaoPedido:              Optional[str] = None
    DataPagamento:              Optional[str] = None
    NumeroPedido:               Optional[str] = None
    NumeroPedidoMarketplace:    Optional[str] = None
    NumeroPedidoErp:            Optional[str] = None
    IdsAuxiliares:              Optional[str] = None
    NumeroPedidoAux:            Optional[str] = None
    Marketplace:                Optional[str] = None
    Marca:                      Optional[str] = None
    Seller:                     Optional[str] = None
    CanalDeVenda:               Optional[dict] = None
    Warehouse:                  Optional[str] = None
    UnidadeDeNegocio:           Optional[str] = None
    Rede:                       Optional[str] = None
    Campanha:                   Optional[str] = None
    Itens:                      Optional[List[Item]] = None
    NotaFiscal:                 Optional[NotaFiscal] = None
    InfosAdicionais:            Optional[InfosAdicionais] = None


class RotaPayload(BaseModel):
    NumeroPedido:      Optional[str] = None
    NumeroPedidoErp:   Optional[str] = None
    Itens:             Optional[List[Item]] = None
