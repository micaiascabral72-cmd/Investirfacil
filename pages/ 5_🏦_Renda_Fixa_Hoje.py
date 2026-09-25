import streamlit as st
import requests

st.set_page_config(page_title="Renda Fixa Hoje - InvestFácil", page_icon="🏦", layout="wide")

st.title("🏦 Renda Fixa Hoje")
st.caption("Taxas atualizadas via API do Banco Central (SGS).")

# Códigos das séries no SGS/BCB
SERIES = {
    "Taxa Selic (% a.a.)": 432,
    "CDI (% a.a.)": 4389,
    "IPCA acumulado 12 meses (%)": 13522,
}


def buscar_serie(codigo, qtd=1):
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados/ultimos/{qtd}?formato=json"
    resp = requests.get(url, timeout=10)
    return resp.json()


col1, col2, col3 = st.columns(3)
colunas = [col1, col2, col3]

for (nome, codigo), coluna in zip(SERIES.items(), colunas):
    try:
        dados = buscar_serie(codigo)
        if dados:
            valor = dados[-1]["valor"]
            data_ref = dados[-1]["data"]
            coluna.metric(nome, f"{valor}%", help=f"Referente a {data_ref}")
        else:
            coluna.metric(nome, "—")
    except Exception:
        coluna.metric(nome, "Indisponível")

st.markdown("---")

st.subheader("O que essas taxas significam?")
st.markdown("""
- **Selic** — taxa básica de juros da economia, define o piso de rendimento do
  Tesouro Selic e influencia todas as outras taxas de renda fixa.
- **CDI** — taxa usada como referência para CDBs, LCIs e LCAs. A maioria das
  ofertas de renda fixa é anunciada como "% do CDI" (ex: 110% do CDI).
- **IPCA** — índice oficial de inflação. Títulos como o **Tesouro IPCA+** pagam
  esse índice mais uma taxa fixa, protegendo o poder de compra no longo prazo.
""")

st.info(
    "💡 Dica: quanto mais próxima do CDI (ou acima de 100% do CDI) for a taxa "
    "de um CDB, melhor tende a ser a oferta em relação à média do mercado."
)
