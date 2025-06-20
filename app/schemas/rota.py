from pydantic import BaseModel
from typing import Optional, List


class Produto(BaseModel):
    Descricao: str
    Altura: Optional[float] = None
    Comprimento: Optional[float] = None
    Largura: Optional[float] = None
    Peso: Optional[float] = None
    Preco: float
    Quantidade: int
    SKU: str
    CodigoProduto: Optional[str] = None
    NumeroDeSerie: str
    TipoProduto: Optional[str] = None
    Fabricante: Optional[str] = None


class Transportadora(BaseModel):
    PrevisaoDeEntrega: Optional[str] = None
    DataPrometida: Optional[str] = None
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
    CodigoAutorizacao: Optional[str] = None
    PrazoDiasUteis: Optional[int] = None
    PrazoEntregaFinal: Optional[str] = None
    ValorAR: Optional[float] = None
    ValorAverbadoPago: Optional[float] = None
    ValorDeclarado: Optional[float] = None
    ValorFrete: Optional[float] = None
    CNPJ: Optional[str] = None
    ResponsavelRecebimento: Optional[str] = None
    SenhaVerificacao: Optional[str] = None
    TipoOperacao: Optional[str] = None
    TipoDevolucao: Optional[str] = None
    MotivoDevolucao: Optional[str] = None
    Prioridade: Optional[bool] = None
    TipoPrioridade: Optional[str] = None
    ServicosAdicionais: Optional[str] = None


class Pessoa(BaseModel):
    Nome: str
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
    Lat: Optional[float] = None
    Long: Optional[float] = None
    Referencia: Optional[str] = None
    Loja: Optional[str] = None
    NomeCentroDistribuicao: Optional[str] = None
    CodigoCentroDistribuicao: Optional[str] = None


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
    Destinatario: Optional[Pessoa] = None
    Remetente: Optional[Pessoa] = None
    Tomador: Optional[Tomador] = None


class Item(BaseModel):
    IdUnico: str
    QuantidadeProdutos: int
    Volumes: int
    Largura: Optional[float] = None
    Peso: Optional[float] = None
    Altura: Optional[float] = None
    Comprimento: Optional[float] = None
    Formato: Optional[str] = None
    Produtos: Optional[List[Produto]] = None
    Frete: Optional[Frete] = None


class NotaFiscal(BaseModel):
    DataEmissao: str
    Numero: int
    Serie: int
    Cfop: Optional[str] = None
    Chave: Optional[str] = None
    ValorTotal: float
    ValorTotalProdutos: float
    StringXML: Optional[str] = None


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


class DispatchToutbox(BaseModel):
    CriacaoPedido: str
    DataPagamento: Optional[str] = None
    NumeroPedido: str
    NumeroPedidoMarketplace: Optional[str] = None
    NumeroPedidoErp: Optional[str] = None
    IdsAuxiliares: Optional[str] = None
    NumeroPedidoAux: Optional[str] = None
    Marketplace: Optional[str] = None
    Marca: Optional[str] = None
    Seller: Optional[str] = None
    CanalDeVenda: Optional[dict] = None
    Warehouse: Optional[str] = None
    UnidadeDeNegocio: Optional[str] = None
    Rede: Optional[str] = None
    Campanha: Optional[str] = None
    Itens: List[Item]
    NotaFiscal: NotaFiscal
    InfosAdicionais: Optional[InfosAdicionais] = None
