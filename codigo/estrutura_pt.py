"""
Estrutura comum dos papéis de trabalho (PT) e das normas - usada pela planilha,
pelo dossiê e pela matriz de cobertura. Preparadora: matrícula 232025417.
"""

# Versões das NBC TA consultadas (página do CFC acessada em 24/10/2026 - fonte F09).
# Regra: usar a versão vigente para auditorias do exercício de 2025.
NORMAS = [
    # (codigo, versão aplicável a 2025, publicação, título, observação de vigência)
    ("NBC TA Estrutura Conceitual", "Estrutura Conceitual", "DOU 25/11/2015",
     "Estrutura Conceitual para Trabalhos de Asseguração", "Vigente."),
    ("NBC TA 200", "NBC TA 200 (R1)", "DOU 05/09/2016",
     "Objetivos Gerais do Auditor Independente e a Condução da Auditoria", "Vigente."),
    ("NBC TA 210", "NBC TA 210 (R1)", "DOU 05/09/2016", "Concordância com os Termos do Trabalho de Auditoria", "Vigente."),
    ("NBC TA 220", "NBC TA 220 (R3)", "DOU 09/12/2021", "Gestão de Qualidade da Auditoria de Demonstrações Contábeis",
     "Vigente."),
    ("NBC TA 230", "NBC TA 230 (R1)", "DOU 05/09/2016", "Documentação de Auditoria", "Vigente."),
    ("NBC TA 240", "NBC TA 240 (R1)", "DOU 05/09/2016",
     "Responsabilidade do Auditor em Relação a Fraude", "A NBC TA 240 (R2), DOU 25/09/2026, aplica-se a períodos "
     "iniciados em ou após 01/01/2027; para 2025 vale a (R1)."),
    ("NBC TA 250", "NBC TA 250", "DOU 14/02/2019", "Consideração de Leis e Regulamentos", "Vigente."),
    ("NBC TA 260", "NBC TA 260 (R2)", "DOU 04/07/2016", "Comunicação com os Responsáveis pela Governança", "Vigente."),
    ("NBC TA 265", "NBC TA 265", "Res. CFC 1.210/2009", "Comunicação de Deficiências de Controle Interno", "Vigente."),
    ("NBC TA 300", "NBC TA 300 (R1)", "DOU 05/09/2016", "Planejamento da Auditoria de Demonstrações Contábeis", "Vigente."),
    ("NBC TA 315", "NBC TA 315 (R2)", "DOU 02/09/2021",
     "Identificação e Avaliação dos Riscos de Distorção Relevante", "Vigente."),
    ("NBC TA 320", "NBC TA 320 (R1)", "DOU 05/09/2016", "Materialidade no Planejamento e na Execução da Auditoria", "Vigente."),
    ("NBC TA 330", "NBC TA 330 (R1)", "DOU 05/09/2016", "Resposta do Auditor aos Riscos Avaliados", "Vigente."),
    ("NBC TA 402", "NBC TA 402", "Res. CFC 1.215/2009",
     "Considerações de Auditoria para a Entidade que Utiliza Organização Prestadora de Serviços", "Vigente."),
    ("NBC TA 450", "NBC TA 450 (R1)", "DOU 05/09/2016", "Avaliação das Distorções Identificadas", "Vigente."),
    ("NBC TA 500", "NBC TA 500 (R1)", "DOU 05/09/2016", "Evidência de Auditoria", "Vigente."),
    ("NBC TA 501", "NBC TA 501", "Res. CFC 1.218/2009", "Evidência de Auditoria - Considerações Específicas para Itens Selecionados",
     "Vigente."),
    ("NBC TA 505", "NBC TA 505", "Res. CFC 1.219/2009", "Confirmações Externas", "Vigente."),
    ("NBC TA 510", "NBC TA 510 (R1)", "DOU 05/09/2016", "Trabalhos Iniciais - Saldos Iniciais", "Vigente."),
    ("NBC TA 520", "NBC TA 520", "Res. CFC 1.221/2009", "Procedimentos Analíticos", "Vigente."),
    ("NBC TA 530", "NBC TA 530", "Res. CFC 1.222/2009", "Amostragem em Auditoria", "Vigente."),
    ("NBC TA 540", "NBC TA 540 (R2)", "DOU 23/10/2019",
     "Auditoria de Estimativas Contábeis, Inclusive do Valor Justo, e Divulgações Relacionadas", "Vigente."),
    ("NBC TA 550", "NBC TA 550", "Res. CFC 1.224/2009", "Partes Relacionadas", "Vigente."),
    ("NBC TA 560", "NBC TA 560 (R1)", "DOU 05/09/2016", "Eventos Subsequentes", "Vigente."),
    ("NBC TA 570", "NBC TA 570", "DOU 04/07/2016", "Continuidade Operacional",
     "A NBC TA 570 (R1), DOU 25/09/2026, aplica-se a períodos iniciados em ou após 01/01/2027; para 2025 "
     "vale a versão anterior."),
    ("NBC TA 580", "NBC TA 580 (R1)", "DOU 05/09/2016", "Representações Formais", "Vigente."),
    ("NBC TA 600", "NBC TA 600 (R2)", "DOU 06/12/2023",
     "Considerações Especiais - Auditorias de Demonstrações Contábeis de Grupos", "Vigente para períodos "
     "iniciados em ou após 01/01/2024."),
]

# Papéis de trabalho: (código, título, normas principais, normas secundárias)
PAPEIS = [
    ("PT 000", "Identificação do trabalho, da entidade e das fontes", ["NBC TA 230"], ["NBC TA 300"]),
    ("PT EC", "Estrutura Conceitual: natureza do trabalho e elementos de asseguração", ["NBC TA Estrutura Conceitual"], ["NBC TA 200"]),
    ("PT 500.2", "Classificação dos procedimentos e limitações do trabalho", ["NBC TA 500"], ["NBC TA 200", "NBC TA 230"]),
    ("PT 200", "Objetivos gerais, ceticismo e julgamento profissional", ["NBC TA 200"], []),
    ("PT 210", "Termos do trabalho e precondições", ["NBC TA 210"], []),
    ("PT 220", "Gestão de qualidade do trabalho", ["NBC TA 220"], ["NBC TA 230"]),
    ("PT 230", "Documentação e organização do dossiê", ["NBC TA 230"], []),
    ("PT 240", "Fraude: fatores de risco e respostas", ["NBC TA 240"], ["NBC TA 315", "NBC TA 330"]),
    ("PT 250", "Leis e regulamentos (setor elétrico, societário, CVM/SEC)", ["NBC TA 250"], []),
    ("PT 260", "Comunicação com os responsáveis pela governança", ["NBC TA 260"], ["NBC TA 265"]),
    ("PT 265", "Deficiências de controle interno", ["NBC TA 265"], ["NBC TA 315"]),
    ("PT 300", "Estratégia global e plano de auditoria", ["NBC TA 300"], ["NBC TA 220"]),
    ("PT 315.1", "Entendimento da entidade, do setor elétrico e do controle interno", ["NBC TA 315"], ["NBC TA 250"]),
    ("PT 315.2", "Matriz de riscos de distorção relevante", ["NBC TA 315"], ["NBC TA 240", "NBC TA 540"]),
    ("PT 320", "Materialidade", ["NBC TA 320"], ["NBC TA 450"]),
    ("PT 330", "Respostas aos riscos avaliados", ["NBC TA 330"], ["NBC TA 315"]),
    ("PT 402", "Organizações prestadoras de serviços", ["NBC TA 402"], []),
    ("PT 450", "Avaliação das distorções identificadas", ["NBC TA 450"], ["NBC TA 320", "NBC TA 530"]),
    ("PT 500.1", "Evidência de auditoria: suficiência e adequação", ["NBC TA 500"], []),
    ("PT 501", "Itens selecionados: estoques, litígios e segmentos", ["NBC TA 501"], ["NBC TA 505"]),
    ("PT 505", "Confirmações externas", ["NBC TA 505"], []),
    ("PT 510", "Saldos iniciais", ["NBC TA 510"], ["NBC TA 710"]),
    ("PT 520", "Procedimentos analíticos", ["NBC TA 520"], []),
    ("PT 530", "Amostragem por unidade monetária (base sintética)", ["NBC TA 530"], ["NBC TA 450"]),
    ("PT 540", "Estimativas contábeis", ["NBC TA 540"], ["NBC TA 620"]),
    ("PT 550", "Partes relacionadas", ["NBC TA 550"], []),
    ("PT 560", "Eventos subsequentes", ["NBC TA 560"], []),
    ("PT 570", "Continuidade operacional", ["NBC TA 570"], []),
    ("PT 580", "Representações formais", ["NBC TA 580"], []),
    ("PT 600", "Auditoria de grupo e componentes", ["NBC TA 600"], ["NBC TA 220"]),
    ("PT PA-01", "Programa de auditoria - Receitas", ["NBC TA 330"], ["NBC TA 240", "NBC TA 520"]),
    ("PT PA-02", "Programa de auditoria - Disponibilidades", ["NBC TA 330"], ["NBC TA 505"]),
    ("PT PA-03", "Programa de auditoria - Estoques", ["NBC TA 330"], ["NBC TA 501"]),
    ("PT PA-04", "Programa de auditoria - Imobilizado, intangível e ativos de contrato", ["NBC TA 330"], ["NBC TA 540"]),
    ("PT PA-05", "Programa de auditoria - Passivos", ["NBC TA 330"], ["NBC TA 501", "NBC TA 505"]),
    ("PT PA-06", "Programa de auditoria - Estimativas", ["NBC TA 540"], ["NBC TA 330"]),
    ("PT BS-01", "Base sintética: seleção e materialidade da conta", ["NBC TA 320"], ["NBC TA 315"]),
    ("PT BS-02", "Base sintética: premissas e método de geração", ["NBC TA 500"], ["NBC TA 230"]),
    ("PT BS-03", "Base sintética: dicionário de variáveis", ["NBC TA 230"], []),
    ("PT BS-04", "Base sintética: conciliação com o saldo contábil", ["NBC TA 500"], ["NBC TA 330"]),
    ("PT BS-05", "Base sintética: testes de dados e exceções", ["NBC TA 330"], ["NBC TA 240", "NBC TA 520"]),
    ("PT BS-06", "Base sintética: erros inseridos x identificados", ["NBC TA 450"], ["NBC TA 530"]),
    ("PT RA", "Leitura do relatório do auditor publicado", ["NBC TA 200"], ["NBC TA 260"]),
    ("PT CI", "Conclusão integrada", ["NBC TA 200"], ["NBC TA 450"]),
    ("PT MC", "Matriz de cobertura das normas", ["NBC TA 230"], []),
]


def matriz_cobertura():
    """Lista (norma, versão, PT principais, PT secundários)."""
    linhas = []
    for cod, versao, pub, titulo, obs in NORMAS:
        princ = [p[0] for p in PAPEIS if cod in p[2]]
        sec = [p[0] for p in PAPEIS if cod in p[3]]
        linhas.append((cod, versao, pub, titulo, princ, sec))
    return linhas


# Dicionário de variáveis da base sintética (dados/base_intangivel_sintetica.csv.gz)
DICIONARIO = [
    ("id_registro", "texto", "Identificador único do registro sintético (SINT-0000001 ...).", "Sequencial após embaralhamento."),
    ("flag_dado_sintetico", "texto", "Marca obrigatória: SIM = dado sintético, não é registro real da COPEL.", "Constante."),
    ("segmento", "texto", "Empresa/segmento: Copel DIS, Copel GeT ou Holding/Diversos.", "Derivado da subconta."),
    ("categoria_ne16", "texto", "Categoria do intangível conforme a nota 16 das DFs (Distribuição, Geração, Direito de concessão e autorização, Outros intangíveis).", "Derivada da subconta; totais iguais aos da NE 16 (F17)."),
    ("codigo_subconta", "texto", "Código da subconta do intangível (INT-DIS, BON, GSF, UBP, CNB, UBE, EOL, AUO, SGT, SOF).", "Categorias e subtotal GeT reais (F17, F15); divisão interna da geração hipotética (PT BS-02)."),
    ("subconta", "texto", "Descrição da subconta.", "Derivado."),
    ("tipo_bem", "texto", "Tipo de bem ou direito (ex.: transformador de distribuição, bônus de outorga de usina).", "Lista de 10 tipos na distribuição; nomes de usinas reais nos direitos de geração."),
    ("origem", "texto", "Origem contábil (transferência de ativo de contrato, bônus de outorga, combinação de negócios etc.).", "Derivado da subconta."),
    ("contrato_concessao", "texto", "Contrato ou ato de outorga (identificadores sintéticos).", "Constante por subconta; vazio em softwares e nos erros E06/E07."),
    ("vencimento_concessao", "data", "Fim do prazo da concessão/autorização (AAAA-MM-DD).", "DIS 2045-07-07 (F01); bônus 2054-11-20 (F07); demais hipotéticos."),
    ("codigo_municipio_sint", "texto", "Município sintético PR-001 a PR-394 (só distribuição).", "Uniforme."),
    ("odi", "texto", "Ordem de imobilização sintética.", "Aleatório; vazio nos erros E06/E07."),
    ("centro_custo", "texto", "Centro de custo (CC-DIS, CC-GET, CC-HOL).", "Derivado do segmento."),
    ("status", "texto", "Em serviço ou Em curso.", "0,4% em curso na distribuição; E08 altera."),
    ("data_capitalizacao", "data", "Data de capitalização do bem.", "Até 45 dias antes do início de operação; E03 após 31/12/2025."),
    ("data_inicio_operacao", "data", "Início de operação (base da amortização).", "Uniforme por tipo de bem (2008-2025)."),
    ("data_lancamento", "data", "Data do lançamento contábil.", "Até 20 dias após a capitalização, limitada a 31/12/2025."),
    ("lancamento_manual", "texto", "S = lançamento manual; N = integração de sistema.", "1,5% manuais; direitos de geração manuais."),
    ("usuario_lancamento", "texto", "Usuário do lançamento (USR-01 a USR-40; USR-99 = usuário raro dos erros E07).", "Aleatório entre 40 usuários."),
    ("taxa_amortizacao_anual", "decimal", "Taxa anual de amortização aplicada.", "Maior entre a taxa regulatória do tipo de bem e 1/prazo remanescente; E05 altera."),
    ("taxa_minima_prazo_concessao", "decimal", "Taxa mínima para amortizar até o fim da concessão (1/anos remanescentes no início de operação).", "Calculada."),
    ("custo_historico", "decimal (R$)", "Custo do bem em reais.", "Lognormal por tipo, escalado para o alvo da subconta."),
    ("amortizacao_acumulada", "decimal (R$)", "Amortização acumulada até 31/12/2025 em reais.", "custo x min(1, taxa x anos em serviço); zero se em curso."),
    ("valor_liquido", "decimal (R$)", "Valor contábil líquido em reais (soma = R$ 19.206.609.000,00).", "custo - amortização (salvo erros E09)."),
]


def gravar_dicionario(pasta):
    import csv
    from pathlib import Path
    pasta = Path(pasta)
    with open(pasta / "dicionario_variaveis.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["variavel", "tipo", "descricao", "regra_de_geracao"])
        w.writerows(DICIONARIO)
    linhas = ["# Dicionário de variáveis - base sintética do Intangível (COPEL 2025)", "",
              "**DADOS SINTÉTICOS PARA FINS DIDÁTICOS - não são registros reais da companhia.** "
              "Arquivo: `dados/base_intangivel_sintetica.csv.gz` (CSV, UTF-8, separador vírgula, decimal ponto).", "",
              "| Variável | Tipo | Descrição | Regra de geração |", "|---|---|---|---|"]
    linhas += [f"| `{a}` | {b} | {c} | {d} |" for a, b, c, d in DICIONARIO]
    (pasta / "dicionario_variaveis.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")
