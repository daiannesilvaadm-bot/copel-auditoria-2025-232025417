"""
01_gerar_base.py - Geração da BASE SINTÉTICA do Intangível consolidado da COPEL.

*** DADOS SINTÉTICOS PARA FINS DIDÁTICOS - NÃO SÃO REGISTROS REAIS DA COMPANHIA ***

Conta: Intangível (consolidado) em 31/12/2025 = R$ 19.206.609 mil
(F01 - Release 4T25, Anexo I, Balanço, p. 24). É a conta de maior saldo do ativo.

Saídas:
  dados/base_intangivel_sintetica.csv.gz    (>= 500.000 linhas)
  dados/log_erros_inseridos.csv             (gabarito dos erros inseridos)
  resultados/geracao_resumo.json

Reprodução: python codigo/01_gerar_base.py   (semente fixa = 232025417)
Preparadora: matrícula 232025417 - 24/10/2026.
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd

import dados_publicos as dp

SEED = 232025417
RAIZ = Path(__file__).resolve().parents[1]
DATA_BASE = pd.Timestamp("2025-12-31")
SALDO_CONTABIL_MIL = 19206609                # R$ mil (F01)
SALDO_CONTABIL_CENTAVOS = SALDO_CONTABIL_MIL * 1000 * 100

rng = np.random.default_rng(SEED)

# ---------------------------------------------------------------------------
# 1. Premissas de composição (HIPÓTESES DIDÁTICAS - a composição real por
#    componente não foi obtida nas fontes consultadas; ver PT BS-02).
#    Valores-alvo de valor líquido em R$ mil.
# ---------------------------------------------------------------------------
SUBCONTAS = {
    # codigo: (descrição, segmento, alvo R$ mil, origem predominante)
    # ÂNCORAS REAIS:
    #  F17 (DFs Copel dez/2025, NE 16, p. 91), consolidado 31/12/2025: Distribuição 11.868.128 | Geração 5.831.357 |
    #     Direito de concessão e autorização/ágio técnico 1.409.777 | Outros intangíveis 97.347 | Total 19.206.609.
    #  F15 (ITR 1T26 Copel GeT, NE 15, p. 21): na Copel GeT, contratos de concessão 5.671.800 | direito de
    #     concessão e autorização/ágio técnico 1.402.043 | outros 76.776 | total 7.150.619.
    #  F07 (DF F.D.A., p. 8): intangível da F.D.A. 1.849.570 (alocado ao bônus de Foz do Areia).
    # HIPÓTESE DIDÁTICA: divisão dos 5.671.800 da GeT entre bônus, GSF, UBP e combinação de negócios.
    "INT-DIS": ("Contrato de concessão - distribuição", "Copel DIS", 11868128, "Transferência de ativo de contrato"),
    "INT-BON": ("Contrato de concessão - geração: bônus de outorga (usinas renovadas)", "Copel GeT", 4191800,
                "Bônus de outorga"),
    "INT-GSF": ("Contrato de concessão - geração: repactuação do risco hidrológico (GSF)", "Copel GeT", 260000,
                "Repactuação GSF"),
    "INT-UBP": ("Contrato de concessão - geração: uso do bem público (UBP)", "Copel GeT", 520000,
                "Concessão onerosa (UBP)"),
    "INT-CNB": ("Contrato de concessão - geração: combinação de negócios (UHE Mauá)", "Copel GeT", 700000,
                "Combinação de negócios"),
    "INT-UBE": ("Contrato de concessão - geração fora da Copel GeT (Elejor e outras)", "Holding/Diversos", 159557,
                "Concessão onerosa (UBP)"),
    "INT-EOL": ("Direito de concessão e autorização / ágio técnico - eólicas (Copel GeT)", "Copel GeT", 1402043,
                "Combinação de negócios"),
    "INT-AUO": ("Direito de concessão e autorização - demais empresas", "Holding/Diversos", 7734,
                "Combinação de negócios"),
    "INT-SGT": ("Outros intangíveis (softwares) - Copel GeT", "Copel GeT", 76776, "Aquisição"),
    "INT-SOF": ("Outros intangíveis (softwares) - demais empresas", "Holding/Diversos", 20571, "Aquisição"),
}
CATEGORIA_NE16 = {"INT-DIS": "Distribuição", "INT-BON": "Geração", "INT-GSF": "Geração", "INT-UBP": "Geração",
                  "INT-CNB": "Geração", "INT-UBE": "Geração", "INT-EOL": "Direito de concessão e autorização",
                  "INT-AUO": "Direito de concessão e autorização", "INT-SGT": "Outros intangíveis",
                  "INT-SOF": "Outros intangíveis"}
NE16_REAL = {"Distribuição": 11868128, "Geração": 5831357, "Direito de concessão e autorização": 1409777,
             "Outros intangíveis": 97347}
for _cat, _v in NE16_REAL.items():
    assert sum(v[2] for k, v in SUBCONTAS.items() if CATEGORIA_NE16[k] == _cat) == _v
assert sum(v[2] for v in SUBCONTAS.values()) == SALDO_CONTABIL_MIL

VENC_DIS = pd.Timestamp("2045-07-07")        # F01, p. 15

# Tipos de bem da distribuição: (nome, quantidade, mediana custo R$, sigma lognormal, taxa anual)
TIPOS_DIS = [
    ("Medidor eletrônico inteligente", 200000, 1150, 0.25, 0.0769),
    ("Poste de concreto", 120000, 3200, 0.35, 0.0357),
    ("Transformador de distribuição", 70000, 26000, 0.55, 0.0400),
    ("Trecho de rede trifásica rural (MT)", 60000, 145000, 0.60, 0.0357),
    ("Religador / chave automatizada", 18000, 78000, 0.40, 0.0385),
    ("Equipamento de subestação de distribuição", 6000, 1800000, 0.90, 0.0333),
    ("Trecho de linha de distribuição AT (138 kV)", 2400, 4200000, 0.80, 0.0278),
    ("Sistema de telecomunicação e automação (Smart Grid)", 3600, 420000, 0.70, 0.1000),
    ("Edificação operacional", 1600, 950000, 0.85, 0.0333),
    ("Veículo e equipamento operacional vinculado", 30400, 9000, 0.50, 0.1429),
]

# Direitos de geração (registros individuais)
USINAS_BONUS = [  # (usina, peso relativo, vencimento)
    ("UHE Gov. Bento Munhoz da Rocha Netto (Foz do Areia) - F.D.A.", None, "2054-11-20"),
    ("UHE Gov. Ney Braga (Segredo)", 0.52, "2054-11-20"),
    ("UHE Gov. José Richa (Salto Caxias)", 0.48, "2054-11-20"),
]
USINAS_GSF = ["Capivari Cachoeira", "Derivação do Rio Jordão", "Foz do Areia", "Mauá", "Salto Caxias",
              "Segredo", "Fundão", "Santa Clara", "Bela Vista"]
USINAS_UBP = ["UHE Mauá", "PCH Bela Vista", "UHE Salto Caxias", "UHE Segredo",
              "UHE Capivari Cachoeira", "UHE Derivação do Rio Jordão"]
USINAS_UBE = ["UHE Fundão (Elejor)", "UHE Santa Clara (Elejor)"]
N_PARQUES_EOL = 42                            # F02, Item 4, p. 20


def lognormal(mediana, sigma, n):
    return rng.lognormal(np.log(mediana), sigma, n)


def datas_uniformes(ini, fim, n):
    a, b = pd.Timestamp(ini).value // 10**9, pd.Timestamp(fim).value // 10**9
    return pd.to_datetime(rng.integers(a, b, n), unit="s").normalize()


def anos_entre(d0, d1):
    dif = pd.to_datetime(d1) - pd.to_datetime(d0)
    dias = dif.dt.days if isinstance(dif, pd.Series) else dif.days
    return np.clip(np.asarray(dias, dtype=float) / 365.25, 0, None)


# ---------------------------------------------------------------------------
# 2. Geração dos registros "limpos"
# ---------------------------------------------------------------------------
partes = []

# 2.1 Distribuição
for nome, qtd, med, sig, taxa in TIPOS_DIS:
    custo = lognormal(med, sig, qtd)
    dt_ini_op = datas_uniformes("2008-01-01", "2025-12-15", qtd)
    if nome.startswith("Medidor"):
        dt_ini_op = datas_uniformes("2019-01-01", "2025-12-15", qtd)
    if nome.startswith("Trecho de rede trifásica"):
        dt_ini_op = datas_uniformes("2017-01-01", "2025-12-15", qtd)
    dt_cap = dt_ini_op - pd.to_timedelta(rng.integers(0, 45, qtd), unit="D")
    em_curso = rng.random(qtd) < 0.004          # pequena parcela ainda em curso
    partes.append(pd.DataFrame({
        "codigo_subconta": "INT-DIS", "tipo_bem": nome, "custo": custo,
        "taxa_regulatoria": taxa, "data_capitalizacao": dt_cap, "data_inicio_operacao": dt_ini_op,
        "status": np.where(em_curso, "Em curso", "Em serviço"),
        "vencimento_concessao": VENC_DIS,
    }))

# 2.2 Bônus de outorga (3 registros; Foz do Areia ancorado na DF da F.D.A.)
venc_bonus = pd.Timestamp("2054-11-20")
partes.append(pd.DataFrame({
    "codigo_subconta": "INT-BON", "tipo_bem": [u[0] for u in USINAS_BONUS],
    "custo": [1.0, 1.0, 1.0], "taxa_regulatoria": 1 / 30.0,
    "data_capitalizacao": pd.Timestamp("2024-11-18"), "data_inicio_operacao": pd.Timestamp("2024-11-20"),
    "status": "Em serviço", "vencimento_concessao": [pd.Timestamp(u[2]) for u in USINAS_BONUS],
}))
# 2.3 GSF
n = len(USINAS_GSF)
partes.append(pd.DataFrame({
    "codigo_subconta": "INT-GSF", "tipo_bem": [f"Extensão de outorga GSF - {u}" for u in USINAS_GSF],
    "custo": rng.uniform(0.5, 1.5, n), "taxa_regulatoria": np.nan,
    "data_capitalizacao": pd.Timestamp("2021-03-31"), "data_inicio_operacao": pd.Timestamp("2021-03-31"),
    "status": "Em serviço", "vencimento_concessao": pd.Timestamp("2055-06-30"),
}))
# 2.4 UBP
n = len(USINAS_UBP)
partes.append(pd.DataFrame({
    "codigo_subconta": "INT-UBP", "tipo_bem": [f"UBP - {u}" for u in USINAS_UBP],
    "custo": rng.uniform(0.5, 1.5, n), "taxa_regulatoria": np.nan,
    "data_capitalizacao": datas_uniformes("2006-01-01", "2016-12-31", n),
    "data_inicio_operacao": datas_uniformes("2007-01-01", "2017-12-31", n),
    "status": "Em serviço", "vencimento_concessao": pd.Timestamp("2049-06-30"),
}))
# 2.4b UBP fora da GeT (Elejor)
partes.append(pd.DataFrame({
    "codigo_subconta": "INT-UBE", "tipo_bem": [f"UBP - {u}" for u in USINAS_UBE],
    "custo": [1.0, 1.0], "taxa_regulatoria": np.nan,
    "data_capitalizacao": pd.Timestamp("2005-10-25"), "data_inicio_operacao": pd.Timestamp("2006-06-01"),
    "status": "Em serviço", "vencimento_concessao": pd.Timestamp("2040-10-25"),
}))
partes.append(pd.DataFrame({
    "codigo_subconta": "INT-AUO", "tipo_bem": ["Direito de autorização - demais empresas (sintético)"],
    "custo": [1.0], "taxa_regulatoria": np.nan,
    "data_capitalizacao": pd.Timestamp("2020-01-01"), "data_inicio_operacao": pd.Timestamp("2020-01-01"),
    "status": "Em serviço", "vencimento_concessao": pd.Timestamp("2050-12-31"),
}))
# 2.5 Eólicas (42 parques)
partes.append(pd.DataFrame({
    "codigo_subconta": "INT-EOL",
    "tipo_bem": [f"Autorização eólica - Parque {i:02d} (sintético)" for i in range(1, N_PARQUES_EOL + 1)],
    "custo": rng.uniform(0.6, 1.4, N_PARQUES_EOL), "taxa_regulatoria": np.nan,
    "data_capitalizacao": datas_uniformes("2015-01-01", "2023-12-31", N_PARQUES_EOL),
    "data_inicio_operacao": datas_uniformes("2016-01-01", "2024-06-30", N_PARQUES_EOL),
    "status": "Em serviço", "vencimento_concessao": pd.Timestamp("2054-12-31"),
}))
# 2.6 Combinação de negócios 2025 (Mauá)
partes.append(pd.DataFrame({
    "codigo_subconta": "INT-CNB", "tipo_bem": ["Direito de concessão - UHE Mauá (49% adquiridos)",
                                                "Direito de concessão - UHE Mauá (mais-valia alocada)"],
    "custo": [0.7, 0.3], "taxa_regulatoria": np.nan,
    "data_capitalizacao": pd.Timestamp("2025-05-30"), "data_inicio_operacao": pd.Timestamp("2025-05-30"),
    "status": "Em serviço", "vencimento_concessao": pd.Timestamp("2049-06-30"),
}))
# 2.7 Softwares (5.950 demais empresas + 2.000 Copel GeT)
n = 7950
partes.append(pd.DataFrame({
    "codigo_subconta": np.where(np.arange(n) < 2000, "INT-SGT", "INT-SOF"),
    "tipo_bem": rng.choice(["Licença de software", "Sistema desenvolvido internamente",
                            "Módulo ERP", "Licença de cibersegurança"], n, p=[0.6, 0.15, 0.15, 0.10]),
    "custo": lognormal(28000, 1.1, n), "taxa_regulatoria": 0.20,
    "data_capitalizacao": datas_uniformes("2021-01-01", "2025-12-20", n),
    "data_inicio_operacao": pd.NaT, "status": "Em serviço",
    "vencimento_concessao": pd.NaT,
}))

df = pd.concat(partes, ignore_index=True)
SOFT = ["INT-SOF", "INT-SGT"]
df.loc[df["codigo_subconta"].isin(SOFT), "data_inicio_operacao"] = (
    df.loc[df["codigo_subconta"].isin(SOFT), "data_capitalizacao"])

# ---------------------------------------------------------------------------
# 3. Taxa efetiva e amortização acumulada (registros limpos)
#    Regra: amortização linear pelo menor entre vida útil regulatória e o prazo
#    remanescente da concessão (ICPC 01 / CPC 04).
# ---------------------------------------------------------------------------
vida_rem = anos_entre(df["data_inicio_operacao"], df["vencimento_concessao"].fillna(pd.Timestamp("2100-01-01")))
taxa_min = np.where(vida_rem > 0, 1 / np.maximum(vida_rem, 0.5), 1.0)
taxa_reg = df["taxa_regulatoria"].to_numpy()
taxa = np.where(np.isnan(taxa_reg), taxa_min, np.maximum(np.nan_to_num(taxa_reg), taxa_min))
df["taxa_amortizacao_anual"] = np.round(taxa, 6)
df["taxa_minima_prazo_concessao"] = np.round(np.where(df["codigo_subconta"].isin(SOFT), 0.0, taxa_min), 6)
anos_uso = anos_entre(df["data_inicio_operacao"], DATA_BASE)
frac = np.clip(df["taxa_amortizacao_anual"] * anos_uso, 0, 1)
frac = np.where(df["status"] == "Em curso", 0.0, frac)
df["frac_amortizada"] = frac

# ---------------------------------------------------------------------------
# 4. Escala por subconta para atingir o valor líquido-alvo
# ---------------------------------------------------------------------------
for cod, (desc, seg, alvo_mil, origem) in SUBCONTAS.items():
    m = df["codigo_subconta"] == cod
    liq = df.loc[m, "custo"] * (1 - df.loc[m, "frac_amortizada"])
    if cod == "INT-BON":
        # Âncora verificável: Intangível da F.D.A. = R$ 1.849.570 mil (F07, p. 8).
        # Todo o intangível da F.D.A. foi alocado ao registro de Foz do Areia (simplificação).
        idx = df.index[m]
        liq_alvo = np.array([dp.FDA_INTANGIVEL_RS_MIL, 0, 0], dtype=float)
        resto = alvo_mil - dp.FDA_INTANGIVEL_RS_MIL
        liq_alvo[1], liq_alvo[2] = resto * 0.52, resto * 0.48
        df.loc[idx, "custo"] = liq_alvo * 1000 / (1 - df.loc[idx, "frac_amortizada"])
    else:
        fator = alvo_mil * 1000 / liq.sum()
        df.loc[m, "custo"] = df.loc[m, "custo"] * fator

df["custo_historico"] = df["custo"].round(2)
df["amortizacao_acumulada"] = (df["custo_historico"] * df["frac_amortizada"]).round(2)
df["valor_liquido"] = (df["custo_historico"] - df["amortizacao_acumulada"]).round(2)
# Ajuste de centavos por subconta (fora da DIS): cada subconta fecha exatamente no alvo
for cod, (desc, seg, alvo_mil, origem) in SUBCONTAS.items():
    if cod == "INT-DIS":
        continue
    m = df["codigo_subconta"] == cod
    res_c = alvo_mil * 100000 - int((df.loc[m, "valor_liquido"] * 100).round().sum())
    i_max = df.loc[m, "valor_liquido"].idxmax()
    df.at[i_max, "custo_historico"] = round(df.at[i_max, "custo_historico"] + res_c / 100, 2)
    df.at[i_max, "valor_liquido"] = round(df.at[i_max, "valor_liquido"] + res_c / 100, 2)

# ---------------------------------------------------------------------------
# 5. Atributos descritivos
# ---------------------------------------------------------------------------
N = len(df)
desc_map = {k: v[0] for k, v in SUBCONTAS.items()}
seg_map = {k: v[1] for k, v in SUBCONTAS.items()}
orig_map = {k: v[3] for k, v in SUBCONTAS.items()}
df["subconta"] = df["codigo_subconta"].map(desc_map)
df["categoria_ne16"] = df["codigo_subconta"].map(CATEGORIA_NE16)
df["segmento"] = df["codigo_subconta"].map(seg_map)
df["origem"] = df["codigo_subconta"].map(orig_map)
contrato = {"INT-DIS": "CC-DIS-046/1999 (sintético)", "INT-BON": "CC-GER-2024 (sintético)",
            "INT-GSF": "Resolução de extensão (sintético)", "INT-UBP": "CC-UBP (sintético)",
            "INT-EOL": "Portaria de autorização (sintético)", "INT-CNB": "CC-MAUA (sintético)",
            "INT-SOF": "", "INT-SGT": "", "INT-UBE": "CC-UBP Elejor (sintético)",
            "INT-AUO": "Ato de autorização (sintético)"}
df["contrato_concessao"] = df["codigo_subconta"].map(contrato)
m_dis = df["codigo_subconta"] == "INT-DIS"
df["codigo_municipio_sint"] = ""
df.loc[m_dis, "codigo_municipio_sint"] = ["PR-" + f"{x:03d}" for x in rng.integers(1, 395, m_dis.sum())]
df["odi"] = ["ODI-" + f"{x:08d}" for x in rng.integers(1, 99_999_999, N)]
df["lancamento_manual"] = np.where(rng.random(N) < 0.015, "S", "N")
df.loc[df["codigo_subconta"].isin(["INT-BON", "INT-GSF", "INT-UBP", "INT-EOL", "INT-CNB", "INT-UBE", "INT-AUO"]),
       "lancamento_manual"] = "S"
usuarios = [f"USR-{i:02d}" for i in range(1, 41)]
df["usuario_lancamento"] = np.where(df["lancamento_manual"] == "S", rng.choice(usuarios, N), "INTEGRACAO-SIST")
df["data_lancamento"] = df["data_capitalizacao"] + pd.to_timedelta(rng.integers(0, 20, N), unit="D")
df["data_lancamento"] = df["data_lancamento"].where(df["data_lancamento"] <= DATA_BASE, DATA_BASE)

# ---------------------------------------------------------------------------
# 6. Inserção de ERROS (gabarito em log_erros_inseridos.csv)
#    valor_liquido_correto = valor que uma inspeção documental revelaria.
# ---------------------------------------------------------------------------
log = []
disponiveis = set(df.index[m_dis & (df["status"] == "Em serviço")])


def sortear(n, cond=None):
    pool = [i for i in disponiveis if cond is None or cond(i)]
    escolhidos = rng.choice(pool, n, replace=False)
    for i in escolhidos:
        disponiveis.discard(i)
    return list(escolhidos)


def registrar(idx, cod, natureza, correto, afirmacao):
    log.append({"indice": int(idx), "codigo_erro": cod, "natureza": natureza,
                "afirmacao_afetada": afirmacao,
                "valor_liquido_contabil": float(df.at[idx, "valor_liquido"]),
                "valor_liquido_correto": float(round(correto, 2))})


# E02 - amortização acumulada superior ao custo (valor líquido negativo)
for i in sortear(40):
    correto = df.at[i, "valor_liquido"]
    df.at[i, "amortizacao_acumulada"] = round(df.at[i, "custo_historico"] * rng.uniform(1.1, 1.3), 2)
    df.at[i, "valor_liquido"] = round(df.at[i, "custo_historico"] - df.at[i, "amortizacao_acumulada"], 2)
    registrar(i, "E02", "Amortização acumulada superior ao custo (valor líquido negativo)", correto, "Valorização")

# E03 - capitalização posterior à data-base (corte)
for i in sortear(60):
    nova = pd.Timestamp("2026-01-02") + pd.Timedelta(days=int(rng.integers(0, 40)))
    df.at[i, "data_capitalizacao"] = nova
    df.at[i, "data_inicio_operacao"] = nova
    df.at[i, "data_lancamento"] = pd.Timestamp("2025-12-31")
    df.at[i, "amortizacao_acumulada"] = 0.0
    df.at[i, "valor_liquido"] = df.at[i, "custo_historico"]
    registrar(i, "E03", "Bem capitalizado com data posterior a 31/12/2025 (corte)", 0.0, "Existência / Corte")

# E04 - em serviço há mais de 2 anos sem amortização
for i in sortear(80, lambda k: df.at[k, "data_inicio_operacao"] <= pd.Timestamp("2023-06-30")):
    correto = df.at[i, "valor_liquido"]
    df.at[i, "amortizacao_acumulada"] = 0.0
    df.at[i, "valor_liquido"] = df.at[i, "custo_historico"]
    registrar(i, "E04", "Bem em serviço sem amortização registrada", correto, "Valorização")

# E05 - taxa inferior à mínima do prazo da concessão (amortiza além do vencimento)
for i in sortear(70, lambda k: df.at[k, "data_inicio_operacao"] <= pd.Timestamp("2022-12-31")):
    correto = df.at[i, "valor_liquido"]
    tx_err = round(df.at[i, "taxa_minima_prazo_concessao"] * 0.45, 6)
    df.at[i, "taxa_amortizacao_anual"] = tx_err
    anos = anos_entre(pd.Series([df.at[i, "data_inicio_operacao"]]), DATA_BASE)[0]
    df.at[i, "amortizacao_acumulada"] = round(df.at[i, "custo_historico"] * min(1, tx_err * anos), 2)
    df.at[i, "valor_liquido"] = round(df.at[i, "custo_historico"] - df.at[i, "amortizacao_acumulada"], 2)
    registrar(i, "E05", "Taxa de amortização inferior à mínima exigida pelo prazo da concessão", correto,
              "Valorização")

# E06 - campos obrigatórios em branco (sem efeito monetário)
for i in sortear(50):
    df.at[i, "odi"] = ""
    df.at[i, "contrato_concessao"] = ""
    registrar(i, "E06", "Campos obrigatórios (ODI e contrato) em branco", df.at[i, "valor_liquido"],
              "Direitos e obrigações / documentação")

# E07 - lançamentos manuais fictícios logo abaixo da alçada (R$ 1 milhão), fim de exercício
for i in sortear(30):
    v = round(float(rng.uniform(990000, 999999.99)), 2)
    df.at[i, "custo_historico"] = v
    df.at[i, "amortizacao_acumulada"] = 0.0
    df.at[i, "valor_liquido"] = v
    df.at[i, "lancamento_manual"] = "S"
    df.at[i, "usuario_lancamento"] = "USR-99"
    df.at[i, "odi"] = ""
    df.at[i, "data_capitalizacao"] = pd.Timestamp("2025-12-29")
    df.at[i, "data_inicio_operacao"] = pd.Timestamp("2025-12-29")
    df.at[i, "data_lancamento"] = pd.Timestamp("2025-12-30")
    registrar(i, "E07", "Lançamento manual fictício, valor redondo abaixo da alçada, fim de exercício", 0.0,
              "Ocorrência / Existência (indicador de fraude)")

# E08 - bem em curso com amortização
cand = [i for i in df.index[m_dis & (df["status"] == "Em serviço")] if i in disponiveis]
for i in rng.choice(cand, 45, replace=False):
    disponiveis.discard(i)
    df.at[i, "status"] = "Em curso"
    correto = df.at[i, "custo_historico"]           # em curso: não amortiza
    if df.at[i, "amortizacao_acumulada"] == 0:
        df.at[i, "amortizacao_acumulada"] = round(df.at[i, "custo_historico"] * 0.05, 2)
        df.at[i, "valor_liquido"] = round(df.at[i, "custo_historico"] - df.at[i, "amortizacao_acumulada"], 2)
    registrar(i, "E08", "Bem em curso com amortização acumulada", correto, "Valorização")

# E09 - valor líquido divergente de custo menos amortização
for i in sortear(55):
    correto = df.at[i, "valor_liquido"]
    delta = round(float(df.at[i, "custo_historico"] * rng.uniform(0.2, 0.6)), 2)
    df.at[i, "valor_liquido"] = round(df.at[i, "valor_liquido"] + delta, 2)
    registrar(i, "E09", "Valor líquido diverge de custo menos amortização acumulada", correto,
              "Exatidão / Valorização")

# E01 - duplicidades (novas linhas copiando registros existentes)
orig_dup = sortear(150)
dups = df.loc[orig_dup].copy()
dups["data_lancamento"] = dups["data_lancamento"] + pd.to_timedelta(rng.integers(1, 15, len(dups)), unit="D")
dups["data_lancamento"] = dups["data_lancamento"].where(dups["data_lancamento"] <= DATA_BASE, DATA_BASE)
dups.index = range(df.index.max() + 1, df.index.max() + 1 + len(dups))
df = pd.concat([df, dups])
for novo, origem_idx in zip(dups.index, orig_dup):
    log.append({"indice": int(novo), "codigo_erro": "E01",
                "natureza": f"Registro duplicado (cópia do índice {int(origem_idx)})",
                "afirmacao_afetada": "Existência / Ocorrência",
                "valor_liquido_contabil": float(df.at[novo, "valor_liquido"]),
                "valor_liquido_correto": 0.0})

idx_erro = {r["indice"] for r in log} | set(orig_dup)   # originais das duplicidades não são reescalados

# ---------------------------------------------------------------------------
# 7. Ajuste final: o total da base deve igualar o saldo contábil (com erros).
#    A diferença é distribuída proporcionalmente aos registros limpos da DIS.
# ---------------------------------------------------------------------------
limpos = df.index[(df["codigo_subconta"] == "INT-DIS") & (~df.index.isin(idx_erro))
                  & (df["status"] == "Em serviço")]
total_atual = df["valor_liquido"].sum()
fator = 1 + (SALDO_CONTABIL_MIL * 1000 - total_atual) / df.loc[limpos, "valor_liquido"].sum()
df.loc[limpos, "custo_historico"] = (df.loc[limpos, "custo_historico"] * fator).round(2)
df.loc[limpos, "amortizacao_acumulada"] = (df.loc[limpos, "amortizacao_acumulada"] * fator).round(2)
df.loc[limpos, "valor_liquido"] = (df.loc[limpos, "custo_historico"] - df.loc[limpos, "amortizacao_acumulada"]).round(2)
cent = (df["valor_liquido"] * 100).round().astype("int64")
residuo = SALDO_CONTABIL_CENTAVOS - int(cent.sum())
maior = df.loc[limpos, "valor_liquido"].idxmax()
df.at[maior, "custo_historico"] = round(df.at[maior, "custo_historico"] + residuo / 100, 2)
df.at[maior, "valor_liquido"] = round(df.at[maior, "valor_liquido"] + residuo / 100, 2)
assert int((df["valor_liquido"] * 100).round().astype("int64").sum()) == SALDO_CONTABIL_CENTAVOS

# ---------------------------------------------------------------------------
# 8. Embaralhar, criar identificadores e gravar
# ---------------------------------------------------------------------------
df = df.sample(frac=1, random_state=SEED)
df["id_registro"] = [f"SINT-{i:07d}" for i in range(1, len(df) + 1)]
mapa_id = dict(zip(df.index, df["id_registro"]))
df["flag_dado_sintetico"] = "SIM"
df["centro_custo"] = df["segmento"].map({"Copel DIS": "CC-DIS", "Copel GeT": "CC-GET",
                                         "Holding/Diversos": "CC-HOL"})
GET_ANCORA_MIL = 7150619   # F15, NE 15, p. 21
assert sum(v[2] for k, v in SUBCONTAS.items() if v[1] == "Copel GeT") == GET_ANCORA_MIL

colunas = ["id_registro", "flag_dado_sintetico", "segmento", "categoria_ne16", "codigo_subconta", "subconta", "tipo_bem",
           "origem", "contrato_concessao", "vencimento_concessao", "codigo_municipio_sint", "odi",
           "centro_custo", "status", "data_capitalizacao", "data_inicio_operacao", "data_lancamento",
           "lancamento_manual", "usuario_lancamento", "taxa_amortizacao_anual",
           "taxa_minima_prazo_concessao", "custo_historico", "amortizacao_acumulada", "valor_liquido"]
for c in ["vencimento_concessao", "data_capitalizacao", "data_inicio_operacao", "data_lancamento"]:
    df[c] = pd.to_datetime(df[c]).dt.strftime("%Y-%m-%d").fillna("")
saida = df[colunas]
(RAIZ / "dados").mkdir(exist_ok=True)
saida.to_csv(RAIZ / "dados" / "base_intangivel_sintetica.csv.gz", index=False, compression="gzip",
             float_format="%.6f")

log_df = pd.DataFrame(log)
log_df.insert(0, "id_registro", log_df["indice"].map(mapa_id))
log_df["distorcao_inserida"] = (log_df["valor_liquido_contabil"] - log_df["valor_liquido_correto"]).round(2)
log_df = log_df.drop(columns="indice").sort_values(["codigo_erro", "id_registro"])
log_df.insert(1, "flag_dado_sintetico", "SIM")
log_df.to_csv(RAIZ / "dados" / "log_erros_inseridos.csv", index=False)

resumo = {
    "semente": SEED, "linhas": int(len(saida)), "colunas": len(colunas),
    "saldo_contabil_R$mil": SALDO_CONTABIL_MIL,
    "total_base_R$": round(float(saida["valor_liquido"].sum()), 2),
    "diferenca_R$": round(float(saida["valor_liquido"].sum()) - SALDO_CONTABIL_MIL * 1000, 2),
    "erros_inseridos_registros": int(len(log_df)),
    "erros_por_tipo": log_df["codigo_erro"].value_counts().sort_index().to_dict(),
    "distorcao_inserida_liquida_R$": round(float(log_df["distorcao_inserida"].sum()), 2),
    "por_subconta_R$": saida.groupby("codigo_subconta")["valor_liquido"].sum().round(2).to_dict(),
    "linhas_por_subconta": saida["codigo_subconta"].value_counts().to_dict(),
}
(RAIZ / "resultados").mkdir(exist_ok=True)
(RAIZ / "resultados" / "geracao_resumo.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=2))
print(json.dumps(resumo, ensure_ascii=False, indent=2))

# Dicionário de variáveis (dados/dicionario_variaveis.csv e .md)
import estrutura_pt  # noqa: E402
estrutura_pt.gravar_dicionario(RAIZ / "dados")
