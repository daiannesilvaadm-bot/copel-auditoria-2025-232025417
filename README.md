# Dossiê de auditoria — COPEL, exercício 2025 (P2)

| | |
|---|---|
| **Estudante** | Daiane da Silva |
| **Matrícula** | 232025417 |
| **Disciplina** | Auditoria — Ciências Contábeis (UnB), trabalho P2 |
| **Companhia** | Companhia Paranaense de Energia — COPEL (CNPJ 76.483.817/0001-20, código CVM 1431-1; B3: CPLE3; NYSE: ELPC) |
| **Exercício** | Demonstrações consolidadas de 31/12/2025, com comparativo de 31/12/2024 |
| **Data de consulta das fontes** | 24/10/2026 |
| **Auditor independente da companhia** | PricewaterhouseCoopers Auditores Independentes Ltda. |

> **Natureza do trabalho.** Trabalho acadêmico feito integralmente com apoio de inteligência artificial, a partir de documentos públicos. **Não é relatório de auditoria e não contém opinião profissional independente.** Os dados da pasta `dados/` são **sintéticos**: foram gerados por código, estão marcados (`flag_dado_sintetico = SIM`, identificadores `SINT-`) e não são registros reais da COPEL.

## Onde está cada entrega exigida (enunciado, item 6)

| Exigência | Arquivo |
|---|---|
| Dossiê em PDF, com papéis de trabalho e referências cruzadas | `dossie/Dossie_Auditoria_COPEL_2025_232025417.pdf` |
| Base simulada com no mínimo 500.000 linhas | `dados/base_intangivel_sintetica.csv.gz` (520.165 linhas, 24 colunas, ~22 MB) |
| Dicionário de variáveis | `dados/dicionario_variaveis.md` e `.csv` |
| Registro dos erros inseridos (gabarito) | `dados/log_erros_inseridos.csv` |
| Código de geração e análise | `codigo/` (ver "Reprodução") |
| Planilhas editáveis: materialidade, amostra, análises, conciliações | `planilhas/PT_calculos_COPEL_2025.xlsx` |
| Matriz de cobertura das normas | `docs/matriz_cobertura.md` e `.csv`; aba `Matriz_Cobertura`; PT MC do dossiê |
| Relação das fontes, com links, páginas e data de acesso | `docs/fontes.md`; aba `Fontes`; Apêndice C do dossiê |
| Resultados dos testes | `resultados/` |

## Organização do repositório

```
README.md
requirements.txt
dossie/       Dossie_Auditoria_COPEL_2025_232025417.pdf
dados/        base_intangivel_sintetica.csv.gz | log_erros_inseridos.csv | dicionario_variaveis.(md|csv)
codigo/       dados_publicos.py      números públicos (fonte única, com página de cada dado)
              estrutura_pt.py        lista de PT, versões das normas, dicionário
              01_gerar_base.py       gera a base sintética e o gabarito de erros
              02_testes_auditoria.py testes T01–T11 (CAAT e amostragem MUS) e comparação inseridos x detectados
              03_planilhas.py        gera a planilha editável e a matriz de cobertura
              dossie_conteudo.py     texto dos papéis de trabalho
              04_dossie_pdf.py       gera o PDF
              rodar_tudo.sh          executa 01 → 04
planilhas/    PT_calculos_COPEL_2025.xlsx
resultados/   resultados_testes.json | excecoes_detectadas.csv | amostra_mus.csv
              erros_inseridos_x_detectados.csv | matriz_inseridos_detectados.csv | falsos_positivos.csv
              geracao_resumo.json
docs/         fontes.md | matriz_cobertura.(md|csv)
```

## Estrutura do dossiê

Os papéis seguem os **códigos do roteiro obrigatório (item 5 do enunciado)**: PT EC e PT 200 a PT 600, um por norma. Cada papel transcreve a atividade exigida no campo "Atividade exigida (roteiro)" e traz os anexos que ela pede, como minutas, matrizes, cronograma, mapas e cálculos.

| Parte | PT | Conteúdo |
|---|---|---|
| A | PT 000, PT EC | Identificação, fontes, mudanças de nome e de código de negociação; Estrutura Conceitual |
| B | PT 200, 210, 220, 230, 240, 250, 260, 265 | Princípios e responsabilidades (minutas de carta de contratação e de comunicação; matriz de deficiências) |
| C | PT 300, 315.1, 315.2, 320, 330, 402, 450 | Planejamento, entendimento, matriz de riscos, materialidade, respostas, prestadores de serviço, mapa de distorções |
| D | PT 500.1, 500.2, 501, 505, 510, 520, 530, 540, 550, 560, 570, 580 | Evidência e limitações, itens específicos, modelos de confirmação, saldos iniciais, expectativas, amostragem, estimativas com sensibilidade, partes relacionadas, eventos subsequentes, continuidade, minuta de representação |
| E | PT 600 | Grupo, componentes, consolidação e materialidade dos componentes |
| F | PT PA-01 a PA-06 | Programas: receitas, disponibilidades, estoques, imobilizado/intangível, passivos, estimativas |
| G | PT BS-01 a BS-06 | Base simulada: escolha da conta, método, dicionário, conciliação, testes, inseridos x detectados |
| H | PT RA, PT CI, PT MC | Relatório do auditor publicado, conclusão integrada, matriz de cobertura |

Cada procedimento aparece classificado como **R** (realizado com evidência pública), **P** (planejado por falta de acesso) ou **S** (simulado com dados sintéticos). No texto, **[F]** marca fato verificado em fonte, **[J]** marca julgamento ou inferência e **[S]** marca resultado sintético.

## Base simulada (resumo)

- **Conta:** Intangível consolidado, R$ 19.206.609 mil em 31/12/2025, a maior conta do ativo (31,8%). Fonte: release 4T25, Anexo I, p. 24 (F01).
- **Registros:** 520.165 bens e direitos de concessão (512.150 da distribuição, 7.950 softwares e 65 direitos de geração e autorização). **Âncoras reais:** as quatro categorias do intangível da nota 16 das DFs de 2025 (F17), o subtotal da Copel GeT da nota 15 da ITR 1T26 (F15) e o intangível da F.D.A. (F07). Só a divisão interna da geração na Copel GeT é **hipótese didática**.
- **Conciliação:** o total da base, cada categoria da nota 16 e o subtotal da Copel GeT batem ao centavo com os saldos publicados (diferença R$ 0,00).
- **Erros inseridos:** 580 registros de 9 tipos (E01 a E09), com distorção líquida de R$ 33,9 milhões. Os testes sobre 100% da base detectaram todos, sem falsos positivos. A amostra MUS (n = 603, intervalo de R$ 31,9 milhões) encontrou 2 dos 30 lançamentos fictícios, projetou um limite superior (R$ 200,5 milhões) acima do tolerável e levou à extensão dos testes.

## Reprodução

Requisitos: Python 3.10 ou superior. Fontes DejaVu, para o PDF (pacote `fonts-dejavu` no Linux).

```bash
pip install -r requirements.txt
cd codigo
bash rodar_tudo.sh          # (python3) ou execute 01, 02, 03 e 04 em sequência
```

- A semente fixa `232025417` garante a mesma base, os mesmos erros e a mesma amostra em qualquer execução. A geração leva cerca de 1 minuto.
- A planilha é gravada com fórmulas e sem valores em cache. Ao abrir no Excel ou no LibreOffice, ela recalcula sozinha. As células de checagem devem mostrar "Confere com publicado" e "Planilha = código".
- O arquivo da base tem cerca de 22 MB compactado, abaixo do limite de 100 MB do GitHub, por isso fica no próprio repositório. Se for preciso removê-lo, basta rodar `01_gerar_base.py`, que o recria de forma idêntica.

## Principais limitações

Sem acesso a registros, sistemas, contratos, administração, advogados ou auditores. Nenhuma confirmação, entrevista, inspeção física ou acesso a sistema foi realizado. As DFs anuais completas da holding (F17) foram lidas integralmente: notas 1 a 38, relatório do Comitê de Auditoria, parecer do Conselho Fiscal e relatório da PwC com os três principais assuntos de auditoria. O arquivo do RI foi conferido com a DFP versão 1 entregue à CVM (F18), sem divergência; as tabelas por segmento não foram recalculadas. Os detalhes estão no PT 500.2 e no PT CI.
