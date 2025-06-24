from __future__ import annotations
from typing import List, Optional, Union
from pydantic import BaseModel, ConfigDict, Field, root_validator

def to_snake_case(alias: str) -> str:
    return alias[0].lower() + ''.join(['_' + c.lower() if c.isupper() else c for c in alias[1:]])

class MeuBaseModel(BaseModel):
    model_config = ConfigDict(
        extra="allow",
        alias_generator=to_snake_case,
        populate_by_name=True
    )

class Produto(MeuBaseModel):
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

class Transportadora(MeuBaseModel):
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

class Pessoa(MeuBaseModel):
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

class Tomador(Pessoa):
    pass

class Frete(MeuBaseModel):
    Transportadora: Optional[Transportadora] = None
    Destinatario: Optional[Pessoa] = None
    Remetente: Optional[Pessoa] = None
    Tomador: Optional[Tomador] = None

class Item(MeuBaseModel):
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

class InfosAdicionais(MeuBaseModel):
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

class NotaFiscal(MeuBaseModel):
    Numero: Optional[Union[int, str]] = None
    Serie: Optional[Union[int, str]] = None
    Cfop: Optional[str] = None
    Chave: Optional[str] = None
    DataEmissao: Optional[str] = None
    ValorTotal: Optional[float] = None
    ValorTotalProdutos: Optional[float] = None
    StringXML: Optional[str] = None
    InfosAdicionais: Optional[Union[InfosAdicionais, dict]] = None

class DispatchToutbox(MeuBaseModel):
    CriacaoPedido: Optional[str] = None
    DataPagamento: Optional[str] = None
    NumeroPedido: Optional[str] = None
    NumeroPedidomarketplace: Optional[str] = None
    NumeroPedidoMarketplace: Optional[str] = None
    NumeroPedidoErp: Optional[str] = None
    NumeroPedidoAux: Optional[str] = None
    IdsAuxiliares: Optional[str] = None
    Marketplace: Optional[dict] = None
    Marca: Optional[dict] = None
    Seller: Optional[dict] = None
    CanalDeVenda: Optional[dict] = None
    Warehouse: Optional[str] = None
    UnidadeDeNegocio: Optional[str] = None
    Rede: Optional[str] = None
    Campanha: Optional[str] = None
    Itens: Optional[List[Item]] = Field(default=None, alias="Itens")
    NotaFiscal: Optional[NotaFiscal] = None
    InfosAdicionais: Optional[InfosAdicionais] = None
    VersaoSchema: Optional[str] = "v2.11.3"

    @root_validator(pre=True)
    def remove_extraneous_fields(cls, values):
        if "Transportadora" in values and isinstance(values["Transportadora"], dict):
            print("🚫 Ignorando 'Transportadora' fora de Frete")
            values.pop("Transportadora")

        if "Tomador" in values and isinstance(values["Tomador"], dict):
            print("🚫 Ignorando 'Tomador' fora de Frete")
            values.pop("Tomador")

        if "NotaFiscal" in values and isinstance(values["NotaFiscal"], dict):
            values["NotaFiscal"] = NotaFiscal(**values["NotaFiscal"])

        if "InfosAdicionais" in values and isinstance(values["InfosAdicionais"], dict):
            values["InfosAdicionais"] = InfosAdicionais(**values["InfosAdicionais"])

        if "Itens" in values and isinstance(values["Itens"], list):
            coerced = []
            for i in values["Itens"]:
                if isinstance(i, dict) and "Frete" in i and isinstance(i["Frete"], dict):
                    i["Frete"] = Frete(**i["Frete"])
                coerced.append(Item(**i) if isinstance(i, dict) else i)
            values["Itens"] = coerced

        return values

class RotaPayload(DispatchToutbox):
    pass
