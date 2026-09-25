import streamlit as st

st.set_page_config(page_title="Simuladores - InvestFácil", page_icon="🧮", layout="wide")

st.title("🧮 Simuladores")

aba1, aba2 = st.tabs(["Juros Compostos", "Renda Fixa vs FII"])

# ---------- Simulador de Juros Compostos ----------
with aba1:
    st.subheader("Simulador de Juros Compostos")
    st.caption("Veja como seu dinheiro pode crescer ao longo do tempo.")

    col1, col2 = st.columns(2)
    with col1:
        valor_inicial = st.number_input("Valor inicial (R$)", min_value=0.0, value=1000.0, step=100.0)
        aporte_mensal = st.number_input("Aporte mensal (R$)", min_value=0.0, value=200.0, step=50.0)
    with col2:
        taxa_anual = st.number_input("Taxa de juros anual (%)", min_value=0.0, value=10.0, step=0.5)
        meses = st.slider("Período (meses)", min_value=1, max_value=480, value=60)

    taxa_mensal = (1 + taxa_anual / 100) ** (1 / 12) - 1

    saldo = valor_inicial
    total_investido = valor_inicial
    historico = []
    for mes in range(1, meses + 1):
        saldo = saldo * (1 + taxa_mensal) + aporte_mensal
        total_investido += aporte_mensal
        historico.append(saldo)

    rendimento = saldo - total_investido

    c1, c2, c3 = st.columns(3)
    c1.metric("Total investido", f"R$ {total_investido:,.2f}")
    c2.metric("Rendimento estimado", f"R$ {rendimento:,.2f}")
    c3.metric("Valor final", f"R$ {saldo:,.2f}")

    st.line_chart(historico)

# ---------- Comparador Renda Fixa vs FII ----------
with aba2:
    st.subheader("Comparador: Renda Fixa vs FII")
    st.caption("Comparação simplificada — não considera oscilação de preço da cota nem impostos.")

    valor = st.number_input("Valor a investir (R$)", min_value=0.0, value=10000.0, step=500.0, key="comp_valor")
    col1, col2 = st.columns(2)
    with col1:
        taxa_rf = st.number_input("Taxa anual da Renda Fixa (%)", min_value=0.0, value=11.0, step=0.5)
    with col2:
        dy_fii = st.number_input("Dividend Yield anual do FII (%)", min_value=0.0, value=9.0, step=0.5)

    anos = st.slider("Período (anos)", min_value=1, max_value=30, value=5, key="comp_anos")

    resultado_rf = valor * (1 + taxa_rf / 100) ** anos
    resultado_fii_renda = valor * (dy_fii / 100) * anos  # renda distribuída, sem reinvestir

    c1, c2 = st.columns(2)
    c1.metric(f"Renda Fixa em {anos} anos (com juros compostos)", f"R$ {resultado_rf:,.2f}")
    c2.metric(f"FII — renda distribuída em {anos} anos (sem reinvestir)", f"R$ {resultado_fii_renda:,.2f}")

    st.info(
        "💡 No FII, além da renda distribuída mensalmente, o valor da cota também pode "
        "se valorizar (ou desvalorizar) — isso não está incluído nesta simulação."
    )
