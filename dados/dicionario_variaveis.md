# Dicionário de variáveis - base sintética do Intangível (COPEL 2025)

**DADOS SINTÉTICOS PARA FINS DIDÁTICOS - não são registros reais da companhia.** Arquivo: `dados/base_intangivel_sintetica.csv.gz` (CSV, UTF-8, separador vírgula, decimal ponto).

| Variável | Tipo | Descrição | Regra de geração |
|---|---|---|---|
| `id_registro` | texto | Identificador único do registro sintético (SINT-0000001 ...). | Sequencial após embaralhamento. |
| `flag_dado_sintetico` | texto | Marca obrigatória: SIM = dado sintético, não é registro real da COPEL. | Constante. |
| `segmento` | texto | Empresa/segmento: Copel DIS, Copel GeT ou Holding/Diversos. | Derivado da subconta. |
| `categoria_ne16` | texto | Categoria do intangível conforme a nota 16 das DFs (Distribuição, Geração, Direito de concessão e autorização, Outros intangíveis). | Derivada da subconta; totais iguais aos da NE 16 (F17). |
| `codigo_subconta` | texto | Código da subconta do intangível (INT-DIS, BON, GSF, UBP, CNB, UBE, EOL, AUO, SGT, SOF). | Categorias e subtotal GeT reais (F17, F15); divisão interna da geração hipotética (PT BS-02). |
| `subconta` | texto | Descrição da subconta. | Derivado. |
| `tipo_bem` | texto | Tipo de bem ou direito (ex.: transformador de distribuição, bônus de outorga de usina). | Lista de 10 tipos na distribuição; nomes de usinas reais nos direitos de geração. |
| `origem` | texto | Origem contábil (transferência de ativo de contrato, bônus de outorga, combinação de negócios etc.). | Derivado da subconta. |
| `contrato_concessao` | texto | Contrato ou ato de outorga (identificadores sintéticos). | Constante por subconta; vazio em softwares e nos erros E06/E07. |
| `vencimento_concessao` | data | Fim do prazo da concessão/autorização (AAAA-MM-DD). | DIS 2045-07-07 (F01); bônus 2054-11-20 (F07); demais hipotéticos. |
| `codigo_municipio_sint` | texto | Município sintético PR-001 a PR-394 (só distribuição). | Uniforme. |
| `odi` | texto | Ordem de imobilização sintética. | Aleatório; vazio nos erros E06/E07. |
| `centro_custo` | texto | Centro de custo (CC-DIS, CC-GET, CC-HOL). | Derivado do segmento. |
| `status` | texto | Em serviço ou Em curso. | 0,4% em curso na distribuição; E08 altera. |
| `data_capitalizacao` | data | Data de capitalização do bem. | Até 45 dias antes do início de operação; E03 após 31/12/2025. |
| `data_inicio_operacao` | data | Início de operação (base da amortização). | Uniforme por tipo de bem (2008-2025). |
| `data_lancamento` | data | Data do lançamento contábil. | Até 20 dias após a capitalização, limitada a 31/12/2025. |
| `lancamento_manual` | texto | S = lançamento manual; N = integração de sistema. | 1,5% manuais; direitos de geração manuais. |
| `usuario_lancamento` | texto | Usuário do lançamento (USR-01 a USR-40; USR-99 = usuário raro dos erros E07). | Aleatório entre 40 usuários. |
| `taxa_amortizacao_anual` | decimal | Taxa anual de amortização aplicada. | Maior entre a taxa regulatória do tipo de bem e 1/prazo remanescente; E05 altera. |
| `taxa_minima_prazo_concessao` | decimal | Taxa mínima para amortizar até o fim da concessão (1/anos remanescentes no início de operação). | Calculada. |
| `custo_historico` | decimal (R$) | Custo do bem em reais. | Lognormal por tipo, escalado para o alvo da subconta. |
| `amortizacao_acumulada` | decimal (R$) | Amortização acumulada até 31/12/2025 em reais. | custo x min(1, taxa x anos em serviço); zero se em curso. |
| `valor_liquido` | decimal (R$) | Valor contábil líquido em reais (soma = R$ 19.206.609.000,00). | custo - amortização (salvo erros E09). |
