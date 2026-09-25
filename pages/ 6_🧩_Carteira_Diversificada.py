import streamlit as st

st.set_page_config(page_title="Carteira Diversificada - InvestFácil", page_icon="🧩", layout="wide")

st.title("🧩 Montando uma Carteira Diversificada")
st.markdown("""
Diversificar significa **não colocar todo o dinheiro em um único tipo de investimento**,
reduzindo o risco de perdas concentradas. Veja como pensar na diversificação
tanto dentro de FIIs quanto entre Renda Fixa e Renda Variável.
""")

st.subheader("1. Diversificando entre segmentos de FIIs")
st.markdown("""
Dentro dos fundos imobiliários, existem diferentes segmentos, e cada um reage
de um jeito diferente à economia:

| Segmento | O que é | Exemplo |
|---|---|---|
| 🏢 Lajes corporativas | Prédios de escritórios alugados para empresas | KNRI11 |
| 📦 Logística | Galpões de e-commerce e distribuição | HGLG11 |
| 🛍️ Shoppings | Participação em shopping centers | XPML11, VISC11 |
| 📄 Papel (CRI) | Títulos de dívida ligados ao setor imobiliário | MXRF11 |
| 🧺 Fundo de Fundos (FOF) | Compra cotas de outros FIIs | BCFF11 |

Uma carteira diversificada de FIIs costuma combinar **pelo menos 2 ou 3 segmentos
diferentes**, evitando depender de um único tipo de imóvel ou inquilino.
""")

st.subheader("2. Equilibrando Renda Fixa e Renda Variável (FIIs)")
st.markdown("""
Não existe uma regra única — depende do seu **perfil de investidor** e do seu
**objetivo** — mas alguns exemplos didáticos de composição:
""")

perfil = st.radio(
    "Veja um exemplo de composição por perfil:",
    ["Conservador", "Moderado", "Arrojado"],
    horizontal=True,
)

exemplos = {
    "Conservador": {
        "Renda Fixa (Tesouro Selic, CDB liquidez diária)": 70,
        "Renda Fixa (CDB/LCI prazo maior)": 20,
        "FIIs diversificados": 10,
    },
    "Moderado": {
        "Renda Fixa (Tesouro Selic/IPCA+)": 40,
        "Renda Fixa (CDB/LCI prazo maior)": 20,
        "FIIs de tijolo (logística, lajes)": 25,
        "FIIs de papel": 15,
    },
    "Arrojado": {
        "Renda Fixa (reserva de emergência)": 20,
        "FIIs de tijolo (logística, shoppings, lajes)": 40,
        "FIIs de papel e FOFs": 30,
        "Outros (ações, ETFs, etc.)": 10,
    },
}

composicao = exemplos[perfil]
for item, pct in composicao.items():
    st.progress(pct / 100, text=f"{item} — {pct}%")

st.warning(
    "⚠️ Estes são exemplos **didáticos e simplificados**, não recomendações "
    "personalizadas. O ideal é ajustar a composição conforme sua reserva de "
    "emergência, prazo dos objetivos e tolerância a risco — se possível, com "
    "ajuda de um profissional certificado."
)

st.subheader("3. Boas práticas gerais de diversificação")
st.markdown("""
- 🛟 **Tenha uma reserva de emergência** em renda fixa de alta liquidez antes de
  investir em FIIs ou renda variável.
- 🏗️ **Não concentre tudo em um segmento** de FII (ex: só shoppings) — misture
  tijolo, papel e, se quiser, fundos de fundos.
- 🏦 **Não concentre tudo em um único banco/emissor** na renda fixa — respeite
  o limite de R$ 250 mil por CPF/instituição garantido pelo FGC.
- 📅 **Reavalie periodicamente** — sua carteira deve evoluir conforme seus
  objetivos e o cenário econômico mudam.
""")
