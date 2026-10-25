"""
04_dossie_pdf.py - Renderiza o dossiê de auditoria em PDF (01_DOSSIE/Dossie_Auditoria_COPEL_2025_232025417.pdf).
Executar após 01, 02 e 03. Preparadora: matrícula 232025417.
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, NextPageTemplate, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

import dados_publicos as dp
import dossie_conteudo as dc
import estrutura_pt as ep

RAIZ = Path(__file__).resolve().parents[1]
SAIDA = RAIZ / "01_DOSSIE" / f"Dossie_Auditoria_COPEL_2025_{dp.MATRICULA}.pdf"

F = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", F + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DV-B", F + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DV-I", F + "DejaVuSans-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("DV-BI", F + "DejaVuSans-BoldOblique.ttf"))
pdfmetrics.registerFontFamily("DV", normal="DV", bold="DV-B", italic="DV-I", boldItalic="DV-BI")

AZUL = colors.HexColor("#1F3864")
CINZA = colors.HexColor("#F2F2F2")
LINHA = colors.HexColor("#BFBFBF")
COR_CLASS = {"R": colors.HexColor("#DDEBF7"), "P": colors.HexColor("#FFF2CC"), "S": colors.HexColor("#E2EFDA"),
             "R/P": colors.HexColor("#EDEDED")}

st = {
    "corpo": ParagraphStyle("corpo", fontName="DV", fontSize=9.2, leading=13, alignment=TA_JUSTIFY, spaceAfter=6),
    "cel": ParagraphStyle("cel", fontName="DV", fontSize=7.8, leading=10.2),
    "anexo": ParagraphStyle("anexo", fontName="DV", fontSize=8.2, leading=11.2, alignment=TA_JUSTIFY, spaceAfter=4,
                            leftIndent=8, borderPadding=0),
    "celb": ParagraphStyle("celb", fontName="DV-B", fontSize=7.8, leading=10.2),
    "celh": ParagraphStyle("celh", fontName="DV-B", fontSize=7.8, leading=10, textColor=colors.white),
    "h1": ParagraphStyle("h1", fontName="DV-B", fontSize=14, leading=18, textColor=AZUL, spaceBefore=4, spaceAfter=8),
    "h2": ParagraphStyle("h2", fontName="DV-B", fontSize=11.5, leading=15, textColor=AZUL, spaceBefore=6, spaceAfter=6),
    "pt": ParagraphStyle("pt", fontName="DV-B", fontSize=11, leading=14, textColor=colors.white),
    "capa1": ParagraphStyle("capa1", fontName="DV-B", fontSize=20, leading=26, alignment=TA_CENTER, textColor=AZUL),
    "capa2": ParagraphStyle("capa2", fontName="DV", fontSize=11.5, leading=17, alignment=TA_CENTER),
    "toc1": ParagraphStyle("toc1", fontName="DV-B", fontSize=9.5, leading=13),
    "toc2": ParagraphStyle("toc2", fontName="DV", fontSize=8.5, leading=11.5, leftIndent=14),
}


def esc(t):
    return str(t).replace("&", "&amp;")


def P(t, s="corpo"):
    return Paragraph(esc(t), st[s])


class Doc(BaseDocTemplate):
    def __init__(self, fn, **kw):
        super().__init__(fn, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=2.3 * cm,
                         bottomMargin=2 * cm, title="Dossiê de auditoria - COPEL 2025",
                         author=f"{dp.ESTUDANTE} - matrícula {dp.MATRICULA}",
                         subject="Trabalho acadêmico de auditoria (P2) - dados públicos e sintéticos", **kw)
        fr = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="f")
        self.addPageTemplates([PageTemplate("capa", [fr], onPage=lambda c, d: None),
                               PageTemplate("normal", [fr], onPage=self.cabecalho)])

    def cabecalho(self, c, d):
        c.saveState()
        c.setFont("DV", 7.5)
        c.setFillColor(AZUL)
        c.drawString(2 * cm, A4[1] - 1.3 * cm, "COPEL - Companhia Paranaense de Energia | Dossiê de auditoria 2025")
        c.drawRightString(A4[0] - 2 * cm, A4[1] - 1.3 * cm, f"{dp.ESTUDANTE} - matrícula {dp.MATRICULA}")
        c.setStrokeColor(LINHA)
        c.line(2 * cm, A4[1] - 1.45 * cm, A4[0] - 2 * cm, A4[1] - 1.45 * cm)
        c.setFillColor(colors.grey)
        c.drawString(2 * cm, 1.2 * cm, "Trabalho acadêmico - não constitui opinião de auditoria. "
                                       "Dados sintéticos identificados como [S].")
        c.drawRightString(A4[0] - 2 * cm, 1.2 * cm, f"Página {d.page}")
        c.restoreState()

    def afterFlowable(self, f):
        if isinstance(f, Paragraph) and getattr(f, "_toc", None) is not None:
            self.notify("TOCEntry", (f._toc, f.getPlainText(), self.page))


def titulo(t, nivel=0, estilo="h1"):
    p = Paragraph(esc(t), st[estilo])
    p._toc = nivel
    return p


def tabela(cab, linhas, larg, estilo_corpo="cel"):
    dados = [[Paragraph(esc(c), st["celh"]) for c in cab]]
    dados += [[Paragraph(esc(c), st[estilo_corpo]) for c in l] for l in linhas]
    t = Table(dados, colWidths=larg, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), AZUL), ("GRID", (0, 0), (-1, -1), 0.4, LINHA),
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, CINZA]),
        ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]))
    return t


def campos(pares):
    dados = [[Paragraph(esc(a), st["celb"]), Paragraph(esc(b), st["cel"])] for a, b in pares]
    t = Table(dados, colWidths=[3.6 * cm, 13.4 * cm])
    t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, LINHA), ("BACKGROUND", (0, 0), (0, -1), CINZA),
                           ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]))
    return t


def faixa_pt(cod, tit):
    p = Paragraph(esc(f"{cod} - {tit}"), st["pt"])
    p._toc = 1
    t = Table([[p]], colWidths=[17 * cm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), AZUL), ("TOPPADDING", (0, 0), (-1, -1), 5),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    return t, p


REVISAO = "Revisor: ______________________   Data: ___/___/______   (campo não preenchido - não houve revisão de terceiros)"
PREPARADORA = f"Matrícula {dp.MATRICULA} - {dp.DATA_PREPARACAO}"


def render_pt(d):
    out = []
    faixa, p = faixa_pt(d["cod"], d["titulo"])
    lin1 = [("Código / norma e itens", f"{d['cod']} | {d['normas']}")]
    if d.get("atividade"):
        lin1.append(("Atividade exigida (roteiro)", d["atividade"]))
    out.append(KeepTogether([faixa, Spacer(1, 4), campos(lin1 + [
                       ("Objetivo", d["objetivo"]),
                       ("Conta, processo ou divulgação", d["objeto"]),
                       ("Afirmações e riscos", d["afirmacoes"]),
                       ("População, fontes e critérios de seleção", d["populacao"])])]))
    out.append(Spacer(1, 4))
    linhas = [[str(i), txt, cl, ref] for i, (txt, cl, ref) in enumerate(d["procedimentos"], 1)]
    t = tabela(["Nº", "Procedimento", "Classif.", "Ref."], linhas, [0.7 * cm, 11.9 * cm, 1.8 * cm, 2.6 * cm])
    estilos = []
    for i, (_, cl, _) in enumerate(d["procedimentos"], 1):
        estilos.append(("BACKGROUND", (2, i), (2, i), COR_CLASS.get(cl, CINZA)))
    t.setStyle(TableStyle(estilos))
    out.append(t)
    if d.get("tabela_extra"):
        nome, cab, linhas = d["tabela_extra"]
        out.append(Spacer(1, 4))
        out.append(P(f"<b>{nome}</b>", "cel"))
        if linhas == "DICIONARIO":
            out.append(tabela(["Variável", "Tipo", "Descrição", "Regra de geração"],
                              [list(x) for x in ep.DICIONARIO], [3.6 * cm, 1.8 * cm, 6.4 * cm, 5.2 * cm]))
        elif linhas == "MATRIZ":
            out.append(tabela(["Norma", "Versão (2025)", "Publicação", "PT principais", "PT de apoio"],
                              [[a, b, c, ", ".join(e), ", ".join(f)] for a, b, c, _, e, f in ep.matriz_cobertura()],
                              [3.4 * cm, 2.8 * cm, 2.8 * cm, 4.2 * cm, 3.8 * cm]))
        else:
            n = len(cab)
            larg = {5: [4.3 * cm, 3.4 * cm, 4.1 * cm, 2.5 * cm, 2.7 * cm],
                    6: [1.4 * cm, 5.6 * cm, 1.7 * cm, 1.9 * cm, 3.4 * cm, 3.0 * cm]}[n]
            out.append(tabela(cab, linhas, larg))
    for ax in d.get("anexos", []):
        out.append(Spacer(1, 5))
        out.append(P(f"<b>{ax['titulo']}</b>", "celb"))
        if "paragrafos" in ax:
            for p_ in ax["paragrafos"]:
                out.append(P(p_, "anexo"))
        else:
            out.append(tabela(ax["cab"], ax["linhas"], [w * cm for w in ax["larg"]]))
    out.append(Spacer(1, 4))
    out.append(campos([("Evidências e referências cruzadas", d["evidencias"]),
                       ("Resultados e exceções", d["resultados"]),
                       ("Conclusão", d["conclusao"]),
                       ("Limitações", d["limitacoes"]),
                       ("Preparadora", PREPARADORA),
                       ("Revisão", REVISAO)]))
    out.append(Spacer(1, 12))
    return out


GRUPOS = {"A": "Parte A - Identificação e Estrutura Conceitual (PT 000 e PT EC)", "B": "Parte B - Princípios e responsabilidades (NBC TA 200 a 265)",
          "C": "Parte C - Planejamento e avaliação de riscos (NBC TA 300 a 450)",
          "D": "Parte D - Evidência de auditoria (NBC TA 500 a 580)", "E": "Parte E - Auditoria de grupo (NBC TA 600)",
          "F": "Parte F - Programas de auditoria por área (PT PA)", "G": "Parte G - Base de dados simulada - Intangível (PT BS)",
          "H": "Parte H - Relatório do auditor, conclusão integrada e matriz (PT RA, PT CI, PT MC)"}

story = []
# ---------------- capa
story += [Spacer(1, 2.5 * cm),
          Paragraph("Universidade de Brasília - Ciências Contábeis<br/>Auditoria - Trabalho P2", st["capa2"]),
          Spacer(1, 1.6 * cm),
          Paragraph("DOSSIÊ DE AUDITORIA DAS DEMONSTRAÇÕES CONTÁBEIS CONSOLIDADAS", st["capa1"]),
          Spacer(1, 0.4 * cm),
          Paragraph("Companhia Paranaense de Energia - COPEL<br/>Exercício findo em 31/12/2025 (comparativo 2024)",
                    st["capa2"]),
          Spacer(1, 1.4 * cm),
          Paragraph(f"<b>Estudante:</b> {dp.ESTUDANTE}<br/><b>Matrícula:</b> {dp.MATRICULA}", st["capa2"]),
          Spacer(1, 0.6 * cm),
          Paragraph(f"CNPJ {dp.CNPJ} | Código CVM {dp.CODIGO_CVM} | B3: CPLE3 | NYSE: ELPC<br/>"
                    f"Auditor independente da companhia: PricewaterhouseCoopers Auditores Independentes Ltda.<br/>"
                    f"Data de consulta das fontes: {dp.DATA_CONSULTA} | Data de preparação: {dp.DATA_PREPARACAO}",
                    st["capa2"]),
          Spacer(1, 1.6 * cm),
          Paragraph("Trabalho acadêmico realizado integralmente com apoio de inteligência artificial, com base em "
                    "documentos públicos. Não constitui relatório nem opinião de auditoria independente. "
                    "Os dados identificados como sintéticos [S] foram gerados por código e não são registros "
                    "reais da companhia.", st["capa2"]),
          NextPageTemplate("normal"), PageBreak()]
# ---------------- sumário
story.append(Paragraph("Sumário", st["h1"]))
toc = TableOfContents()
toc.levelStyles = [st["toc1"], st["toc2"]]
story += [toc, PageBreak()]
# ---------------- abertura
for t, pars in dc.ABERTURA:
    story.append(titulo(t))
    for p_ in pars:
        story.append(P(p_))
    story.append(Spacer(1, 6))
story.append(P("<b>Legenda das classificações:</b> R = realizado com evidência pública; P = planejado por falta de "
               "acesso; S = simulado com dados sintéticos; R/P = parte realizada e parte planejada."))
story.append(PageBreak())

# ---------------- PTs
grupo_atual = None
for d in dc.PTS:
    c = d["cod"]
    g = ("A" if c in ("PT 000", "PT EC") else "F" if c.startswith("PT PA") else "G" if c.startswith("PT BS")
         else "H" if c in ("PT RA", "PT MC") else "E" if c == "PT 600" else "B" if c[3] == "2"
         else "C" if c[3] in "34" else "D")
    if g == "H" and d["cod"] == "PT MC":
        # PT CI (conclusão integrada) vem antes do H03
        faixa, _ = faixa_pt("PT CI", "Conclusão integrada")
        story += [faixa, Spacer(1, 4),
                  campos([("Código / norma e itens", "PT CI | NBC TA 200 (R1), item 11; NBC TA 450 (R1), item 11; "
                                                     "enunciado do P2, item 6"),
                          ("Objetivo", "Integrar riscos, procedimentos, evidências e limitações, sem emitir opinião."),
                          ("Conta, processo ou divulgação", "Demonstrações consolidadas de 2025."),
                          ("Afirmações e riscos", "Todos os riscos do PT 315.2."),
                          ("População, fontes e critérios de seleção", "Todos os PT; fontes F01 a F19.")]),
                  Spacer(1, 6)]
        for p_ in dc.CONCLUSAO:
            story.append(P(p_))
        story += [campos([("Preparadora", PREPARADORA), ("Revisão", REVISAO)]), Spacer(1, 12)]
    if g != grupo_atual:
        if grupo_atual is not None:
            story.append(PageBreak())
        story.append(titulo(GRUPOS[g]))
        grupo_atual = g
    story += render_pt(d)

# ---------------- apêndices
story.append(PageBreak())
story.append(titulo("Apêndice A - Versões das NBC TA consultadas"))
story.append(P("Fonte: página do CFC acessada em 24/10/2026 [F09]. Para cada norma, a versão aplicável a auditorias "
               "do exercício de 2025."))
story.append(tabela(["Norma", "Versão aplicada", "Publicação", "Título", "Vigência"],
                    [list(n) for n in ep.NORMAS], [2.6 * cm, 2.4 * cm, 2.4 * cm, 5.0 * cm, 4.6 * cm]))
story.append(PageBreak())
story.append(titulo("Apêndice B - Balanço e DRE resumidos (dados públicos, R$ mil)"))
bp_lin = [["Ativo circulante", dc.br(dp.TOTAL_AC[0]), dc.br(dp.TOTAL_AC[1])],
          ["Realizável a longo prazo", dc.br(dp.TOTAL_RLP[0]), dc.br(dp.TOTAL_RLP[1])]]
bp_lin += [[n, dc.br(a), dc.br(b)] for n, a, b in dp.ATIVO_NC_OUTROS]
bp_lin += [["TOTAL DO ATIVO", dc.br(dp.TOTAL_ATIVO[0]), dc.br(dp.TOTAL_ATIVO[1])],
           ["Passivo circulante", dc.br(dp.TOTAL_PC[0]), dc.br(dp.TOTAL_PC[1])],
           ["Passivo não circulante", dc.br(dp.TOTAL_PNC[0]), dc.br(dp.TOTAL_PNC[1])],
           ["Patrimônio líquido", dc.br(dp.TOTAL_PL[0]), dc.br(dp.TOTAL_PL[1])],
           ["TOTAL DO PASSIVO E PL", dc.br(dp.TOTAL_PASSIVO_PL[0]), dc.br(dp.TOTAL_PASSIVO_PL[1])]]
story.append(P(f"Balanço patrimonial consolidado [{dp.FONTE_BP}]", "cel"))
story.append(tabela(["Rubrica", "31/12/2025", "31/12/2024"], bp_lin, [9 * cm, 4 * cm, 4 * cm]))
story.append(Spacer(1, 8))
story.append(P(f"Demonstração do resultado consolidada [{dp.FONTE_DRE}]", "cel"))
story.append(tabela(["Rubrica", "2025", "2024"], [[n, dc.br(a), dc.br(b)] for n, a, b in dp.DRE],
                    [9 * cm, 4 * cm, 4 * cm]))
story.append(PageBreak())
story.append(titulo("Apêndice C - Relação de fontes"))
story.append(P("Data de acesso de todas as fontes: 24/10/2026. Lista completa, com páginas, em 06_FONTES_E_COBERTURA/fontes.md."))
fontes = [l for l in (RAIZ / "06_FONTES_E_COBERTURA" / "fontes.md").read_text().splitlines() if l.startswith("| F")]
lin_f = []
for l in fontes:
    c = [x.strip() for x in l.strip("|").split("|")]
    lin_f.append([c[0], c[1], c[2], c[3], c[4]])
story.append(tabela(["ID", "Documento", "Endereço eletrônico", "Páginas / seções", "Exercício"], lin_f,
                    [1.1 * cm, 4.1 * cm, 5.6 * cm, 4.4 * cm, 1.8 * cm]))

SAIDA.parent.mkdir(exist_ok=True)
doc = Doc(str(SAIDA))
doc.multiBuild(story)
print("Gravado:", SAIDA)
