#!/usr/bin/env bash
# Reproduz todo o trabalho: base sintética -> testes -> planilhas -> dossiê.
set -euo pipefail
cd "$(dirname "$0")"
python3 01_gerar_base.py
python3 02_testes_auditoria.py
python3 03_planilhas.py
python3 04_dossie_pdf.py
echo "Concluído. Abra a planilha no Excel/LibreOffice para recalcular as fórmulas (ou use recalc do LibreOffice)."
