"""
Conteúdo textual do dossiê (papéis de trabalho). Renderizado por 04_dossie_pdf.py.
Convenções no texto:  [F] = fato verificado em fonte pública (com ID da fonte);
[J] = julgamento ou inferência da preparadora; [S] = resultado com dados sintéticos.
Classificação dos procedimentos: R = realizado com evidência pública;
P = planejado por falta de acesso; S = simulado para fins didáticos.
Preparadora: matrícula 232025417 - 24/10/2026.
"""
import json
from pathlib import Path

import dados_publicos as dp

RAIZ = Path(__file__).resolve().parents[1]
RES = json.loads((RAIZ / "resultados" / "resultados_testes.json").read_text())
GER = json.loads((RAIZ / "resultados" / "geracao_resumo.json").read_text())
T11 = RES["T11"]
CMP = RES["comparacao"]
MG = RES["parametros"]["materialidade_global_R$mil"]
ME = RES["parametros"]["materialidade_execucao_R$mil"]
TRIV = RES["parametros"]["trivial_R$mil"]


def br(x, casas=0):
    s = f"{x:,.{casas}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def mi(x_rs):
    """R$ (reais) -> 'R$ x,x milhões'."""
    return f"R$ {br(x_rs / 1e6, 1)} milhões"


LIMITE_GERAL = ("Trabalho baseado apenas em documentos públicos; sem acesso a registros contábeis, sistemas, "
                "contratos, administração, advogados ou auditores. Nenhuma confirmação, entrevista, inspeção "
                "física ou acesso a sistema foi realizado.")

# ---------------------------------------------------------------------------
# Textos de abertura
# ---------------------------------------------------------------------------
ABERTURA = [
    ("1. Apresentação", [
        "Este dossiê reúne os papéis de trabalho de uma auditoria acadêmica das demonstrações contábeis "
        "consolidadas da Companhia Paranaense de Energia - COPEL referentes ao exercício findo em "
        "31/12/2025, com comparativos de 31/12/2024. O trabalho foi elaborado integralmente com apoio de "
        "inteligência artificial, para a disciplina de Auditoria do curso de Ciências Contábeis, e segue a "
        "estrutura das NBC TA: a Estrutura Conceitual para Trabalhos de Asseguração e as normas de 200 a 600.",
        "<b>Este documento não é um relatório de auditoria e não contém opinião profissional independente.</b> "
        "Ele aplica, em ambiente didático, o raciocínio de planejamento, avaliação de riscos e obtenção de "
        "evidência que as normas exigem. A conclusão do item final é integrada e acadêmica: descreve riscos, "
        "procedimentos, evidências e limitações, sem emitir opinião sobre as demonstrações.",
        f"<b>Exercício de referência:</b> 2025. <b>Data de consulta das fontes:</b> {dp.DATA_CONSULTA}. "
        "<b>Base contábil:</b> práticas contábeis adotadas no Brasil (CPC) e IFRS, conforme declarado pela "
        "companhia [F: F02, p. 1]. <b>Unidade:</b> R$ mil, salvo indicação.",
    ]),
    ("2. Como ler este dossiê", [
        "<b>Fato x julgamento.</b> No texto, [F] indica fato verificado em fonte pública, sempre com o "
        "identificador da fonte (F01 a F19, ver docs/fontes.md e o PT 000). [J] indica julgamento ou inferência "
        "da preparadora. [S] indica resultado obtido com dados sintéticos. Quando um dado não pôde ser "
        "confirmado nas fontes, o texto diz isso expressamente; nenhum número foi estimado para preencher lacunas.",
        "<b>Classificação dos procedimentos.</b> Cada procedimento recebe uma de três classificações: "
        "<b>R - realizado com evidência pública</b> (executado com documentos efetivamente obtidos); "
        "<b>P - planejado por falta de acesso</b> (detalhado, mas dependente de informação interna); "
        "<b>S - simulado para fins didáticos</b> (executado sobre a base sintética, identificada e separada "
        "dos dados reais).",
        "<b>Estrutura de cada papel de trabalho.</b> Código, título, norma e itens; objetivo e objeto examinado; "
        "afirmações e riscos; população, fontes e critérios de seleção; procedimentos; evidências e referências "
        "cruzadas; resultados, exceções, conclusão e limitações; preparadora (matrícula e data) e campo de "
        "revisão, deixado em branco porque não houve revisão de terceiros.",
        "<b>Arquivos de apoio.</b> Planilha editável planilhas/PT_calculos_COPEL_2025.xlsx (abas citadas como "
        "XLS:nome_da_aba); base sintética dados/base_intangivel_sintetica.csv.gz; código em codigo/; resultados em "
        "resultados/. A forma de reproduzir está no README.",
    ]),
    ("3. Síntese da companhia e do exercício", [
        "[F] A COPEL atua em geração, transmissão, distribuição e comercialização de energia elétrica, com "
        "concessão de distribuição em 394 dos 399 municípios do Paraná e em Porto União (SC), 218.470 km de "
        "linhas de distribuição e capacidade instalada de 6.226,1 MW, 100% renovável, incluídas as participações "
        "[F02, p. 20]. A concessão de distribuição vence em 07/07/2045 [F01, p. 15].",
        "[F] Desde agosto de 2023 a companhia é uma corporação sem acionista controlador; em 31/12/2025 o capital "
        "era formado por 2.982.810.590 ações ordinárias, com BNDESPAR (22,0%), Estado do Paraná (15,9%, mais uma "
        "ação preferencial de classe especial com direito de veto) e 61,5% em circulação [F01, Anexo I; F02, p. 21].",
        "[F] Fatos do exercício com efeito contábil relevante: migração para o Novo Mercado da B3 concluída em "
        "22/12/2025, com pagamento de prêmio de R$ 1.273.727 mil aos acionistas [F01, p. 1 e DFC p. 25; F05]; "
        "troca de ativos com a Axia (antiga Eletrobras), concluída em 30/05/2025, que levou a 100% da UHE Mauá e "
        "da transmissora Mata de Santa Genebra, com saída da UHE Colíder e desembolso de R$ 196,6 milhões "
        "[F02, p. 22]; venda da UHE Baixo Iguaçu (equity value de R$ 1.683,3 milhões, outubro/2025) e de pequenas "
        "usinas [F02, p. 22]; emissão de R$ 5.000.000 mil em debêntures [F01, p. 25].",
        "[F] Números principais (consolidado): ativo total de R$ 60.414.456 mil; intangível de R$ 19.206.609 mil "
        "(31,8% do ativo); receita operacional líquida de R$ 26.116.856 mil (+15,3%); lucro antes do IR e CSLL de "
        "R$ 3.246.659 mil; lucro líquido das operações continuadas de R$ 2.669.041 mil (+15,7%); dívida bruta de "
        "R$ 20.038,9 milhões e alavancagem de 2,7x dívida líquida/EBITDA [F01, pp. 1, 7, 23-24].",
        "[F] O auditor independente é a PricewaterhouseCoopers Auditores Independentes Ltda. (PwC), contratada "
        "em março de 2024 em substituição à Deloitte, com início dos trabalhos em 2024 e contrato "
        "até o exercício de 2028 [F04]. O Conselho de Administração aprovou as demonstrações em 26/02/2026 [F03], "
        "mesma data do relatório da PwC, sem ressalvas e com três principais assuntos de auditoria [F17, pp. 149-155].",
    ]),
]

# ---------------------------------------------------------------------------
# Papéis de trabalho
# ---------------------------------------------------------------------------
PTS = []


def pt(**k):
    PTS.append(k)


# ======================== A - Gerais ========================================
pt(cod="PT 000", titulo="Identificação do trabalho, da entidade e das fontes",
   normas="NBC TA 230 (R1), itens 8 a 11 (forma e conteúdo da documentação); NBC TA 300 (R1), item 7",
   objetivo="Identificar a entidade auditada, o exercício, as fontes públicas usadas e eventuais mudanças de "
            "nome empresarial e de códigos de negociação, mantendo a companhia atribuída.",
   objeto="Entidade e conjunto completo de demonstrações consolidadas de 2025.",
   afirmacoes="Não se aplica a afirmações específicas; risco de usar documento de outra entidade ou exercício "
              "(por exemplo, demonstrações de controladas com nomes semelhantes).",
   populacao="Documentos da companhia na SEC (EDGAR), no site de RI (plataforma MZ) e na página do CFC; "
             "documentos de controladas usados apenas como apoio e identificados como tais.",
   procedimentos=[
       ("Confirmar razão social, CNPJ e código CVM nos documentos arquivados: Companhia Paranaense de Energia - "
        "COPEL, CNPJ 76.483.817/0001-20, registro CVM 1431-1 [F04].", "R", "F04"),
       ("Levantar alterações de códigos de negociação. Antes da migração ao Novo Mercado: B3 CPLE3, CPLE5, CPLE6 "
        "e CPLE11 (units); NYSE ELP e ELPC; Latibex XCOP, XCOPO e XCOPU [F04, cabeçalho]. Depois de 22/12/2025: "
        "somente ações ordinárias CPLE3 na B3 e ADS ELPC na NYSE; pedido de deslistagem do Latibex noticiado "
        "[F02, p. 1; F05; F14].", "R", "F02, F04, F05, F14"),
       ("Verificar mudança de nome empresarial: não houve alteração da razão social no período. Registram-se, "
        "porém: a marca 'Copel Mercado Livre' para a controlada Copel Comercialização S.A. e a nova denominação "
        "da contraparte Eletrobras, hoje Axia Energia S.A. [F02, p. 22].", "R", "F02"),
       ("Registrar, para cada fonte, endereço eletrônico, data de acesso, documento, página e exercício "
        "(docs/fontes.md e XLS:Fontes).", "R", "PT 230"),
       ("Obter a DFP oficial no sistema da CVM (RAD/ENET) e confrontar com os valores do release e do 20-F.",
        "P", "PT 500.2"),
   ],
   evidencias="docs/fontes.md; XLS:Fontes; XLS:BP (checagem de totais = 'Confere com publicado').",
   resultados="[F] Entidade e exercício identificados sem ambiguidade. As demonstrações das controladas F.D.A. "
              "(F07) e Copel GeT (F10) foram usadas só como apoio, com indicação expressa. [J] A ausência do "
              "download da DFP na CVM é limitação de forma, não de conteúdo: o release (F01) e o 20-F (F02) "
              "trazem as demonstrações consolidadas da mesma entidade e data. Os papéis seguem os códigos do "
              "roteiro obrigatório (item 5 do enunciado): PT EC e PT 200 a PT 600, cada um com a atividade exigida "
              "transcrita. Os papéis complementares (PT 000, PT PA, PT BS, PT RA, PT CI e PT MC) atendem aos itens 3 "
              "e 6 do enunciado.",
   conclusao="Identificação adequada; uma pendência formal (download da DFP na CVM).",
   limitacoes=LIMITE_GERAL)

pt(cod="PT EC", titulo="Estrutura Conceitual: natureza do trabalho e elementos de asseguração",
   normas="NBC TA Estrutura Conceitual (DOU 25/11/2015): elementos do trabalho de asseguração - relação entre "
          "três partes, objeto, critérios, evidência e relatório; NBC TA 200 (R1), item 5",
   objetivo="Demonstrar como os elementos de um trabalho de asseguração se aplicam e quais faltam neste "
            "trabalho acadêmico.",
   objeto="O trabalho como um todo.",
   afirmacoes="Risco de o leitor confundir o trabalho acadêmico com asseguração razoável.",
   populacao="Estrutura Conceitual; demonstrações da COPEL; relatório do auditor (PT RA).",
   procedimentos=[
       ("Mapear as três partes: responsável (administração da COPEL), usuários previstos (acionistas, credores, "
        "reguladores) e profissional (no caso real, a PwC; aqui, a estudante em papel simulado).", "R", "F03, F04"),
       ("Identificar o objeto (posição patrimonial e desempenho de 2025) e os critérios (CPC e IFRS); "
        "avaliar a adequação dos critérios: relevantes, completos, confiáveis, neutros e compreensíveis.", "R", "F02"),
       ("Avaliar se seria possível obter evidência suficiente e apropriada: não, por falta de acesso a "
        "registros e pessoas.", "R", "PT 500.2"),
       ("Definir a forma de conclusão: conclusão integrada acadêmica, sem opinião (PT CI).", "R", "PT CI"),
   ],
   evidencias="PT 500.2 (classificação das evidências); PT RA; PT CI.",
   resultados="[J] Estão presentes objeto apropriado e critérios adequados (CPC/IFRS são estrutura de relatório "
              "financeiro para fins gerais aceitável para companhia aberta). Falta o elemento evidência "
              "suficiente e apropriada para asseguração razoável e não há independência formal nem contratação. "
              "Por isso o trabalho não é de asseguração e não pode resultar em opinião.",
   conclusao="O trabalho é uma aplicação didática das normas; a conclusão final é descritiva.",
   limitacoes="Ausência de contratação, de independência atestada e de acesso à evidência.")

pt(cod="PT 500.2", titulo="Classificação dos procedimentos e limitações do trabalho",
   normas="NBC TA 500 (R1), itens 6 a 9 e A31 (confiabilidade da evidência); NBC TA 200 (R1), itens A47 a A52 "
          "(limitações inerentes)",
   objetivo="Separar o que foi realizado com evidência pública, o que ficou planejado e o que foi simulado; "
            "explicitar as limitações de uma auditoria feita apenas com dados públicos.",
   objeto="Todos os procedimentos do dossiê.",
   afirmacoes="Risco de apresentar como realizado procedimento que não ocorreu.",
   populacao="Todos os PT.",
   procedimentos=[
       ("Classificar cada procedimento como R, P ou S e manter a classificação nas tabelas dos PT.", "R", "Todos"),
       ("Separar fisicamente os dados sintéticos (pasta dados/, prefixo SINT- e coluna flag_dado_sintetico = SIM).",
        "S", "PT BS-02"),
       ("Listar as limitações principais (abaixo) e refleti-las na conclusão.", "R", "PT CI"),
   ],
   evidencias="Tabelas de procedimentos dos PT; resumo quantitativo no PT CI.",
   resultados="[J] Limitações principais: (1) sem acesso a razão, sistemas, contratos e documentos-suporte; "
              "(2) sem confirmações externas, entrevistas, observação de inventário ou carta de representação; "
              "(3) as DFs anuais completas (F17, site de RI) foram conferidas com a DFP versão 1 entregue à "
              "CVM (F18), sem divergência; todas as notas explicativas (1 a 38), o relatório do CAE e o parecer do Conselho Fiscal "
              "foram lidos, mas as tabelas por segmento (NE 31) não foram recalculadas; (4) a divisão interna da geração na base sintética é hipotética, embora "
              "as categorias da nota 16 sejam reais; (5) as normas foram aplicadas por uma única pessoa, sem "
              "revisão.",
   conclusao="Classificação aplicada em todo o dossiê. As limitações impedem qualquer forma de asseguração.",
   limitacoes=LIMITE_GERAL)

# ======================== B - 200 a 265 ====================================
pt(cod="PT 200", titulo="Objetivos gerais, ceticismo e julgamento profissional",
   normas="NBC TA 200 (R1), itens 11 (objetivos), 13 (definições), 15 (ceticismo), 16 (julgamento), "
          "17 (evidência e risco de auditoria) e A47-A52 (limitações inerentes)",
   objetivo="Registrar como o ceticismo e o julgamento foram aplicados à COPEL e onde o risco de auditoria "
            "se concentra.",
   objeto="Demonstrações consolidadas de 2025.",
   afirmacoes="Todas; risco de auditoria = risco de distorção relevante x risco de detecção.",
   populacao="F01, F02, F03, F12.",
   procedimentos=[
       ("Identificar situações que exigem ceticismo reforçado: estimativas regulatórias de grande valor "
        "(CVA, ativo indenizável, ativos de contrato), aumento de 102% nas provisões para litígios, ganhos não "
        "recorrentes (alienações de R$ 477,3 milhões e indenização de curtailment de R$ 265,7 milhões no EBITDA) "
        "e metas públicas de alavancagem e dividendos [F01, pp. 1, 4].", "R", "F01"),
       ("Considerar o histórico: a CVM instaurou processo sancionador contra a firma que auditou DFs anteriores "
        "da Copel (relatório do relator publicado em 2025), apontando falhas de documentação e de procedimentos relacionados à UEGA [F12]. "
        "[J] O fato não indica erro nas DFs de 2025, mas reforça a atenção a investidas e componentes.", "R", "F12"),
       ("Exercer julgamento na materialidade (PT 320), na avaliação de riscos (PT 315.2) e na avaliação da "
        "amostra (PT 530).", "R", "PT 315.2, PT 320"),
       ("Obter evidência corroborativa das alegações da administração (por exemplo, recorrência do EBITDA) "
        "junto a documentos-suporte.", "P", "PT 500.1"),
   ],
   evidencias="F01 seções 1.1 e 1.6; F12; XLS:Indicadores.",
   resultados="[J] O risco de auditoria se concentra em estimativas e em transações não usuais, não em "
              "operações rotineiras. O lucro 'recorrente' divulgado é métrica gerencial, fora do escopo das DFs, "
              "mas seus ajustes revelam onde estão os julgamentos da administração.",
   conclusao="Ceticismo direcionado às áreas de estimativa e às transações não usuais (PT 315.2).",
   limitacoes=LIMITE_GERAL)

pt(cod="PT 210", titulo="Termos do trabalho e precondições",
   normas="NBC TA 210 (R1), itens 6 (precondições), 9 a 12 (carta de contratação)",
   objetivo="Avaliar as precondições para uma auditoria e descrever os termos que uma carta de contratação "
            "deveria conter.",
   objeto="Estrutura de relatório financeiro e responsabilidades da administração.",
   afirmacoes="Risco de estrutura inaceitável ou de a administração não reconhecer suas responsabilidades.",
   populacao="F02 (base de preparação), F03 (aprovação), F04 (contratação da PwC).",
   procedimentos=[
       ("Verificar a estrutura de relatório: CPC e IFRS emitidas pelo IASB, aceitáveis para companhia aberta "
        "(Lei 6.404/1976, art. 177, e regulamentação da CVM) [F02, p. 1].", "R", "F02"),
       ("Verificar evidência pública de que a administração reconhece sua responsabilidade: aprovação pela "
        "Diretoria (20/02/2026), pelo Comitê de Auditoria Estatutário (25/02/2026) e pelo Conselho (26/02/2026) "
        "[F03]; declaração da administração sobre controles internos efetivos no 20-F [F02, p. 117].", "R", "F03, F02"),
       ("Verificar existência de contrato com auditor independente e prazo: PwC até o exercício de 2028 [F04].",
        "R", "F04"),
       ("Redigir os termos que constariam da carta de contratação: objetivo e alcance, responsabilidades do "
        "auditor e da administração, estrutura aplicável, forma do relatório (NBC TA 700), acesso irrestrito a "
        "registros e pessoas e honorários.", "P", "—"),
   ],
   evidencias="F02, F03, F04.",
   resultados="[F] As precondições existem no trabalho real. [J] Neste trabalho acadêmico não há carta de "
              "contratação; a preparadora não tem acesso nem mandato. O enunciado proíbe contatos com a "
              "empresa em nome da UnB, e essa regra foi respeitada.",
   conclusao="Precondições atendidas pela entidade; carta apenas descrita.",
   limitacoes="Sem contratação formal.")

pt(cod="PT 220", titulo="Gestão de qualidade do trabalho",
   normas="NBC TA 220 (R3), itens 13 a 15 (responsabilidade do sócio), 16 a 21 (ética e independência), "
          "25 a 28 (recursos), 29 a 34 (direção, supervisão e revisão)",
   objetivo="Descrever como a qualidade foi gerida num trabalho individual feito com apoio de IA.",
   objeto="Processo de elaboração do dossiê.",
   afirmacoes="Risco de erro de transcrição, de cálculo ou de uso indevido de fonte.",
   populacao="Todo o dossiê e arquivos de apoio.",
   procedimentos=[
       ("Independência: a preparadora declara não ter vínculo com a COPEL; não houve contato com a empresa "
        "ou com seus auditores.", "R", "—"),
       ("Controle de transcrição: todos os números públicos ficam num único arquivo (codigo/dados_publicos.py), "
        "com somas automáticas que conferem cada subtotal com o total publicado.", "R", "XLS:BP"),
       ("Reprodutibilidade: semente fixa (232025417) na geração da base e na seleção da amostra; planilha "
        "confere seus resultados com o código (células 'Planilha = código').", "S", "PT BS-02"),
       ("Uso de IA: o texto e o código foram gerados com IA; os números foram conferidos com as fontes; a "
        "responsabilidade pelo conteúdo é da estudante.", "R", "—"),
       ("Revisão por sócio ou revisor de qualidade do trabalho: não houve; campo deixado em branco.", "P", "—"),
   ],
   evidencias="codigo/dados_publicos.py; XLS:BP, XLS:Materialidade, XLS:MUS_Parametros (checagens).",
   resultados="[F/S] Todas as checagens automáticas retornaram 'Confere com publicado' e 'Planilha = código'.",
   conclusao="Controles de qualidade adequados ao porte do trabalho; falta revisão independente.",
   limitacoes="Ausência de revisor e de sistema de gestão de qualidade de firma.")

pt(cod="PT 230", titulo="Documentação e organização do dossiê",
   normas="NBC TA 230 (R1), itens 7 a 11 (documentação oportuna, forma e conteúdo) e 14 (montagem do arquivo)",
   objetivo="Garantir que um auditor experiente, sem ligação com o trabalho, entenda o que foi feito, os "
            "resultados e as conclusões.",
   objeto="Repositório GitHub.",
   afirmacoes="Risco de documentação insuficiente ou não rastreável.",
   populacao="Pastas dossie/, dados/, codigo/, planilhas/, resultados/ e docs/.",
   procedimentos=[
       ("Organizar o repositório com README, fontes, matriz de cobertura e dicionário de variáveis.", "R", "README"),
       ("Usar referências cruzadas entre PT, abas da planilha e arquivos de resultado.", "R", "Todos"),
       ("Registrar preparadora (matrícula 232025417) e data (24/10/2026) em cada PT e aba.", "R", "Todos"),
       ("Montagem final do arquivo em até 60 dias após o relatório e retenção por 5 anos (prática da firma).",
        "P", "—"),
   ],
   evidencias="Estrutura do repositório (README).",
   resultados="[J] Documentação rastreável do dado público ao cálculo e à conclusão.",
   conclusao="Atendido no limite do trabalho acadêmico.",
   limitacoes="Sem sistema de arquivo eletrônico de firma, trilha de revisão ou bloqueio de alterações.")

pt(cod="PT 240", titulo="Fraude: fatores de risco e respostas",
   normas="NBC TA 240 (R1), itens 15 (ceticismo), 16 a 24 (discussão e procedimentos de risco), 26 (presunção "
          "de risco na receita), 31 a 33 (burlar controles: lançamentos, estimativas, transações não usuais)",
   objetivo="Identificar fatores de risco de fraude na COPEL e definir respostas.",
   objeto="Receita, estimativas, lançamentos manuais e transações não usuais.",
   afirmacoes="Ocorrência e corte (receita); valorização (estimativas); ocorrência e apresentação "
              "(transações não usuais).",
   populacao="F01, F02, F06; base sintética para teste de lançamentos.",
   procedimentos=[
       ("Fatores de incentivo e pressão [F]: política de dividendos de 75% do lucro, condicionada à alavancagem "
        "dentro da faixa de 2,5x a 3,1x [F01, p. 7]; remuneração variável (PLR, PPD e ILP) ligada a "
        "desempenho [F01, p. 6]; expectativas de mercado após a migração ao Novo Mercado. [J] Esses fatores "
        "criam incentivo a apresentar EBITDA e alavancagem favoráveis.", "R", "F01"),
       ("Fatores de oportunidade [F]: estimativas de alta subjetividade (CVA, VNR, ativos de contrato, "
        "provisões) e transações não usuais (troca de ativos, alienações, prêmio do Novo Mercado).", "R", "F01, F02"),
       ("Presunção de risco na receita (item 26): mantida para receita não faturada da distribuição e "
        "contratos bilaterais da comercializadora; refutada para receita de construção (custo + margem pequena, "
        "XLS:Analiticos) e para receita de disponibilidade da transmissão (RAP homologada pela ANEEL).", "R", "PT 315.2"),
       ("Teste de lançamentos manuais (item 32a) sobre a base sintética: lançamentos manuais entre 95% e 100% "
        "da alçada de R$ 1 milhão no fim do exercício, por usuário raro (T09).", "S", "PT BS-05"),
       ("Revisar estimativas quanto a viés (item 32b): comparar estimativas de 2024 com a realização em 2025.",
        "P", "PT 540"),
       ("Avaliar a razão econômica das transações não usuais (item 32c): troca de ativos com a Axia e venda da "
        "UHE Baixo Iguaçu, lendo contratos e laudos.", "P", "PT PA-04"),
       ("Indagar administração, auditoria interna e Comitê de Auditoria sobre fraudes conhecidas ou suspeitas.",
        "P", "PT 260"),
   ],
   evidencias="F01 pp. 1, 4, 6-7; XLS:Analiticos; resultados/excecoes_detectadas.csv.",
   resultados=f"[S] O teste T09 isolou os {CMP['matriz'][6]['inseridos']} lançamentos fictícios inseridos (E07), "
              f"de R$ {br(CMP['matriz'][6]['distorcao_inserida_R'], 2)}, sem falsos positivos. [J] Na base real "
              "esses lançamentos seriam investigados como possível fraude, independentemente do valor.",
   conclusao="Riscos de fraude identificados: receita não faturada, estimativas regulatórias, burlar controles "
             "e transações não usuais (PT 315.2, R01, R02, R09, R10).",
   limitacoes=LIMITE_GERAL + " Não houve indagação a pessoas nem acesso ao razão real.")

pt(cod="PT 250", titulo="Leis e regulamentos (setor elétrico, societário, CVM/SEC)",
   normas="NBC TA 250, itens 13 (leis com efeito direto), 14 (outras leis) e 19 a 22 (não conformidade)",
   objetivo="Identificar o arcabouço legal que afeta valores e divulgações.",
   objeto="Concessões, tarifas, tributos, dividendos e mercado de capitais.",
   afirmacoes="Ocorrência, completude e divulgação de passivos regulatórios e contingências.",
   populacao="F01, F02, F07, F08; legislação citada em docs/fontes.md.",
   procedimentos=[
       ("Leis com efeito direto: Lei 6.404/1976 (arts. 176, 177 e 202, dividendo obrigatório); Lei 9.249/1995 "
        "(JCP); regulação da ANEEL sobre tarifas, CVA, revisão tarifária e P&D/eficiência energética; Lei "
        "10.848/2004 (contratação de 100% da demanda pelas distribuidoras) [F02, p. 12]; Lei 14.385/2022 "
        "(devolução de créditos de PIS/Cofins, saldo de R$ 780.553 mil) [F01, p. 24].", "R", "F01, F02"),
       ("Outras leis relevantes: LGPD (multas de até R$ 50 milhões por infração) [F02, p. 6]; legislação "
        "ambiental e de segurança de barragens [F02, p. 6]; eliminação de PCBs até 2025 e gestão até 2028 "
        "[F02, p. 13]; SOX seção 404 (ICFR auditado) [F02, p. 117].", "R", "F02"),
       ("Eventos regulatórios do período: renovação da concessão de Foz do Areia por 30 anos com bônus de "
        "outorga de R$ 1,84 bilhão (contrato de 18/11/2024) [F07, p. 6]; revisão da RBSE com efeito negativo "
        "de R$ 115,1 milhões (REH 3.467/2025) [F01, p. 13].", "R", "F01, F07"),
       ("Ler correspondência com ANEEL, autos de infração, multas por indicadores de qualidade (DEC/FEC) e "
        "atas, e indagar o jurídico sobre não conformidades.", "P", "PT 501"),
   ],
   evidencias="F01, F02, F07.",
   resultados="[F] DEC de 7,17 h e FEC de 4,65 em 2025, dentro dos limites regulatórios [F01, p. 15]; perdas "
              "totais 0,49% abaixo do limite regulatório em dezembro/2025 [F01, p. 16]. [J] Não foram "
              "identificados indícios públicos de não conformidade que exigissem comunicação.",
   conclusao="Arcabouço mapeado; riscos regulatórios refletidos em R02, R03, R05 e R11 (PT 315.2).",
   limitacoes=LIMITE_GERAL)

pt(cod="PT 260", titulo="Comunicação com os responsáveis pela governança",
   normas="NBC TA 260 (R2), itens 11 a 13 (identificação dos responsáveis) e 14 a 17 (assuntos a comunicar)",
   objetivo="Identificar a governança e os assuntos que seriam comunicados.",
   objeto="Conselho de Administração, Comitê de Auditoria Estatutário (CAE) e Conselho Fiscal.",
   afirmacoes="Não se aplica a afirmações; risco de omissão de comunicação obrigatória.",
   populacao="F03; F02 (Item 6).",
   procedimentos=[
       ("Identificar os responsáveis: Conselho de Administração (88,8% de membros independentes [F01, seção 6.3]), "
        "CAE (324ª reunião em 25/02/2026) e Conselho Fiscal, ao qual as DFs foram encaminhadas [F03].", "R", "F03, F01"),
       ("Verificar evidência pública de comunicação do auditor: manifestação da PwC ao Conselho sobre o trabalho "
        "de 2025, sem ressalvas [F03].", "R", "F03"),
       ("Assuntos que seriam comunicados neste trabalho: escopo e época; riscos significativos (PT 315.2); "
        "distorções da simulação, incluindo os lançamentos E07 com natureza de fraude (PT 450); a diferença "
        "não explicada nas provisões para litígios (PT 540); independência.", "P", "PT 315.2, PT 450"),
   ],
   evidencias="F03.",
   resultados="[F] Há estrutura de governança com comitê de auditoria estatutário e evidência pública de "
              "interação com o auditor. [J] O conteúdo das comunicações não é público.",
   conclusao="Destinatários identificados; comunicações apenas descritas.",
   limitacoes="Atas detalhadas do CAE e cartas do auditor não são públicas.")

pt(cod="PT 265", titulo="Deficiências de controle interno",
   normas="NBC TA 265, itens 7 e 8 (determinar deficiências e deficiências significativas) e 9 a 11 "
          "(comunicação)",
   objetivo="Avaliar a evidência pública sobre controles e registrar deficiências encontradas na simulação.",
   objeto="Controles sobre relatórios financeiros (ICFR).",
   afirmacoes="Todas, via controles.",
   populacao="F02 Item 15; F02 fatores de risco; base sintética.",
   procedimentos=[
       ("Ler a conclusão da administração: ICFR efetivo em 31/12/2025 pelos critérios COSO 2013; auditoria "
        "integrada da PwC sobre ICFR incluída no 20-F; nenhuma mudança relevante nos controles [F02, p. 117].",
        "R", "F02"),
       ("Identificar riscos de controle anunciados: novo sistema de faturamento com entrada em operação "
        "prevista para 2026 [F02, p. 7]; ataques cibernéticos já sofridos [F02, p. 6].", "R", "F02"),
       ("Na simulação, classificar como deficiências: ausência de ODI/contrato em 50 registros (E06) e lançamentos "
        "manuais sem suporte acima de 95% da alçada (E07).", "S", "PT BS-05"),
       ("Testar controles-chave (aprovação de ODI, conciliação ativo de contrato x intangível, medição e "
        "faturamento).", "P", "PT 330"),
   ],
   evidencias="F02 pp. 6-7 e 117; resultados/excecoes_detectadas.csv.",
   resultados="[F] Não há deficiência material divulgada. [S] A falta de suporte (E06) seria deficiência; a "
              "combinação E06 + E07 (lançamentos manuais sem ODI) seria deficiência significativa, a comunicar "
              "por escrito à governança.",
   conclusao="Sem deficiências públicas; deficiências simuladas documentadas.",
   limitacoes="O relatório integrado sobre ICFR não foi lido na íntegra (PT RA).")

# ======================== C - 300 a 450 =====================================
pt(cod="PT 300", titulo="Estratégia global e plano de auditoria",
   normas="NBC TA 300 (R1), itens 7 e 8 (estratégia global), 9 (plano), 11 (direção e supervisão)",
   objetivo="Definir alcance, época, direção e recursos.",
   objeto="Auditoria do consolidado de 2025.",
   afirmacoes="Todas.",
   populacao="Resultado dos PT 315.1, PT 315.2 e PT 320.",
   procedimentos=[
       ("Alcance: consolidado (holding, Copel DIS, Copel GeT, Copel Com, Copel Serviços, SPEs eólicas e de "
        "transmissão) e investidas por equivalência (PT 600).", "R", "PT 600"),
       ("Época (planejamento real típico): planejamento no 3º trimestre, intermediária no 4º trimestre, "
        "final em janeiro-fevereiro, relatório em 26/02/2026 (data da aprovação) [F03].", "R", "F03"),
       ("Direção: abordagem combinada (controles + substantivos) nas áreas de grande volume (receita, "
        "intangível); substantiva com especialistas nas estimativas (atuário para benefícios; especialista "
        "regulatório para CVA, VNR e ativos de contrato) (NBC TA 620).", "P", "PT 330"),
       ("Plano deste trabalho: análise pública (R), programas por área (P) e testes na base sintética (S).",
        "R", "PT PA-01 a PA-06"),
   ],
   evidencias="Sequência dos PT; XLS:Materialidade.",
   resultados="[J] A estratégia prioriza os riscos significativos R01 a R10.",
   conclusao="Estratégia e plano definidos.",
   limitacoes="Recursos limitados a uma pessoa; sem especialistas.")

pt(cod="PT 315.1", titulo="Entendimento da entidade, do setor elétrico e do controle interno",
   normas="NBC TA 315 (R2), itens 19 e 20 (entidade, ambiente e estrutura de relatório), 21 a 27 "
          "(componentes do controle interno)",
   objetivo="Entender o negócio, o setor e o controle interno para identificar riscos.",
   objeto="Modelo de negócio e ambiente regulatório.",
   afirmacoes="Base para todas.",
   populacao="F01, F02, F07.",
   procedimentos=[
       ("Segmentos [F]: distribuição (receita líquida de R$ 19.202.210 mil; concessão até 2045); geração e "
        "transmissão (R$ 5.096.936 mil; 9.687 km de linhas com participações); comercialização (R$ 4.402.327 mil; "
        "1.537 clientes livres) [F01, pp. 10-17, 29-31; F02, p. 12]. Valores antes de eliminações.", "R", "F01, F02"),
       ("Modelo contábil das concessões [J]: distribuição pelo modelo bifurcado da ICPC 01 (R1)/IFRIC 12 - "
        "ativo de contrato durante a obra (CPC 47), intangível pelo direito de cobrar tarifa (CPC 04) e ativo "
        "financeiro indenizável no fim da concessão (CPC 48, VNR); transmissão como ativo de contrato; geração "
        "com bônus de outorga e UBP no intangível e imobilizado.", "R", "F01, F02"),
       ("Fatores externos [F]: Selic de 15% e IPCA de 4,26% em 2025 [F02, p. 15]; GSF baixo e PLD alto no 4T25; "
        "curtailment de 34,2% nas eólicas [F01, p. 4]; avanço da micro e minigeração distribuída e migração ao "
        "mercado livre (consumo cativo -5,7% no ano) [F01, p. 15].", "R", "F01, F02"),
       ("Controle interno [F]: ambiente com conselho majoritariamente independente, CAE, programa de "
        "integridade certificado ISO 37301 [F07, p. 5], avaliação COSO 2013 [F02, p. 117].", "R", "F02, F07"),
       ("Percorrer processos (walkthrough) de faturamento, compra de energia, capitalização de obras e "
        "fechamento contábil.", "P", "PT 330"),
   ],
   evidencias="F01, F02, F07; XLS:DRE.",
   resultados="[J] A demonstração de resultado mistura receitas com e sem margem (construção, CVA, repasse de "
              "energia), o que reduz o poder dos indicadores de margem e exige analíticos por componente.",
   conclusao="Entendimento suficiente para a matriz de riscos (PT 315.2).",
   limitacoes="Sem walkthrough e sem acesso a políticas internas.")

pt(cod="PT 315.2", titulo="Matriz de riscos de distorção relevante",
   normas="NBC TA 315 (R2), itens 28 a 37 (identificação e avaliação dos riscos, risco inerente separado do "
          "risco de controle, riscos significativos); NBC TA 240 (R1), itens 26 e 31; NBC TA 540 (R2), item 16",
   objetivo="Identificar e avaliar os riscos de distorção relevante no nível das demonstrações e das afirmações.",
   objeto="Contas significativas (XLS:Contas_Significativas).",
   afirmacoes="Indicadas na tabela.",
   populacao="Balanço e DRE consolidados; fatores de risco inerente: complexidade, subjetividade, mudança, "
             "incerteza e suscetibilidade a viés.",
   procedimentos=[
       ("Classificar as contas pela materialidade de execução (XLS:Contas_Significativas) e pelos fatores de "
        "risco inerente.", "R", "XLS"),
       ("Avaliar o risco inerente no espectro (baixo, moderado, alto, significativo).", "R", "Tabela"),
       ("Avaliar o risco de controle: mantido como máximo neste trabalho (sem teste de controles).", "R", "PT 330"),
   ],
   tabela_extra=("Matriz de riscos", ["Risco", "Conta / afirmação", "Base factual", "Risco inerente", "Resposta"], [
       ["R01 Receita não faturada e contratos bilaterais (fraude presumida)", "Receita - ocorrência, corte",
        "Fornecimento R$ 7.961.249; suprimento R$ 4.756.273 [F01]", "Significativo", "PT PA-01"],
       ["R02 Ativos e passivos financeiros setoriais (CVA)", "Ativos/passivos setoriais - valorização, ocorrência",
        "Resultado R$ 2.348.143 (+180%) [F01]", "Significativo", "PT PA-06"],
       ["R03 Ativos de contrato (distribuição e transmissão)", "Ativos de contrato - valorização",
        "R$ 9.595.006 (CP+LP) [F01]", "Significativo", "PT PA-04"],
       ["R04 Intangível de concessão (amortização, transferências, impairment)", "Intangível - existência, valorização",
        "R$ 19.206.609; 31,8% do ativo [F01]", "Alto", "PT PA-04, PT BS-01 a BS-06"],
       ["R05 Ativo financeiro indenizável (VNR, nível 3)", "Contas a receber da concessão - valorização",
        "R$ 4.603.446; VNR no resultado R$ 161.244 [F01]", "Significativo", "PT PA-06"],
       ["R06 Provisões para litígios", "Provisões - completude, valorização",
        "R$ 1.934.020 (+102%); 20-F informa R$ 1.571,6 mi [F01; F02 p. 7]", "Significativo", "PT PA-05, PT 501"],
       ["R07 Benefícios pós-emprego", "Passivo atuarial - valorização", "R$ 1.478.157 (CP+LP) [F01]",
        "Alto", "PT PA-06"],
       ["R08 Instrumentos financeiros e dívida (MTM de energia, debêntures, covenants)",
        "Valorização, apresentação", "Debêntures R$ 16.646.924; MTM ativo R$ 861.501 [F01]", "Alto", "PT PA-05"],
       ["R09 Transações não usuais (troca de ativos, alienações, Novo Mercado)", "Ocorrência, apresentação",
        "Ganhos de R$ 477,3 mi; prêmio R$ 1.273.727 [F01]", "Significativo", "PT PA-04, PT 550"],
       ["R10 Burlar controles pela administração", "Todas", "Presunção da NBC TA 240", "Significativo", "PT 240"],
       ["R11 Provisão para destinação de créditos de PIS/Cofins", "Completude, valorização",
        "R$ 780.553 (era R$ 1.580.588) [F01]", "Alto", "PT PA-05"],
       ["R12 IR e CSLL diferidos", "Ativo diferido - valorização", "Ativo R$ 991.404; passivo R$ 1.982.596 [F01]",
        "Moderado", "PT PA-06"],
       ["R13 Divulgações (partes relacionadas, eventos subsequentes, segmentos)", "Apresentação e divulgação",
        "Estado do PR, BNDESPAR, Fundação Copel [F01; F07]", "Moderado", "PT 550, PT 560"],
       ["R14 Continuidade operacional", "Base de elaboração", "Liquidez corrente 0,98 [XLS:Indicadores]",
        "Baixo", "PT 570"],
   ]),
   evidencias="XLS:Contas_Significativas; XLS:Indicadores; XLS:Analiticos.",
   resultados="[J] Sete riscos significativos (R01, R02, R03, R05, R06, R09 e R10) e quatro altos (R04, R07, R08 e R11). "
              "O risco no nível das demonstrações vem da pressão por métricas (dividendos e alavancagem) e da "
              "complexidade regulatória.",
   conclusao="Matriz concluída; respostas no PT 330 e nos programas F.",
   limitacoes="Avaliação sem conhecimento de controles e sem notas explicativas integrais.")

pt(cod="PT 320", titulo="Materialidade",
   normas="NBC TA 320 (R1), itens 10 (materialidade global), 11 (materialidade para execução), 12 e 13 "
          "(revisão) e 14 (documentação); A3 a A8 (referenciais)",
   objetivo="Determinar a materialidade global, a de execução e o limite claramente trivial.",
   objeto="Demonstrações consolidadas.",
   afirmacoes="Todas.",
   populacao="DRE e balanço consolidados [F01, pp. 23-24].",
   procedimentos=[
       (f"Referencial escolhido: lucro antes do IR e CSLL das operações continuadas, R$ {br(RES['parametros']['LAIR_R$mil'])} "
        "mil, x 5%. [J] É o indicador que os usuários acompanham (lucro e dividendos) e é estável.", "R", "XLS:Materialidade"),
       ("Comparar com referenciais alternativos: 0,5% da ROL, 1% do PL, 0,5% do ativo e 3% do EBITDA.", "R", "XLS"),
       (f"Materialidade de execução = 70% da global; limite trivial = 5% da global.", "R", "XLS"),
       ("Revisar a materialidade ao fim do trabalho se surgirem novas informações.", "P", "—"),
   ],
   evidencias="XLS:Materialidade (fórmulas; checagem 'Planilha = código').",
   resultados=f"[J] Materialidade global R$ {br(MG)} mil (6,1% do lucro líquido continuado e 0,27% do ativo); "
              f"execução R$ {br(ME)} mil; trivial R$ {br(TRIV)} mil. A PwC não divulga a materialidade que usou.",
   conclusao="Parâmetros usados em todo o dossiê, inclusive na amostragem (PT 530).",
   limitacoes="Julgamento individual, sem calibração com a política de uma firma.")

pt(cod="PT 330", titulo="Respostas aos riscos avaliados",
   normas="NBC TA 330 (R1), itens 5 (respostas gerais), 6 e 7 (procedimentos adicionais), 18 "
          "(substantivos para cada classe relevante), 21 (riscos significativos) e 24 (apresentação)",
   objetivo="Vincular cada risco a procedimentos de natureza, época e extensão adequadas.",
   objeto="Riscos R01 a R14.",
   afirmacoes="Conforme PT 315.2.",
   populacao="Matriz de riscos.",
   procedimentos=[
       ("Respostas gerais: equipe com experiência no setor elétrico, imprevisibilidade na seleção de itens, "
        "ênfase em ceticismo nas estimativas.", "P", "PT 300"),
       ("Para riscos significativos, incluir testes de detalhes (não apenas analíticos), como exige o item 21.",
        "P", "PT PA-01 a PA-06"),
       ("Executar substantivos em todas as contas relevantes (item 18), mesmo com controles efetivos.", "P", "PT PA-01 a PA-06"),
       ("Executar com dados sintéticos os testes de detalhes do intangível (R04).", "S", "PT BS-05, PT 530"),
   ],
   evidencias="Programas PT PA-01 a PT PA-06.",
   resultados="[J] Cada risco tem resposta definida; as respostas que exigem acesso ficaram planejadas.",
   conclusao="Respostas desenhadas; execução real depende de acesso.",
   limitacoes=LIMITE_GERAL)

pt(cod="PT 402", titulo="Organizações prestadoras de serviços",
   normas="NBC TA 402, itens 9 a 14 (entendimento dos serviços) e 15 a 17 (respostas; relatórios tipo 1 e 2)",
   objetivo="Identificar prestadores cujos serviços fazem parte do sistema de informação relevante.",
   objeto="Liquidação de energia, folha/benefícios, custódia.",
   afirmacoes="Ocorrência e exatidão de receitas e custos liquidados por terceiros.",
   populacao="F01, F02, F07.",
   procedimentos=[
       ("Identificar a CCEE como liquidante do mercado de curto prazo e do MRE [F07, p. 25] e o ONS, cujas "
        "decisões de despacho e curtailment afetam receitas [F01, p. 4]. [J] São entidades setoriais, não "
        "prestadoras contratadas, mas seus relatórios são insumos do sistema de informação.", "R", "F01, F07"),
       ("Identificar a Fundação Copel como administradora dos planos de benefícios, cujos dados alimentam a "
        "avaliação atuarial (CPC 33).", "R", "F02"),
       ("Obter relatórios de asseguração sobre controles (tipo 2) de prestadores relevantes, se houver, ou "
        "testar diretamente as informações (por exemplo, conciliar liquidações da CCEE com a receita).", "P", "PT PA-01"),
   ],
   evidencias="F01, F07; F02 fatores de risco.",
   resultados="[J] A CCEE e o ONS não emitem relatório tipo 2; a resposta adequada é testar diretamente os "
              "relatórios de liquidação. Isso torna a NBC TA 402 relevante, mesmo sem prestador típico.",
   conclusao="Aplicável; procedimentos planejados.",
   limitacoes="Sem acesso a contratos com prestadores e relatórios de liquidação.")

pt(cod="PT 450", titulo="Avaliação das distorções identificadas",
   normas="NBC TA 450 (R1), itens 5 (acumulação), 8 e 9 (comunicação e correção), 11 (avaliação do efeito)",
   objetivo="Acumular e avaliar distorções.",
   objeto="Distorções da evidência pública e da simulação.",
   afirmacoes="Todas.",
   populacao="XLS:Distorcoes; resultados/erros_inseridos_x_detectados.csv.",
   procedimentos=[
       ("Evidência pública: nenhuma distorção identificada. A diferença das provisões foi explicada (PT 501) e "
        "a dos dividendos a pagar foi reduzida a um resíduo de R$ 43.898 mil (PT 520), que não é distorção, "
        "mas diferença a explicar com a composição do saldo.", "R", "PT 520"),
       (f"Simulação: acumular a distorção factual da base sintética, R$ {br(CMP['distorcao_total_inserida_R$'], 2)} "
        f"líquidos (superavaliação R$ {br(CMP['distorcao_superavaliacao_R$'], 2)}; subavaliação "
        f"R$ {br(abs(CMP['distorcao_subavaliacao_R$']), 2)}).", "S", "PT BS-06"),
       ("Comparar com o trivial e a execução; avaliar natureza (E07 indica fraude).", "S", "XLS:Distorcoes"),
       ("Solicitar correção à administração e obter representação sobre distorções não corrigidas.", "P", "PT 580"),
   ],
   evidencias="XLS:Distorcoes; XLS:Excecoes.",
   resultados=f"[S] A distorção líquida de R$ {br(CMP['distorcao_total_inserida_R$'] / 1000, 0)} mil fica acima "
              f"do trivial (R$ {br(TRIV)} mil) e abaixo da execução (R$ {br(ME)} mil): seria acumulada e "
              "sua correção solicitada. Os lançamentos E07 são relevantes pela natureza.",
   conclusao="Na simulação, não há distorção relevante pelo valor, mas há assunto relevante pela natureza.",
   limitacoes="Distorções reais não podem ser identificadas sem acesso aos registros.")

# ======================== D - 500 a 580 =====================================
pt(cod="PT 500.1", titulo="Evidência de auditoria: suficiência e adequação",
   normas="NBC TA 500 (R1), itens 6 (evidência suficiente e apropriada), 7 a 9 (relevância e confiabilidade "
          "da informação) e A31 (hierarquia de confiabilidade)",
   objetivo="Avaliar a qualidade das evidências obtidas.",
   objeto="Fontes F01 a F19.",
   afirmacoes="Todas.",
   populacao="docs/fontes.md.",
   procedimentos=[
       ("Classificar a confiabilidade: documentos arquivados em órgão regulador (SEC) e aprovados pela "
        "governança (F01-F06, F08) = alta; documentos de controladas (F07, F10) = alta, mas de outra entidade; "
        "notícias (F14) = apenas corroborativas.", "R", "docs/fontes.md"),
       ("Testar a integridade da informação: somas e subtotais do balanço e da DRE recalculados.", "R", "XLS:BP, XLS:DRE"),
       ("Confrontar o mesmo dado em duas fontes: lucro líquido 2025 no release e no 20-F; intangível da F.D.A. "
        "no balanço e na nota 9 da controlada [F07, pp. 8 e 20].", "R", "F01, F02, F07"),
       ("Obter evidência externa e documental (confirmações, contratos, laudos).", "P", "PT 505"),
   ],
   evidencias="XLS:BP e XLS:DRE (todas as checagens 'Confere').",
   resultados="[F] Todos os subtotais recalculados conferem com os publicados. [J] A evidência pública é "
              "confiável quanto à fidedignidade da transcrição, mas insuficiente para concluir sobre as "
              "afirmações (existência, valorização etc.).",
   conclusao="Evidência adequada para análise; insuficiente para asseguração.",
   limitacoes=LIMITE_GERAL)

pt(cod="PT 501", titulo="Itens selecionados: estoques, litígios e segmentos",
   normas="NBC TA 501, itens 4 a 8 (estoques), 9 a 12 (litígios e reclamações) e 13 (informações por segmento)",
   objetivo="Planejar os procedimentos específicos exigidos para estoques, litígios e segmentos.",
   objeto="Estoques R$ 173.398 mil; provisões para litígios R$ 1.934.020 mil; segmentos.",
   afirmacoes="Existência e condição (estoques); completude e valorização (litígios); divulgação (segmentos).",
   populacao="F01, F02.",
   procedimentos=[
       ("Estoques: saldo de R$ 173.398 mil (R$ 136.324 mil em 2024) [F01]. [J] Acima da materialidade de "
        "execução (R$ 113.633 mil): a observação da contagem física é exigida. Planejar acompanhamento do "
        "inventário nos almoxarifados de materiais de manutenção e obras.", "P", "PT PA-03"),
       ("Litígios: indagar administração e jurídico, ler atas e enviar carta de circularização aos assessores "
        "jurídicos externos.", "P", "PT 505"),
       ("Litígios: reconciliar a linha do balanço (R$ 1.934.020 mil) com a provisão para processos judiciais "
        "informada no 20-F (R$ 1.571,6 milhões); diferença de R$ 362.420 mil [F01; F02, p. 7].", "R", "XLS:Analiticos"),
       ("Explicar a diferença com a nota 25 da Copel GeT: 'Provisões para litígios e outras provisões' de "
        "R$ 1.357.070 mil em 31/12/2025, dos quais R$ 994.605 mil de litígios e R$ 362.465 mil de 'outras "
        "provisões - contraprestação contingente' de combinação de negócios [F15, NE 25, p. 27].", "R", "F15"),
       ("Segmentos: verificar se a divulgação segue o CPC 22/IFRS 8 e confere com a informação gerencial "
        "(DIS, GeT, Com, holding) [F01, pp. 29-34].", "R", "F01"),
   ],
   evidencias="XLS:Analiticos linha 5; F01 Anexo II.",
   resultados="[F] A linha do balanço (R$ 1.934.020 mil) menos a contraprestação contingente da Copel GeT "
              "(R$ 362.465 mil) resulta em R$ 1.571.555 mil, igual aos R$ 1.571,6 milhões do 20-F após "
              "arredondamento. [J] A diferença está explicada: a linha consolidada inclui 'outras provisões'. Ponto "
              "encerrado. A GeT tem ainda R$ 685.022 mil de passivo contingente reconhecido em combinação de "
              "negócios (CPC 15), parte dos litígios consolidados [F15, p. 27].",
   conclusao="NBC TA 501 aplicável nos três itens; estoques exigem observação física (planejada).",
   limitacoes="Sem cartas a advogados nem inventário observado.")

pt(cod="PT 505", titulo="Confirmações externas",
   normas="NBC TA 505, itens 7 (procedimentos de confirmação), 8 e 9 (recusa da administração), 10 a 14 "
          "(resultados)",
   objetivo="Desenhar o plano de confirmações.",
   objeto="Caixa, dívidas, clientes livres, CCEE, advogados.",
   afirmacoes="Existência, direitos e obrigações, completude.",
   populacao="Balanço consolidado.",
   procedimentos=[
       ("Bancos: saldos de caixa e aplicações (R$ 3.130.363 mil) e garantias.", "P", "PT PA-02"),
       ("Agentes fiduciários e bancos credores: debêntures (R$ 16.646.924 mil), empréstimos (R$ 3.368.419 mil) "
        "e cumprimento de covenants.", "P", "PT PA-05"),
       ("Clientes: amostra de clientes livres e contratos bilaterais da comercializadora; CCEE para saldos de "
        "liquidação.", "P", "PT PA-01"),
       ("Advogados externos: processos, prognósticos e valores.", "P", "PT 501"),
   ],
   evidencias="Plano descrito.",
   resultados="[J] Nenhuma confirmação foi enviada ou recebida. O enunciado proíbe contato com terceiros.",
   conclusao="Plano pronto; nenhuma confirmação realizada.",
   limitacoes="Procedimento inteiramente dependente de acesso.")

pt(cod="PT 510", titulo="Saldos iniciais",
   normas="NBC TA 510 (R1), itens 5 a 9 (procedimentos sobre saldos iniciais e consistência de políticas)",
   objetivo="Avaliar se os saldos de abertura de 2025 são confiáveis.",
   objeto="Balanço de 31/12/2024.",
   afirmacoes="Existência e valorização dos saldos de abertura; consistência das políticas.",
   populacao="F02 (relatórios PwC e Deloitte); F04.",
   procedimentos=[
       ("Verificar quem auditou o ano anterior: a PwC auditou 2024 (primeiro ano, após revisar a ITR do 1T24) "
        "e a Deloitte auditou 2023 [F04; F02, índice F-3 e F-7]. [J] Para a PwC, 2025 não é trabalho inicial; "
        "a NBC TA 510 seria exigida da PwC em 2024.", "R", "F02, F04"),
       ("Para este trabalho acadêmico (inicial para a preparadora), conferir que os comparativos de 2024 no "
        "release de 2025 são os mesmos auditados e identificar reclassificações.", "R", "F01"),
       ("Verificar operações descontinuadas reapresentadas nos comparativos: lucro de operações descontinuadas "
        "de R$ 491.571 mil em 2024 [F01, p. 23].", "R", "F01"),
       ("Ler os papéis do auditor anterior sobre saldos de abertura.", "P", "—"),
   ],
   evidencias="F01, F02, F04.",
   resultados="[F] O 20-F não marca reapresentação por correção de erro [F02, capa]. [J] Saldos de abertura "
              "auditados sem modificação conhecida; consistência de políticas a confirmar na nota de políticas.",
   conclusao="Sem indício de problema nos saldos iniciais.",
   limitacoes="Relatório da PwC de 2024 não lido na íntegra.")

pt(cod="PT 520", titulo="Procedimentos analíticos",
   normas="NBC TA 520, itens 5 (analíticos substantivos: adequação, confiabilidade dos dados, expectativa, "
          "diferença aceitável) e 6 (analíticos na conclusão)",
   objetivo="Usar análises horizontal, vertical e de expectativa para identificar variações não usuais.",
   objeto="Balanço, DRE e indicadores.",
   afirmacoes="Ocorrência, completude, valorização.",
   populacao="XLS:BP, XLS:DRE, XLS:Indicadores, XLS:Analiticos.",
   procedimentos=[
       ("Análise horizontal e vertical de todas as rubricas.", "R", "XLS:BP, XLS:DRE"),
       ("Expectativa da despesa financeira: dívida média x custo nominal de 13,22% = R$ 2.462.985 mil; despesa "
        "registrada de R$ 3.142.010 mil (27,6% acima). Investigação com a nota 30 [F17, p. 117]: encargos e "
        "variação monetária da dívida de R$ 2.490.902 mil (1,1% acima da expectativa, dentro do limite); os "
        "R$ 651.108 mil restantes são itens fora da dívida (concessões, PIS/Cofins sobre JCP, CVA, litígios, "
        "arrendamentos, swap). Diferença explicada.", "R", "XLS:Analiticos"),
       ("Receita de construção x custo de construção: margem de R$ 30.387 mil (0,9%), coerente com a política "
        "de custo mais margem pequena.", "R", "XLS:Analiticos"),
       ("Dividendos mínimos a pagar (R$ 2.325.889 mil) x proventos declarados no 4T25 (R$ 1,35 bilhão de "
        "dividendos e R$ 1,1 bilhão de JCP) [F01, p. 1; F06]: diferença de R$ 124.111 mil. Investigação [F17]: o "
        "IRRF sobre JCP de R$ 168.009 mil está em outras obrigações fiscais (NE 12.2, p. 81); o JCP foi pago em "
        "19/01/2026 e os dividendos vencem até 30/06/2026 (NE 27.6, p. 112). Proventos líquidos do IRRF "
        "(R$ 2.281.991 mil) ficam R$ 43.898 mil abaixo do saldo; resíduo não explicado pelas notas.", "R", "XLS:Analiticos"),
       ("EBITDA recalculado (EBIT + D&A) = publicado (R$ 6.526.897 mil).", "R", "XLS:DRE"),
       ("Analíticos de receita por classe de consumo e por mês, com dados de mercado (GWh x tarifa).", "P", "PT PA-01"),
   ],
   evidencias="XLS:Analiticos; XLS:Indicadores.",
   resultados="[F] Variações relevantes: intangível +15,5%; ativos de contrato +33%; debêntures +31%; provisões "
              "para litígios +102%; dividendos a pagar de R$ 3.878 mil para R$ 2.325.889 mil; liquidez corrente "
              "de 1,26 para 0,98. [F] A despesa financeira está explicada pela nota 30. [J] A diferença dos "
              "dividendos foi reduzida a R$ 43.898 mil pelo IRRF sobre JCP; o resíduo fica acima do trivial "
              "(R$ 8.117 mil) e abaixo da materialidade de execução, e exigiria a composição do saldo.",
   conclusao="Variações explicadas, exceto o resíduo de R$ 43.898 mil nos dividendos a pagar, abaixo da "
             "materialidade de execução.",
   limitacoes="Sem dados mensais e sem razão.")

pt(cod="PT 530", titulo="Amostragem por unidade monetária (base sintética)",
   normas="NBC TA 530, itens 6 a 8 (desenho e tamanho da amostra), 9 (seleção), 12 a 15 (natureza das "
          "distorções, projeção e avaliação)",
   objetivo="Testar existência e valorização do intangível por amostragem estatística.",
   objeto="Intangível - base sintética (registros com valor positivo).",
   afirmacoes="Existência e valorização (superavaliação).",
   populacao=f"[S] {br(T11['registros_populacao'])} registros com valor positivo, total R$ "
             f"{br(T11['populacao_valor_positivo_R$'], 2)}; {br(T11['registros_negativos_excluidos'])} registros "
             "com valor zero ou negativo ficaram fora e foram testados por CAAT (T02).",
   procedimentos=[
       (f"Parâmetros: distorção tolerável = materialidade de execução (R$ {br(ME)} mil); distorção esperada de "
        f"10%; confiança de 95% (fator {T11['fator_confiabilidade_95%']}); fator de expansão 1,6.", "S", "XLS:MUS_Parametros"),
       (f"Tamanho: n = {T11['tamanho_amostra']}; intervalo J = R$ {br(T11['intervalo_amostral_R$'], 2)}; seleção "
        f"sistemática com início aleatório (semente 232025417).", "S", "XLS:MUS_Parametros"),
       (f"Itens selecionados: {T11['itens_selecionados_unicos']} registros únicos, sendo {T11['itens_chave']} itens-chave "
        f"(valor maior ou igual a J, R$ {br(T11['valor_itens_chave_R$'], 2)}).", "S", "resultados/amostra_mus.csv"),
       ("Inspeção simulada: o valor auditado é tirado do gabarito de erros, representando o que o exame do "
        "documento revelaria.", "S", "XLS:MUS_Amostra"),
       ("Projeção e limite superior de distorção (LSD).", "S", "XLS:MUS_Avaliacao"),
   ],
   evidencias="XLS:MUS_Parametros, MUS_Amostra, MUS_Avaliacao; resultados/amostra_mus.csv.",
   resultados=f"[S] Itens com distorção na amostra: {T11['itens_com_distorcao']}, todos lançamentos fictícios E07, com "
              f"contaminação de 100%. Distorção projetada R$ {br(T11['distorcao_projetada_R$'], 2)}; LSD R$ "
              f"{br(T11['limite_superior_distorcao_R$'], 2)}, maior que a distorção tolerável (R$ {br(ME * 1000, 2)}). "
              "Pela NBC TA 530, item 15, a amostra não dá base razoável: o teste foi estendido a 100% da população "
              "com CAAT (T09), que isolou os 30 lançamentos E07, somando R$ "
              f"{br(CMP['matriz'][6]['distorcao_inserida_R'], 2)}. A distorção real total é menor que a projetada: "
              "a projeção é conservadora quando os erros se concentram em itens de valor alto e atípico.",
   conclusao="Amostra estendida por CAAT; distorção conhecida e isolada; ver PT 450.",
   limitacoes="Dados e inspeção simulados. Os testes foram desenhados conhecendo os tipos de erro, o que "
              "explica a detecção de 100% sem falsos positivos; em dados reais isso não ocorre.")

pt(cod="PT 540", titulo="Estimativas contábeis",
   normas="NBC TA 540 (R2), itens 13 (entendimento), 16 e 17 (avaliação de riscos com risco inerente separado), "
          "18 a 30 (respostas: método, premissas, dados, estimativa independente), 32 (indicadores de viés)",
   objetivo="Identificar as estimativas relevantes e planejar as respostas.",
   objeto="CVA, VNR, ativos de contrato, receita não faturada, PECLD, provisões, benefícios, impairment, IR "
          "diferido, MTM de energia, provisão de PIS/Cofins.",
   afirmacoes="Valorização, divulgação.",
   populacao="F01, F02, F07.",
   procedimentos=[
       ("Listar estimativas e valores [F]: resultado da CVA R$ 2.348.143 mil; VNR R$ 161.244 mil; ativos de "
        "contrato R$ 9.595.006 mil; PECLD R$ 245,6 milhões [F02, p. 5]; provisões R$ 1.934.020 mil; benefícios "
        "pós-emprego R$ 1.478.157 mil; MTM de energia (ativo R$ 861.501 mil; passivo R$ 531.442 mil); provisão "
        "de PIS/Cofins R$ 780.553 mil.", "R", "F01, F02"),
       ("Avaliar incerteza: alta para VNR e ativos de contrato (taxas de desconto e índices regulatórios); alta "
        "para provisões (prognóstico jurídico); moderada para PECLD.", "R", "PT 315.2"),
       ("Indicador de viés: a mudança de estimativa de vida útil por renovação de concessão reduziu a "
        "depreciação da F.D.A. de R$ 119.234 mil para R$ 76.748 mil [F07, p. 6]. [J] É efeito legítimo de "
        "renovação, mas mostra a sensibilidade do resultado às premissas de prazo.", "R", "F07"),
       ("Testar método, premissas e dados; desenvolver estimativa independente para VNR e CVA com "
        "especialista regulatório; recalcular PECLD por faixa de atraso; ler laudo atuarial.", "P", "PT PA-06"),
       ("Retrospectiva: comparar provisões de 2024 com os desfechos de 2025.", "P", "PT PA-06"),
   ],
   evidencias="F01, F02, F07.",
   resultados="[F] As estimativas somam mais de dez vezes a materialidade global. [F] A diferença nas provisões foi explicada "
              "pela contraprestação contingente (PT 501). [J] Os passivos de combinação de negócios (contraprestação "
              "contingente e passivo contingente) são estimativas relevantes a acrescentar ao programa PT PA-06.",
   conclusao="Estimativas são a principal fonte de risco; respostas planejadas com especialistas.",
   limitacoes="Sem acesso a premissas, laudos e modelos.")

pt(cod="PT 550", titulo="Partes relacionadas",
   normas="NBC TA 550, itens 11 a 17 (entendimento e riscos), 18 a 24 (respostas, inclusive transações "
          "fora do curso normal), 25 (avaliação da divulgação)",
   objetivo="Identificar partes relacionadas e transações relevantes.",
   objeto="Acionistas relevantes, entidades ligadas, investidas, pessoal-chave.",
   afirmacoes="Completude e divulgação (CPC 05 (R1)/IAS 24).",
   populacao="F01 (composição acionária), F07 (NE 19), F02.",
   procedimentos=[
       ("Identificar: Estado do Paraná (15,9% e golden share) e entidades ligadas a ele (Sanepar, Simepar); "
        "BNDESPAR (22,0%); Fundação Copel; Lactec (OSCIP da qual a Copel é associada); joint ventures de "
        "transmissão e coligadas; pessoal-chave [F01; F07, p. 26].", "R", "F01, F07"),
       ("Transações relevantes intragrupo vistas na F.D.A.: venda de energia à Copel Comercialização de "
        "R$ 573.606 mil em 2025 [F07, p. 26]. [J] Eliminadas no consolidado; testar eliminações.", "R", "F07"),
       ("Verificar se o BNDES/BNDESPAR é também credor (financiamentos via repasse BNDES) e se a relação está "
        "divulgada.", "P", "PT PA-05"),
       ("Avaliar a troca de ativos com a Axia: a Axia não é parte relacionada conhecida; [J] o risco é de "
        "transação não usual, não de parte relacionada.", "R", "F02"),
   ],
   evidencias="F01 Anexo I (capital); F07 NE 19.",
   resultados="[J] Partes relacionadas relevantes identificadas; após a privatização, o Estado deixou de ser "
              "controlador, mas segue com influência via golden share e participação, o que mantém a "
              "necessidade de divulgação.",
   conclusao="Riscos de divulgação moderados (R13).",
   limitacoes="Sem acesso a contratos e ao processo de aprovação das transações.")

pt(cod="PT 560", titulo="Eventos subsequentes",
   normas="NBC TA 560 (R1), itens 6 a 9 (eventos até a data do relatório), 10 a 13 (fatos conhecidos após "
          "a data do relatório); CPC 24/IAS 10",
   objetivo="Identificar eventos após 31/12/2025 e classificá-los.",
   objeto="Período de 01/01/2026 até a data do relatório (26/02/2026) e depois.",
   afirmacoes="Completude, divulgação.",
   populacao="F06, F07, F08, F02.",
   procedimentos=[
       ("Antes do relatório: dividendos de R$ 1,35 bilhão aprovados em 10/12/2025 (data-base 30/12/2025, "
        "pagamento até 30/06/2026) [F06]. [J] Fato do próprio exercício, refletido no passivo; não é evento "
        "subsequente.", "R", "F06"),
       ("Antes do relatório: antecipação de dividendos da F.D.A. de R$ 120.000 mil em 16/01/2026 [F07, p. 22]. "
        "[J] Intragrupo; sem efeito consolidado.", "R", "F07"),
       ("Após o relatório consolidado: F.D.A. vencedora do leilão de potência (18/03/2026), receita fixa de "
        "R$ 963,2 milhões/ano por 15 anos e investimento estimado de R$ 1,3 bilhão [F07, p. 27]; "
        "renegociação do UBP da Elejor (maio/2026) [F08]. [J] Eventos que não ajustam 2025.", "R", "F07, F08"),
       ("Indagar a administração, ler atas posteriores e obter representação sobre eventos subsequentes.", "P", "PT 580"),
   ],
   evidencias="F06, F07, F08.",
   resultados="[J] Nenhum evento conhecido exigiria ajuste nas DFs de 2025. Os eventos posteriores à data do "
              "relatório não obrigariam o auditor a agir (NBC TA 560, item 10), salvo se tornassem as DFs "
              "enganosas, o que não é o caso.",
   conclusao="Sem eventos que exijam ajuste.",
   limitacoes="Sem acesso a atas e sem indagações.")

pt(cod="PT 570", titulo="Continuidade operacional",
   normas="NBC TA 570 (versão vigente para 2025), itens 10 e 11 (avaliação de riscos), 12 e 13 (avaliação "
          "da administração para 12 meses) e 16 (procedimentos adicionais)",
   objetivo="Avaliar se há eventos ou condições que levantem dúvida significativa.",
   objeto="Liquidez, endividamento e geração de caixa.",
   afirmacoes="Base de elaboração.",
   populacao="F01; XLS:Continuidade.",
   procedimentos=[
       ("Indicadores: liquidez corrente de 0,98 (1,26 em 2024); caixa de R$ 3.739 milhões contra amortizações "
        "de R$ 2.068 milhões em 2026 (cobertura de 1,8x); fluxo operacional de R$ 3,0 bilhões; alavancagem de "
        "2,7x, dentro da faixa de 2,5x a 3,1x [F01, pp. 7-8, 25].", "R", "XLS:Continuidade"),
       ("Explicar a liquidez abaixo de 1: aumento dos dividendos a pagar (R$ 2.325.889 mil) e venda de ativos "
        "mantidos para venda que estavam no circulante em 2024 [F01, p. 24].", "R", "XLS:BP"),
       ("Ler a avaliação da administração, projeções de caixa e cláusulas de covenants.", "P", "PT PA-05"),
   ],
   evidencias="XLS:Continuidade; XLS:Indicadores.",
   resultados="[J] Sem indício de incerteza relevante. A F.D.A. declara não haver incertezas materiais "
              "[F07, p. 13], e a holding também (NE 3.5) [F17, p. 64].",
   conclusao="Base de continuidade adequada pelos dados públicos.",
   limitacoes="Sem projeções da administração.")

pt(cod="PT 580", titulo="Representações formais",
   normas="NBC TA 580 (R1), itens 10 e 11 (responsabilidades da administração), 13 (outras representações), "
          "14 (data)",
   objetivo="Definir o conteúdo da carta de representação.",
   objeto="Carta a ser assinada pelo diretor-presidente e pelo diretor financeiro.",
   afirmacoes="Todas.",
   populacao="Riscos e pontos em aberto deste dossiê.",
   procedimentos=[
       ("Representações gerais: responsabilidade pelas DFs e pelos controles; acesso a todas as informações; "
        "registro de todas as transações.", "P", "—"),
       ("Representações específicas: premissas de VNR, CVA e ativos de contrato; completude de litígios; "
        "partes relacionadas; eventos subsequentes; distorções não corrigidas (simulação).", "P", "PT 540"),
       ("Exemplo de evidência pública análoga: declaração dos diretores da F.D.A. de que revisaram as DFs e "
        "concordam com o relatório da PwC [F07, p. 28].", "R", "F07"),
   ],
   evidencias="F07 p. 28.",
   resultados="[J] Nenhuma carta foi obtida nem simulada como assinada.",
   conclusao="Conteúdo definido; procedimento não realizado.",
   limitacoes="Dependente de acesso à administração.")

pt(cod="PT 600", titulo="Auditoria de grupo e componentes",
   normas="NBC TA 600 (R2): entendimento do grupo e dos componentes, avaliação dos riscos no nível do grupo, "
          "determinação do trabalho nos componentes, envolvimento com auditores de componentes e consolidação; "
          "NBC TA 220 (R3) aplicada ao trabalho de grupo",
   objetivo="Definir componentes e escopo da auditoria do grupo.",
   objeto="Grupo COPEL consolidado e investidas.",
   afirmacoes="Todas; consolidação e eliminações.",
   populacao="F01 Anexo II (DRE por empresa); F01 Anexo I (equivalência).",
   procedimentos=[
       ("Componentes pela receita líquida antes de eliminações [F]: Copel DIS R$ 19.202.210 mil; Copel GeT "
        "(geração R$ 2.253.075 mil e transmissão R$ 1.097.358 mil); Copel Com R$ 4.402.327 mil; parques eólicos "
        "R$ 877.553 mil; F.D.A. R$ 598.908 mil; Elejor R$ 153.989 mil; eliminações (R$ 2.851.941 mil) "
        "[F01, Anexo II, DRE acumulada por empresa].", "R", "F01"),
       ("[J] Copel DIS e Copel GeT são componentes significativos (auditoria completa); Copel Com tem risco "
        "específico (MTM, contratos bilaterais); demais com procedimentos analíticos no nível do grupo.", "R", "PT 315.2"),
       ("Investidas por equivalência: equivalência de R$ 239.997 mil e investimentos de R$ 2.849.002 mil; "
        "transmissoras em conjunto (Matrinchã, Guaraciaba, Paranaíba, Cantareira, Caiuá, Integração "
        "Maranhense) e coligadas [F01, p. 27]. Obter DFs auditadas das investidas.", "R/P", "F01"),
       ("Auditores dos componentes: a PwC audita controladas (por exemplo, F.D.A. [F07, p. 31]); os auditores "
        "das joint ventures não foram identificados. Avaliar competência e independência e revisar papéis.", "P", "—"),
       ("Testar eliminações intragrupo, como a venda de energia da F.D.A. à Copel Com (R$ 573.606 mil).", "P", "PT 550"),
   ],
   evidencias="F01 Anexos I e II; F07.",
   resultados="[F] A Copel DIS responde por cerca de 66% da receita somada dos componentes antes de eliminações (73,5% da receita consolidada). [J] O escopo "
              "proposto cobre os componentes de maior risco e valor.",
   conclusao="Escopo de grupo definido.",
   limitacoes="Sem acesso a auditores de componentes e a pacotes de consolidação.")

# ======================== F - programas =====================================
pt(cod="PT PA-01", titulo="Programa de auditoria - Receitas",
   normas="NBC TA 330 (R1), itens 18 e 21; NBC TA 240 (R1), item 26; NBC TA 520; CPC 47/IFRS 15; ICPC 01",
   objetivo="Obter evidência sobre ocorrência, completude, exatidão e corte das receitas.",
   objeto="ROL de R$ 26.116.856 mil.",
   afirmacoes="Ocorrência, completude, exatidão, corte, classificação.",
   populacao="Faturamento de distribuição, suprimento, TUSD/TUST, construção, CVA, outras receitas.",
   procedimentos=[
       ("Analíticos: análise horizontal e vertical por componente da receita.", "R", "XLS:DRE"),
       ("Testar controles do ciclo de faturamento (leitura, tarifa homologada, emissão, arrecadação).", "P", "—"),
       ("Recalcular tarifas aplicadas com as resoluções homologatórias da ANEEL (reajuste de junho/2025).", "P", "—"),
       ("Receita não faturada: recalcular com consumo estimado entre a última leitura e 31/12; comparar com o "
        "faturamento de janeiro/2026 (corte).", "P", "—"),
       ("Contratos bilaterais da Copel Com: confirmar com contrapartes e conciliar com registros na CCEE.", "P", "PT 505"),
       ("Receita de construção: conciliar com adições aos ativos de contrato (R$ 2.903.661 mil na DFC).", "P", "PT PA-04"),
       ("Lançamentos manuais em contas de receita perto da data-base (NBC TA 240).", "P", "PT 240"),
   ],
   evidencias="XLS:DRE; XLS:Analiticos.",
   resultados="[F] Receita +15,3%, puxada por suprimento (+52,4%) e CVA (+180,1%); fornecimento a consumidores "
              "finais -5,8% (migração ao mercado livre e redução da tarifa de energia) [F01, pp. 5, 23].",
   conclusao="Variações coerentes com o release; testes de detalhes planejados.",
   limitacoes=LIMITE_GERAL)

pt(cod="PT PA-02", titulo="Programa de auditoria - Disponibilidades",
   normas="NBC TA 330 (R1), item 18; NBC TA 505; CPC 03 (R2)",
   objetivo="Existência e direitos sobre caixa e aplicações.",
   objeto="Caixa e equivalentes R$ 3.130.363 mil; TVM R$ 691.781 mil (CP+LP).",
   afirmacoes="Existência, direitos, valorização, classificação.",
   populacao="Contas bancárias e aplicações do grupo.",
   procedimentos=[
       ("Conferir caixa final da DFC com o balanço: R$ 3.130.363 mil nos dois [F01, pp. 24-25].", "R", "F01"),
       ("Circularizar bancos; obter extratos e conciliações bancárias de 31/12/2025.", "P", "PT 505"),
       ("Verificar classificação como equivalente de caixa (liquidez em 90 dias, risco insignificante).", "P", "—"),
       ("Identificar saldos vinculados a garantias (por exemplo, CDBs em garantia de contratos de uso do "
        "sistema de transmissão, como na F.D.A. [F07, p. 18]).", "R/P", "F07"),
   ],
   evidencias="F01; F07.",
   resultados="[F] Caixa confere entre balanço e DFC; redução de R$ 1.031.576 mil no ano, explicada por "
              "investimentos, prêmio do Novo Mercado e dividendos [F01, p. 25].",
   conclusao="Sem exceção nos procedimentos públicos.",
   limitacoes="Sem confirmação bancária.")

pt(cod="PT PA-03", titulo="Programa de auditoria - Estoques",
   normas="NBC TA 501, itens 4 a 8; NBC TA 330 (R1); CPC 16 (R1)/IAS 2",
   objetivo="Existência, condição e valorização dos estoques.",
   objeto="Estoques R$ 173.398 mil (materiais de manutenção e operação).",
   afirmacoes="Existência, valorização (custo ou valor realizável).",
   populacao="Almoxarifados do grupo.",
   procedimentos=[
       ("Avaliar materialidade: saldo acima da execução (R$ 113.633 mil), variação de +27,2% [F01].", "R", "XLS:BP"),
       ("Acompanhar a contagem física de fim de ano nos principais almoxarifados; testes de contagem nos dois "
        "sentidos (registro para físico e físico para registro).", "P", "—"),
       ("Testar custo médio e obsolescência (itens parados há mais de 12 meses).", "P", "—"),
       ("Separar materiais de obra (que vão para ativo de contrato) de materiais de manutenção.", "P", "PT PA-04"),
   ],
   evidencias="XLS:BP.",
   resultados="[J] A conta é relevante pelo valor, mas de risco moderado (materiais, sem produção).",
   conclusao="Aplicável; observação física planejada.",
   limitacoes="Sem acesso físico.")

pt(cod="PT PA-04", titulo="Programa de auditoria - Imobilizado, intangível e ativos de contrato",
   normas="NBC TA 330 (R1), itens 18 e 21; NBC TA 540 (R2); ICPC 01 (R1)/IFRIC 12; OCPC 05; CPC 04 (R1)/IAS 38; "
          "CPC 27/IAS 16; CPC 01 (R1)/IAS 36; CPC 15 (R1)/IFRS 3; CPC 31/IFRS 5",
   objetivo="Existência, valorização e apresentação dos ativos de concessão.",
   objeto="Intangível R$ 19.206.609 mil; ativos de contrato R$ 9.595.006 mil; imobilizado R$ 8.145.552 mil; "
          "contas a receber da concessão R$ 4.603.446 mil.",
   afirmacoes="Existência, direitos, valorização, classificação, apresentação.",
   populacao="Cadastro de bens de concessão; ODI; contratos de concessão; combinação de negócios.",
   procedimentos=[
       ("Conciliar o razão analítico com o balanço (base sintética: diferença zero).", "S", "PT BS-04"),
       ("Testes de dados em 100% do cadastro (duplicidades, corte, recálculo de amortização, prazo da "
        "concessão, em curso com amortização, campos em branco, lançamentos manuais).", "S", "PT BS-05"),
       ("Amostragem MUS para existência e valorização.", "S", "PT 530"),
       ("Conciliar a variação do intangível (+R$ 2.582.999 mil) com adições de caixa (R$ 43.788 mil), "
        "transferências de ativos de contrato, combinação de negócios (UHE Mauá) e amortização.", "R/P", "XLS:Conciliacao_Intangivel"),
       ("Bônus de outorga: conferir com contratos de concessão; Foz do Areia R$ 1.840.358 mil [F07, p. 20].", "R", "F07"),
       ("Troca de ativos com a Axia: ler contrato, laudo de alocação do preço de compra e cálculo de "
        "ganho/perda (CPC 15).", "P", "PT 240"),
       ("Alienações (Baixo Iguaçu e pequenas usinas): conferir baixa de ativos mantidos para venda "
        "(R$ 1.881.826 mil em 2024 para R$ 25.177 mil) e ganhos (CPC 31).", "R/P", "F01"),
       ("Impairment: obter teste por unidade geradora de caixa para eólicas (curtailment de 34,2%).", "P", "PT PA-06"),
   ],
   evidencias="PT BS-04 a BS-06; PT 530; XLS:Conciliacao_Intangivel; F07.",
   resultados="[F] A variação do intangível não passa pelo caixa: adições de caixa somam R$ 43.788 mil contra "
              "aumento líquido de R$ 2.582.999 mil, o que indica transferências de ativos de contrato e "
              "combinação de negócios. [J] A movimentação da nota explicativa é necessária para concluir.",
   conclusao="Testes simulados concluídos; testes reais planejados.",
   limitacoes="Composição real do intangível não obtida.")

pt(cod="PT PA-05", titulo="Programa de auditoria - Passivos",
   normas="NBC TA 330 (R1); NBC TA 501, itens 9 a 12; NBC TA 505; CPC 25/IAS 37; CPC 33 (R1)/IAS 19; "
          "CPC 48/IFRS 9; CPC 40 (R1)/IFRS 7; OCPC 08",
   objetivo="Completude, existência e valorização dos passivos.",
   objeto="Debêntures e empréstimos R$ 20.015.343 mil; fornecedores R$ 3.193.211 mil; provisões R$ 1.934.020 mil; "
          "benefícios R$ 1.478.157 mil; passivos setoriais R$ 883.990 mil; PIS/Cofins R$ 780.553 mil.",
   afirmacoes="Completude, existência, valorização, classificação (circulante/não circulante).",
   populacao="Contratos de dívida, fornecedores, processos, laudo atuarial.",
   procedimentos=[
       ("Dívida: conferir com cronograma (R$ 2.068 milhões vencendo em 2026) e com emissões e amortizações da "
        "DFC (emissão R$ 5.000.000 mil; amortização R$ 3.317.499 mil) [F01, pp. 8, 25].", "R", "F01"),
       ("Covenants: obter escrituras e recalcular índices; verificar cross-default.", "P", "PT 505"),
       ("Fornecedores: busca de passivos não registrados (pagamentos de janeiro-fevereiro/2026).", "P", "—"),
       ("Provisões: carta a advogados; diferença de R$ 362.420 mil com o 20-F explicada pela contraprestação "
        "contingente de R$ 362.465 mil [F15].", "R/P", "PT 501"),
       ("Benefícios: revisar premissas atuariais com atuário (NBC TA 620).", "P", "PT PA-06"),
       ("Passivos setoriais e PIS/Cofins: conferir com despachos da ANEEL e valores devolvidos nas tarifas.", "P", "—"),
   ],
   evidencias="F01; XLS:Analiticos.",
   resultados="[F] Debêntures cresceram 31% e a parcela circulante de empréstimos caiu de R$ 1.231.205 mil para "
              "R$ 217.827 mil, coerente com a amortização de R$ 1.254.405 mil [F01, p. 25].",
   conclusao="Coerência entre balanço e DFC; testes de detalhe planejados.",
   limitacoes=LIMITE_GERAL)

pt(cod="PT PA-06", titulo="Programa de auditoria - Estimativas",
   normas="NBC TA 540 (R2), itens 18 a 30; NBC TA 620; CPC 46/IFRS 13; CPC 48/IFRS 9; CPC 33 (R1); CPC 32/IAS 12; "
          "OCPC 08",
   objetivo="Responder aos riscos das estimativas (R02, R03, R05, R07, R08, R12).",
   objeto="Estimativas listadas no PT 540.",
   afirmacoes="Valorização, divulgação.",
   populacao="Modelos da administração.",
   procedimentos=[
       ("CVA: recalcular saldos com custos realizados x cobertura tarifária, conferir com despachos da ANEEL.", "P", "—"),
       ("VNR (ativo indenizável): testar base de remuneração regulatória e índices de atualização (nível 3).", "P", "—"),
       ("Ativos de contrato: testar taxa de remuneração e margem; reconciliar RAP com a REH 3.467/2025.", "P", "—"),
       ("PECLD: recalcular por faixa de atraso; vencidos líquidos de R$ 605,5 milhões [F02, p. 5] = 14% dos "
        "clientes de curto prazo.", "R/P", "XLS:Analiticos"),
       ("IR diferido: projeções de lucro tributável; o JCP reduz a carga (alíquota efetiva de 17,8% em 2025 = "
        "577.618 / 3.246.659).", "R/P", "XLS:DRE"),
       ("MTM de energia: preços futuros e curva de desconto (hierarquia do CPC 46).", "P", "—"),
   ],
   evidencias="XLS:Analiticos; F02.",
   resultados="[F] Alíquota efetiva de 17,8% (577.618/3.246.659), abaixo dos 34% nominais, explicada em parte "
              "pelo JCP declarado [F01, p. 7]. [J] A conciliação da alíquota na nota é necessária.",
   conclusao="Programa definido; execução depende de especialistas e de acesso.",
   limitacoes=LIMITE_GERAL)

# ======================== G - base sintética ================================
lin = GER["linhas_por_subconta"]
pt(cod="PT BS-01", titulo="Base sintética: seleção e materialidade da conta",
   normas="NBC TA 320 (R1), item 10; NBC TA 315 (R2), item 28",
   objetivo="Justificar a escolha do intangível como conta de maior materialidade do ativo.",
   objeto="Intangível consolidado.",
   afirmacoes="Existência, valorização.",
   populacao="Balanço de 31/12/2025 [F01, p. 24].",
   procedimentos=[
       ("Ordenar as contas do ativo por saldo: intangível R$ 19.206.609 mil (31,8%); ativos de contrato "
        "(LP) R$ 9.202.412 mil; imobilizado R$ 8.145.552 mil; contas a receber da concessão (LP) "
        "R$ 4.590.579 mil; clientes (CP) R$ 4.300.957 mil.", "R", "XLS:BP"),
       ("Comparar com a materialidade: o intangível equivale a 118 vezes a materialidade global.", "R", "XLS:Materialidade"),
   ],
   evidencias="XLS:BP; XLS:Indicadores.",
   resultados="[F] O intangível é a maior conta do ativo nas duas datas e cresceu 15,5%. [J] Sua natureza "
              "(milhares de bens de concessão da distribuição, direitos de concessão de geração e softwares) "
              "permite uma base analítica de registros individuais.",
   conclusao="Intangível escolhido.",
   limitacoes="—")

pt(cod="PT BS-02", titulo="Base sintética: premissas e método de geração",
   normas="NBC TA 500 (R1), item 7 (informação usada como evidência); NBC TA 230 (R1)",
   objetivo="Explicar como a base foi gerada, com quais premissas e onde ela se afasta da realidade.",
   objeto="dados/base_intangivel_sintetica.csv.gz.",
   afirmacoes="—",
   populacao=f"[S] {br(GER['linhas'])} linhas, {GER['colunas']} colunas, semente {GER['semente']}.",
   procedimentos=[
       ("Composição (R$ mil). Real, nota 16 [F17, p. 91]: distribuição 11.868.128; geração 5.831.357; direito de "
        "concessão e autorização/ágio técnico 1.409.777; outros intangíveis 97.347. Real, Copel GeT [F15, NE 15, "
        "p. 21]: geração 5.671.800, direito de autorização 1.402.043, outros 76.776; por diferença, fora da GeT: "
        "geração 159.557 (Elejor e outras), direito de autorização 7.734 e outros 20.571. Hipótese didática: "
        "divisão dos 5.671.800 da GeT em bônus de outorga 4.191.800, combinação de negócios (Mauá) 700.000, "
        "UBP 520.000 e GSF 260.000. Cada categoria da nota 16 e o subtotal da GeT fecham ao centavo.",
        "S", "codigo/01_gerar_base.py"),
       (f"Registros: distribuição {br(lin['INT-DIS'])} (10 tipos de bem, custos lognormais, datas de 2008 a 2025); "
        f"softwares {br(lin['INT-SOF'])}; 42 parques eólicos (número real de parques [F02, p. 20]); 9 extensões GSF; "
        "6 UBP; 3 bônus; 2 combinação de negócios.", "S", "—"),
       ("Âncora real: o registro de Foz do Areia recebeu o intangível da F.D.A., R$ 1.849.570 mil [F07, p. 8].", "S", "F07"),
       ("Amortização linear pela maior taxa entre a regulatória e a do prazo remanescente da concessão "
        "(distribuição até 07/07/2045 [F01, p. 15]; bônus em 30 anos até 20/11/2054 [F07, p. 6]).", "S", "—"),
       ("Erros inseridos (E01 a E09, 580 registros) com gabarito em dados/log_erros_inseridos.csv; ajuste final "
        "proporcional nos registros limpos para que o total iguale o saldo contábil ao centavo.", "S", "PT BS-06"),
   ],
   evidencias="codigo/01_gerar_base.py; resultados/geracao_resumo.json.",
   resultados="[S] Base gerada com identificador SINT-, coluna flag_dado_sintetico = SIM e sem qualquer "
              "registro real. [J] Afastamentos da realidade: composição, custos e datas são hipotéticos; o "
              "intangível real da distribuição deriva de transferências do ativo de contrato e o cadastro real "
              "segue o Manual de Controle Patrimonial do Setor Elétrico.",
   conclusao="Método reproduzível e documentado.",
   limitacoes="Dados sintéticos não permitem concluir sobre a conta real.")

pt(cod="PT BS-03", titulo="Base sintética: dicionário de variáveis",
   normas="NBC TA 230 (R1), item 8",
   objetivo=f"Descrever as {GER['colunas']} variáveis da base.",
   objeto="Base sintética.",
   afirmacoes="—",
   populacao="Colunas do arquivo.",
   procedimentos=[("Documentar nome, tipo, descrição e regra de geração (tabela abaixo e "
                   "dados/dicionario_variaveis.csv).", "S", "dados/")],
   tabela_extra=("Dicionário", ["Variável", "Tipo", "Descrição"], "DICIONARIO"),
   evidencias="dados/dicionario_variaveis.csv.",
   resultados="[S] Dicionário completo.",
   conclusao="Atendido.",
   limitacoes="—")

pt(cod="PT BS-04", titulo="Base sintética: conciliação com o saldo contábil",
   normas="NBC TA 500 (R1), item 9 (integridade da informação gerada pela entidade); NBC TA 330 (R1), item 20",
   objetivo="Conciliar o total da base com o saldo do balanço.",
   objeto="Intangível.",
   afirmacoes="Integridade (base completa e exata).",
   populacao="Base inteira.",
   procedimentos=[
       ("Somar o valor líquido por subconta e no total (T01).", "S", "XLS:Conciliacao_Intangivel"),
       ("Comparar com o saldo do balanço (R$ 19.206.609 mil).", "S", "XLS:Conciliacao_Intangivel"),
       ("Verificar unicidade de ids e marcação sintética.", "S", "resultados_testes.json"),
   ],
   evidencias="XLS:Conciliacao_Intangivel; resultados/resultados_testes.json (T01).",
   resultados=f"[S] Total da base R$ {br(RES['T01']['total_base_R$'], 2)} = saldo contábil; diferença R$ 0,00. "
              f"{br(RES['T01']['linhas'])} ids únicos, todos marcados como sintéticos. [J] A diferença zero é "
              "esperada por construção (ajuste final do gerador). A base inclui os erros inseridos, como um "
              "razão real incluiria as distorções.",
   conclusao="Conciliado sem diferença.",
   limitacoes="Conciliação de base sintética.")

mat = {m["codigo_erro"]: m for m in CMP["matriz"]}
pt(cod="PT BS-05", titulo="Base sintética: testes de dados e exceções",
   normas="NBC TA 330 (R1), item 18; NBC TA 240 (R1), item 32(a); NBC TA 520",
   objetivo="Aplicar testes a 100% dos registros para identificar exceções.",
   objeto="Intangível - base sintética.",
   afirmacoes="Existência, exatidão, valorização, corte, ocorrência.",
   populacao=f"[S] {br(RES['T01']['linhas'])} registros.",
   procedimentos=[
       (f"T02 recálculo do valor líquido e valores negativos: {RES['contagem_por_teste']['T02_liquido_divergente']} "
        f"divergentes e {RES['contagem_por_teste']['T02_liquido_negativo']} negativos.", "S", "excecoes_detectadas.csv"),
       (f"T03 duplicidades (mesma subconta, tipo, ODI, município, custo e data): "
        f"{RES['contagem_por_teste']['T03_duplicidade']}.", "S", "—"),
       (f"T04 corte (capitalização após 31/12/2025): {RES['contagem_por_teste']['T04_corte']}.", "S", "—"),
       (f"T05 recálculo da amortização (tolerância de 0,5% do custo): "
        f"{RES['contagem_por_teste']['T05_amortizacao_recalculada']}.", "S", "—"),
       (f"T06 taxa abaixo da mínima do prazo de concessão: {RES['contagem_por_teste']['T06_taxa_abaixo_minima']}.",
        "S", "—"),
       (f"T07 em curso com amortização: {RES['contagem_por_teste']['T07_em_curso_amortizado']}.", "S", "—"),
       (f"T08 ODI ou contrato em branco: {RES['contagem_por_teste']['T08_campos_em_branco']}.", "S", "—"),
       (f"T09 lançamentos manuais de 95% a 100% da alçada após 24/12/2025: "
        f"{RES['contagem_por_teste']['T09_manual_alcada_fim_exercicio']}.", "S", "—"),
       (f"T10 Lei de Benford (primeiro dígito, distribuição): MAD = {br(RES['T10']['MAD'], 5)} "
        f"({RES['T10']['classificacao_Nigrini']}).", "S", "resultados_testes.json"),
   ],
   evidencias="resultados/excecoes_detectadas.csv; resultados/resultados_testes.json.",
   resultados=f"[S] {CMP['excecoes_totais']} registros com exceção; {CMP['falsos_positivos']} falsos positivos. "
              "[J] O teste de Benford indicou não conformidade, mas não aponta erro: custos de bens homogêneos "
              "(medidores, postes) se concentram em faixas de preço e não seguem Benford. O teste é inadequado "
              "para esta população (NBC TA 520, item 5a) e foi mantido apenas como lição de método.",
   conclusao="Exceções isoladas e avaliadas no PT BS-06.",
   limitacoes="Testes desenhados conhecendo os tipos de erro inseridos.")

pt(cod="PT BS-06", titulo="Base sintética: erros inseridos x identificados",
   normas="NBC TA 450 (R1), itens 5 e 11; NBC TA 530, item 14",
   objetivo="Comparar os erros inseridos com as exceções encontradas pelos testes.",
   objeto="Gabarito x exceções.",
   afirmacoes="Conforme o tipo de erro.",
   populacao="dados/log_erros_inseridos.csv; resultados/excecoes_detectadas.csv.",
   procedimentos=[("Cruzar o gabarito com as exceções por id_registro.", "S", "resultados/erros_inseridos_x_detectados.csv")],
   tabela_extra=("Erros inseridos x detectados (dados sintéticos)",
                 ["Código", "Natureza", "Inseridos", "Detectados", "Distorção (R$)", "Teste"], [
                     [c, n, str(mat[c]["inseridos"]), str(mat[c]["detectados"]), br(mat[c]["distorcao_inserida_R"], 2),
                      mat[c]["teste_principal"]] for c, n in [
                         ("E01", "Registro duplicado"), ("E02", "Amortização > custo"), ("E03", "Corte (após 31/12)"),
                         ("E04", "Em serviço sem amortização"), ("E05", "Taxa abaixo do prazo da concessão"),
                         ("E06", "ODI/contrato em branco"), ("E07", "Manual fictício abaixo da alçada"),
                         ("E08", "Em curso amortizado"), ("E09", "Líquido diverge de custo - amortização")]]
                 + [["Total", "", str(CMP["registros_com_erro_inserido"]), str(CMP["detectados"]),
                     br(CMP["distorcao_total_inserida_R$"], 2), ""]]),
   evidencias="XLS:Excecoes; resultados/matriz_inseridos_detectados.csv.",
   resultados=f"[S] {CMP['detectados']} de {CMP['registros_com_erro_inserido']} erros detectados (100%) e nenhum "
              f"falso positivo. A amostra MUS, sozinha, encontrou {T11['itens_com_distorcao']} dos 30 lançamentos E07 (PT 530). [J] A "
              "comparação mostra que os testes sobre 100% da população são mais eficazes que a amostragem para "
              "erros de regra; a amostragem continua útil para a existência física, que a CAAT não alcança.",
   conclusao="Gabarito e exceções conferem.",
   limitacoes="Resultados de laboratório; não extrapoláveis à conta real.")

# ======================== H ==================================================
pt(cod="PT RA", titulo="Leitura do relatório do auditor publicado",
   normas="NBC TA 200 (R1), item 11; leitura à luz das NBC TA 700 e 701 (fora do intervalo exigido)",
   objetivo="Registrar o conteúdo do relatório da PwC sobre as DFs de 2025 e compará-lo com os riscos deste dossiê.",
   objeto="Relatório do auditor independente sobre as DFs individuais e consolidadas de 31/12/2025 [F17, pp. 149-155].",
   afirmacoes="Não há afirmação da administração em exame; o risco é de interpretar a opinião sem considerar os "
              "principais assuntos de auditoria e o alcance do trabalho do auditor.",
   populacao="F17 (relatório completo); F03 (aprovação); F02 (versão SEC).",
   procedimentos=[
       ("Opinião: sem modificação (sem ressalva, sem parágrafo de ênfase), sobre as DFs individuais e "
        "consolidadas, de acordo com as práticas contábeis adotadas no Brasil e as IFRS. Relatório datado de "
        "26/02/2026, firmado pela PwC (CRC 2SP000160/F-6), sócio Guilherme Naves Valle [F17, pp. 149 e 155].",
        "R", "F17"),
       ("PAA 1 - Provisões para litígios e passivos contingentes (NE 4.10 e 26): relevância dos valores e "
        "julgamentos sobre eventos futuros. Resposta do auditor: avaliação de controles, confirmações diretas "
        "com assessores jurídicos internos e externos, análise da movimentação e leitura das divulgações "
        "[F17, p. 150].", "R", "F17"),
       ("PAA 2 - Receita de energia fornecida e disponibilizada, mas não faturada (NE 4.11, 7 e 28): saldo de "
        "R$ 931.460 mil na Copel DIS; estimativa baseada em dados de sistemas. Resposta: controles e "
        "especialistas de TI, comparação da receita real subsequente com estimativas históricas, recálculo "
        "analítico por classe de consumo e tarifa [F17, p. 151].", "R", "F17"),
       ("PAA 3 - Combinação de negócios (NE 1.2): aquisição do controle da UHE Mauá e da MSG em maio/2025; "
        "julgamentos sobre data de aquisição e valores justos. Resposta: leitura de contratos, avaliação dos "
        "especialistas da administração, especialistas de avaliação da firma, teste do modelo [F17, pp. 151-152].",
        "R", "F17"),
       ("Outros assuntos: DVA auditada como informação suplementar; Relatório da Administração lido, sem nada a "
        "relatar [F17, pp. 152-153].", "R", "F17"),
       ("Comparar os PAA com a matriz de riscos (abaixo).", "R", "PT 315.2"),
   ],
   anexos=[{"titulo": "PAA da PwC x riscos deste dossiê",
            "cab": ["Risco do dossiê (PT 315.2)", "É PAA da PwC?", "Leitura"], "larg": [5.0, 2.6, 9.4],
            "linhas": [
                ["R01 Receita não faturada", "Sim (PAA 2)", "Coincide; o valor de R$ 931.460 mil é cerca de 6x a "
                 "materialidade global deste dossiê"],
                ["R06 Provisões para litígios", "Sim (PAA 1)", "Coincide; a resposta da PwC inclui as confirmações "
                 "com advogados planejadas no PT 505"],
                ["R09 Transações não usuais (troca de ativos)", "Sim (PAA 3)", "Coincide na combinação de negócios; "
                 "alienações e Novo Mercado não foram PAA"],
                ["R02 CVA, R03 ativos de contrato, R05 VNR", "Não", "[J] O auditor tratou como riscos sem destaque "
                 "no relatório; aqui permanecem significativos por prudência, sem acesso a controles"],
                ["R07 Benefícios, R08 dívida/MTM, R11 PIS/Cofins", "Não", "Riscos altos neste dossiê, não PAA"],
            ]},
           {"titulo": "Correção registrada", "paragrafos": [
               "A versão anterior deste dossiê listava seis PAA por inferência, antes de o relatório completo estar "
               "disponível. O relatório real tem três PAA. Três das seis inferências estavam corretas (receita não "
               "faturada, provisões e troca de ativos) e três não constam do relatório (CVA, ativos de contrato e "
               "VNR). A lista inferida foi substituída pela transcrição resumida acima."]}],
   evidencias="F17, pp. 149-155.",
   resultados="[F] Opinião sem modificação, sem ênfase, com três PAA. [J] Os três PAA estão entre os riscos "
              "significativos identificados de forma independente neste dossiê, o que indica coerência do "
              "planejamento; a diferença está em riscos regulatórios que a PwC não destacou.",
   conclusao="Relatório lido e comparado; coerente com as conclusões deste trabalho.",
   limitacoes="Não há acesso aos papéis da PwC; as respostas descritas no relatório são resumos.")

pt(cod="PT MC", titulo="Matriz de cobertura das normas",
   normas="NBC TA 230 (R1); enunciado do P2, item 6",
   objetivo="Mostrar em quais PT cada norma foi aplicada e a versão consultada.",
   objeto="NBC TA Estrutura Conceitual e NBC TA 200 a 600.",
   afirmacoes="—",
   populacao="Lista de normas do CFC [F09].",
   procedimentos=[("Mapear norma, versão vigente para 2025 e PT principais e de apoio.", "R", "XLS:Matriz_Cobertura")],
   tabela_extra=("Matriz de cobertura", ["Norma", "Versão (2025)", "Publicação", "PT principais", "PT de apoio"], "MATRIZ"),
   evidencias="XLS:Matriz_Cobertura; docs/matriz_cobertura.md.",
   resultados="[F] Todas as 27 normas do intervalo exigido têm ao menos um PT principal. Para 2025 aplicam-se a "
              "NBC TA 240 (R1) e a NBC TA 570 anterior; as novas versões publicadas em 25/09/2026 valem a "
              "partir de 2027 [F09].",
   conclusao="Cobertura completa.",
   limitacoes="—")

CONCLUSAO = [
    "<b>Natureza desta conclusão.</b> Esta é uma conclusão integrada de trabalho acadêmico. Ela não constitui "
    "opinião de auditoria, não oferece asseguração e não substitui o relatório do auditor independente da "
    "companhia (PricewaterhouseCoopers), emitido sem ressalvas em 26/02/2026 [F17, p. 149].",
    "<b>Relatório do auditor.</b> [F] A PwC emitiu, em 26/02/2026, opinião sem modificação e sem ênfase, com "
    "três principais assuntos de auditoria: provisões para litígios e passivos contingentes, receita não faturada "
    "(R$ 931.460 mil) e combinação de negócios da UHE Mauá e da MSG [F17, pp. 149-152]. Os três estão entre os "
    "riscos significativos identificados de forma independente neste dossiê (PT RA).",
    "<b>Riscos identificados.</b> [J] O risco de distorção relevante nas demonstrações consolidadas da COPEL "
    "de 2025 se concentra em estimativas regulatórias e contábeis de grande valor: ativos e passivos "
    "financeiros setoriais (resultado de R$ 2.348.143 mil), ativos de contrato (R$ 9.595.006 mil), ativo "
    "indenizável da concessão (R$ 4.603.446 mil), provisões para litígios e outras provisões (R$ 1.934.020 mil, +102%, dos quais R$ 1.571.555 mil de litígios) e "
    "benefícios pós-emprego (R$ 1.478.157 mil); na receita não faturada; e em transações não usuais do "
    "exercício (troca de ativos com a Axia, alienações e migração ao Novo Mercado). A pressão por métricas "
    "(política de dividendos ligada à alavancagem) e a remuneração variável são fatores de risco de fraude. "
    "O intangível (R$ 19.206.609 mil) é a maior conta do ativo e foi o objeto da base sintética.",
    "<b>Procedimentos realizados e evidências.</b> Com evidência pública (R): identificação da entidade e "
    "das fontes; recálculo de todos os subtotais do balanço e da DRE, que conferem com os publicados; "
    "materialidade (global de R$ 162.333 mil); análises horizontal, vertical e de expectativa; mapeamento de "
    "leis, governança, partes relacionadas, componentes do grupo e eventos subsequentes; avaliação de "
    "continuidade (sem indício de incerteza relevante). Com dados sintéticos (S): conciliação da base de "
    f"{br(GER['linhas'])} registros com o saldo contábil e com as quatro categorias da nota 16 (diferença "
    "zero), nove testes sobre 100% dos registros e "
    "amostragem MUS, que detectaram os 580 erros inseridos; a projeção da amostra superou a distorção "
    f"tolerável e levou à extensão dos testes, que isolaram distorção de R$ {br(CMP['distorcao_total_inserida_R$'] / 1e6, 1)} milhões, abaixo da "
    "materialidade de execução, mas com lançamentos fictícios relevantes por natureza. Os demais "
    "procedimentos (confirmações, inspeções, observação de estoques, testes de controles, carta de "
    "representação, especialistas) ficaram planejados (P).",
    "<b>Pontos em aberto.</b> Resta um resíduo de R$ 43.898 mil entre dividendos a pagar e proventos declarados "
    "líquidos do IRRF sobre JCP (a diferença inicial era de R$ 124.111 mil). Não foi caracterizado como "
    "distorção: exigiria a composição do saldo. A despesa financeira, antes 27,6% acima da expectativa, foi "
    "explicada pela nota 30 (encargos da dívida 1,1% acima da expectativa). Com a leitura integral das notas, "
    "surgiram pontos de atenção de julgamento, não de distorção: ganhos não recorrentes de 2025 (alienações "
    "R$ 335.595 mil, combinação de negócios R$ 141.661 mil e ressarcimento de curtailment R$ 273.382 mil "
    "reconhecido com a regulamentação ainda em consulta pública), folga de apenas 8,18% no teste de "
    "impairment do Complexo Jandaíra e anuência temporária dos debenturistas para alavancagem de até 4,5x."
    " A diferença de "
    "R$ 362.420 mil nas provisões para litígios, antes em aberto, foi explicada pela contraprestação "
    "contingente de R$ 362.465 mil (nota 26, PT 501).",
    "<b>Limitações.</b> O trabalho usou apenas documentos públicos e foi feito por uma única pessoa, com apoio "
    "de IA e sem revisão. Não houve acesso a registros, sistemas, contratos, administração, advogados ou "
    "auditores; nenhuma confirmação, entrevista, inspeção física ou acesso a sistema foi realizado. Por isso "
    "a evidência obtida é insuficiente para qualquer conclusão sobre as afirmações da administração, e os "
    "resultados com dados sintéticos servem para demonstrar método, não para avaliar a conta real.",
    "<b>Síntese.</b> [J] Com base nas evidências públicas analisadas, não foram encontrados indícios de "
    "distorção relevante nas demonstrações consolidadas da COPEL de 2025, e as informações analisadas são "
    "coerentes entre si e com o relatório do auditor divulgado sem ressalvas. Essa constatação é limitada "
    "pelo alcance descrito e não equivale a uma opinião sobre a adequação das demonstrações.",
]


# ===========================================================================
# COMPLEMENTOS EXIGIDOS PELO ROTEIRO DO PROFESSOR (item 5 do enunciado)
# Cada PT do roteiro (PT EC, PT 200 ... PT 600) recebe aqui os anexos que a
# "atividade exigida" pede. Anexos: {"titulo", "paragrafos"} ou {"titulo","cab","linhas","larg"}.
# ===========================================================================
IDX = {d["cod"]: d for d in PTS}


def upd(cod, proc=None, anexos=None, **campos):
    d = IDX[cod]
    if proc:
        d["procedimentos"] = d["procedimentos"] + proc
    if anexos:
        d.setdefault("anexos", []).extend(anexos)
    d.update(campos)


MINUTA = "MINUTA DIDÁTICA - NÃO ENVIADA, NÃO ASSINADA E SEM VALIDADE. Elaborada apenas para fins acadêmicos."

# ---------------- PT EC
upd("PT EC",
    atividade="Caracterizar o trabalho, os usuários, o objeto, os critérios, as responsabilidades, a evidência e o "
              "nível de asseguração. Diferenciar auditoria de outros trabalhos de asseguração.",
    proc=[("Comparar a auditoria com outros trabalhos de asseguração e serviços correlatos realizados para a "
           "própria COPEL (tabela abaixo).", "R", "F02, F10")],
    anexos=[{"titulo": "Elementos do trabalho: caso real x este trabalho",
             "cab": ["Elemento", "Auditoria real das DFs 2025", "Este trabalho acadêmico"],
             "larg": [3.2, 7.0, 6.8],
             "linhas": [
                 ["Usuários previstos", "Acionistas, debenturistas, credores, CVM, SEC, ANEEL, mercado [F02]",
                  "Professor e banca da disciplina"],
                 ["Objeto", "DFs individuais e consolidadas de 31/12/2025", "DFs consolidadas (leitura pública)"],
                 ["Critérios", "CPC e IFRS emitidas pelo IASB [F02, p. 1]", "Os mesmos critérios"],
                 ["Responsáveis", "Administração (elaboração) e governança (supervisão) [F03]",
                  "Administração (elaboração); estudante não tem responsabilidade sobre as DFs"],
                 ["Profissional", "PwC, independente e contratada [F04]", "Estudante, sem contratação"],
                 ["Evidência", "Registros, documentos, confirmações, controles", "Apenas documentos públicos e dados sintéticos"],
                 ["Nível de asseguração", "Razoável (opinião positiva)", "Nenhum (conclusão descritiva)"],
             ]},
            {"titulo": "Auditoria x outros trabalhos de asseguração",
             "cab": ["Trabalho", "Norma", "Nível", "Forma da conclusão", "Exemplo na COPEL"],
             "larg": [3.4, 3.0, 2.4, 3.4, 4.8],
             "linhas": [
                 ["Auditoria de DFs", "NBC TA", "Razoável", "Opinião (positiva)",
                  "Relatório da PwC sobre as DFs de 2025, sem ressalvas [F03]"],
                 ["Auditoria de controles (ICFR)", "Normas do PCAOB (SOX 404)", "Razoável", "Opinião sobre eficácia",
                  "Auditoria integrada no 20-F [F02, p. 117]"],
                 ["Revisão de informações intermediárias", "NBC TR 2410", "Limitada", "Conclusão negativa",
                  "Revisão das ITR trimestrais (a PwC assumiu as revisões trimestrais em 2024) [F04; F10]"],
                 ["Asseguração de informação não financeira", "NBC TO 3000", "Limitada ou razoável", "Conclusão",
                  "Asseguração do Relato Integrado contratada com a PwC (honorários na Copel GeT) [F10]"],
                 ["Procedimentos previamente acordados", "NBC TSC 4400", "Nenhum", "Relato de constatações",
                  "Não identificado nas fontes"],
                 ["Este trabalho", "Aplicação didática das NBC TA", "Nenhum", "Conclusão integrada descritiva", "—"],
             ]}])

# ---------------- PT 200
upd("PT 200",
    atividade="Documentar ética, independência, ceticismo, julgamento profissional, risco de auditoria e condições "
              "para obter segurança razoável.",
    proc=[("Ética e independência no caso real: o modelo de relatório da PwC declara independência segundo o Código "
           "de Ética Profissional do Contador e as normas do CFC [F07, p. 29]; contratação em 2024, portanto sem "
           "risco de rodízio obrigatório (Resolução CVM 23/2021) no período [F04]; serviço não relacionado à "
           "auditoria identificado: asseguração do Relato Integrado, de pequeno valor frente aos honorários de "
           "auditoria (R$ 83,8 mil contra R$ 1,9 milhão na Copel GeT) [F10]. [J] Ameaça de interesse próprio baixa.",
           "R", "F04, F07, F10"),
          ("Ética e independência neste trabalho: sem vínculo da estudante com a COPEL, sem contato com a empresa, "
           "com fontes citadas e uso de IA declarado.", "R", "PT 220"),
          ("Condições para segurança razoável: acesso irrestrito, evidência suficiente, equipe competente, "
           "independência e tempo. [J] Neste trabalho falta a primeira e a segunda, por isso não há segurança "
           "razoável.", "R", "PT 500.2")],
    anexos=[{"titulo": "Risco de auditoria por componente (julgamento)",
             "cab": ["Componente", "Avaliação", "Fundamento"], "larg": [3.6, 2.8, 10.6],
             "linhas": [
                 ["Risco inerente", "Alto nas estimativas", "Estimativas regulatórias e provisões somam mais de 10x a "
                                                            "materialidade (PT 540)"],
                 ["Risco de controle", "Máximo (não testado)", "Sem teste de controles; apesar de ICFR declarado efetivo [F02]"],
                 ["Risco de detecção aceitável", "Baixo", "Exige procedimentos substantivos extensos (PT 330)"],
                 ["Limitações inerentes", "Presentes", "Fraude com conluio, julgamentos e evidência persuasiva, "
                                                      "não conclusiva (NBC TA 200, itens A47 a A52)"],
             ]}])

# ---------------- PT 210
upd("PT 210",
    atividade="Preparar carta de contratação didática com objetivo, alcance, responsabilidades e estrutura de "
              "relatório. Avaliar as precondições para a auditoria.",
    proc=[("Redigir a minuta didática da carta de contratação (abaixo).", "S", "Anexo")],
    anexos=[{"titulo": "Minuta didática de carta de contratação", "paragrafos": [
        MINUTA,
        "Curitiba, [data]. Ao Conselho de Administração e ao Comitê de Auditoria Estatutário da Companhia Paranaense "
        "de Energia - COPEL. Ref.: Auditoria das demonstrações contábeis individuais e consolidadas do exercício "
        "findo em 31/12/2025.",
        "<b>1. Objetivo e alcance.</b> Auditar as demonstrações contábeis individuais e consolidadas (balanço "
        "patrimonial, demonstrações do resultado, do resultado abrangente, das mutações do patrimônio líquido, dos "
        "fluxos de caixa e do valor adicionado, e notas explicativas) com o objetivo de expressar opinião sobre se "
        "estão apresentadas adequadamente, em todos os aspectos relevantes, de acordo com as práticas contábeis "
        "adotadas no Brasil e as IFRS.",
        "<b>2. Responsabilidades do auditor.</b> Conduzir a auditoria de acordo com as normas brasileiras e "
        "internacionais de auditoria (NBC TA), cumprir as exigências éticas e planejar e executar a auditoria para "
        "obter segurança razoável de que as demonstrações estão livres de distorção relevante, causada por fraude "
        "ou erro. Em razão das limitações inerentes, há risco inevitável de que distorções relevantes não sejam "
        "detectadas.",
        "<b>3. Responsabilidades da administração.</b> (a) Elaborar as demonstrações de acordo com a estrutura "
        "aplicável; (b) manter os controles internos necessários; (c) dar ao auditor acesso a todas as "
        "informações, registros e pessoas relevantes; (d) fornecer representações formais escritas.",
        "<b>4. Relatório.</b> Relatório do auditor independente na forma da NBC TA 700, com principais assuntos de "
        "auditoria (NBC TA 701) por se tratar de companhia aberta; a forma pode mudar conforme as constatações.",
        "<b>5. Outras condições.</b> Cronograma (PT 300), equipe, uso de especialistas e auditores de componentes "
        "(PT 600), honorários e prazo de guarda dos papéis.",
        "Concordância: [assinatura do auditor] e [assinatura da administração] - campos deixados em branco.",
    ]},
        {"titulo": "Avaliação das precondições (NBC TA 210, item 6)",
         "cab": ["Precondição", "Evidência", "Atendida?"], "larg": [5.4, 9.0, 2.6],
         "linhas": [
             ["Estrutura de relatório aceitável", "CPC e IFRS para companhia aberta [F02, p. 1]", "Sim [F]"],
             ["Administração reconhece responsabilidade pela elaboração", "Aprovação da Diretoria, CAE e Conselho [F03]", "Sim [F]"],
             ["Administração reconhece responsabilidade pelos controles", "Declaração de ICFR efetivo [F02, p. 117]", "Sim [F]"],
             ["Acesso a informações e pessoas", "Não aplicável a este trabalho; no caso real, previsto na carta", "Não verificável"],
         ]}])

# ---------------- PT 220
upd("PT 220",
    atividade="Planejar direção, supervisão, revisão, consultas e recursos. Documentar conflitos e riscos à qualidade.",
    anexos=[{"titulo": "Riscos à qualidade e respostas",
             "cab": ["Risco à qualidade", "Resposta adotada", "Status"], "larg": [5.0, 9.0, 3.0],
             "linhas": [
                 ["IA gerar número sem fonte ou errado", "Fonte única (dados_publicos.py) com página; somas automáticas "
                                                         "contra totais publicados", "Implementada"],
                 ["Erro de transcrição ou fórmula", "Checagens 'Confere com publicado' e 'Planilha = código'", "Implementada"],
                 ["Fonte incompleta (notas, PAA)", "Procedimento classificado como P e limitação declarada", "Implementada"],
                 ["Falta de revisão por terceiro", "Campo de revisão em branco; reprodução integral do código", "Parcial"],
                 ["Prazo curto", "Priorização dos riscos significativos (PT 315.2)", "Implementada"],
                 ["Roteiro recebido depois da 1ª versão", "Recodificação de todos os PT e nova conferência", "Implementada"],
             ]},
            {"titulo": "Direção, supervisão, revisão, consultas e recursos", "paragrafos": [
                "<b>Direção e supervisão:</b> trabalho individual; a estudante atua como preparadora e responsável. "
                "<b>Revisão:</b> não houve revisor; nenhum campo de revisão foi preenchido. <b>Consultas planejadas "
                "(P):</b> especialista regulatório do setor elétrico (CVA, VNR, ativos de contrato), atuário "
                "(benefícios pós-emprego) e área técnica da firma (combinação de negócios da troca de ativos). "
                "Nenhuma consulta foi realizada. <b>Recursos:</b> Python (pandas, numpy, openpyxl, reportlab), "
                "LibreOffice e assistente de IA. <b>Conflitos:</b> não há conflito de interesse nem divergência "
                "de opinião a registrar."]}])

# ---------------- PT 230
upd("PT 230",
    atividade="Criar índice, convenção de códigos, referências cruzadas, controle de versões e procedimentos de "
              "montagem e guarda do arquivo.",
    anexos=[{"titulo": "Convenção de códigos e referências",
             "cab": ["Código", "Significado", "Exemplo"], "larg": [3.0, 9.0, 5.0],
             "linhas": [
                 ["PT nnn", "Papel de trabalho da norma NBC TA nnn (roteiro do professor)", "PT 315.2 = matriz de riscos"],
                 ["PT EC", "Estrutura Conceitual", "—"],
                 ["PT 000", "Identificação do trabalho e das fontes", "—"],
                 ["PT PA-nn", "Programa de auditoria por área", "PT PA-01 Receitas"],
                 ["PT BS-nn", "Papel da base simulada", "PT BS-04 Conciliação"],
                 ["PT RA / CI / MC", "Relatório do auditor / conclusão integrada / matriz de cobertura", "—"],
                 ["Fnn", "Fonte pública (docs/fontes.md)", "F01, p. 24"],
                 ["XLS:aba", "Aba da planilha PT_calculos_COPEL_2025.xlsx", "XLS:Materialidade"],
                 ["R / P / S", "Realizado / planejado / simulado", "—"],
                 ["[F] / [J] / [S]", "Fato com fonte / julgamento / dado sintético", "—"],
             ]},
            {"titulo": "Índice, versões, montagem e guarda", "paragrafos": [
                "<b>Índice:</b> sumário do dossiê e índice de PT em docs/matriz_cobertura.md. <b>Controle de "
                "versões:</b> o repositório GitHub registra cada alteração (histórico de commits); versão 1.0 de "
                "24/10/2026 (estrutura por norma) e versão 1.1 de 24/10/2026 (recodificação conforme o roteiro do "
                "professor e anexos exigidos). Os resultados são reproduzíveis pela semente 232025417. "
                "<b>Montagem:</b> PDF, planilha, base, código e resultados gerados pelo script rodar_tudo.sh. "
                "<b>Guarda (P):</b> no caso real, montagem final em até 60 dias após o relatório e guarda por no "
                "mínimo 5 anos, sem alteração após a montagem."]}])

# ---------------- PT 240
upd("PT 240", atividade="Avaliar fatores de risco de fraude, incluindo reconhecimento de receitas e burla de controles "
                        "pela administração. Planejar testes de lançamentos e respostas aos riscos.",
    anexos=[{"titulo": "Plano de testes de lançamentos contábeis (NBC TA 240, item 32a)",
             "cab": ["Critério de seleção", "Justificativa", "Status"], "larg": [6.0, 8.0, 3.0],
             "linhas": [
                 ["Lançamentos manuais acima de 95% da alçada", "Fracionamento para fugir da aprovação", "S (T09)"],
                 ["Lançamentos no fim do exercício e após o fechamento", "Ajuste de resultado", "S (T09) / P"],
                 ["Usuários com poucos lançamentos ou sem função contábil", "Acesso indevido", "S (T09) / P"],
                 ["Lançamentos em receita e CVA sem documento-suporte", "Presunção de fraude na receita", "P"],
                 ["Valores redondos e contas pouco usadas", "Indicadores clássicos de fraude", "P"],
                 ["Ajustes de consolidação e eliminações manuais", "Componentes e transações intragrupo", "P"],
             ]}])

# ---------------- PT 250
upd("PT 250", atividade="Mapear obrigações relevantes e riscos de descumprimento. Definir procedimentos e comunicações "
                        "diante de indícios.",
    anexos=[{"titulo": "Conduta diante de indícios de não conformidade", "paragrafos": [
        "(1) Obter entendimento do ato e das circunstâncias e avaliar o efeito nas DFs (provisão, contingência, "
        "divulgação); (2) discutir com a administração no nível adequado e, se necessário, com a governança (CAE); "
        "(3) obter assessoria jurídica se a administração não comprovar conformidade; (4) avaliar o efeito na "
        "avaliação de riscos e na confiabilidade das representações; (5) considerar a comunicação a autoridades "
        "quando exigida por lei (por exemplo, CVM); (6) documentar. Neste trabalho, nenhum indício foi identificado "
        "e nenhuma comunicação foi feita."]}])

# ---------------- PT 260
upd("PT 260", atividade="Preparar comunicação sobre alcance, época, riscos significativos, independência e principais "
                        "dificuldades.",
    anexos=[{"titulo": "Minuta didática de comunicação ao Comitê de Auditoria Estatutário", "paragrafos": [
        MINUTA,
        "<b>Alcance e época.</b> Auditoria das DFs consolidadas de 2025 conforme as NBC TA; materialidade global de "
        f"R$ {br(MG)} mil; planejamento, fase intermediária e final conforme PT 300.",
        "<b>Riscos significativos.</b> Receita não faturada e contratos bilaterais; ativos e passivos financeiros "
        "setoriais; ativos de contrato; ativo indenizável (VNR); provisões para litígios; transações não usuais do "
        "exercício (troca de ativos com a Axia, alienações, Novo Mercado); burla de controles (PT 315.2).",
        "<b>Constatações (simulação).</b> 30 lançamentos manuais fictícios no intangível, abaixo da alçada, no fim do "
        f"exercício, com natureza de fraude; distorção total de R$ {br(CMP['distorcao_total_inserida_R$'] / 1e6, 1)} milhões, a corrigir (PT 450).",
        "<b>Independência.</b> Declaramos cumprir as exigências de independência; serviços não relacionados à "
        "auditoria avaliados (PT 200).",
        "<b>Principais dificuldades.</b> Acesso restrito a documentos públicos; sem acesso a registros, sistemas "
        "e pessoas.",
        "<b>Deficiências de controle.</b> Ver PT 265 (comunicação por escrito).",
    ]}])

# ---------------- PT 265
upd("PT 265", atividade="Preparar matriz com condição, critério, causa, efeito e recomendação. Distinguir hipóteses de "
                        "constatações sustentadas por evidências.",
    anexos=[{"titulo": "Matriz de deficiências (condição, critério, causa, efeito, recomendação)",
             "cab": ["Condição", "Critério", "Causa", "Efeito", "Recomendação", "Natureza"],
             "larg": [3.2, 2.6, 2.6, 2.6, 3.2, 2.8],
             "linhas": [
                 ["[S] 50 registros do intangível sem ODI ou contrato", "Bem capitalizado deve ter suporte (CPC 04; "
                  "controle de capitalização)", "Campo não obrigatório no sistema (hipótese)", "Risco de existência; "
                  "dificuldade de inspeção", "Tornar ODI e contrato obrigatórios na gravação",
                  "Constatação sustentada por evidência simulada"],
                 ["[S] 30 lançamentos manuais sem ODI, de 95% a 100% da alçada, por usuário raro, em 29-30/12",
                  "Alçada de aprovação e segregação de funções", "Ausência de revisão de lançamentos manuais (hipótese)",
                  "Ativo fictício de R$ 29,8 milhões", "Dupla aprovação; monitoramento de lançamentos próximos à "
                  "alçada", "Constatação sustentada por evidência simulada (deficiência significativa)"],
                 ["[S] 70 bens amortizados além do prazo da concessão", "ICPC 01 e CPC 04: amortização limitada ao "
                  "prazo", "Parametrização da taxa sem validação do vencimento", "Intangível superavaliado",
                  "Validação automática taxa x vencimento", "Constatação sustentada por evidência simulada"],
                 ["Novo sistema de faturamento com entrada em operação em 2026 [F02, p. 7]", "COSO 2013: gestão de "
                  "mudanças de sistemas", "Projeto de transformação", "Risco potencial na receita de 2026",
                  "Testes de migração de dados e controles gerais de TI", "Hipótese (risco, não constatação)"],
                 ["Diferença de R$ 362.420 mil nas provisões (balanço x 20-F)", "Consistência de divulgação (CPC 25)",
                  "Contraprestação contingente (R$ 362.465 mil) incluída na linha; o 20-F cita só os litígios",
                  "Nenhum: o balanço oficial usa o rótulo 'Provisões para litígios e outras provisões' e a nota 26 "
                  "abre os valores [F17, pp. 48 e 105]", "Nenhuma", "Hipótese inicial afastada por evidência (não é "
                  "deficiência)"],
             ]}])

# ---------------- PT 300
upd("PT 300", atividade="Elaborar estratégia global, plano, cronograma e programas por ciclo. Justificar prioridades e "
                        "alterações.",
    anexos=[{"titulo": "Cronograma",
             "cab": ["Fase", "Auditoria real (referência)", "Este trabalho"], "larg": [3.8, 7.2, 6.0],
             "linhas": [
                 ["Aceitação e contratação", "Contrato PwC desde 2024, até 2028 [F04]", "Atribuição pelo professor"],
                 ["Revisões trimestrais", "ITR de 1T25, 2T25 e 3T25 (NBC TR 2410)", "Não aplicável ao escopo anual"],
                 ["Planejamento e avaliação de riscos", "3º trimestre de 2025 (típico)", "24/10/2026"],
                 ["Fase intermediária (controles)", "4º trimestre de 2025 (típico)", "Planejada (P)"],
                 ["Fase final (substantivos)", "Janeiro e fevereiro de 2026", "24/10/2026 (públicos e simulados)"],
                 ["Relatório", "Aprovação das DFs em 26/02/2026 [F03]", "Conclusão integrada em 24/10/2026"],
                 ["Eventos posteriores", "20-F em 15/04/2026 [F02]; AGO em 23/04/2026 [F03]", "Pesquisa até 24/10/2026"],
             ]},
            {"titulo": "Programas por ciclo e prioridades",
             "cab": ["Ciclo", "Programa", "Prioridade", "Justificativa"], "larg": [3.6, 2.6, 2.2, 8.6],
             "linhas": [
                 ["Receitas e contas a receber", "PT PA-01", "Alta", "Presunção de fraude; receita não faturada; CVA"],
                 ["Ativos de concessão", "PT PA-04", "Alta", "Maior conta do ativo; base simulada"],
                 ["Estimativas", "PT PA-06", "Alta", "Mais de 10x a materialidade"],
                 ["Financiamentos e passivos", "PT PA-05", "Média-alta", "Debêntures +31%; covenants; provisões +102%"],
                 ["Tesouraria", "PT PA-02", "Média", "Saldo relevante, risco baixo de valorização"],
                 ["Estoques", "PT PA-03", "Média-baixa", "Acima da ME, mas materiais de manutenção"],
             ]},
            {"titulo": "Alterações ao plano", "paragrafos": [
                "(1) A amostra MUS projetou distorção acima da tolerável: o teste do intangível foi estendido a 100% "
                "da população com CAAT (PT 530). (2) Os procedimentos que dependiam das notas explicativas e do "
                "texto dos PAA foram reclassificados como planejados (P) após a não obtenção dos documentos. (3) O "
                "roteiro do professor foi recebido depois da primeira versão: os PT foram recodificados e "
                "complementados com as atividades exigidas."]}])

# ---------------- PT 315.1 (TI)
upd("PT 315.1", atividade="Compreender a entidade, seu ambiente, a estrutura contábil, a TI e os controles.",
    proc=[("Ambiente de TI [F]: centros de dados próprios com dados de clientes [F02, p. 6]; ataques cibernéticos "
           "em anos anteriores [F02, p. 6]; LGPD; 2.026.837 medidores inteligentes (medição automatizada que "
           "alimenta o faturamento) [F01, p. 9]; novo sistema de faturamento em 2026 [F02, p. 7]. [J] Controles "
           "gerais de TI relevantes: acesso lógico, gestão de mudanças, operação e interfaces medição-faturamento-"
           "contabilidade e CCEE-contabilidade.", "R", "F01, F02"),
          ("Testar controles gerais de TI (acessos privilegiados, mudanças de programa, interfaces).", "P", "PT 330")])
upd("PT 315.2", atividade="Elaborar matriz de riscos por conta e afirmação e identificar riscos significativos.")

# ---------------- PT 320
upd("PT 320", atividade="Calcular e justificar a materialidade global, a materialidade para execução e, quando "
                        "pertinente, materialidades específicas. Fundamentar bases, percentuais e revisões.",
    proc=[("Materialidades específicas [J]: (a) remuneração do pessoal-chave e transações com partes "
           "relacionadas - qualquer distorção é relevante pela natureza; (b) divulgação de covenants e da "
           "classificação circulante/não circulante da dívida - limite menor, pelo efeito sobre a percepção de "
           "liquidez (liquidez corrente de 0,98); (c) indicadores regulatórios divulgados (DEC/FEC) - sem valor "
           "monetário, avaliação qualitativa.", "R", "XLS:Materialidade"),
          ("Revisão: os valores usados são os das DFs finais; não houve mudança no referencial. Se o planejamento "
           "real tivesse usado a ITR de setembro/2025 anualizada, a materialidade seria revista com o lucro "
           "final (item 12).", "R", "XLS:Materialidade")],
    anexos=[{"titulo": "Bases e percentuais (R$ mil)",
             "cab": ["Base", "Valor 2025", "%", "Resultado", "Uso"], "larg": [5.4, 3.0, 1.6, 3.0, 4.0],
             "linhas": [
                 ["Lucro antes do IR e CSLL (continuadas)", br(RES["parametros"]["LAIR_R$mil"]), "5,0%", br(MG), "Escolhida"],
                 ["Receita operacional líquida", "26.116.856", "0,5%", "130.584", "Comparação"],
                 ["Patrimônio líquido", "23.091.978", "1,0%", "230.920", "Comparação"],
                 ["Ativo total", "60.414.456", "0,5%", "302.072", "Comparação"],
                 ["EBITDA", "6.526.897", "3,0%", "195.807", "Comparação"],
                 ["Materialidade para execução", br(MG), "70%", br(ME), "Testes e amostragem"],
                 ["Limite claramente trivial", br(MG), "5%", br(TRIV), "Acúmulo de distorções"],
             ]}])

# ---------------- PT 330
upd("PT 330", atividade="Relacionar cada risco aos testes de controles e procedimentos substantivos. Definir natureza, "
                        "época e extensão, distinguindo testes executados de testes planejados.",
    anexos=[{"titulo": "Riscos x respostas (natureza, época e extensão)",
             "cab": ["Risco", "Teste de controle", "Procedimento substantivo", "Época / extensão", "Status"],
             "larg": [2.6, 3.6, 5.0, 3.4, 2.4],
             "linhas": [
                 ["R01 Receita", "Leitura, tarifa e faturamento; ITGC", "Recálculo de não faturado; corte; "
                  "confirmação de bilaterais", "Final; 100% do não faturado; amostra de contratos", "P"],
                 ["R02 CVA", "Revisão da apuração pela controladoria", "Recálculo com despachos da ANEEL",
                  "Final; 100% dos componentes", "P"],
                 ["R03 Ativos de contrato", "Aprovação de obras e medição", "Recálculo de margem e taxa; "
                  "conciliação com RAP", "Final; todos os contratos de transmissão", "P"],
                 ["R04 Intangível", "Aprovação de ODI; conciliação ativo de contrato x intangível",
                  "CAAT 100% (T02-T09); MUS; recálculo de amortização", "Final; 100% e n = 603", "S"],
                 ["R05 VNR", "Revisão da base regulatória", "Estimativa independente com especialista",
                  "Final; 100%", "P"],
                 ["R06 Provisões", "Revisão jurídica periódica", "Cartas a advogados; conciliação balanço x nota",
                  "Final; processos acima do trivial", "R (conciliação) / P"],
                 ["R07 Benefícios", "Revisão do laudo", "Teste de premissas e dados do censo com atuário",
                  "Final; 100% dos planos", "P"],
                 ["R08 Dívida e MTM", "Aprovação de captações", "Confirmação; recálculo de covenants e de MTM",
                  "Final; 100% das emissões", "R (DFC x balanço) / P"],
                 ["R09 Transações não usuais", "Aprovação pelo Conselho", "Leitura de contratos e laudos; "
                  "recálculo de ganhos", "Final; 100%", "P"],
                 ["R10 Burla de controles", "—", "Testes de lançamentos; revisão de estimativas quanto a viés",
                  "Final; critérios do PT 240", "S / P"],
                 ["R11 PIS/Cofins", "Acompanhamento regulatório", "Conciliação com devoluções tarifárias",
                  "Final; 100%", "P"],
                 ["R12 IR diferido", "Revisão de projeções", "Teste de recuperabilidade", "Final", "P"],
                 ["R13 Divulgações", "Checklist de divulgação", "Leitura das notas contra CPC", "Final", "P"],
                 ["R14 Continuidade", "—", "Indicadores e cronograma de dívida", "Final", "R"],
             ]}])

# ---------------- PT 402
upd("PT 402", atividade="Identificar serviços terceirizados relevantes e controles complementares. Planejar a análise "
                        "de relatórios tipo 1 ou tipo 2 e procedimentos alternativos.",
    anexos=[{"titulo": "Prestadores, relatórios e alternativas",
             "cab": ["Prestador / serviço", "Relevância", "Relatório planejado", "Controles complementares da COPEL",
                     "Procedimento alternativo"], "larg": [3.2, 2.6, 3.0, 4.0, 4.2],
             "linhas": [
                 ["CCEE - liquidação do mercado de curto prazo e MRE [F07]", "Alta (suprimento, GSF)",
                  "Não existe tipo 1/2", "Conferência dos relatórios de pré-liquidação", "Conciliação direta "
                  "CCEE x razão; recálculo por amostra"],
                 ["Fundação Copel - administração dos planos e dados do censo", "Alta (benefícios)",
                  "Tipo 2, se existir", "Revisão do censo pelo RH", "Teste do censo e do laudo atuarial"],
                 ["Agentes arrecadadores de faturas (hipótese)", "Média (recebimentos)", "Tipo 2 dos bancos",
                  "Conciliação diária de arrecadação", "Conciliação arrecadação x baixa de contas a receber"],
                 ["Provedores de TI e nuvem (hipótese)", "Média", "Tipo 2 (ISAE 3402/SOC 1)",
                  "Gestão de acessos de usuários", "Testes de ITGC diretos"],
             ]},
            {"titulo": "Tipo 1 x tipo 2", "paragrafos": [
                "Relatório tipo 1 descreve o desenho dos controles em uma data e serve para entender o sistema; tipo 2 "
                "inclui testes de efetividade operacional ao longo de um período e é necessário quando o auditor "
                "pretende confiar nos controles do prestador. Para a COPEL, a estratégia seria pedir tipo 2 onde houver "
                "e, onde não houver (CCEE), testar diretamente os relatórios."]}])

# ---------------- PT 450
mapa = [[c, n, br(mat[c]["distorcao_inserida_R"] / 1000, 1), t, "Não corrigida - correção a solicitar", q]
        for c, n, t, q in [
            ("E01", "Duplicidades", "Factual", "-"), ("E02", "Amortização > custo", "Factual", "Subavaliação"),
            ("E03", "Corte", "Factual", "-"), ("E04", "Sem amortização", "Factual", "-"),
            ("E05", "Prazo da concessão", "De julgamento", "Política"), ("E06", "Campos em branco", "Sem valor", "Controle"),
            ("E07", "Lançamentos fictícios", "Factual", "Fraude: relevante pela natureza"),
            ("E08", "Em curso amortizado", "Factual", "Subavaliação"), ("E09", "Líquido divergente", "Factual", "-")]]
mapa.append(["Total", "", br(CMP["distorcao_total_inserida_R$"] / 1000, 1), "", "", ""])
mapa.append(["MUS", "Projetada (antes da extensão)", br(T11["distorcao_projetada_R$"] / 1000, 1), "Projetada",
             "Substituída pelo teste de 100%", "-"])
upd("PT 450", atividade="Elaborar mapa de distorções identificadas ou simuladas, corrigidas e não corrigidas. Avaliar "
                        "os efeitos quantitativos e qualitativos.",
    anexos=[{"titulo": "Mapa de distorções [S] (R$ mil)",
             "cab": ["Código", "Natureza", "Valor", "Tipo", "Situação", "Efeito qualitativo"],
             "larg": [1.6, 3.6, 2.0, 2.4, 3.8, 3.6], "linhas": mapa},
            {"titulo": "Avaliação", "paragrafos": [
                f"Quantitativa: total não corrigido de R$ {br(CMP['distorcao_total_inserida_R$'] / 1000, 0)} mil, "
                f"acima do trivial (R$ {br(TRIV)} mil) e abaixo da materialidade de execução (R$ {br(ME)} mil) e da "
                f"global (R$ {br(MG)} mil). Qualitativa: os lançamentos E07 têm natureza de fraude e são relevantes "
                "independentemente do valor; exigem comunicação à governança, reavaliação da confiabilidade das "
                "representações e extensão dos testes de lançamentos a outras contas. Nenhuma distorção foi corrigida, "
                "porque não há administração real a quem solicitar correção. Evidência pública: nenhuma distorção."]}])

# ---------------- PT 500
upd("PT 500.1", atividade="Avaliar relevância, confiabilidade e suficiência das evidências. Reconciliar saldos com as "
                          "demonstrações e explicitar as limitações das fontes públicas e dos dados simulados.")
upd("PT 500.2", afirmacoes="Risco de apresentar como realizado procedimento que não ocorreu, de tratar dado sintético "
                           "como real e de superestimar a força da evidência pública.")

# ---------------- PT 501
upd("PT 501", atividade="Planejar procedimentos sobre estoques, litígios e informações por segmento. Executar os "
                        "procedimentos permitidos pelas fontes disponíveis.")

# ---------------- PT 505
upd("PT 505", atividade="Preparar modelos, controle de circularização, tratamento de diferenças e procedimentos "
                        "alternativos. Não enviar solicitações reais.",
    anexos=[{"titulo": "Modelos didáticos de cartas de confirmação", "paragrafos": [
        MINUTA,
        "<b>Bancos.</b> \"Solicitamos que informem diretamente aos nossos auditores [nome e endereço] os saldos de "
        "contas correntes, aplicações, empréstimos, garantias e outros compromissos da Companhia Paranaense de Energia "
        "- COPEL e controladas em 31/12/2025.\" Assinatura da administração.",
        "<b>Agentes fiduciários / credores.</b> \"Favor confirmar o saldo devedor, as taxas, o cronograma, as garantias "
        "e o cumprimento dos covenants das emissões listadas em anexo, em 31/12/2025.\"",
        "<b>Clientes e contrapartes de contratos bilaterais.</b> Confirmação positiva do saldo a receber e das "
        "quantidades (MWh) faturadas em dezembro/2025.",
        "<b>Assessores jurídicos.</b> \"Favor informar os processos sob seu patrocínio, a natureza, o valor envolvido, "
        "o prognóstico (provável, possível ou remoto) e a estimativa de desembolso em 31/12/2025.\"",
    ]},
        {"titulo": "Controle de circularização (nenhuma solicitação enviada)",
         "cab": ["Nº", "Tipo de destinatário", "Saldo / assunto (R$ mil)", "Envio", "Resposta", "Diferença",
                 "Alternativo se não houver resposta"],
         "larg": [0.8, 2.8, 3.2, 1.6, 1.6, 1.6, 5.4],
         "linhas": [
             ["1", "Bancos", "Caixa 3.130.363; TVM 691.781", "Não enviado", "—", "—", "Extratos e conciliações; "
              "rendimentos posteriores"],
             ["2", "Agentes fiduciários", "Debêntures 16.646.924", "Não enviado", "—", "—", "Escrituras; "
              "pagamentos posteriores; B3"],
             ["3", "Bancos credores", "Empréstimos 3.368.419", "Não enviado", "—", "—", "Contratos e extratos"],
             ["4", "Clientes livres / bilaterais", "Clientes 4.463.146", "Não enviado", "—", "—",
              "Recebimentos subsequentes; faturas; registros na CCEE"],
             ["5", "Advogados externos", "Provisões 1.934.020", "Não enviado", "—", "—", "Leitura de processos; "
              "consulta pública a tribunais; jurídico interno"],
         ]},
        {"titulo": "Tratamento de diferenças", "paragrafos": [
            "Toda diferença seria investigada: diferença de época (valor em trânsito, conciliado com documento "
            "posterior), de erro (distorção acumulada no PT 450) ou de fraude (comunicação imediata e reavaliação de "
            "riscos). A recusa da administração em permitir a confirmação exigiria indagar os motivos, avaliar a "
            "implicação para o risco de fraude e aplicar procedimentos alternativos (itens 8 e 9)."]}])

# ---------------- PT 510
upd("PT 510", atividade="Tratar o caso como auditoria inicial didática. Examinar saldos de abertura, políticas contábeis "
                        "e efeitos de modificações na opinião do auditor anterior.",
    proc=[("Tratamento como auditoria inicial didática: o auditor anterior é a PwC (2024) e, antes dela, a Deloitte "
           "(2023) [F02; F04].", "R", "F02, F04"),
          ("Testar saldos de abertura por realização posterior: os ativos mantidos para venda de 31/12/2024 "
           "(R$ 1.881.826 mil) caíram para R$ 25.177 mil com a venda da UHE Baixo Iguaçu e de pequenas usinas em "
           "2025 [F01; F02, p. 22]; os empréstimos circulantes de abertura (R$ 1.231.205 mil) foram amortizados "
           "(principal pago de R$ 1.254.405 mil) [F01, p. 25].", "R", "F01, F02"),
          ("Consistência de políticas: as controladas declaram políticas aplicadas de modo consistente e "
           "listam normas novas de 2025 sem impacto relevante [F07, pp. 13 e 16]; a nota consolidada não foi lida.",
           "R/P", "F07"),
          ("Modificações na opinião do auditor anterior: não foi encontrada indicação pública de modificação no "
           "relatório sobre 2024; o 20-F não registra reapresentação [F02]. Ler o relatório de 2024 para confirmar.",
           "R/P", "F02")])

# ---------------- PT 520
desp_esp = (sum(v for _, v, _ in [x for x in dp.PASSIVO_CIRCULANTE if x[0] in ("Empréstimos e financiamentos", "Debêntures")]
                + [x for x in dp.PASSIVO_NAO_CIRCULANTE if x[0] in ("Empréstimos e financiamentos", "Debêntures")])
            + sum(v for _, _, v in [x for x in dp.PASSIVO_CIRCULANTE if x[0] in ("Empréstimos e financiamentos", "Debêntures")]
                  + [x for x in dp.PASSIVO_NAO_CIRCULANTE if x[0] in ("Empréstimos e financiamentos", "Debêntures")])) / 2 * 0.1322
base24 = 8516697 + 16623610
base25 = 8145552 + 19206609
da_esp = 1465478 / base24 * (base24 + base25) / 2
cons_esp = 3272763 * (2550809 / 2522908)
exp_linhas = [
    ["Despesa financeira", "Dívida média x 13,22% (custo nominal informado) [F01, p. 7]", br(desp_esp), "3.142.010",
     br(3142010 - desp_esp), "Investigada: encargos da dívida R$ 2.490.902 mil (+1,1%); restante fora da dívida (F17, NE 30)"],
    ["Depreciação e amortização", "Taxa implícita 2024 x base média 2025 (imobilizado + intangível)", br(da_esp),
     "1.481.886", br(1481886 - da_esp), "Dentro do limite; queda coerente com renovação de concessões (F07)"],
    ["Receita de construção", "Custo de construção 2025 x (1 + margem de 2024)", br(cons_esp), "3.303.150",
     br(3303150 - cons_esp), "Dentro do limite"],
    ["Dividendos a pagar", "Proventos declarados no 4T25 (1.350.000 + 1.100.000)", "2.450.000", "2.325.889",
     "-124.111", "Investigada: IRRF s/ JCP R$ 168.009 mil (F17, NE 12.2); resíduo R$ 43.898 mil em aberto"],
]
upd("PT 520", atividade="Construir expectativas, definir precisão e limites de investigação, calcular relações e "
                        "variações e investigar diferenças. Apresentar cálculos reproduzíveis.",
    anexos=[{"titulo": f"Expectativas, limites e diferenças (R$ mil) - limite de investigação = materialidade de "
                       f"execução (R$ {br(ME)} mil); cálculo em XLS:Expectativas_520",
             "cab": ["Item", "Base da expectativa", "Esperado", "Registrado", "Diferença", "Conclusão"],
             "larg": [2.6, 4.6, 2.0, 2.0, 1.8, 4.0], "linhas": exp_linhas},
            {"titulo": "Precisão", "paragrafos": [
                "As expectativas usam dados agregados anuais e premissas simples (taxa média, margem do ano anterior), "
                "por isso têm precisão baixa e servem como analíticos de avaliação de riscos e de conclusão, não como "
                "substantivos isolados para riscos significativos (NBC TA 330, item 21). Diferenças acima do limite "
                "exigem explicação documentada da administração e corroboração."]}])

# ---------------- PT 530
upd("PT 530", atividade="Aplicar amostragem à base simulada obrigatória. Definir população, unidade amostral, método, "
                        "tamanho, seleção, risco amostral, tratamento e projeção de erros.",
    anexos=[{"titulo": "Desenho da amostra", "cab": ["Elemento", "Definição"], "larg": [3.6, 13.4],
             "linhas": [
                 ["População", f"[S] {br(T11['registros_populacao'])} registros do intangível com valor positivo"],
                 ["Unidade amostral", "Cada real (R$ 1) de valor contábil líquido (amostragem por unidade monetária)"],
                 ["Método", "Seleção sistemática por intervalo monetário com início aleatório; itens >= intervalo são "
                            "itens-chave"],
                 ["Tamanho", f"n = {T11['tamanho_amostra']}; intervalo R$ {br(T11['intervalo_amostral_R$'], 2)}"],
                 ["Risco amostral", "5% (confiança de 95%) de aceitar a população com distorção acima da tolerável; "
                                    "risco não amostral tratado por desenho dos testes e supervisão"],
                 ["Tratamento de erros", "Contaminação (distorção / valor contábil) projetada pelo intervalo; itens-chave "
                                         "pelo valor real; registros com valor <= 0 testados por CAAT"],
                 ["Projeção e avaliação", f"Projetada R$ {br(T11['distorcao_projetada_R$'], 2)}; LSD R$ "
                                          f"{br(T11['limite_superior_distorcao_R$'], 2)} > tolerável: extensão a 100%"],
             ]}])

# ---------------- PT 540 (sensibilidade da PECLD)
bruto = dp.VENCIDOS_LIQUIDOS_PECLD_RS_MI + dp.PECLD_RS_MI
cob = dp.PECLD_RS_MI / bruto
sens = []
for c in (0.20, 0.35, 0.40, 0.50):
    nova = bruto * c
    dlt = nova - dp.PECLD_RS_MI
    sens.append([f"{br(c * 100, 0)}%", br(nova, 1), br(dlt, 1),
                 "Acima da global" if abs(dlt) * 1000 > MG else "Acima da ME" if abs(dlt) * 1000 > ME
                 else "Abaixo da ME"])
upd("PT 540", atividade="Selecionar estimativa relevante e avaliar método, premissas, dados, incerteza e possível viés "
                        "da administração. Executar análise de sensibilidade.",
    proc=[("Estimativa selecionada para avaliação detalhada: perda de crédito esperada (PECLD) de clientes. [J] É "
           "relevante (R$ 245,6 milhões, acima da ME), sensível à conjuntura (Selic de 15%) e é a única estimativa "
           "com dados públicos suficientes para sensibilidade quantitativa.", "R", "F02, p. 5"),
          ("Análise de sensibilidade da cobertura da PECLD sobre os vencidos (tabela).", "R", "XLS:Sensibilidade_540")],
    anexos=[{"titulo": "Avaliação da PECLD", "cab": ["Aspecto", "Análise"], "larg": [3.0, 14.0],
             "linhas": [
                 ["Método", "Abordagem simplificada do CPC 48/IFRS 9 por faixa de atraso e classe de consumidor "
                            "(política descrita nas DFs das controladas, por exemplo F07, p. 14). [J] Adequado para "
                            "carteira pulverizada."],
                 ["Premissas", "Taxas históricas de perda por faixa, efeito de ações de cobrança e de "
                               "acordos; cenário macroeconômico. Não divulgadas no material lido (P)."],
                 ["Dados", f"Vencidos líquidos R$ {br(dp.VENCIDOS_LIQUIDOS_PECLD_RS_MI, 1)} mi e PECLD R$ "
                           f"{br(dp.PECLD_RS_MI, 1)} mi [F02, p. 5] = vencidos brutos de R$ {br(bruto, 1)} mi; "
                           f"cobertura de {br(cob * 100, 1)}%. Pressuposto: a PECLD informada refere-se aos vencidos."],
                 ["Incerteza", "Moderada: depende da inadimplência futura e da migração para o mercado livre."],
                 ["Possível viés", "Incentivo a reduzir a PECLD para melhorar o EBITDA; o release informa aumento de "
                                   "R$ 13,2 mi na PECLD da DIS no 4T25 [F01, p. 14], o que não indica viés de redução."],
             ]},
            {"titulo": "Sensibilidade da PECLD à cobertura dos vencidos (R$ milhões)",
             "cab": ["Cobertura", "PECLD no cenário", "Variação vs. registrado", "Comparação com materialidade"],
             "larg": [3.0, 4.0, 4.6, 5.4], "linhas": [[f"Atual {br(cob * 100, 1)}%", br(dp.PECLD_RS_MI, 1), "0,0", "—"]] + sens},
            {"titulo": "Leitura", "paragrafos": [
                "Uma cobertura até cerca de 40% muda a PECLD em menos que a materialidade de execução; acima de "
                "aproximadamente 48%, a variação supera a materialidade global. [J] A estimativa é relevante, mas só "
                "se tornaria distorção relevante com mudança grande de premissa; o teste das taxas de perda por faixa "
                "(P) é a resposta principal."]}])

# ---------------- PT 550
upd("PT 550", atividade="Mapear vínculos, saldos e transações. Avaliar completude e divulgações e planejar a "
                        "identificação de operações não informadas.",
    anexos=[{"titulo": "Mapa de partes relacionadas",
             "cab": ["Parte", "Vínculo", "Saldos / transações conhecidos", "Fonte", "Atenção"],
             "larg": [3.0, 3.4, 4.4, 1.8, 4.4],
             "linhas": [
                 ["Estado do Paraná", "15,9% e ação de classe especial (veto)", "Tributos estaduais (ICMS), "
                  "entidades ligadas", "F01, F02", "Influência significativa sem controle"],
                 ["Sanepar e Simepar", "Ligadas ao Estado", "Serviços à F.D.A. (Simepar R$ 996 mil em 2024)", "F07, p. 26",
                  "Divulgação no consolidado"],
                 ["BNDESPAR / BNDES", "22,0% do capital", "Repasses BNDES em financiamentos (a confirmar)", "F01",
                  "Credor e acionista ao mesmo tempo"],
                 ["Fundação Copel", "Plano de benefícios", "Contribuições; passivo atuarial R$ 1.478.157 mil", "F01",
                  "Premissas atuariais"],
                 ["Lactec", "OSCIP da qual a Copel é associada", "Contratos de P&D", "F07, p. 26", "Aprovação ANEEL"],
                 ["Joint ventures e coligadas", "Controle conjunto / influência", "Dividendos a receber R$ 141.297 mil; "
                  "equivalência R$ 239.997 mil", "F01", "Transações de O&M e energia"],
                 ["Pessoal-chave", "Administradores", "Remuneração, PLR, ILP", "F01, p. 6", "Relevante pela natureza"],
             ]},
            {"titulo": "Identificação de operações não informadas (planejado)", "paragrafos": [
                "(1) Obter da administração a lista de partes relacionadas e comparar com o formulário de referência, "
                "atas e registro de acionistas; (2) cruzar CNPJ de fornecedores e clientes com participações de "
                "administradores e acionistas relevantes; (3) ler contratos acima do trivial e transações fora do "
                "curso normal (troca de ativos, alienações); (4) indagar o CAE; (5) revisar confirmações bancárias e "
                "jurídicas em busca de garantias a terceiros ligados."]}])

# ---------------- PT 560
upd("PT 560", atividade="Fixar a data de corte da pesquisa, examinar publicações posteriores ao encerramento e "
                        "distinguir eventos que exigem ajuste daqueles que exigem divulgação.",
    proc=[("Data de corte da pesquisa: 24/10/2026. Período examinado: 01/01/2026 a 24/10/2026, com marco na data "
           "de aprovação das DFs (26/02/2026) [F03].", "R", "F03")],
    anexos=[{"titulo": "Eventos após 31/12/2025",
             "cab": ["Evento", "Data", "Antes/depois do relatório", "Classificação", "Fonte"],
             "larg": [6.0, 2.2, 2.8, 3.6, 2.4],
             "linhas": [
                 ["Dividendos de R$ 1,35 bilhão (data-base 30/12/2025)", "10/12/2025", "Antes do encerramento",
                  "Fato do exercício (passivo)", "F06"],
                 ["Antecipação de dividendos da F.D.A. (R$ 120 milhões)", "16/01/2026", "Antes",
                  "Sem efeito consolidado (intragrupo)", "F07"],
                 ["Leilão de reserva de capacidade (LRCAP): UHE Segredo e UHE Foz do Areia vencedoras; compromisso "
                  "de ampliação de R$ 4.249.072 mil (F.D.A.: R$ 963,2 mi/ano por 15 anos)", "18/03/2026", "Depois",
                  "Não ajusta; divulgação de compromisso em 2026", "F07, F16 p. 46"],
                 ["Extinção da concessão e venda da UTE Figueira (ativo mantido para venda de R$ 25.177 mil em "
                  "31/12/2025)", "15 e 30/04/2026", "Depois", "Não ajusta; realização do saldo classificado em 2025",
                  "F16, p. 47"],
                 ["Arquivamento do 20-F", "15/04/2026", "Depois", "Não ajusta", "F02"],
                 ["Renegociação do UBP da Elejor", "25/05/2026", "Depois", "Não ajusta; efeito em 2026", "F08"],
                 ["Portaria MME 140/2026: compensação de curtailment a geradores eólicos e solares", "21/07/2026",
                  "Depois", "Não ajusta 2025; reforça a incerteza do ressarcimento de curtailment reconhecido em 2025",
                  "F16, p. 47"],
             ]}])

# ---------------- PT 570
upd("PT 570", atividade="Analisar liquidez, endividamento, cláusulas contratuais, fluxos de caixa e eventos adversos. "
                        "Avaliar incertezas relevantes e divulgações.",
    proc=[("Cláusulas contratuais: a companhia informa que parte dos financiamentos tem covenants financeiros e "
           "cláusulas de vencimento antecipado e cross-default [F02, p. 19]; os índices e limites não foram obtidos "
           "(P). [J] Alavancagem de 2,7x dentro da faixa-alvo de 2,5x a 3,1x sugere folga.", "R/P", "F02"),
          ("Eventos adversos [F]: tornado em Rio Bonito do Iguaçu (2025) com danos à rede [F02, p. 9]; "
           "curtailment de 34,2% nas eólicas no 4T25 [F01, p. 4]; Selic de 15% [F02, p. 15]; eleições "
           "presidenciais de 2026 [F02, p. 15].", "R", "F01, F02"),
          ("Divulgações: verificar nota de base de preparação e continuidade das DFs consolidadas (P); exemplo "
           "público na controlada F.D.A., sem incerteza relevante [F07, p. 13].", "R/P", "F07")])

# ---------------- PT 580
upd("PT 580", atividade="Preparar minuta didática da carta de representações da administração. Explicar por que ela "
                        "não substitui outras evidências.",
    anexos=[{"titulo": "Minuta didática de carta de representação", "paragrafos": [
        MINUTA,
        "Curitiba, [data do relatório]. À [firma de auditoria]. Em conexão com a auditoria das DFs individuais e "
        "consolidadas da COPEL de 31/12/2025, confirmamos, segundo nosso melhor conhecimento:",
        "(1) Cumprimos nossa responsabilidade pela elaboração das DFs de acordo com as práticas contábeis adotadas "
        "no Brasil e as IFRS. (2) Fornecemos acesso a todas as informações, registros e pessoas, e todas as "
        "transações foram registradas. (3) As premissas das estimativas (CVA, VNR, ativos de contrato, PECLD, "
        "provisões, benefícios, impairment e IR diferido) são razoáveis. (4) Todos os litígios e reclamações "
        "conhecidos foram avaliados e divulgados. (5) Divulgamos todas as partes relacionadas e transações com "
        "elas. (6) Todos os eventos subsequentes que exigem ajuste ou divulgação foram tratados. (7) Os efeitos das "
        "distorções não corrigidas listadas em anexo são irrelevantes. (8) Não temos conhecimento de fraude ou "
        "suspeita de fraude além das informadas. (9) Não houve descumprimento de leis e regulamentos não divulgado.",
        "[Diretor-Presidente] [Diretor de Finanças e RI] - assinaturas deixadas em branco."]},
        {"titulo": "Por que a carta não substitui outras evidências", "paragrafos": [
            "A representação é evidência necessária, mas não suficiente por si só (NBC TA 580, item 4): vem da própria "
            "parte responsável, não é independente e não comprova existência, valor ou completude. Ela complementa e "
            "não dispensa confirmações, inspeções e recálculos. Se uma representação for incoerente com outra "
            "evidência (por exemplo, a distorção E07 da simulação), o auditor deve reavaliar a confiabilidade de "
            "todas as representações."]}])

# ---------------- PT 600 (materialidade dos componentes)
comp = [("Copel DIS", 0.75), ("Copel GeT (geração e transmissão)", 0.65), ("Copel Comercialização", 0.40),
        ("Demais (eólicas, F.D.A., Elejor, SPEs, holding)", 0.25)]
upd("PT 600", atividade="Mapear o grupo, seus componentes e o processo de consolidação. Avaliar riscos, materialidade dos "
                        "componentes, envolvimento de auditores de componentes e suficiência das evidências.",
    proc=[("Processo de consolidação: eliminação de receitas intragrupo (R$ 2.851.941 mil em 2025), de saldos de "
           "dividendos e de investimentos; equivalência das joint ventures [F01, Anexo II]. Testar o pacote de "
           "consolidação e as eliminações.", "R/P", "F01"),
          ("Suficiência das evidências do grupo: [J] cobertura proposta por auditoria completa da DIS e da GeT "
           "(cerca de 78% da receita somada antes de eliminações) e procedimentos específicos na Copel Com; "
           "demais com analíticos de grupo.", "R", "XLS:Grupo_600")],
    anexos=[{"titulo": f"Materialidade dos componentes (R$ mil) - base: ME do grupo R$ {br(ME)} mil; "
                       "cálculo em XLS:Grupo_600",
             "cab": ["Componente", "% da ME do grupo", "Materialidade do componente", "Justificativa"],
             "larg": [5.0, 2.6, 3.4, 6.0],
             "linhas": [[n, f"{br(p * 100, 0)}%", br(ME * p), j] for (n, p), j in zip(comp, [
                 "Maior componente; ainda abaixo da ME do grupo para reduzir o risco de agregação",
                 "Significativo; estimativas de transmissão e geração",
                 "Risco específico (MTM e bilaterais)",
                 "Muitos componentes pequenos: limite menor pelo risco de agregação"])]}])

# ---------------- Programas, base e finais: remover campos com traço
upd("PT BS-01", limitacoes="A escolha usa o saldo publicado; sem a nota explicativa, a composição interna do "
                           "intangível não foi conhecida, por isso a base usa composição hipotética (PT BS-02).")
upd("PT BS-02", afirmacoes="Não há afirmação da administração em exame; o risco é de a base sintética não representar "
                           "bem a conta real e levar a conclusões indevidas.")
upd("PT BS-03", afirmacoes="Não há afirmação em exame; o risco é de uso incorreto das variáveis nos testes.",
    limitacoes="Variáveis definidas para fins didáticos; o cadastro real segue o Manual de Controle Patrimonial do "
               "Setor Elétrico e tem outros campos.")
upd("PT RA", afirmacoes="Não há afirmação em exame; o risco é de interpretar a opinião do auditor de forma "
                        "incompleta sem o texto integral.")
upd("PT MC", afirmacoes="Não há afirmação em exame; o risco é de norma sem papel de trabalho correspondente.",
    limitacoes="A matriz depende da correta numeração dos itens citados, conferida contra as versões do CFC (F09).")

# ---------------- ordem final (PT 500.2 depois de PT 500.1)
_ordem = [d["cod"] for d in PTS]
_ordem.remove("PT 500.2")
_ordem.insert(_ordem.index("PT 500.1") + 1, "PT 500.2")
PTS = [IDX[c] for c in _ordem]


# ---------------- Evidências das ITR 2026 da Copel GeT (F15, F16), fornecidas pela estudante
upd("PT EC", proc=[("Exemplo real de revisão (asseguração limitada): o relatório da PwC sobre a ITR de março/2026 da "
                    "Copel GeT diz que o alcance da revisão é significativamente menor que o de uma auditoria e que, "
                    "por isso, não expressa opinião de auditoria; a conclusão é negativa ('não temos conhecimento de "
                    "nenhum fato...') [F15, pp. 47-48].", "R", "F15")])
upd("PT 510", proc=[("Realização posterior de saldo de abertura: a UTE Figueira, último dos ativos de pequeno porte "
                     "mantidos para venda (R$ 25.177 mil em 31/12/2025), teve a venda concluída em 30/04/2026 "
                     "[F16, p. 47].", "R", "F16")])
upd("PT 600", proc=[("Componente Copel GeT com evidência própria [F]: ativo total consolidado de R$ 32.660.978 mil e "
                     "intangível de R$ 7.150.619 mil em 31/12/2025 (54% do ativo e 37% do intangível do grupo); "
                     "informações trimestrais de 2026 revisadas pela PwC, a mesma firma do grupo (relatórios de "
                     "05/05/2026 e 05/08/2026) [F15, pp. 3 e 48; F16, p. 53]. [J] Componente significativo, auditado pela "
                     "própria firma do grupo, o que reduz o risco de envolvimento de auditor de outro escritório.",
                     "R", "F15, F16"),
                    ("Conciliar o intangível da GeT com a base sintética: o segmento Copel GeT da base soma "
                     f"R$ {br(RES['T01_GeT']['base_segmento_GeT_R$'], 2)}, diferença de R$ "
                     f"{br(RES['T01_GeT']['diferenca_R$'], 2)}.", "S", "PT BS-04")])
upd("PT BS-04", proc=[("Conciliar o subtotal do segmento Copel GeT da base com o intangível consolidado da GeT em "
                       "31/12/2025 (R$ 7.150.619 mil) [F15, NE 15, p. 21].", "S", "F15")],
    resultados=IDX["PT BS-04"]["resultados"] + f" Subtotal Copel GeT: R$ {br(RES['T01_GeT']['base_segmento_GeT_R$'], 2)} "
               f"contra R$ 7.150.619.000,00 reais; diferença de R$ {br(RES['T01_GeT']['diferenca_R$'], 2)}.")
upd("PT PA-06", proc=[("Passivos de combinação de negócios (CPC 15): contraprestação contingente de R$ 362.465 mil e "
                       "passivo contingente de R$ 685.022 mil na Copel GeT em 31/12/2025 [F15, p. 27]. Testar premissas "
                       "de mensuração a valor justo e a atualização posterior.", "R/P", "F15")])
upd("PT 315.2", proc=[("Atualização com F15: os passivos de combinação de negócios da Copel GeT somam R$ 1.047.487 mil "
                       "(contraprestação contingente R$ 362.465 mil + passivo contingente R$ 685.022 mil) e integram o "
                       "risco R06/R09.", "R", "F15")])


# ---------------- DFs anuais completas da holding (F17), fornecidas pela estudante
upd("PT 000", proc=[("DFs individuais e consolidadas de dezembro/2025 da Companhia Paranaense de Energia (CNPJ "
                     "76.483.817/0001-20), com relatório da administração, notas e relatório do auditor, obtidas no RI "
                     "[F17]. Conferência: intangível R$ 19.206.609 mil, total do ativo R$ 60.414.456 mil e 'Provisões "
                     "para litígios e outras provisões' R$ 1.934.020 mil no balanço [F17, pp. 47-48] iguais ao release "
                     "(F01).", "R", "F17")])
upd("PT 501", proc=[("Nota 26 da holding [F17, pp. 105-107]: provisões para litígios R$ 1.571.555 mil (fiscais, "
                     "trabalhistas R$ 287.244 mil, cíveis R$ 408.044 mil, regulatórias R$ 13.939 mil, benefícios a "
                     "empregados R$ 31.222 mil e passivo contingente de combinação de negócios R$ 685.022 mil) + "
                     "contraprestação contingente R$ 362.465 mil (UHE Colíder) = R$ 1.934.020 mil. Passivos "
                     "contingentes com perda possível: R$ 2.390.222 mil (R$ 2.807.918 mil em 2024).", "R", "F17")])
IDX["PT 501"]["resultados"] = ("[F] O balanço oficial já denomina a linha 'Provisões para litígios e outras "
    "provisões' [F17, p. 48]; a nota 26 abre R$ 1.571.555 mil de litígios e R$ 362.465 mil de contraprestação "
    "contingente. A diferença com o 20-F (que cita só os litígios) está explicada. Perdas possíveis de "
    "R$ 2.390.222 mil, divulgadas e não provisionadas, equivalem a 15 vezes a materialidade global. [J] Esse é o "
    "PAA 1 da PwC.")
upd("PT 540", proc=[("Confirmação dos dados da PECLD na nota 7 [F17, p. 73]: PECLD total R$ 255.318 mil, dos quais "
                     "R$ 17.637 mil sobre vencidos até 90 dias e R$ 228.012 mil sobre vencidos há mais de 90 dias "
                     "(R$ 245.649 mil sobre vencidos, igual aos R$ 245,6 milhões do 20-F); vencidos líquidos de "
                     "R$ 605.536 mil. A premissa da sensibilidade (PECLD sobre vencidos) está confirmada.", "R", "F17"),
                    ("Estimativa do PAA 2: receita não faturada de R$ 931.460 mil (R$ 930.801 mil em 2024) [F17, p. 73]. "
                     "[J] Variação de apenas 0,07%, coerente com a estabilidade do mercado fio; procedimento planejado: "
                     "comparar com o faturamento de janeiro/2026.", "R/P", "F17")])
upd("PT PA-04", proc=[("Movimentação real do intangível [F17, NE 16, p. 91]: saldo inicial 16.623.610 + combinação de "
                       "negócios 731.591 - UBP 1.728 + aquisições 43.788 - amortização 930.256 + transferências de "
                       "ativos de contrato 2.901.548 - baixas 148.017 - reclassificação para mantidos para venda "
                       "13.927 = 19.206.609 (recalculado em XLS:Conciliacao_Intangivel).", "R", "F17")])
IDX["PT PA-04"]["resultados"] = ("[F] A variação do intangível (+R$ 2.582.999 mil) se explica sobretudo por "
    "transferências de ativos de contrato (R$ 2.901.548 mil) e pela combinação de negócios (R$ 731.591 mil), "
    "menos amortização (R$ 930.256 mil); a movimentação recalculada fecha com o saldo. A combinação de negócios "
    "(PAA 3) teve ativos líquidos a valor justo de R$ 1.341.720 mil, pagos com caixa de R$ 196.609 mil, a UHE "
    "Colíder (R$ 1.104.829 mil) e contraprestação contingente de R$ 383.115 mil, menos ativo de indenização de "
    "R$ 342.833 mil, sem ágio [F17, p. 59].")
upd("PT 560", anexos=[{"titulo": "Eventos subsequentes divulgados nas DFs (NE 38) [F17, pp. 136-137]",
    "cab": ["Evento", "Data", "Classificação"], "larg": [10.4, 2.4, 4.2],
    "linhas": [
        ["Copel GeT: 11ª emissão de debêntures, R$ 1.200.000 mil, IPCA + 7,1841% a.a., 12 anos, com swap para DI",
         "27/01/2026", "Não ajusta; divulgado"],
        ["Copel DIS: 1ª emissão de notas comerciais, R$ 550.000 mil (DI + 0,30%), quitada em 29/01/2026",
         "19/01/2026", "Não ajusta; divulgado"],
        ["Copel DIS: 11ª emissão de debêntures, R$ 2.000.000 mil, IPCA + 7,1841% a.a., 12 anos, com swap",
         "27/01/2026", "Não ajusta; divulgado"],
        ["Elejor: ANEEL aprova repactuação do UBP, pagamento de R$ 420.631 mil (antes da data do relatório)",
         "24/02/2026", "Não ajusta; divulgado (efeito em 2026)"],
    ]}])
upd("PT 570", proc=[("Avaliação da administração [F17, NE 3.5, p. 64]: não há incertezas materiais; bases: concessões "
                     "de longo prazo, patrimônio líquido, geração de caixa, histórico de lucros e metas do "
                     "planejamento. Relatório da PwC sem parágrafo de incerteza relevante [F17, p. 149].", "R", "F17")])
upd("PT 600", proc=[("Responsabilidade do auditor do grupo declarada no relatório: direção, supervisão e revisão do "
                     "trabalho de auditoria do grupo [F17, p. 154]. Joint ventures e coligadas listadas na NE 1.1 "
                     "[F17, p. 58].", "R", "F17")])
upd("PT 200", proc=[("Relatório real: a PwC declara independência segundo o Código de Ética Profissional do Contador e "
                     "as normas do CFC aplicáveis a entidades de interesse público [F17, p. 149].", "R", "F17")])
upd("PT 230", anexos=[{"titulo": "Versões posteriores", "paragrafos": [
    "Versão 1.2 (24/10/2026): inclusão das ITR de 2026 da Copel GeT (F15, F16). Versão 1.3 (24/10/2026): inclusão "
    "das DFs anuais completas da holding (F17), com substituição dos PAA inferidos pelos reais e reancoragem da "
    "base sintética nas categorias da nota 16."]}])
IDX["PT BS-01"]["limitacoes"] = ("A escolha usa o saldo e a composição publicados (NE 16, F17); a divisão interna da "
    "geração na base é hipotética (PT BS-02).")


# ---------------- Leitura integral das notas da holding (F17, NE 1 a 38, CAE e Conselho Fiscal)
upd("PT 240", proc=[("Ganhos não recorrentes de 2025 [F17, NE 29.6, p. 116; NE 32.2.9, p. 128]: resultado de "
                     "alienação de ativos R$ 335.595 mil, resultado da combinação de negócios R$ 141.661 mil e "
                     "ressarcimento de curtailment R$ 273.382 mil (R$ 170.125 mil na receita, R$ 95.599 mil em outras "
                     "receitas e R$ 7.658 mil na receita financeira). Juntos, equivalem a 23% do LAIR. [J] Com a "
                     "remuneração variável e o ILP ligados a resultado e TSR (NE 27.4) e a política de dividendos "
                     "ligada à alavancagem, esses itens são indicadores de possível viés da administração e exigiriam "
                     "teste do suporte e da competência de cada ganho.", "R/P", "F17")])
upd("PT 250", proc=[("Normas novas com efeito nas DFs [F17]: Lei 15.269/2025 (compensação de curtailment e novas "
                     "regras de prorrogação de concessões hidrelétricas, NE 32.2.6 e 32.2.9, pp. 126-128); ADI 7324 "
                     "sobre devolução de créditos de PIS/Cofins a consumidores, com embargos pendentes no STF "
                     "(NE 12.3, p. 82, provisão de R$ 780.553 mil); reforma tributária do consumo (LC 214/2025 e "
                     "227/2025, NE 12.5, p. 83); indicadores de eficiência da concessão de distribuição, com DEC 7,17 "
                     "e FEC 4,65 em 2025 dentro dos limites de 8,14 e 5,80 (NE 32.2.7, p. 127).", "R", "F17")])
upd("PT 260", proc=[("Relatório anual do Comitê de Auditoria Estatutário [F17, pp. 141-148]: 15 reuniões em 2025, 12 "
                     "pautas com a PwC (planejamento, controles internos, assuntos significativos e acompanhamento dos "
                     "planos de ação para as deficiências apontadas pelo auditor) e 11 pautas sobre partes "
                     "relacionadas; o CAE não identificou situações que afetassem a independência do auditor. O "
                     "Conselho Fiscal opinou favoravelmente às DFs em 26/02/2026 [F17, p. 140].", "R", "F17")])
IDX["PT 265"]["anexos"][0]["linhas"].append(
    ["Deficiências de controle apontadas pela PwC em 2025, com planos de ação acompanhados pelo CAE [F17, p. 143]",
     "Comunicação de deficiências (NBC TA 265; SOx 404)", "Não divulgada", "Não divulgado; o relatório da PwC "
     "não traz modificação e o CAE avalia os controles como adequados", "Obter a carta de recomendações e "
     "avaliar a severidade de cada deficiência", "Fato público sem detalhe (natureza e severidade desconhecidas)"])
upd("PT 505", proc=[("Covenants lidos [F17, NE 19.3 e 20.3, pp. 93-96]: dívida líquida/EBITDA consolidado limite 3,5 "
                     "(anuência temporária dos debenturistas para até 4,5, negociada no 4T25), ICSD de 1,2 a 1,5 "
                     "conforme o contrato. Todos atendidos em 31/12/2025, exceto Ventos de Santo Uriel, dispensada do "
                     "ICSD de 2025 por carta do BNDES. Alavancagem pela política de dividendos: 2,7x [F17, p. 138]. "
                     "Modelos de confirmação com os credores continuam planejados.", "R/P", "F17")])
upd("PT 540", proc=[("Impairment [F17, NE 15.4, p. 90]: sem perda em 2025; a menor folga é do Complexo Jandaíra "
                     "(valor recuperável 8,18% acima do contábil, taxa de 5,84%; folga de 1,44% com a taxa 10% maior). "
                     "[J] Premissa sensível: pequena alta da taxa de desconto levaria a impairment.", "R", "F17"),
                    ("Benefícios pós-emprego [F17, NE 21.4, pp. 98-99]: passivo do plano assistencial R$ 1.471.964 mil; "
                     "com a taxa de desconto 0,5 p.p. menor, a obrigação iria a R$ 1.784.104 mil (+R$ 312 milhões, "
                     "cerca de 2 vezes a materialidade global). Planos previdenciários superavitários sem ativo "
                     "reconhecido.", "R", "F17"),
                    ("Ressarcimento de curtailment [F17, NE 32.2.9, p. 128]: ganho de R$ 273.382 mil reconhecido com "
                     "base na adesão ao termo de compromisso (Lei 15.269/2025), com a regulamentação em consulta "
                     "pública (CP MME 210/2025) na data do balanço. [J] Estimativa com alta incerteza e julgamento "
                     "sobre o momento do reconhecimento (CPC 25: ativo contingente só com realização praticamente "
                     "certa); seria prioridade de teste.", "R/P", "F17"),
                    ("MTM de energia [F17, NE 32.2.10, p. 129]: saldo líquido de R$ 330.059 mil, com preços definidos "
                     "internamente; cenários de ±50% no preço levam a R$ 161.165 mil ou R$ 498.952 mil.", "R", "F17")])
upd("PT 550", proc=[("Nota 33 lida [F17, pp. 130-132]: dividendos a pagar ao Estado R$ 215.742 mil e à BNDESPAR "
                     "R$ 298.087 mil; financiamentos do BNDES R$ 1.114.432 mil e debêntures eólicas R$ 65.631 mil "
                     "(BNDES é credor e acionista); aluguel de imóveis da Fundação Copel (passivo R$ 135.085 mil); "
                     "vendas de energia a entidades do Estado (Sanepar R$ 39.288 mil); honorários do pessoal-chave "
                     "R$ 67.852 mil (R$ 40.800 mil em 2024, +66%). A relação de credor do BNDES está divulgada.",
                     "R", "F17")])
upd("PT 570", proc=[("Liquidez e dívida [F17]: covenants atendidos com anuência temporária para alavancagem até 4,5x "
                     "(NE 20.3); fluxo contratual de passivos de R$ 8,5 bilhões em até 1 ano (NE 32.2.2, p. 124); "
                     "captações de R$ 3,75 bilhões em janeiro/2026 'para melhorar a capacidade financeira de curto "
                     "prazo' (NE 32.2.2 e 38); Elejor com patrimônio líquido negativo de R$ 126.806 mil (NE 14.2.1, "
                     "p. 85). [J] São fatores de atenção, mas não dúvida significativa: concessões longas, geração de "
                     "caixa, acesso comprovado ao mercado e alavancagem de 2,7x.", "R", "F17")])
upd("PT 600", proc=[("Investidas [F17, NE 14, pp. 84-87]: equivalência de R$ 239.997 mil; passivos contingentes das "
                     "joint ventures (parte da Copel) com perda possível de R$ 114.902 mil e das coligadas de "
                     "R$ 7.729 mil; garantias da Copel e da Copel GeT a dívidas das transmissoras em conjunto "
                     "(NE 33.1).", "R", "F17")])
IDX["PT 265"]["conclusao"] = ("Nenhuma deficiência material divulgada; o CAE informa deficiências apontadas pela PwC em "
                              "2025, de natureza e severidade não divulgadas, com planos de ação acompanhados.")


# ---------------- DFP entregue à CVM (F18), baixada pela estudante no sistema RAD/ENET
upd("PT 000", proc=[("Conferência da fonte oficial: DFP de 31/12/2025, versão 1, entregue à CVM (código 014311) [F18]. "
                     "Os 218 valores do balanço, DRE e DFC usados neste dossiê foram procurados por código na DFP: 182 "
                     "aparecem nas demonstrações padronizadas e 33 nas notas; os 3 restantes vêm da abertura do release "
                     "(F01): fornecimento e suprimento de 2025 (PT 500.1) e outros custos de 2024 (inclui R$ 936 mil de "
                     "matéria-prima, linha separada nas DFs). O relatório da PwC é idêntico ao do arquivo do RI (F17): mesma data "
                     "(26/02/2026), mesmo sócio (Guilherme Naves Valle) e os mesmos três PAA [F18, pp. 156-159]. "
                     "[J] O arquivo do RI corresponde à DFP oficial; F17 e F18 podem ser usadas como a mesma evidência.",
                     "R", "F18")])
upd("PT 500.1", proc=[("Consistência entre release (F01, não auditado) e DFs (F18): a receita de fornecimento e a de "
                       "suprimento aparecem com R$ 28.396 mil de diferença de classificação (release 7.961.249 e "
                       "4.756.273; DFs 7.932.853 e 4.784.669 [F18, p. 129]); o total de R$ 12.717.522 mil é igual. "
                       "[J] Diferença de apresentação acima do trivial, sem efeito no resultado; para análises por "
                       "linha prevalece a DF auditada.", "R", "F18")])
upd("PT RA", proc=[("Conferir o relatório do auditor na DFP entregue à CVM: texto, data, assinatura e PAA iguais aos "
                    "do arquivo do RI [F18, pp. 156-159].", "R", "F18")])
upd("PT 580", proc=[("Evidência pública análoga na holding: declarações da Diretoria Executiva (Resolução CVM 80/2022) "
                     "de que reviu, discutiu e concorda com as DFs e com a opinião da PwC, datadas de 26/02/2026 "
                     "[F18, pp. 166-167]. [J] Não substituem a carta de representação da NBC TA 580, que é dirigida "
                     "ao auditor e cobre afirmações específicas.", "R", "F18")])

# ---------------- Consulta à página da companhia na B3 (print da estudante, 24/10/2026)
upd("PT 000", proc=[("Códigos na B3 em 24/10/2026 [F19]: nome de pregão COPEL; CPLE3 (ISIN BRCPLEACNOR8) e CPLE99 "
                     "(ISIN BRCPLECDAXX8), exibido como código principal; código CVM 14311; CNPJ 76.483.817/0001-20; "
                     "setor Utilidade Pública / Energia Elétrica. CPLE5, CPLE6 e CPLE11 não aparecem mais. "
                     "[J] O CPLE99 deve corresponder à ação preferencial de classe especial do Estado (1 ação, NE 27.1) "
                     "ou à PNC resgatável da migração; a página não informa a espécie, e a hipótese não foi confirmada.",
                     "R", "F19")])
