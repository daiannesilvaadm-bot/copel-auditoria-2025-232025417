"""
Dados PÚBLICOS da COPEL (Companhia Paranaense de Energia) - exercício 2025.

Fonte única de verdade para o código, as planilhas e o dossiê.
Valores em R$ mil (milhares de reais), consolidado, conforme publicado.
Cada bloco indica o identificador da fonte (ver 06_FONTES_E_COBERTURA/fontes.md).

Preparadora: matrícula 232025417 - data de consulta das fontes: 24/10/2026.
NADA neste arquivo é sintético. Os dados sintéticos ficam em 03_BASE_SINTETICA/ e são
gerados por 05_CODIGO/01_gerar_base.py.
"""

MATRICULA = "232025417"
ESTUDANTE = "Daiane da Silva"
COMPANHIA = "Companhia Paranaense de Energia - COPEL"
CNPJ = "76.483.817/0001-20"
CODIGO_CVM = "1431-1"
EXERCICIO = 2025
DATA_CONSULTA = "24/10/2026"
DATA_PREPARACAO = "24/10/2026"

# ---------------------------------------------------------------------------
# F01 - Release de resultados 4T25, Anexo I (Form 6-K, SEC, arquivado em
# 27/02/2026). DRE p. 23, Balanço p. 24, DFC p. 25 do release.
# ---------------------------------------------------------------------------
FONTE_BP = "F01, Anexo I, p. 24"
FONTE_DRE = "F01, Anexo I, p. 23"
FONTE_DFC = "F01, Anexo I, p. 25"

# (rubrica, 31/12/2025, 31/12/2024)
ATIVO_CIRCULANTE = [
    ("Caixa e equivalentes de caixa", 3130363, 4161939),
    ("Títulos e valores mobiliários", 895, 623),
    ("Cauções e depósitos vinculados", 9, 9),
    ("Clientes", 4300957, 3962702),
    ("Dividendos a receber", 141297, 82278),
    ("Ativos financeiros setoriais", 400463, 0),
    ("Contas a receber vinculadas à concessão", 12867, 10609),
    ("Ativos de contrato", 392594, 283896),
    ("Valor justo nas operações de compra e venda de energia", 263645, 217350),
    ("Outros créditos", 1050086, 949674),
    ("Estoques", 173398, 136324),
    ("Imposto de renda e contribuição social a recuperar", 502825, 296128),
    ("Outros tributos a recuperar", 426106, 994618),
    ("Despesas antecipadas", 60972, 63211),
    ("Partes relacionadas", 0, 621),
    ("Ativos classificados como mantidos para venda", 25177, 1881826),
]
TOTAL_AC = (10881654, 13041808)

REALIZAVEL_LP = [
    ("Títulos e valores mobiliários", 690886, 529085),
    ("Outros investimentos temporários", 30627, 30603),
    ("Clientes", 162189, 116180),
    ("Depósitos judiciais", 373949, 394364),
    ("Ativos financeiros setoriais", 400463, 0),
    ("Contas a receber vinculadas à concessão", 4590579, 3497351),
    ("Ativos de contrato", 9202412, 6927010),
    ("Valor justo nas operações de compra e venda de energia", 597856, 479938),
    ("Outros créditos", 794296, 681846),
    ("Imposto de renda e contribuição social a recuperar", 102589, 164043),
    ("Imposto de renda e contribuição social diferidos", 991404, 1174175),
    ("Outros tributos a recuperar", 1127582, 1320526),
    ("Despesas antecipadas", 507, 0),
]
TOTAL_RLP = (19065339, 15315121)

ATIVO_NC_OUTROS = [
    ("Investimentos", 2849002, 3577937),
    ("Imobilizado", 8145552, 8516697),
    ("Intangível", 19206609, 16623610),
    ("Direito de uso de ativos", 266300, 308983),
]
TOTAL_ANC = (49532802, 44342348)
TOTAL_ATIVO = (60414456, 57384156)

PASSIVO_CIRCULANTE = [
    ("Obrigações sociais e trabalhistas", 310773, 411102),
    ("Fornecedores", 3059667, 2324423),
    ("Imposto de renda e contribuição social a recolher", 81875, 83482),
    ("Outras obrigações fiscais", 677273, 302345),
    ("Empréstimos e financiamentos", 217827, 1231205),
    ("Debêntures", 1850538, 2025110),
    ("Dividendos mínimos obrigatórios a pagar", 2325889, 3878),
    ("Benefícios pós-emprego", 118854, 95383),
    ("Encargos do consumidor a recolher", 60108, 44825),
    ("Pesquisa e desenvolvimento e eficiência energética", 99244, 179149),
    ("Contas a pagar vinculadas à concessão", 147205, 113092),
    ("Passivos financeiros setoriais líquidos", 883990, 935322),
    ("Passivo de arrendamentos", 58741, 57502),
    ("Valor justo nas operações de compra e venda de energia", 262821, 214955),
    ("Outras contas a pagar", 788232, 1199195),
    ("Provisão para destinação de créditos de PIS e Cofins", 119280, 580000),
    ("Passivos associados a ativos mantidos para venda", 0, 541412),
]
TOTAL_PC = (11062317, 10342380)

PASSIVO_NAO_CIRCULANTE = [
    ("Obrigações sociais e trabalhistas", 4764, 457),
    ("Fornecedores", 133544, 142380),
    ("Imposto de renda e contribuição social diferidos", 1982596, 1895459),
    ("Outras obrigações fiscais", 239448, 291195),
    ("Empréstimos e financiamentos", 3150592, 3387589),
    ("Debêntures", 14796386, 10602255),
    ("Benefícios pós-emprego", 1359303, 1063326),
    ("Pesquisa e desenvolvimento e eficiência energética", 311856, 241294),
    ("Contas a pagar vinculadas à concessão", 959122, 992252),
    ("Passivos financeiros setoriais líquidos", 0, 142488),
    ("Passivo de arrendamentos", 234221, 271004),
    ("Valor justo nas operações de compra e venda de energia", 268621, 170837),
    ("Outras contas a pagar", 224415, 247021),
    ("Provisão para destinação de créditos de PIS e Cofins", 661273, 1000588),
    ("Provisões para litígios e outras provisões", 1934020, 956696),
]
TOTAL_PNC = (26260161, 21404841)

PATRIMONIO_LIQUIDO = [
    ("Capital social", 12821758, 12821758),
    ("Reservas de capital", 18638, 5595),
    ("Ajustes de avaliação patrimonial", 287992, 517408),
    ("Ações em tesouraria", -113389, -50044),
    ("Reserva legal", 1900541, 1766110),
    ("Reserva de retenção de lucros", 8214479, 9363866),
    ("Dividendo adicional proposto", 0, 1250025),
]
PL_CONTROLADORES = (23130019, 25674718)
PL_NAO_CONTROLADORES = (-38041, -37783)
TOTAL_PL = (23091978, 25636935)
TOTAL_PASSIVO_PL = (60414456, 57384156)

# DRE consolidada (R$ mil) - F01, Anexo I, p. 23
DRE = [
    ("Receita operacional líquida", 26116856, 22651036),
    ("  Fornecimento de energia a consumidores finais", 7961249, 8454990),
    ("  Suprimento de energia a distribuidoras", 4756273, 3120628),
    ("  Disponibilidade da rede elétrica (TUSD/TUST)", 6974666, 7048036),
    ("  Receita de construção", 3303150, 2550809),
    ("  Valor justo do ativo indenizável da concessão (VNR)", 161244, 82424),
    ("  Resultado de ativos e passivos financeiros setoriais", 2348143, 838280),
    ("  Outras receitas operacionais", 612131, 555869),
    ("Custos e despesas operacionais", -21311842, -18867990),
    ("  Energia elétrica comprada para revenda", -11110778, -8924895),
    ("  Encargos de uso da rede elétrica", -2755534, -2865490),
    ("  Pessoal e administradores", -960788, -1081797),
    ("  Planos previdenciário e assistencial", -234547, -259352),
    ("  Material", -108061, -86882),
    ("  Serviços de terceiros", -1192282, -1074308),
    ("  Depreciação e amortização", -1481886, -1465478),
    ("  Provisões e reversões", -270787, -345102),
    ("  Custo de construção", -3272763, -2522908),
    ("  Outros custos e despesas", 75584, -241778),
    ("Resultado de equivalência patrimonial", 239997, 281202),
    ("Lucro antes do resultado financeiro e dos tributos", 5045011, 4064248),
    ("Resultado financeiro", -1798352, -1157014),
    ("  Receitas financeiras", 1343658, 1184779),
    ("  Despesas financeiras", -3142010, -2341793),
    ("Lucro antes do IR e da CSLL", 3246659, 2907234),
    ("IR e CSLL (correntes e diferidos)", -577618, -599435),
    ("Lucro líquido das operações continuadas", 2669041, 2307799),
    ("Lucro líquido das operações descontinuadas", 18898, 491571),
    ("Lucro líquido do exercício", 2687939, 2799370),
]
# Observação: no release, "Outros custos e despesas" 2024 aparece como (240.842)
# e "Material para energia elétrica" (936). Aqui foram somados (241.778) para
# manter a soma; ver PT 520.
EBITDA = (6526897, 5529726)
EBITDA_RECORRENTE_RS_MI = (5533.8, 5021.7)
LUCRO_RECORRENTE_RS_MI = (2105.7, 2140.6)

# DFC (R$ mil) - F01, Anexo I, p. 25
DFC = [
    ("Caixa líquido das atividades operacionais", 3028446, 3393536),
    ("Caixa líquido das atividades de investimento", -1759364, -5739414),
    ("Caixa líquido das atividades de financiamento", -2300671, 803856),
    ("Adições ao ativo de contrato (investimento)", -2903661, -2174902),
    ("Adições ao intangível (investimento)", -43788, -4098286),
    ("Adições ao imobilizado (investimento)", -162100, -137635),
    ("Emissão de debêntures", 5000000, 3920000),
    ("Amortização de principal de debêntures", -3317499, -1079912),
    ("Prêmio pago aos acionistas (Novo Mercado)", -1273727, 0),
    ("Dividendos e JCP pagos", -1249045, -1586565),
    ("Caixa e equivalentes no início", 4161939, 5634623),
    ("Caixa e equivalentes no fim", 3130363, 4161939),
]

# Endividamento (F01, seção 1.7, p. 7)
DIVIDA_BRUTA_RS_MI = (20038.9, 17753.8)
DIVIDA_LIQUIDA_AJUSTADA_RS_MI = 16300.1
ALAVANCAGEM = (2.7, 2.6)
CRONOGRAMA_AMORTIZACAO_RS_MI = {"Caixa": 3739, "2026": 2068, "2027": 1672, "2028": 2045,
                                "2029": 2452, "2030": 2474, "2031": 2288, ">2031": 7036}

# Investimentos realizados 2025 (F01, seção 2, p. 9) - R$ milhões
CAPEX_2025_RS_MI = {"Copel DIS": 2959.0, "Copel GeT": 626.7, "Holding": 3.7,
                    "Copel Com": 2.0, "Copel Serviços e outros": 1.1, "Total": 3592.5}

# ---------------------------------------------------------------------------
# F02 - Form 20-F 2025 (SEC, arquivado em 15/04/2026)
# ---------------------------------------------------------------------------
VENCIDOS_LIQUIDOS_PECLD_RS_MI = 605.5      # Item 3, p. 5
PECLD_RS_MI = 245.6                        # Item 3, p. 5
PROVISAO_PROCESSOS_JUDICIAIS_RS_MI = 1571.6  # Item 3, p. 7
CAPACIDADE_INSTALADA_MW = 6226.1           # Item 4, p. 20 (incl. participações)
CAPACIDADE_100PCT_MW = 5961.2              # Item 4, p. 20
KM_DISTRIBUICAO = 218470                   # Item 4, p. 20
KM_TRANSMISSAO_PROPRIA = 4594              # Item 4, p. 20
MUNICIPIOS = "394 dos 399 municípios do Paraná e Porto União (SC)"  # Item 4, p. 20
CLIENTES_LIVRES_COPEL_COM = 1537           # Item 3, p. 12
CAMBIO_31_12_2025 = 5.5024                 # Item 3, p. 18
SELIC_31_12_2025 = 15.00                   # Item 3, p. 15
IPCA_2025 = 4.26                           # Item 3, p. 15

# Outros fatos (F01)
VENC_CONCESSAO_DIS = "07/07/2045"          # F01, seção 4.2.3, p. 15
MEDIDORES_INTELIGENTES = 2026837           # F01, seção 2, p. 9
DEC_2025_H = 7.17                          # F01, seção 4.2.3, p. 15
FEC_2025 = 4.65                            # F01, seção 4.2.3, p. 15

# F07 - F.D.A. Geração de Energia Elétrica S.A. (controlada) DF 2025
FDA_INTANGIVEL_RS_MIL = 1849570            # F07, Balanço p. 8 e NE 9 p. 20
FDA_BONUS_OUTORGA_RS_MIL = 1840358         # F07, NE 9 p. 20
FDA_VENC_CONCESSAO = "20/11/2054"          # F07, p. 6
FDA_DATA_RELATORIO_AUDITOR = "20/03/2026"  # F07, p. 31

# Composição acionária 31/12/2025 (F01, Anexo I - Capital social)
ACIONISTAS = [
    ("Estado do Paraná (ON + 1 PN classe especial)", 15.9),
    ("BNDESPAR", 22.0),
    ("Free float (B3, NYSE, Latibex, outros)", 61.5),
    ("Ações em tesouraria", 0.4),
]
ACOES_TOTAL = 2982810590

# ---------------------------------------------------------------------------
# F17 - DFs individuais e consolidadas de dezembro/2025 da holding (RI Copel)
# ---------------------------------------------------------------------------
NE16_INTANGIVEL = {"Distribuição": (11868128, 9788358), "Geração": (5831357, 5320920),
                   "Direito de concessão e autorização / ágio técnico": (1409777, 1454161),
                   "Outros intangíveis": (97347, 60171)}                       # NE 16, p. 91
NE16_MOVIMENTO_2025 = [("Saldo em 31.12.2024", 16623610), ("Efeito de combinação de negócios", 731591),
                       ("Outorga Aneel - uso do bem público", -1728), ("Aquisições", 43788),
                       ("Quotas de amortização", -930256), ("Transferências de ativos de contrato", 2901548),
                       ("Baixas", -148017), ("Reclassificação para mantidos para venda", -13927)]
PROV_LITIGIOS = 1571555          # NE 26, p. 105
CONTRAPRESTACAO_CONTINGENTE = 362465   # NE 26.3, p. 105
PASSIVO_CONTINGENTE_CN = 685022  # NE 26, p. 105
PERDAS_POSSIVEIS = (2390222, 2807918)  # NE 26.2, p. 107
RECEITA_NAO_FATURADA = (931460, 930801)  # NE 7, p. 73
PECLD_TOTAL = (255318, 240714)   # NE 7, p. 73
