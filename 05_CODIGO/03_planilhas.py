"""
03_planilhas.py - Gera 02_PLANILHAS/PT_calculos_COPEL_2025.xlsx (editável, com fórmulas).

Abas: Capa, BP, DRE, Indicadores, Materialidade, Contas_Significativas,
Conciliacao_Intangivel, MUS_Parametros, MUS_Amostra, MUS_Avaliacao,
Excecoes, Distorcoes, Analiticos, Continuidade, Matriz_Cobertura, Fontes.

Convenção de cores: azul = dado de entrada (fonte pública ou premissa);
preto = fórmula; verde = vínculo com outra aba; fundo amarelo = premissa de julgamento.
Executar após 02_testes_auditoria.py. Preparadora: matrícula 232025417.
"""
import json
from pathlib import Path

import pandas as pd
from openpyxl import Workbook
from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

import dados_publicos as dp
import estrutura_pt as ep

RAIZ = Path(__file__).resolve().parents[1]
RES = json.loads((RAIZ / "04_RESULTADOS_TESTES" / "resultados_testes.json").read_text())

AZUL = Font(name="Arial", size=10, color="0000FF")
PRETO = Font(name="Arial", size=10)
VERDE = Font(name="Arial", size=10, color="008000")
NEG = Font(name="Arial", size=10, bold=True)
TIT = Font(name="Arial", size=13, bold=True, color="1F3864")
CAB = Font(name="Arial", size=10, bold=True, color="FFFFFF")
FUNDO_CAB = PatternFill("solid", fgColor="1F3864")
AMARELO = PatternFill("solid", fgColor="FFFF00")
CINZA = PatternFill("solid", fgColor="F2F2F2")
FINO = Side(style="thin", color="BFBFBF")
BORDA = Border(top=FINO, bottom=FINO, left=FINO, right=FINO)
NUM = '#,##0;(#,##0);"-"'
NUM2 = '#,##0.00;(#,##0.00);"-"'
PCT = '0.0%;(0.0%);"-"'

wb = Workbook()


def aba(nome, titulo, larguras):
    ws = wb.create_sheet(nome)
    ws["A1"] = titulo
    ws["A1"].font = TIT
    ws["A2"] = (f"COPEL - exercício 2025 | Preparadora: matrícula {dp.MATRICULA} | Data: {dp.DATA_PREPARACAO} | "
                "Revisão: ____________ (campo não preenchido - sem revisão de terceiros)")
    ws["A2"].font = Font(name="Arial", size=8, italic=True)
    for i, w in enumerate(larguras, 1):
        ws.column_dimensions[get_column_letter(i)].width = w
    return ws


def cab(ws, linha, textos):
    for j, t in enumerate(textos, 1):
        c = ws.cell(linha, j, t)
        c.font, c.fill, c.border = CAB, FUNDO_CAB, BORDA
        c.alignment = Alignment(wrap_text=True, vertical="center")


def put(ws, ref, valor, fonte=PRETO, fmt=None, fill=None, comentario=None):
    c = ws[ref]
    c.value = valor
    c.font = fonte
    if fmt:
        c.number_format = fmt
    if fill:
        c.fill = fill
    if comentario:
        c.comment = Comment(comentario, "232025417")
    c.border = BORDA
    return c


# ---------------------------------------------------------------- Capa
ws = wb.active
ws.title = "Capa"
ws.column_dimensions["A"].width = 30
ws.column_dimensions["B"].width = 95
linhas = [
    ("Trabalho", "Dossiê de auditoria acadêmico - P2 - Auditoria (UnB)"),
    ("Estudante", f"{dp.ESTUDANTE} - matrícula {dp.MATRICULA}"),
    ("Companhia", f"{dp.COMPANHIA} - CNPJ {dp.CNPJ} - Código CVM {dp.CODIGO_CVM}"),
    ("Exercício", "31/12/2025 (comparativo 31/12/2024) - demonstrações consolidadas"),
    ("Data de consulta das fontes", dp.DATA_CONSULTA),
    ("Natureza", "Trabalho acadêmico realizado com apoio de IA. NÃO é opinião profissional independente."),
    ("Dados sintéticos", "Abas MUS_*, Excecoes, Distorcoes (parte simulada) e Conciliacao_Intangivel (base) usam "
                         "DADOS SINTÉTICOS gerados por código; não são registros reais da COPEL."),
    ("Unidade", "R$ mil, salvo indicação (R$ = reais nas abas da base sintética)."),
    ("Cores", "Azul = entrada (fonte pública/premissa) | Preto = fórmula | Verde = vínculo entre abas | "
              "Amarelo = premissa de julgamento editável"),
    ("Revisão", "Campo de revisão não preenchido: não há revisão de terceiros."),
]
ws["A1"] = "PT_calculos_COPEL_2025 - Planilhas editáveis do dossiê"
ws["A1"].font = TIT
for i, (a, b) in enumerate(linhas, 3):
    ws.cell(i, 1, a).font = NEG
    c = ws.cell(i, 2, b)
    c.font = PRETO
    c.alignment = Alignment(wrap_text=True)

# ---------------------------------------------------------------- BP
ws = aba("BP", "Balanço patrimonial consolidado (R$ mil) - PT 520 / PT 320", [52, 16, 16, 16, 11, 11, 18])
put(ws, "A3", f"Fonte: {dp.FONTE_BP} (release 4T25, Form 6-K, SEC, 27/02/2026)", AZUL)
cab(ws, 5, ["Rubrica", "31/12/2025", "31/12/2024", "Variação R$", "Variação %", "AV % 2025", "Checagem"])
r = 6
ref = {}


def bloco(titulo, itens, total_pub, chave):
    global r
    ws.cell(r, 1, titulo).font = NEG
    r += 1
    ini = r
    for nome, v25, v24 in itens:
        put(ws, f"A{r}", nome)
        put(ws, f"B{r}", v25, AZUL, NUM)
        put(ws, f"C{r}", v24, AZUL, NUM)
        ref[(chave, nome)] = r
        r += 1
    fim = r - 1
    put(ws, f"A{r}", f"Total {titulo.lower()} (soma)", NEG)
    put(ws, f"B{r}", f"=SUM(B{ini}:B{fim})", NEG, NUM)
    put(ws, f"C{r}", f"=SUM(C{ini}:C{fim})", NEG, NUM)
    put(ws, f"G{r}", f'=IF(AND(B{r}={total_pub[0]},C{r}={total_pub[1]}),"Confere com publicado","DIFERENÇA")')
    ref[(chave, "TOTAL")] = r
    r += 2


bloco("Ativo circulante", dp.ATIVO_CIRCULANTE, dp.TOTAL_AC, "AC")
bloco("Realizável a longo prazo", dp.REALIZAVEL_LP, dp.TOTAL_RLP, "RLP")
bloco("Investimentos, imobilizado e intangível", dp.ATIVO_NC_OUTROS,
      (dp.TOTAL_ANC[0] - dp.TOTAL_RLP[0], dp.TOTAL_ANC[1] - dp.TOTAL_RLP[1]), "ANC")
put(ws, f"A{r}", "TOTAL DO ATIVO", NEG)
put(ws, f"B{r}", f"=B{ref[('AC','TOTAL')]}+B{ref[('RLP','TOTAL')]}+B{ref[('ANC','TOTAL')]}", NEG, NUM)
put(ws, f"C{r}", f"=C{ref[('AC','TOTAL')]}+C{ref[('RLP','TOTAL')]}+C{ref[('ANC','TOTAL')]}", NEG, NUM)
put(ws, f"G{r}", f'=IF(AND(B{r}={dp.TOTAL_ATIVO[0]},C{r}={dp.TOTAL_ATIVO[1]}),"Confere com publicado","DIFERENÇA")')
LIN_ATIVO = r
r += 2
bloco("Passivo circulante", dp.PASSIVO_CIRCULANTE, dp.TOTAL_PC, "PC")
bloco("Passivo não circulante", dp.PASSIVO_NAO_CIRCULANTE, dp.TOTAL_PNC, "PNC")
bloco("Patrimônio líquido - controladores", dp.PATRIMONIO_LIQUIDO, dp.PL_CONTROLADORES, "PL")
put(ws, f"A{r}", "Participação de não controladores")
put(ws, f"B{r}", dp.PL_NAO_CONTROLADORES[0], AZUL, NUM)
put(ws, f"C{r}", dp.PL_NAO_CONTROLADORES[1], AZUL, NUM)
LIN_NC = r
r += 1
put(ws, f"A{r}", "TOTAL DO PATRIMÔNIO LÍQUIDO", NEG)
put(ws, f"B{r}", f"=B{ref[('PL','TOTAL')]}+B{LIN_NC}", NEG, NUM)
put(ws, f"C{r}", f"=C{ref[('PL','TOTAL')]}+C{LIN_NC}", NEG, NUM)
LIN_PL = r
r += 2
put(ws, f"A{r}", "TOTAL DO PASSIVO E PL", NEG)
put(ws, f"B{r}", f"=B{ref[('PC','TOTAL')]}+B{ref[('PNC','TOTAL')]}+B{LIN_PL}", NEG, NUM)
put(ws, f"C{r}", f"=C{ref[('PC','TOTAL')]}+C{ref[('PNC','TOTAL')]}+C{LIN_PL}", NEG, NUM)
put(ws, f"G{r}", f'=IF(AND(B{r}=B{LIN_ATIVO},C{r}=C{LIN_ATIVO}),"Ativo = Passivo + PL","DIFERENÇA")')
LIN_PASSIVO = r
for row in range(6, r + 1):
    if ws[f"B{row}"].value is not None and ws[f"C{row}"].value is not None:
        put(ws, f"D{row}", f"=B{row}-C{row}", PRETO, NUM)
        put(ws, f"E{row}", f'=IF(C{row}=0,"",D{row}/C{row})', PRETO, PCT)
        base = LIN_ATIVO if row <= LIN_ATIVO else LIN_PASSIVO
        put(ws, f"F{row}", f"=B{row}/B${base}", PRETO, PCT)
ws.freeze_panes = "B6"
BP_INT = ref[("ANC", "Intangível")]


def bp(chave, nome, col="B"):
    return f"BP!{col}{ref[(chave, nome)]}"


# ---------------------------------------------------------------- DRE
ws = aba("DRE", "Demonstração do resultado consolidada (R$ mil) - PT 520 / PT PA-01", [58, 16, 16, 16, 11, 11])
put(ws, "A3", f"Fonte: {dp.FONTE_DRE}. 'Outros custos e despesas' 2024 inclui (936) de material para "
              "energia elétrica, apresentado em linha separada no release.", AZUL)
cab(ws, 5, ["Rubrica", "2025", "2024", "Variação R$", "Variação %", "AV % da ROL 2025"])
dre_ref = {}
for i, (nome, v25, v24) in enumerate(dp.DRE):
    rr = 6 + i
    dre_ref[nome.strip()] = rr
    put(ws, f"A{rr}", nome, NEG if not nome.startswith("  ") else PRETO)
    put(ws, f"B{rr}", v25, AZUL, NUM)
    put(ws, f"C{rr}", v24, AZUL, NUM)
for nome, ini, fim in [("Receita operacional líquida", 1, 7), ("Custos e despesas operacionais", 9, 18)]:
    rr = dre_ref[nome]
    for col in "BC":
        put(ws, f"{col}{rr}", f"=SUM({col}{6+ini}:{col}{6+fim})", NEG, NUM)
for col in "BC":
    put(ws, f"{col}{dre_ref['Lucro antes do resultado financeiro e dos tributos']}",
        f"={col}{dre_ref['Receita operacional líquida']}+{col}{dre_ref['Custos e despesas operacionais']}"
        f"+{col}{dre_ref['Resultado de equivalência patrimonial']}", NEG, NUM)
    put(ws, f"{col}{dre_ref['Resultado financeiro']}",
        f"={col}{dre_ref['Receitas financeiras']}+{col}{dre_ref['Despesas financeiras']}", NEG, NUM)
    put(ws, f"{col}{dre_ref['Lucro antes do IR e da CSLL']}",
        f"={col}{dre_ref['Lucro antes do resultado financeiro e dos tributos']}+{col}{dre_ref['Resultado financeiro']}",
        NEG, NUM)
    put(ws, f"{col}{dre_ref['Lucro líquido das operações continuadas']}",
        f"={col}{dre_ref['Lucro antes do IR e da CSLL']}+{col}{dre_ref['IR e CSLL (correntes e diferidos)']}", NEG, NUM)
    put(ws, f"{col}{dre_ref['Lucro líquido do exercício']}",
        f"={col}{dre_ref['Lucro líquido das operações continuadas']}+{col}{dre_ref['Lucro líquido das operações descontinuadas']}",
        NEG, NUM)
fim_dre = 6 + len(dp.DRE) - 1
for rr in range(6, fim_dre + 1):
    put(ws, f"D{rr}", f"=B{rr}-C{rr}", PRETO, NUM)
    put(ws, f"E{rr}", f'=IF(C{rr}=0,"",D{rr}/ABS(C{rr}))', PRETO, PCT)
    put(ws, f"F{rr}", f"=B{rr}/B${dre_ref['Receita operacional líquida']}", PRETO, PCT)
rr = fim_dre + 2
put(ws, f"A{rr}", "Checagem: lucro líquido continuado publicado (2.669.041 / 2.307.799)", NEG)
put(ws, f"B{rr}", f'=IF(B{dre_ref["Lucro líquido das operações continuadas"]}=2669041,"Confere","DIFERENÇA")')
put(ws, f"C{rr}", f'=IF(C{dre_ref["Lucro líquido das operações continuadas"]}=2307799,"Confere","DIFERENÇA")')
put(ws, f"A{rr+1}", "EBITDA publicado (R$ mil)", PRETO)
put(ws, f"B{rr+1}", dp.EBITDA[0], AZUL, NUM)
put(ws, f"C{rr+1}", dp.EBITDA[1], AZUL, NUM)
put(ws, f"A{rr+2}", "EBITDA recalculado = EBIT + depreciação e amortização (diferença = itens de ajuste da companhia)")
for col in "BC":
    put(ws, f"{col}{rr+2}", f"={col}{dre_ref['Lucro antes do resultado financeiro e dos tributos']}"
                            f"-{col}{dre_ref['Depreciação e amortização']}", PRETO, NUM)
    put(ws, f"{col}{rr+3}", f"={col}{rr+1}-{col}{rr+2}", PRETO, NUM)
put(ws, f"A{rr+3}", "Diferença (EBITDA publicado - recalculado): zero indica que o EBITDA publicado reconcilia com EBIT + D&A")


def dre(nome, col="B"):
    return f"DRE!{col}{dre_ref[nome]}"


# ---------------------------------------------------------------- Indicadores
ws = aba("Indicadores", "Indicadores analíticos - PT 520 / PT 570", [62, 14, 14, 60])
cab(ws, 4, ["Indicador", "2025", "2024", "Fórmula / leitura"])
ind = [
    ("Liquidez corrente (AC / PC)", f"={bp('AC','TOTAL')}/{bp('PC','TOTAL')}",
     f"={bp('AC','TOTAL','C')}/{bp('PC','TOTAL','C')}", "0.00", "Abaixo de 1,0 em 2025 - ver PT 570."),
    ("Endividamento bruto (empréstimos + debêntures)",
     f"={bp('PC','Empréstimos e financiamentos')}+{bp('PC','Debêntures')}+{bp('PNC','Empréstimos e financiamentos')}+{bp('PNC','Debêntures')}",
     f"={bp('PC','Empréstimos e financiamentos','C')}+{bp('PC','Debêntures','C')}+{bp('PNC','Empréstimos e financiamentos','C')}+{bp('PNC','Debêntures','C')}",
     NUM, "R$ mil. A companhia informa dívida bruta de R$ 20.038,9 mi (inclui efeito de swap)."),
    ("Dívida bruta / PL", "=B6/BP!B" + str(LIN_PL), "=C6/BP!C" + str(LIN_PL), "0.00", ""),
    ("Margem EBITDA (EBITDA / ROL)", f"=DRE!B{rr+1}/{dre('Receita operacional líquida')}",
     f"=DRE!C{rr+1}/{dre('Receita operacional líquida','C')}", PCT, "Release informa 25,0% e 24,4%."),
    ("Margem líquida continuada", f"={dre('Lucro líquido das operações continuadas')}/{dre('Receita operacional líquida')}",
     f"={dre('Lucro líquido das operações continuadas','C')}/{dre('Receita operacional líquida','C')}", PCT, ""),
    ("ROE simples (LL continuado / PL final)", f"={dre('Lucro líquido das operações continuadas')}/BP!B{LIN_PL}",
     f"={dre('Lucro líquido das operações continuadas','C')}/BP!C{LIN_PL}", PCT,
     "Release usa PL médio/critério próprio (10,5%)."),
    ("Prazo médio de recebimento (clientes CP+LP / ROL x 365)",
     f"=({bp('AC','Clientes')}+{bp('RLP','Clientes')})/{dre('Receita operacional líquida')}*365",
     f"=({bp('AC','Clientes','C')}+{bp('RLP','Clientes','C')})/{dre('Receita operacional líquida','C')}*365",
     "0", "Dias. ROL é líquida de tributos: indicador aproximado."),
    ("Intangível / ativo total", f"={bp('ANC','Intangível')}/BP!B{LIN_ATIVO}",
     f"={bp('ANC','Intangível','C')}/BP!C{LIN_ATIVO}", PCT, "Conta de maior saldo do ativo (PT BS-01)."),
    ("Amortização+depreciação / (imobilizado+intangível) inicial",
     f"=-{dre('Depreciação e amortização')}/({bp('ANC','Imobilizado','C')}+{bp('ANC','Intangível','C')})", "",
     PCT, "Taxa média implícita - comparação com taxas regulatórias."),
    ("Provisões para litígios: variação %", f"=({bp('PNC','Provisões para litígios e outras provisões')}/{bp('PNC','Provisões para litígios e outras provisões','C')})-1",
     "", PCT, "Quase dobrou (+102%) - risco significativo (PT 315.2)."),
]
for i, (nome, f25, f24, fmt, obs) in enumerate(ind):
    rr2 = 5 + i
    put(ws, f"A{rr2}", nome)
    put(ws, f"B{rr2}", f25, VERDE, fmt)
    if f24:
        put(ws, f"C{rr2}", f24, VERDE, fmt)
    put(ws, f"D{rr2}", obs)

# ---------------------------------------------------------------- Materialidade
ws = aba("Materialidade", "Materialidade - PT 320 (NBC TA 320 (R1), itens 10, 11 e 14)", [62, 18, 12, 18, 60])
cab(ws, 4, ["Referencial (2025)", "Valor (R$ mil)", "% aplicado", "Resultado (R$ mil)", "Comentário"])
refs = [
    ("Lucro antes do IR e CSLL - operações continuadas", f"={dre('Lucro antes do IR e da CSLL')}", 0.05,
     "ESCOLHIDO: entidade com fins lucrativos, lucro estável e foco dos usuários (dividendos, payout)."),
    ("Receita operacional líquida", f"={dre('Receita operacional líquida')}", 0.005,
     "Alternativo: receita inclui repasses (energia comprada, construção) sem margem."),
    ("Patrimônio líquido", f"=BP!B{LIN_PL}", 0.01, "Alternativo."),
    ("Ativo total", f"=BP!B{LIN_ATIVO}", 0.005, "Alternativo: intensivo em ativos regulados."),
    ("EBITDA", f"=DRE!B{rr+1}", 0.03, "Alternativo: métrica usada pelo mercado e por covenants."),
]
for i, (nome, f, pct, com) in enumerate(refs):
    rr2 = 5 + i
    put(ws, f"A{rr2}", nome)
    put(ws, f"B{rr2}", f, VERDE, NUM)
    put(ws, f"C{rr2}", pct, AZUL, PCT, AMARELO)
    put(ws, f"D{rr2}", f"=B{rr2}*C{rr2}", PRETO, NUM)
    put(ws, f"E{rr2}", com)
put(ws, "A12", "Materialidade global (MG) - arredondada", NEG)
put(ws, "B12", "=ROUND(D5,0)", NEG, NUM)
put(ws, "A13", "% para materialidade de execução (ME)", PRETO)
put(ws, "B13", 0.70, AZUL, PCT, AMARELO, "Julgamento: 2º ano da firma no cliente, controles atestados (SOX), "
                                        "mas este trabalho não testou controles - 70%.")
put(ws, "A14", "Materialidade para execução (ME)", NEG)
put(ws, "B14", "=ROUND(B12*B13,0)", NEG, NUM)
put(ws, "A15", "% limite de distorção claramente trivial", PRETO)
put(ws, "B15", 0.05, AZUL, PCT, AMARELO)
put(ws, "A16", "Limite claramente trivial", NEG)
put(ws, "B16", "=ROUND(B12*B15,0)", NEG, NUM)
put(ws, "A17", "MG em % do lucro líquido continuado")
put(ws, "B17", f"=B12/{dre('Lucro líquido das operações continuadas')}", PRETO, PCT)
put(ws, "A18", "MG em % do ativo total")
put(ws, "B18", f"=B12/BP!B{LIN_ATIVO}", PRETO, PCT)
put(ws, "A20", "Materialidade específica (menor) - remuneração do pessoal-chave e partes relacionadas: "
               "avaliação qualitativa, qualquer distorção é relevante por natureza (NBC TA 320, item 10).")
put(ws, "A21", "Checagem com o código Python (02_testes_auditoria.py): MG / ME / trivial", NEG)
put(ws, "B21", RES["parametros"]["materialidade_global_R$mil"], AZUL, NUM)
put(ws, "C21", RES["parametros"]["materialidade_execucao_R$mil"], AZUL, NUM)
put(ws, "D21", RES["parametros"]["trivial_R$mil"], AZUL, NUM)
put(ws, "E21", '=IF(AND(B21=B12,C21=B14,D21=B16),"Planilha = código","DIVERGÊNCIA")')

# ---------------------------------------------------------------- Contas significativas
ws = aba("Contas_Significativas", "Contas acima da materialidade de execução - PT 315.2 / PT 330", [58, 16, 16, 22, 40])
cab(ws, 4, ["Rubrica", "31/12/2025", "|Var| R$", "Classificação", "Grupo"])
rr2 = 5
for chave, itens, grupo in [("AC", dp.ATIVO_CIRCULANTE, "Ativo circulante"), ("RLP", dp.REALIZAVEL_LP, "Realizável LP"),
                            ("ANC", dp.ATIVO_NC_OUTROS, "Ativo não circulante"), ("PC", dp.PASSIVO_CIRCULANTE, "Passivo circulante"),
                            ("PNC", dp.PASSIVO_NAO_CIRCULANTE, "Passivo não circulante")]:
    for nome, _, _ in itens:
        put(ws, f"A{rr2}", nome)
        put(ws, f"B{rr2}", f"={bp(chave, nome)}", VERDE, NUM)
        put(ws, f"C{rr2}", f"=ABS({bp(chave, nome)}-{bp(chave, nome, 'C')})", VERDE, NUM)
        put(ws, f"D{rr2}", f'=IF(OR(ABS(B{rr2})>=Materialidade!$B$14,C{rr2}>=Materialidade!$B$14),'
                           f'"Significativa (>= ME)","Abaixo da ME")')
        put(ws, f"E{rr2}", grupo)
        rr2 += 1
put(ws, f"A{rr2+1}", "Contas significativas (contagem)", NEG)
put(ws, f"B{rr2+1}", f'=COUNTIF(D5:D{rr2-1},"Significativa (>= ME)")', NEG)

# ---------------------------------------------------------------- Conciliação Intangível
ws = aba("Conciliacao_Intangivel", "Conciliação da base SINTÉTICA com o saldo contábil - PT BS-04", [16, 62, 12, 20, 20, 20])
put(ws, "A3", "DADOS SINTÉTICOS: totais por subconta extraídos de 04_RESULTADOS_TESTES/resultados_testes.json (T01). "
              "Categorias da NE 16 (F17) e subtotal GeT (F15) são reais; divisão interna da geração é hipótese (PT BS-02).", AZUL)
cab(ws, 5, ["Subconta", "Descrição", "Linhas", "Custo (R$)", "Amortização (R$)", "Valor líquido (R$)"])
desc = {"INT-UBE": "Geração fora da Copel GeT (Elejor e outras) - por diferença F17-F15",
        "INT-AUO": "Direito de autorização - demais empresas - por diferença F17-F15",
        "INT-DIS": "Contrato de concessão - distribuição (real: F17)", "INT-BON": "Bônus de outorga - usinas renovadas",
        "INT-GSF": "Repactuação do risco hidrológico (GSF)", "INT-UBP": "Uso do bem público (UBP)",
        "INT-EOL": "Direito de concessão e autorização / ágio técnico - eólicas (real: F15)",
        "INT-CNB": "Combinação de negócios (UHE Mauá)", "INT-SGT": "Softwares e outros - Copel GeT (real: F15)",
        "INT-SOF": "Softwares e outros - demais empresas"}
for i, s in enumerate(RES["T01"]["por_subconta"]):
    rr2 = 6 + i
    put(ws, f"A{rr2}", s["codigo_subconta"])
    put(ws, f"B{rr2}", desc[s["codigo_subconta"]])
    put(ws, f"C{rr2}", s["linhas"], AZUL, NUM)
    put(ws, f"D{rr2}", s["custo"], AZUL, NUM2)
    put(ws, f"E{rr2}", s["amortizacao"], AZUL, NUM2)
    put(ws, f"F{rr2}", s["liquido"], AZUL, NUM2)
fim = 6 + len(RES["T01"]["por_subconta"]) - 1
t = fim + 1
put(ws, f"B{t}", "Total da base sintética", NEG)
for col, f in [("C", NUM), ("D", NUM2), ("E", NUM2), ("F", NUM2)]:
    put(ws, f"{col}{t}", f"=SUM({col}6:{col}{fim})", NEG, f)
put(ws, f"B{t+1}", "Saldo contábil - Intangível consolidado 31/12/2025 (R$ mil x 1.000)", NEG)
put(ws, f"F{t+1}", f"=BP!B{BP_INT}*1000", VERDE, NUM2)
put(ws, f"B{t+2}", "Diferença (base - contábil)", NEG)
put(ws, f"F{t+2}", f"=ROUND(F{t}-F{t+1},2)", NEG, NUM2)
put(ws, f"B{t+3}", "Conclusão", NEG)
put(ws, f"F{t+3}", f'=IF(F{t+2}=0,"Conciliado sem diferença","Investigar diferença")')
put(ws, f"B{t+5}", "Âncora verificável: Intangível da controlada F.D.A. (F07, p. 8) alocado ao registro "
                    "de Foz do Areia na base (R$ mil)")
put(ws, f"F{t+5}", dp.FDA_INTANGIVEL_RS_MIL, AZUL, NUM)
put(ws, f"B{t+6}", "Variação do intangível no exercício (R$ mil) - movimentação a obter na nota explicativa (P)")
put(ws, f"F{t+6}", f"=BP!B{BP_INT}-BP!C{BP_INT}", VERDE, NUM)
# conciliação por categoria da NE 16 (F17)
r0 = t + 13
cab(ws, r0, ["Categoria NE 16", "", "", "Base (R$)", "NE 16 - F17 (R$)", "Diferença"])
for i, c in enumerate(RES["T01_NE16"]):
    rr_ = r0 + 1 + i
    put(ws, f"A{rr_}", c["categoria"])
    put(ws, f"D{rr_}", c["base_R$"], AZUL, NUM2)
    put(ws, f"E{rr_}", c["nota16_R$"], AZUL, NUM2)
    put(ws, f"F{rr_}", f"=ROUND(D{rr_}-E{rr_},2)", PRETO, NUM2)
rm = r0 + 7
put(ws, f"A{rm}", "Movimentação real do intangível 2025 - F17, NE 16, p. 91 (R$ mil)", NEG)
for i, (n_, v_) in enumerate(dp.NE16_MOVIMENTO_2025):
    put(ws, f"A{rm+1+i}", n_)
    put(ws, f"F{rm+1+i}", v_, AZUL, NUM)
fm = rm + 1 + len(dp.NE16_MOVIMENTO_2025)
put(ws, f"A{fm}", "Saldo recalculado em 31.12.2025", NEG)
put(ws, f"F{fm}", f"=SUM(F{rm+1}:F{fm-1})", NEG, NUM)
put(ws, f"A{fm+1}", "Confere com o balanço?")
put(ws, f"F{fm+1}", f'=IF(F{fm}=BP!B{BP_INT},"Confere","DIFERENÇA")')
put(ws, f"B{t+8}", "Subtotal do segmento Copel GeT na base (R$)")
put(ws, f"F{t+8}", RES["T01_GeT"]["base_segmento_GeT_R$"], AZUL, NUM2)
put(ws, f"B{t+9}", "Intangível consolidado da Copel GeT em 31/12/2025 - F15, ITR 1T26, NE 15, p. 21 (R$)")
put(ws, f"F{t+9}", 7150619000, AZUL, NUM2)
put(ws, f"B{t+10}", "Diferença (base - F15)")
put(ws, f"F{t+10}", f"=ROUND(F{t+8}-F{t+9},2)", PRETO, NUM2)
put(ws, f"B{t+7}", "Adições ao intangível na DFC (R$ mil) - a diferença indica transferências de ativos de "
                    "contrato e combinação de negócios (sem efeito caixa)")
put(ws, f"F{t+7}", 43788, AZUL, NUM)

# ---------------------------------------------------------------- MUS
T11 = RES["T11"]
ws = aba("MUS_Parametros", "Amostragem por unidade monetária - parâmetros (SIMULADO) - PT 530", [62, 22, 50])
linhas = [
    ("Valor contábil da população com saldo positivo (R$)", T11["populacao_valor_positivo_R$"], AZUL, NUM2, "Base sintética, T11."),
    ("Distorção tolerável (R$) = ME x 1.000", "=Materialidade!B14*1000", VERDE, NUM2, "Vinculada à materialidade de execução."),
    ("% distorção esperada sobre a tolerável", 0.10, AZUL, PCT, "Premissa (fill amarelo)."),
    ("Distorção esperada (R$)", "=B6*B7", PRETO, NUM2, ""),
    ("Fator de confiabilidade (95%, zero erros)", T11["fator_confiabilidade_95%"], AZUL, "0.0000", "Poisson."),
    ("Fator de expansão", 1.6, AZUL, "0.00", "Tabela AICPA, 95%."),
    ("Tamanho da amostra n", "=ROUNDUP(B5*B9/(B6-B8*B10),0)", PRETO, NUM, ""),
    ("Intervalo amostral J (R$)", "=B5/B11", PRETO, NUM2, ""),
    ("Início aleatório (R$) - semente 232025417", T11["inicio_aleatorio_R$"], AZUL, NUM2, ""),
    ("Checagem: n do código Python", T11["tamanho_amostra"], AZUL, NUM, ""),
    ("Conferência", '=IF(B11=B14,"Planilha = código","DIVERGÊNCIA")', PRETO, None, ""),
    ("Itens selecionados únicos (há itens maiores que J)", T11["itens_selecionados_unicos"], AZUL, NUM, ""),
    ("Itens-chave (valor >= J) - 100% examinados", T11["itens_chave"], AZUL, NUM, ""),
    ("Registros com valor <= 0 excluídos (testados por CAAT, T02)", T11["registros_negativos_excluidos"], AZUL, NUM,
     "Inclui bens totalmente amortizados (valor zero) e 40 negativos."),
]
for i, (a, b, fnt, fmt, c) in enumerate(linhas):
    rr2 = 5 + i
    put(ws, f"A{rr2}", a)
    put(ws, f"B{rr2}", b, fnt, fmt, AMARELO if rr2 in (7,) else None)
    put(ws, f"C{rr2}", c)

amostra = pd.read_csv(RAIZ / "04_RESULTADOS_TESTES" / "amostra_mus.csv")
ws = aba("MUS_Amostra", "Itens selecionados - inspeção SIMULADA (valor auditado vem do gabarito)", [16, 11, 46, 12, 18, 9, 18, 16, 12])
cab(ws, 4, ["id_registro (SINT)", "Subconta", "Tipo de bem", "Status", "Valor contábil (R$)", "Item-chave",
            "Valor auditado simulado (R$)", "Distorção (R$)", "Contaminação"])
for i, row in enumerate(amostra.itertuples(index=False)):
    rr2 = 5 + i
    put(ws, f"A{rr2}", row.id_registro)
    put(ws, f"B{rr2}", row.codigo_subconta)
    put(ws, f"C{rr2}", row.tipo_bem)
    put(ws, f"D{rr2}", row.status)
    put(ws, f"E{rr2}", float(row.valor_liquido), AZUL, NUM2)
    put(ws, f"F{rr2}", f'=IF(E{rr2}>=MUS_Parametros!$B$12,"SIM","NÃO")', VERDE)
    put(ws, f"G{rr2}", float(row.valor_auditado_simulado), AZUL, NUM2)
    put(ws, f"H{rr2}", f"=E{rr2}-G{rr2}", PRETO, NUM2)
    put(ws, f"I{rr2}", f'=IF(F{rr2}="SIM","",H{rr2}/E{rr2})', PRETO, "0.0000")
fim_a = 4 + len(amostra)

ws = aba("MUS_Avaliacao", "Avaliação da amostra MUS (SIMULADO) - PT 530 / PT 450", [70, 22, 50])
fat = [round(x, 4) for x in [2.9957, 4.7439, 6.2958, 7.7537, 9.1535, 10.5130, 11.8424, 13.1481]]
put(ws, "A4", "Fatores de Poisson 95% (k erros)", NEG)
for k, f in enumerate(fat):
    put(ws, f"A{5+k}", f"k = {k}")
    put(ws, f"B{5+k}", f, AZUL, "0.0000")
put(ws, "A14", "Itens não-chave com distorção (contagem)")
put(ws, "B14", f'=COUNTIFS(MUS_Amostra!F5:F{fim_a},"NÃO",MUS_Amostra!H5:H{fim_a},">0")', VERDE, NUM)
put(ws, "A15", "Soma das contaminações (superavaliação, não-chave)")
put(ws, "B15", f'=SUMIFS(MUS_Amostra!I5:I{fim_a},MUS_Amostra!F5:F{fim_a},"NÃO",MUS_Amostra!H5:H{fim_a},">0")', VERDE, "0.0000")
put(ws, "A16", "Distorção em itens-chave (R$)")
put(ws, "B16", f'=SUMIFS(MUS_Amostra!H5:H{fim_a},MUS_Amostra!F5:F{fim_a},"SIM")', VERDE, NUM2)
put(ws, "A17", "Precisão básica = J x fator(0)")
put(ws, "B17", "=MUS_Parametros!B12*B5", PRETO, NUM2)
put(ws, "A18", "Distorção projetada = soma contaminações x J + itens-chave")
put(ws, "B18", "=B15*MUS_Parametros!B12+B16", PRETO, NUM2)
put(ws, "A19", "Provisão incremental (contaminações = 1,0 ordenadas; fórmula válida para até 7 erros)")
put(ws, "B19", "=IF(B14=0,0,MUS_Parametros!B12*(INDEX(B5:B12,B14+1)-B5-B14))", PRETO, NUM2,
    comentario="Com contaminações todas iguais a 1,0: soma[(f(i)-f(i-1))-1] = f(k)-f(0)-k. Para contaminações "
               "diferentes, usar o cálculo ordenado do código Python.")
put(ws, "A20", "Limite superior de distorção (LSD)", NEG)
put(ws, "B20", "=B17+B18+B19", NEG, NUM2)
put(ws, "A21", "Distorção tolerável")
put(ws, "B21", "=MUS_Parametros!B6", VERDE, NUM2)
put(ws, "A22", "Conclusão (simulação)", NEG)
put(ws, "B22", '=IF(B20<B21,"LSD < tolerável: aceitar","LSD > tolerável: estender testes (100% via CAAT) e propor ajuste")')
put(ws, "A23", "Checagem LSD do código Python")
put(ws, "B23", T11["limite_superior_distorcao_R$"], AZUL, NUM2)
put(ws, "C23", '=IF(ABS(B23-B20)<1,"Planilha = código","DIVERGÊNCIA")')

# ---------------------------------------------------------------- Exceções
cmp_ = RES["comparacao"]
ws = aba("Excecoes", "Erros inseridos x exceções identificadas (SIMULADO) - PT BS-06", [10, 62, 12, 12, 14, 20, 14])
cab(ws, 4, ["Código", "Natureza do erro inserido", "Inseridos", "Detectados", "Taxa", "Distorção inserida (R$)",
            "Teste principal"])
nat = {"E01": "Registro duplicado", "E02": "Amortização acumulada > custo (líquido negativo)",
       "E03": "Capitalização após 31/12/2025 (corte)", "E04": "Em serviço sem amortização",
       "E05": "Taxa abaixo da mínima do prazo de concessão", "E06": "ODI/contrato em branco",
       "E07": "Lançamento manual fictício abaixo da alçada, fim do exercício", "E08": "Em curso com amortização",
       "E09": "Valor líquido diverge de custo - amortização"}
for i, m in enumerate(cmp_["matriz"]):
    rr2 = 5 + i
    put(ws, f"A{rr2}", m["codigo_erro"])
    put(ws, f"B{rr2}", nat[m["codigo_erro"]])
    put(ws, f"C{rr2}", m["inseridos"], AZUL, NUM)
    put(ws, f"D{rr2}", m["detectados"], AZUL, NUM)
    put(ws, f"E{rr2}", f"=D{rr2}/C{rr2}", PRETO, PCT)
    put(ws, f"F{rr2}", m["distorcao_inserida_R"], AZUL, NUM2)
    put(ws, f"G{rr2}", m["teste_principal"])
f = 5 + len(cmp_["matriz"])
put(ws, f"B{f}", "Total", NEG)
for col in "CDF":
    put(ws, f"{col}{f}", f"=SUM({col}5:{col}{f-1})", NEG, NUM2 if col == "F" else NUM)
put(ws, f"E{f}", f"=D{f}/C{f}", NEG, PCT)
put(ws, f"B{f+1}", "Falsos positivos (exceções sem erro inserido)")
put(ws, f"D{f+1}", cmp_["falsos_positivos"], AZUL, NUM)

# ---------------------------------------------------------------- Distorções
ws = aba("Distorcoes", "Sumário de distorções - PT 450 (NBC TA 450 (R1))", [62, 20, 20, 50])
put(ws, "A3", "Parte A - evidência pública: nenhuma distorção identificada (trabalho sem acesso a registros).", AZUL)
put(ws, "A4", "Parte B - SIMULADO: distorções identificadas na base sintética do intangível (CAAT 100%).", AZUL)
cab(ws, 6, ["Item", "Valor (R$ mil)", "Referência", "Comentário"])
put(ws, "A7", "Distorção factual identificada na base sintética (superavaliação líquida)")
put(ws, "B7", f"=Excecoes!F{f}/1000", VERDE, NUM2)
put(ws, "C7", "PT BS-06")
put(ws, "A8", "Limite claramente trivial")
put(ws, "B8", "=Materialidade!B16", VERDE, NUM)
put(ws, "A9", "Materialidade para execução")
put(ws, "B9", "=Materialidade!B14", VERDE, NUM)
put(ws, "A10", "Materialidade global")
put(ws, "B10", "=Materialidade!B12", VERDE, NUM)
put(ws, "A11", "Conclusão quantitativa", NEG)
put(ws, "B11", '=IF(B7<=B8,"Trivial",IF(B7<B9,"Acima do trivial e abaixo da ME: acumular e solicitar correção",'
               'IF(B7<B10,"Acima da ME: solicitar correção; avaliar efeito agregado","Relevante")))')
put(ws, "A12", "Aspecto qualitativo: E07 tem natureza de fraude (lançamentos fictícios) - relevante por natureza, "
               "comunicar à governança (NBC TA 240/260) independentemente do valor.")

# ---------------------------------------------------------------- Analíticos
ws = aba("Analiticos", "Procedimentos analíticos e reconciliações - PT 520 / PT 540", [70, 18, 18, 50])
cab(ws, 4, ["Item", "Valor A", "Valor B", "Resultado / leitura"])
an = [
    ("Provisões para litígios no balanço (R$ mil) x provisão para processos judiciais no 20-F (R$ mi x 1.000)",
     f"={bp('PNC','Provisões para litígios e outras provisões')}", dp.PROVISAO_PROCESSOS_JUDICIAIS_RS_MI * 1000,
     "=B5-C5", "Explicada: a linha inclui contraprestação contingente de R$ 362.465 mil (F17, NE 26, p. 105) - ver linha 12."),
    ("Receita de construção x custo de construção (margem ICPC 01)", f"={dre('Receita de construção')}",
     f"=-{dre('Custo de construção')}", "=B6-C6", "Margem pequena: coerente com reconhecimento a custo + margem."),
    ("Resultado de ativos/passivos setoriais (CVA): variação 2025/2024", f"={dre('Resultado de ativos e passivos financeiros setoriais')}",
     f"={dre('Resultado de ativos e passivos financeiros setoriais','C')}", "=B7/C7-1",
     "Aumento de 180%: estimativa regulatória - risco significativo."),
    ("Energia comprada para revenda: variação", f"={dre('Energia elétrica comprada para revenda')}",
     f"={dre('Energia elétrica comprada para revenda','C')}", "=B8/C8-1", "Crescimento compatível com volumes da Copel Com."),
    ("Despesas financeiras: variação", f"={dre('Despesas financeiras')}", f"={dre('Despesas financeiras','C')}",
     "=B9/C9-1", "Aumento de dívida e Selic 15% (F02, p. 15)."),
    ("Expectativa de despesa financeira: dívida média x custo médio 13,22% (R$ mil)",
     f"=(Indicadores!B6+Indicadores!C6)/2*0.1322", f"=-{dre('Despesas financeiras')}", "=C10/B10-1",
     "Despesa registrada vs. expectativa (dívida média x custo nominal informado). Diferença inclui outros itens."),
    ("Dividendos mínimos a pagar 31/12/2025 x proventos declarados no 4T25 (R$ mi 1.350 + 1.100)",
     f"={bp('PC','Dividendos mínimos obrigatórios a pagar')}", 2450000, "=B11-C11",
     "IRRF sobre JCP (R$ 168.009 mil, F17 NE 12.2) explica a direção; resíduo de R$ 43.898 mil em aberto (Expectativas_520)."),
    ("Diferença de provisões menos contraprestação contingente (F17, NE 26.3)", "=D5", 362465, "=B12-C12",
     "Resíduo de arredondamento (20-F informa R$ milhões com uma casa)."),
    ("Vencidos líquidos de PECLD (R$ mi, F02 p.5) / clientes CP", dp.VENCIDOS_LIQUIDOS_PECLD_RS_MI * 1000,
     f"={bp('AC','Clientes')}", "=B13/C13", "Proporção dos vencidos no saldo de clientes."),
]
for i, (a, b, c, d, e) in enumerate(an):
    rr2 = 5 + i
    put(ws, f"A{rr2}", a)
    put(ws, f"B{rr2}", b, VERDE if isinstance(b, str) else AZUL, NUM)
    put(ws, f"C{rr2}", c, VERDE if isinstance(c, str) else AZUL, NUM)
    put(ws, f"D{rr2}", d, PRETO, NUM if i in (0, 1, 6, 7) else PCT)
    put(ws, f"E{rr2}", e)
ws.column_dimensions["E"].width = 70

# ---------------------------------------------------------------- Continuidade
ws = aba("Continuidade", "Continuidade operacional - PT 570 (NBC TA 570)", [55, 18, 50])
cab(ws, 4, ["Item", "R$ milhões", "Fonte / leitura"])
cont = [("Caixa e aplicações (release, seção 1.7)", dp.CRONOGRAMA_AMORTIZACAO_RS_MI["Caixa"], "F01, p. 8"),
        ("Amortizações de dívida em 2026", dp.CRONOGRAMA_AMORTIZACAO_RS_MI["2026"], "F01, p. 8"),
        ("Amortizações de dívida em 2027", dp.CRONOGRAMA_AMORTIZACAO_RS_MI["2027"], "F01, p. 8")]
for i, (a, b, c) in enumerate(cont):
    put(ws, f"A{5+i}", a)
    put(ws, f"B{5+i}", b, AZUL, NUM)
    put(ws, f"C{5+i}", c)
put(ws, "A8", "Cobertura de 2026 (caixa / amortizações 2026)", NEG)
put(ws, "B8", "=B5/B6", NEG, "0.00x")
put(ws, "A9", "Fluxo de caixa operacional 2025 (R$ mi)")
put(ws, "B9", 3028.446, AZUL, NUM, comentario="F01, Anexo I, DFC, p. 25: R$ 3.028.446 mil.")
put(ws, "A10", "Alavancagem dívida líquida/EBITDA (faixa-alvo 2,5x a 3,1x)")
put(ws, "B10", dp.ALAVANCAGEM[0], AZUL, "0.0x")
put(ws, "A11", "Liquidez corrente")
put(ws, "B11", "=Indicadores!B5", VERDE, "0.00")
put(ws, "A12", "Leitura", NEG)
put(ws, "B12", '=IF(AND(B8>1,B10<=3.1),"Sem indício de incerteza relevante com dados públicos","Aprofundar")')

# ---------------------------------------------------------------- Expectativas (PT 520)
ws = aba("Expectativas_520", "Expectativas analíticas com limite de investigação - PT 520 (NBC TA 520, item 5)",
         [48, 18, 18, 18, 18, 46])
put(ws, "A3", "Limite de investigação = materialidade de execução", NEG)
put(ws, "B3", "=Materialidade!B14", VERDE, NUM)
cab(ws, 5, ["Item", "Esperado (R$ mil)", "Registrado (R$ mil)", "Diferença", "Investigar?", "Base da expectativa"])
put(ws, "A6", "Custo nominal médio da dívida (F01, p. 7)")
put(ws, "B6", 0.1322, AZUL, PCT, AMARELO)
linhas_e = [
    ("Despesa financeira", "=(Indicadores!B6+Indicadores!C6)/2*B6", f"=-{dre('Despesas financeiras')}",
     "Dívida média (empréstimos + debêntures) x custo nominal"),
    ("Depreciação e amortização",
     f"=-{dre('Depreciação e amortização','C')}/({bp('ANC','Imobilizado','C')}+{bp('ANC','Intangível','C')})"
     f"*(({bp('ANC','Imobilizado','C')}+{bp('ANC','Intangível','C')})+({bp('ANC','Imobilizado')}+{bp('ANC','Intangível')}))/2",
     f"=-{dre('Depreciação e amortização')}", "Taxa implícita 2024 x base média 2025 (imobilizado + intangível)"),
    ("Receita de construção", f"=-{dre('Custo de construção')}*({dre('Receita de construção','C')}/-{dre('Custo de construção','C')})",
     f"={dre('Receita de construção')}", "Custo 2025 x (1 + margem 2024)"),
    ("Dividendos mínimos a pagar", 2450000, f"={bp('PC','Dividendos mínimos obrigatórios a pagar')}",
     "Proventos declarados no 4T25: R$ 1,35 bi dividendos + R$ 1,1 bi JCP (F01, p. 1; F06)"),
]
for i, (a, b, c, d) in enumerate(linhas_e):
    r_ = 7 + i
    put(ws, f"A{r_}", a)
    put(ws, f"B{r_}", b, VERDE if isinstance(b, str) else AZUL, NUM)
    put(ws, f"C{r_}", c, VERDE, NUM)
    put(ws, f"D{r_}", f"=C{r_}-B{r_}", PRETO, NUM)
    put(ws, f"E{r_}", f'=IF(ABS(D{r_})>$B$3,"Sim - investigar","Não")')
    put(ws, f"F{r_}", d)

# investigação das diferenças com as notas da holding (F17)
put(ws, "A13", "Investigação das diferenças com as notas explicativas (F17)", NEG)
cab(ws, 14, ["Item", "Esperado (R$ mil)", "Registrado (R$ mil)", "Diferença", "Investigar?", "Fonte / leitura"])
put(ws, "A15", "Encargos e variação monetária da dívida x expectativa")
put(ws, "B15", "=B7", VERDE, NUM)
put(ws, "C15", 2490902, AZUL, NUM)
put(ws, "D15", "=C15-B15", PRETO, NUM)
put(ws, "E15", '=IF(ABS(D15)>$B$3,"Sim - investigar","Não")')
put(ws, "F15", "F17, NE 30, p. 117: a parcela da dívida fica perto da expectativa")
put(ws, "A16", "Demais despesas financeiras (fora da dívida)")
put(ws, "C16", "=C7-C15", VERDE, NUM)
put(ws, "F16", "PIS/Cofins s/ JCP 129.067; concessões 157.858; CVA 77.774; PIS/Cofins 64.510; litígios 63.304; outros")
put(ws, "A17", "Dividendos a pagar: proventos - IRRF sobre JCP")
put(ws, "B17", "=2450000-168009", VERDE, NUM)
put(ws, "C17", "=C10", VERDE, NUM)
put(ws, "D17", "=C17-B17", PRETO, NUM)
put(ws, "E17", '=IF(ABS(D17)>$B$3,"Sim - investigar","Não")')
put(ws, "F17", "IRRF s/ JCP R$ 168.009 mil em outras obrigações fiscais (F17, NE 12.2, p. 81); resíduo não explicado")

# ---------------------------------------------------------------- Sensibilidade (PT 540)
ws = aba("Sensibilidade_540", "Sensibilidade da PECLD à cobertura dos vencidos - PT 540 (R$ milhões)", [52, 18, 18, 30])
put(ws, "A4", "Vencidos líquidos de PECLD (F02, Item 3, p. 5)")
put(ws, "B4", dp.VENCIDOS_LIQUIDOS_PECLD_RS_MI, AZUL, "#,##0.0")
put(ws, "A5", "PECLD registrada (F02, Item 3, p. 5)")
put(ws, "B5", dp.PECLD_RS_MI, AZUL, "#,##0.0")
put(ws, "A6", "Vencidos brutos (premissa: PECLD refere-se aos vencidos)")
put(ws, "B6", "=B4+B5", PRETO, "#,##0.0")
put(ws, "A7", "Cobertura atual")
put(ws, "B7", "=B5/B6", PRETO, PCT)
put(ws, "A8", "Materialidade de execução (R$ mi)")
put(ws, "B8", "=Materialidade!B14/1000", VERDE, "#,##0.0")
put(ws, "A9", "Materialidade global (R$ mi)")
put(ws, "B9", "=Materialidade!B12/1000", VERDE, "#,##0.0")
cab(ws, 11, ["Cenário de cobertura", "PECLD no cenário", "Variação", "Comparação"])
for i, c in enumerate([0.20, 0.35, 0.40, 0.50]):
    r_ = 12 + i
    put(ws, f"A{r_}", c, AZUL, PCT, AMARELO)
    put(ws, f"B{r_}", f"=$B$6*A{r_}", PRETO, "#,##0.0")
    put(ws, f"C{r_}", f"=B{r_}-$B$5", PRETO, "#,##0.0;(#,##0.0)")
    put(ws, f"D{r_}", f'=IF(ABS(C{r_})>$B$9,"Acima da global",IF(ABS(C{r_})>$B$8,"Acima da ME","Abaixo da ME"))')
put(ws, "A17", "Cobertura que gera variação igual à materialidade global")
put(ws, "B17", "=(B5+B9)/B6", PRETO, PCT)

# ---------------------------------------------------------------- Grupo (PT 600)
ws = aba("Grupo_600", "Componentes e materialidade dos componentes - PT 600 (R$ mil)", [46, 18, 14, 18, 16])
put(ws, "A4", "Materialidade de execução do grupo")
put(ws, "B4", "=Materialidade!B14", VERDE, NUM)
cab(ws, 6, ["Componente", "Receita líquida antes de eliminações (F01, Anexo II)", "% da soma", "% da ME do grupo",
            "Materialidade do componente"])
compo = [("Copel DIS", 19202210, 0.75), ("Copel GeT - geração", 2253075, 0.65), ("Copel GeT - transmissão", 1097358, 0.65),
         ("Copel Comercialização", 4402327, 0.40), ("Parques eólicos", 877553, 0.25), ("F.D.A.", 598908, 0.25),
         ("Elejor", 153989, 0.25), ("C. Oeste, Marumbi, Uirapuru", 303765, 0.25), ("Bela Vista", 39744, 0.25),
         ("Pequenos ativos", 27740, 0.25), ("Copel Serviços", 12128, 0.25)]
for i, (n, v, pc) in enumerate(compo):
    r_ = 7 + i
    put(ws, f"A{r_}", n)
    put(ws, f"B{r_}", v, AZUL, NUM)
    put(ws, f"C{r_}", f"=B{r_}/$B${7+len(compo)}", PRETO, PCT)
    put(ws, f"D{r_}", pc, AZUL, PCT, AMARELO)
    put(ws, f"E{r_}", f"=ROUND($B$4*D{r_},0)", PRETO, NUM)
t_ = 7 + len(compo)
put(ws, f"A{t_}", "Soma dos componentes", NEG)
put(ws, f"B{t_}", f"=SUM(B7:B{t_-1})", NEG, NUM)
put(ws, f"A{t_+1}", "Eliminações (F01, Anexo II)")
put(ws, f"B{t_+1}", -2851941, AZUL, NUM)
put(ws, f"A{t_+2}", "Receita consolidada (soma + eliminações)", NEG)
put(ws, f"B{t_+2}", f"=B{t_}+B{t_+1}", NEG, NUM)
put(ws, f"C{t_+2}", f'=IF(B{t_+2}={dre("Receita operacional líquida")},"Confere com DRE","DIFERENÇA")')
put(ws, f"A{t_+3}", "Cobertura DIS + GeT (auditoria completa)")
put(ws, f"B{t_+3}", "=SUM(C7:C9)", PRETO, PCT)

# ---------------------------------------------------------------- Matriz
ws = aba("Matriz_Cobertura", "Matriz de cobertura das normas - PT MC", [28, 18, 18, 60, 30, 30])
cab(ws, 4, ["Norma", "Versão (2025)", "Publicação", "Título", "PT principais", "PT de apoio"])
for i, (cod, versao, pub, titulo, princ, sec) in enumerate(ep.matriz_cobertura()):
    rr2 = 5 + i
    for j, v in enumerate([cod, versao, pub, titulo, ", ".join(princ), ", ".join(sec)], 1):
        c = ws.cell(rr2, j, v)
        c.font, c.border = PRETO, BORDA
        c.alignment = Alignment(wrap_text=True, vertical="top")
put(ws, f"A{rr2+2}", "Normas sem PT principal (contagem)", NEG)
put(ws, f"B{rr2+2}", f'=COUNTIF(E5:E{rr2},"")', NEG)

# ---------------------------------------------------------------- Fontes
ws = aba("Fontes", "Relação de fontes (detalhe em 06_FONTES_E_COBERTURA/fontes.md)", [8, 70, 90])
fontes = [l for l in (RAIZ / "06_FONTES_E_COBERTURA" / "fontes.md").read_text().splitlines() if l.startswith("| F")]
cab(ws, 4, ["ID", "Documento", "Endereço eletrônico / páginas / exercício / acesso"])
for i, l in enumerate(fontes):
    partes = [p.strip() for p in l.strip("|").split("|")]
    put(ws, f"A{5+i}", partes[0])
    put(ws, f"B{5+i}", partes[1])
    put(ws, f"C{5+i}", " | ".join(partes[2:]))
    ws[f"B{5+i}"].alignment = ws[f"C{5+i}"].alignment = Alignment(wrap_text=True, vertical="top")

for s in wb.worksheets:
    s.sheet_view.showGridLines = False
saida = RAIZ / "02_PLANILHAS" / "PT_calculos_COPEL_2025.xlsx"
saida.parent.mkdir(exist_ok=True)
wb.save(saida)
print("Gravado:", saida)

# Matriz de cobertura também em Markdown e CSV (06_FONTES_E_COBERTURA/)
import csv  # noqa: E402
linhas_md = ["# Matriz de cobertura das normas (PT MC)", "",
             "Versões aplicáveis a auditorias do exercício de 2025 (fonte F09, CFC, acesso em 24/10/2026).", "",
             "| Norma | Versão (2025) | Publicação | Título | PT principais | PT de apoio |", "|---|---|---|---|---|---|"]
with open(RAIZ / "06_FONTES_E_COBERTURA" / "matriz_cobertura.csv", "w", newline="", encoding="utf-8") as fcsv:
    w = csv.writer(fcsv)
    w.writerow(["norma", "versao_2025", "publicacao", "titulo", "pt_principais", "pt_apoio"])
    for cod, versao, pub, titulo, princ, sec in ep.matriz_cobertura():
        w.writerow([cod, versao, pub, titulo, "; ".join(princ), "; ".join(sec)])
        linhas_md.append(f"| {cod} | {versao} | {pub} | {titulo} | {', '.join(princ)} | {', '.join(sec)} |")
linhas_md += ["", "## Índice dos papéis de trabalho", "", "| PT | Título | Normas principais |", "|---|---|---|"]
linhas_md += [f"| {c} | {t} | {', '.join(n)} |" for c, t, n, _ in ep.PAPEIS]
(RAIZ / "06_FONTES_E_COBERTURA" / "matriz_cobertura.md").write_text("\n".join(linhas_md) + "\n", encoding="utf-8")
print("Gravado: 06_FONTES_E_COBERTURA/matriz_cobertura.md e .csv")
