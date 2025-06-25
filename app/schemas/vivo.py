from typing import Optional, List, Union
from pydantic import BaseModel, Field, root_validator, ConfigDict

class Produto(BaseModel):
    Descricao: Optional[str]
    SKU: Optional[str]
    NumeroDeSerie: Optional[str]
    Preco: Optional[float]
    Quantidade: Optional[int]
    Altura: Optional[float]
    Comprimento: Optional[float]
    Largura: Optional[float]
    Peso: Optional[float]
    TipoProduto: Optional[str]
    Fabricante: Optional[str]

class Transportadora(BaseModel):
    Id: Optional[str]
    Nome: Optional[str]
    NomeServico: Optional[str]
    IdServico: Optional[str]
    CodigoRastreio: Optional[str]
    ListaPostagem: Optional[str]
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
    CNPJ: Optional[str]
    ResponsavelRecebimento: Optional[str]
    SenhaVerificacao: Optional[str]
    TipoOperacao: Optional[str]
    TipoDevolucao: Optional[str]
    MotivoDevolucao: Optional[str]
    Prioridade: Optional[bool]
    TipoPrioridade: Optional[str]
    ServicosAdicionais: Optional[str]

class Pessoa(BaseModel):
    Nome: Optional[str]
    CPFCNPJ: Optional[str]
    Telefone: Optional[str]
    TelefoneFixo: Optional[str]
    TelefoneAdicional: Optional[str]
    Email: Optional[str]
    Empresa: Optional[str]
    Endereco: Optional[str]
    Numero: Optional[str]
    Complemento: Optional[str]
    Bairro: Optional[str]
    Cidade: Optional[str]
    Estado: Optional[str]
    Pais: Optional[str]
    CEP: Optional[str]
    IE: Optional[str]
    Loja: Optional[Union[str, bool]]
    NomeCentroDistribuicao: Optional[str]
    CodigoCentroDistribuicao: Optional[str]
    Lat: Optional[str]
    Long: Optional[str]
    Referencia: Optional[str]

class Frete(BaseModel):
    Transportadora: Optional[Transportadora]
    Destinatario: Optional[Pessoa]
    Remetente: Optional[Pessoa]
    Tomador: Optional[Pessoa]

class Item(BaseModel):
    IdUnico: Optional[str]
    QuantidadeProdutos: Optional[int]
    Volumes: Optional[Union[int, str]]
    Largura: Optional[float]
    Peso: Optional[float]
    Altura: Optional[float]
    Comprimento: Optional[float]
    Formato: Optional[str]
    Produtos: Optional[List[Produto]]
    Frete: Optional[Frete]

class InfosAdicionais(BaseModel):
    CartaoPostagem: Optional[str]
    CodigoAdmnistrativo: Optional[str]
    ContratoCorreios: Optional[str]
    EntregaAgendada: Optional[bool]
    DataAgendamento: Optional[str]
    PeriodoEntregaAgendamento: Optional[str]
    Cluster: Optional[str]
    TecnologiaDeAcesso: Optional[str]
    Acronimo: Optional[str]
    IdCliente: Optional[str]
    IdDestinatario: Optional[str]
    Portabilidade: Optional[bool]
    SegmentoCliente: Optional[str]

class NotaFiscal(BaseModel):
    Numero: Optional[Union[int, str]]
    Serie: Optional[Union[int, str]]
    Cfop: Optional[str]
    Chave: Optional[str]
    DataEmissao: Optional[str]
    ValorTotal: Optional[float]
    ValorTotalProdutos: Optional[float]
    StringXML: Optional[str]
    InfosAdicionais: Optional[Union[InfosAdicionais, dict]]

class DispatchVivoModel(BaseModel):
    model_config = ConfigDict(extra="ignore")

    CriacaoPedido: Optional[str]
    DataPagamento: Optional[str]
    NumeroPedido: Optional[str]
    NumeroPedidomarketplace: Optional[str]
    NumeroPedidoMarketplace: Optional[str]
    NumeroPedidoErp: Optional[str]
    NumeroPedidoAux: Optional[str]
    IdsAuxiliares: Optional[str]
    Marketplace: Optional[dict]
    Marca: Optional[dict]
    Seller: Optional[dict]
    CanalDeVenda: Optional[dict]
    Warehouse: Optional[str]
    UnidadeDeNegocio: Optional[str]
    Rede: Optional[str]
    Campanha: Optional[str]
    Itens: Optional[List[Item]] = Field(alias="Itens")
    NotaFiscal: Optional[NotaFiscal]
    InfosAdicionais: Optional[InfosAdicionais]
    VersaoSchema: Optional[str] = "v2.11.3"

    @root_validator(pre=True)
    def remove_extras(cls, values):
        values.pop("Transportadora", None)
        values.pop("Tomador", None)
        return values
