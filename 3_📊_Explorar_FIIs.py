import streamlit as st
import requests

st.set_page_config(page_title="Explorar FIIs - InvestFácil", page_icon="📊", layout="wide")

st.title("📊 Explorar FIIs")
st.caption("Dados em tempo real via API pública (brapi.dev).")

# Descrição de FIIs populares: o que cada fundo faz e em que tipo de imóvel/ativo investe
FIIS_INFO = {
    "MXRF11": {
        "nome": "Maxi Renda FII",
        "segmento": "Papel (títulos, CRIs) e cotas de outros FIIs",
        "descricao": "É um dos FIIs mais populares por causa do preço baixo da cota "
                     "(fácil pra quem está começando) e pagamento mensal de rendimentos. "
                     "Investe principalmente em CRIs (Certificados de Recebíveis Imobiliários) "
                     "e cotas de outros fundos imobiliários, funcionando como um fundo mais "
                     "diversificado dentro da categoria 'papel'.",
    },
    "HGLG11": {
        "nome": "CSHG Logística FII",
        "segmento": "Tijolo — galpões logísticos",
        "descricao": "Investe em galpões logísticos e centros de distribuição alugados para "
                     "empresas de e-commerce, transporte e indústria. Quem compra uma cota "
                     "está, na prática, virando 'sócio' desses galpões e recebendo parte do "
                     "aluguel pago pelas empresas locatárias.",
    },
    "KNRI11": {
        "nome": "Kinea Renda Imobiliária FII",
        "segmento": "Tijolo — lajes corporativas e galpões logísticos",
        "descricao": "Um dos fundos mais tradicionais do mercado, com um portfólio misto de "
                     "escritórios (lajes corporativas) e galpões logísticos bem localizados. "
                     "É considerado um fundo mais 'conservador' dentro da renda variável.",
    },
    "XPML11": {
        "nome": "XP Malls FII",
        "segmento": "Tijolo — shopping centers",
        "descricao": "Investe em participações em shopping centers de diversas regiões do "
                     "Brasil. A renda vem do aluguel das lojas dentro dos shoppings, então "
                     "tende a ser mais sensível ao consumo e a datas sazonais (Natal, Dia das Mães etc.).",
    },
    "VISC11": {
        "nome": "Vinci Shopping Centers FII",
        "segmento": "Tijolo — shopping centers",
        "descricao": "Assim como o XPML11, investe em shoppings centers espalhados pelo país. "
                     "É outra opção para quem quer exposição ao varejo físico através de fundos imobiliários.",
    },
    "BCFF11": {
        "nome": "FoF Brasil Plural FII",
        "segmento": "Fundo de Fundos (FOF)",
        "descricao": "É um 'fundo de fundos': em vez de comprar imóveis diretamente, ele compra "
                     "cotas de vários outros FIIs. Isso dá uma diversificação automática em um "
                     "único ativo, o que pode ser interessante para quem quer simplificar a carteira.",
    },
}

tickers_exemplo = list(FIIS_INFO.keys())

with st.expander("ℹ️ O que são esses FIIs? Clique para entender cada um"):
    for ticker, info in FIIS_INFO.items():
        st.markdown(f"**{ticker} — {info['nome']}**  \n"
                    f"*Segmento:* {info['segmento']}  \n"
                    f"{info['descricao']}")
        st.markdown("---")

tickers_input = st.text_input(
    "Digite os tickers dos FIIs separados por vírgula:",
    value=", ".join(tickers_exemplo),
)

if st.button("🔍 Consultar", type="primary"):
    tickers = [t.strip().upper() for t in tickers_input.split(",") if t.strip()]

    if not tickers:
        st.warning("Digite pelo menos um ticker.")
    else:
        with st.spinner("Buscando dados..."):
            resultados = []
            erros = []
            for ticker in tickers:
                try:
                    resp = requests.get(
                        f"https://brapi.dev/api/quote/{ticker}",
                        timeout=10,
                    )
                    data = resp.json()
                    if "results" in data and data["results"]:
                        item = data["results"][0]
                        segmento = FIIS_INFO.get(ticker, {}).get("segmento", "—")
                        resultados.append({
                            "Ticker": ticker,
                            "Segmento": segmento,
                            "Preço (R$)": item.get("regularMarketPrice"),
                            "Variação (%)": item.get("regularMarketChangePercent"),
                            "Máx. dia": item.get("regularMarketDayHigh"),
                            "Mín. dia": item.get("regularMarketDayLow"),
                        })
                    else:
                        erros.append(ticker)
                except Exception:
                    erros.append(ticker)

        if resultados:
            st.dataframe(resultados, use_container_width=True, hide_index=True)
        if erros:
            st.warning(f"Não foi possível obter dados para: {', '.join(erros)}")

st.markdown("---")
st.info(
    "ℹ️ A API gratuita da brapi.dev tem limites de uso. Para uso mais intenso, "
    "considere obter um token gratuito em [brapi.dev](https://brapi.dev)."
)
