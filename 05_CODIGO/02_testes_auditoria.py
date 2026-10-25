"""
02_testes_auditoria.py - Procedimentos de auditoria SIMULADOS sobre a base sintética.

*** PROCEDIMENTOS SIMULADOS PARA FINS DIDÁTICOS SOBRE DADOS SINTÉTICOS ***

Executa:
  T01 Integridade e conciliação com o saldo contábil (PT BS-04)
  T02 Recálculo do valor líquido (custo - amortização) e valores negativos
  T03 Duplicidades
  T04 Corte (capitalização após a data-base)
  T05 Recálculo da amortização acumulada
  T06 Taxa de amortização x prazo remanescente da concessão
  T07 Bens em curso com amortização
  T08 Campos obrigatórios em branco
  T09 Lançamentos manuais próximos à alçada no fim do exercício (NBC TA 240)
  T10 Lei de Benford (primeiro dígito) - indicativo
  T11 Amostragem por unidade monetária (MUS) e avaliação (NBC TA 530)
  Comparação: erros inseridos x exceções identificadas

Reprodução: python 05_CODIGO/02_testes_auditoria.py   (após 01_gerar_base.py)
Preparadora: matrícula 232025417 - 24/10/2026.
"""
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

import dados_publicos as dp

RAIZ = Path(__file__).resolve().parents[1]
RES = RAIZ / "04_RESULTADOS_TESTES"
RES.mkdir(exist_ok=True)
DATA_BASE = pd.Timestamp("2025-12-31")
SEED_AMOSTRA = 232025417

# ---------------------------------------------------------------------------
# Materialidade (mesmos parâmetros da planilha PT_calculos - aba Materialidade)
# ---------------------------------------------------------------------------
LAIR = dict((r[0], r[1]) for r in dp.DRE)["Lucro antes do IR e da CSLL"]
MG = round(LAIR * 0.05)                 # materialidade global (R$ mil)
ME = round(MG * 0.70)                   # materialidade para execução (R$ mil)
TRIVIAL = round(MG * 0.05)              # limite de distorção claramente trivial (R$ mil)
ALCADA = 1_000_000.00                   # alçada de aprovação de lançamento manual (premissa)


def poisson_uel(k, conf=0.95):
    """Limite superior de Poisson para k ocorrências (fator de confiabilidade)."""
    lo, hi = 0.0, 100.0
    for _ in range(200):
        lam = (lo + hi) / 2
        cdf = sum(math.exp(-lam) * lam**i / math.factorial(i) for i in range(k + 1))
        if cdf > 1 - conf:
            lo = lam
        else:
            hi = lam
    return round((lo + hi) / 2, 4)


print("Lendo base sintética...")
df = pd.read_csv(RAIZ / "03_BASE_SINTETICA" / "base_intangivel_sintetica.csv.gz", dtype={"odi": str, "contrato_concessao": str,
                                                                               "codigo_municipio_sint": str})
for c in ["odi", "contrato_concessao", "codigo_municipio_sint"]:
    df[c] = df[c].fillna("")
for c in ["data_capitalizacao", "data_inicio_operacao", "data_lancamento", "vencimento_concessao"]:
    df[c] = pd.to_datetime(df[c], errors="coerce")
log = pd.read_csv(RAIZ / "03_BASE_SINTETICA" / "log_erros_inseridos.csv")

flags = pd.DataFrame(index=df.index)
res = {"parametros": {"LAIR_R$mil": LAIR, "materialidade_global_R$mil": MG,
                      "materialidade_execucao_R$mil": ME, "trivial_R$mil": TRIVIAL}}

# T01 ------------------------------------------------------------------------
saldo = dp.ATIVO_NC_OUTROS[2][1] * 1000
total = round(df["valor_liquido"].sum(), 2)
GET_REAL = 7150619 * 1000  # F15, ITR 1T26 Copel GeT, NE 15, p. 21
res["T01_GeT"] = {"base_segmento_GeT_R$": round(float(df.loc[df["segmento"] == "Copel GeT", "valor_liquido"].sum()), 2),
                  "intangivel_consolidado_GeT_F15_R$": GET_REAL}
res["T01_GeT"]["diferenca_R$"] = round(res["T01_GeT"]["base_segmento_GeT_R$"] - GET_REAL, 2)
NE16_REAL = {"Distribuição": 11868128, "Geração": 5831357, "Direito de concessão e autorização": 1409777,
             "Outros intangíveis": 97347}   # F17, NE 16, p. 91 (R$ mil)
_cat = df.groupby("categoria_ne16")["valor_liquido"].sum()
res["T01_NE16"] = [{"categoria": c, "base_R$": round(float(_cat.get(c, 0)), 2), "nota16_R$": v * 1000,
                    "diferenca_R$": round(float(_cat.get(c, 0)) - v * 1000, 2)} for c, v in NE16_REAL.items()]
res["T01"] = {
    "linhas": int(len(df)), "ids_unicos": bool(df["id_registro"].is_unique),
    "todas_sinteticas": bool((df["flag_dado_sintetico"] == "SIM").all()),
    "saldo_contabil_R$": saldo, "total_base_R$": total, "diferenca_R$": round(total - saldo, 2),
    "por_subconta": df.groupby("codigo_subconta").agg(linhas=("id_registro", "size"),
                                                      custo=("custo_historico", "sum"),
                                                      amortizacao=("amortizacao_acumulada", "sum"),
                                                      liquido=("valor_liquido", "sum")).round(2)
                      .reset_index().to_dict("records"),
}

# T02 ------------------------------------------------------------------------
flags["T02_liquido_divergente"] = (df["custo_historico"] - df["amortizacao_acumulada"] - df["valor_liquido"]).abs() > 0.01
flags["T02_liquido_negativo"] = df["valor_liquido"] < 0

# T03 ------------------------------------------------------------------------
chave = ["codigo_subconta", "tipo_bem", "odi", "codigo_municipio_sint", "custo_historico", "data_capitalizacao"]
ordenado = df.sort_values("data_lancamento")
dup = ordenado.duplicated(subset=chave, keep="first")
flags["T03_duplicidade"] = dup.reindex(df.index)

# T04 ------------------------------------------------------------------------
flags["T04_corte"] = (df["data_capitalizacao"] > DATA_BASE) | (df["data_inicio_operacao"] > DATA_BASE)

# T05 ------------------------------------------------------------------------
anos = np.clip((DATA_BASE - df["data_inicio_operacao"]).dt.days / 365.25, 0, None)
esperado = df["custo_historico"] * np.clip(df["taxa_amortizacao_anual"] * anos, 0, 1)
esperado = np.where(df["status"] == "Em curso", 0.0, esperado)
dif_amort = df["amortizacao_acumulada"] - esperado
tol = np.maximum(df["custo_historico"].abs() * 0.005, 1.00)
flags["T05_amortizacao_recalculada"] = (np.abs(dif_amort) > tol) & (df["status"] == "Em serviço") & ~flags["T04_corte"]

# T06 ------------------------------------------------------------------------
flags["T06_taxa_abaixo_minima"] = (~df["codigo_subconta"].isin(["INT-SOF", "INT-SGT"])) & (
    df["taxa_amortizacao_anual"] < df["taxa_minima_prazo_concessao"] * 0.99)

# T07 ------------------------------------------------------------------------
flags["T07_em_curso_amortizado"] = (df["status"] == "Em curso") & (df["amortizacao_acumulada"] > 0)

# T08 ------------------------------------------------------------------------
flags["T08_campos_em_branco"] = (df["odi"] == "") | ((df["contrato_concessao"] == "") & (~df["codigo_subconta"].isin(["INT-SOF", "INT-SGT"])))

# T09 ------------------------------------------------------------------------
freq_usuario = df.loc[df["lancamento_manual"] == "S", "usuario_lancamento"].value_counts()
usuarios_raros = set(freq_usuario[freq_usuario < 100].index)
flags["T09_manual_alcada_fim_exercicio"] = (
    (df["lancamento_manual"] == "S") & (df["custo_historico"] >= 0.95 * ALCADA) & (df["custo_historico"] < ALCADA)
    & (df["data_lancamento"] >= pd.Timestamp("2025-12-24")))
res["T09"] = {"alcada_R$": ALCADA, "usuarios_manuais_raros": sorted(usuarios_raros),
              "lancamentos_manuais_total": int((df["lancamento_manual"] == "S").sum())}

# T10 Benford ----------------------------------------------------------------
dis = df.loc[(df["codigo_subconta"] == "INT-DIS") & (df["custo_historico"] >= 10), "custo_historico"]
d1 = dis.astype(str).str.lstrip("0.").str[0].astype(int)
obs = d1.value_counts(normalize=True).sort_index()
esp = pd.Series({d: math.log10(1 + 1 / d) for d in range(1, 10)})
mad = float((obs.reindex(range(1, 10), fill_value=0) - esp).abs().mean())
res["T10"] = {"n": int(len(dis)), "MAD": round(mad, 5),
              "classificacao_Nigrini": ("conformidade próxima" if mad < 0.006 else "conformidade aceitável"
                                        if mad < 0.012 else "conformidade marginal" if mad < 0.015 else "não conformidade"),
              "tabela": [{"digito": d, "observado": round(float(obs.get(d, 0)), 4), "esperado": round(float(esp[d]), 4)}
                         for d in range(1, 10)]}

# Consolidação das exceções ---------------------------------------------------
testes = [c for c in flags.columns]
flags = flags.fillna(False).astype(bool)
qualquer = flags.any(axis=1)
exc = df.loc[qualquer, ["id_registro", "codigo_subconta", "tipo_bem", "status", "data_capitalizacao",
                        "custo_historico", "amortizacao_acumulada", "valor_liquido", "taxa_amortizacao_anual",
                        "taxa_minima_prazo_concessao", "usuario_lancamento"]].copy()
exc["testes_acionados"] = flags.loc[qualquer].apply(lambda r: ";".join(t for t in testes if r[t]), axis=1)
exc["flag_dado_sintetico"] = "SIM"
exc.to_csv(RES / "excecoes_detectadas.csv", index=False)

# Inseridos x detectados -----------------------------------------------------
idx_por_id = pd.Series(df.index, index=df["id_registro"])
log["detectado_por"] = log["id_registro"].map(lambda i: exc.set_index("id_registro")["testes_acionados"].get(i, ""))
log["detectado"] = log["detectado_por"] != ""
matriz = log.groupby("codigo_erro").agg(inseridos=("id_registro", "size"), detectados=("detectado", "sum"),
                                        distorcao_inserida_R=("distorcao_inserida", "sum")).reset_index()
matriz["taxa_deteccao_%"] = (100 * matriz["detectados"] / matriz["inseridos"]).round(1)
matriz["teste_principal"] = matriz["codigo_erro"].map({
    "E01": "T03", "E02": "T02", "E03": "T04", "E04": "T05", "E05": "T06", "E06": "T08",
    "E07": "T09/T08", "E08": "T07", "E09": "T02"})
log.to_csv(RES / "erros_inseridos_x_detectados.csv", index=False)
matriz.to_csv(RES / "matriz_inseridos_detectados.csv", index=False)
ids_log = set(log["id_registro"])
falsos_pos = exc.loc[~exc["id_registro"].isin(ids_log)]
falsos_pos.to_csv(RES / "falsos_positivos.csv", index=False)
res["comparacao"] = {
    "registros_com_erro_inserido": int(len(log)), "detectados": int(log["detectado"].sum()),
    "nao_detectados": int((~log["detectado"]).sum()),
    "excecoes_totais": int(len(exc)), "falsos_positivos": int(len(falsos_pos)),
    "falsos_positivos_por_teste": falsos_pos["testes_acionados"].value_counts().to_dict(),
    "matriz": matriz.round(2).to_dict("records"),
    "distorcao_total_inserida_R$": round(float(log["distorcao_inserida"].sum()), 2),
    "distorcao_superavaliacao_R$": round(float(log.loc[log["distorcao_inserida"] > 0, "distorcao_inserida"].sum()), 2),
    "distorcao_subavaliacao_R$": round(float(log.loc[log["distorcao_inserida"] < 0, "distorcao_inserida"].sum()), 2),
}
res["contagem_por_teste"] = {t: int(flags[t].sum()) for t in testes}

# T11 MUS --------------------------------------------------------------------
TM = ME * 1000.0
EM = 0.10 * TM
RF0, EF = poisson_uel(0), 1.6
pop = df.loc[df["valor_liquido"] > 0].copy()
BV = float(pop["valor_liquido"].sum())
n = math.ceil(BV * RF0 / (TM - EM * EF))
J = BV / n
rs = np.random.default_rng(SEED_AMOSTRA)
inicio = float(rs.uniform(0, J))
pontos = inicio + J * np.arange(n)
cum = pop["valor_liquido"].cumsum().to_numpy()
pos = np.searchsorted(cum, pontos, side="left")
sel_idx = pop.index[np.unique(pos)]
amostra = df.loc[sel_idx, ["id_registro", "codigo_subconta", "tipo_bem", "status", "valor_liquido"]].copy()
amostra["item_chave"] = amostra["valor_liquido"] >= J
correto = log.set_index("id_registro")["valor_liquido_correto"]
# SIMULAÇÃO da inspeção documental: o "valor auditado" é obtido do gabarito
# (log de erros), representando o que o exame do suporte revelaria.
amostra["valor_auditado_simulado"] = amostra["id_registro"].map(correto).fillna(amostra["valor_liquido"])
amostra["distorcao"] = (amostra["valor_liquido"] - amostra["valor_auditado_simulado"]).round(2)
amostra["contaminacao"] = np.where(amostra["item_chave"], np.nan, amostra["distorcao"] / amostra["valor_liquido"])
amostra["flag_dado_sintetico"] = "SIM"
amostra.to_csv(RES / "amostra_mus.csv", index=False)

chave_dist = float(amostra.loc[amostra["item_chave"], "distorcao"].sum())
nao_chave = amostra.loc[~amostra["item_chave"]]
sobre = nao_chave.loc[nao_chave["distorcao"] > 0, "contaminacao"].sort_values(ascending=False).to_list()
sub = nao_chave.loc[nao_chave["distorcao"] < 0, "contaminacao"].to_list()
proj_sobre = sum(t * J for t in sobre)
fatores = [poisson_uel(k) for k in range(len(sobre) + 1)]
incremento = sum(t * J * ((fatores[i + 1] - fatores[i]) - 1) for i, t in enumerate(sobre))
BP = RF0 * J
LSD = BP + proj_sobre + incremento + max(chave_dist, 0)
res["T11"] = {
    "populacao_valor_positivo_R$": round(BV, 2), "registros_populacao": int(len(pop)),
    "registros_negativos_excluidos": int((df["valor_liquido"] <= 0).sum()),
    "distorcao_toleravel_R$": TM, "distorcao_esperada_R$": EM, "fator_confiabilidade_95%": RF0,
    "fator_expansao": EF, "tamanho_amostra": n, "intervalo_amostral_R$": round(J, 2),
    "inicio_aleatorio_R$": round(inicio, 2), "itens_selecionados_unicos": int(len(amostra)),
    "itens_chave": int(amostra["item_chave"].sum()),
    "valor_itens_chave_R$": round(float(amostra.loc[amostra["item_chave"], "valor_liquido"].sum()), 2),
    "itens_com_distorcao": int((amostra["distorcao"] != 0).sum()),
    "distorcao_itens_chave_R$": round(chave_dist, 2),
    "contaminacoes_superavaliacao": [round(t, 4) for t in sobre],
    "contaminacoes_subavaliacao": [round(t, 4) for t in sub],
    "precisao_basica_R$": round(BP, 2), "distorcao_projetada_R$": round(proj_sobre + max(chave_dist, 0), 2),
    "provisao_incremental_R$": round(incremento, 2), "limite_superior_distorcao_R$": round(LSD, 2),
    "conclusao": ("LSD inferior à distorção tolerável: a amostra não indica distorção relevante "
                  "por superavaliação (simulação)." if LSD < TM else
                  "LSD superior à distorção tolerável: ampliar procedimentos ou propor ajuste (simulação)."),
}

(RES / "resultados_testes.json").write_text(json.dumps(res, ensure_ascii=False, indent=2, default=str))
print(json.dumps({k: v for k, v in res.items() if k not in ("T01",)}, ensure_ascii=False, indent=2, default=str)[:6000])
print("T01:", {k: v for k, v in res["T01"].items() if k != "por_subconta"})
