import streamlit as st

st.set_page_config(page_title="Perfil de Investidor - InvestFácil", page_icon="🎯", layout="wide")

st.title("🎯 Descubra seu Perfil de Investidor")
st.caption("Um quiz rápido e simplificado — não substitui uma análise profissional.")

with st.form("quiz_perfil"):
    q1 = st.radio(
        "1. Se seus investimentos caíssem 15% em um mês, você...",
        ["Ficaria muito preocupado(a) e venderia tudo", "Ficaria incomodado(a), mas esperaria",
         "Veria como oportunidade de comprar mais"],
    )
    q2 = st.radio(
        "2. Por quanto tempo pretende deixar o dinheiro investido?",
        ["Menos de 1 ano", "Entre 1 e 5 anos", "Mais de 5 anos"],
    )
    q3 = st.radio(
        "3. Qual seu conhecimento sobre investimentos?",
        ["Iniciante", "Intermediário", "Avançado"],
    )
    q4 = st.radio(
        "4. Qual seu principal objetivo?",
        ["Segurança e preservar o capital", "Equilíbrio entre segurança e crescimento",
         "Maximizar retorno, aceitando mais risco"],
    )
    enviado = st.form_submit_button("Ver resultado")

if enviado:
    pontos = 0
    pontos += ["Ficaria muito preocupado(a) e venderia tudo", "Ficaria incomodado(a), mas esperaria",
               "Veria como oportunidade de comprar mais"].index(q1)
    pontos += ["Menos de 1 ano", "Entre 1 e 5 anos", "Mais de 5 anos"].index(q2)
    pontos += ["Iniciante", "Intermediário", "Avançado"].index(q3)
    pontos += ["Segurança e preservar o capital", "Equilíbrio entre segurança e crescimento",
               "Maximizar retorno, aceitando mais risco"].index(q4)

    if pontos <= 3:
        perfil = "Conservador"
        sugestao = "Tesouro Selic, CDB de liquidez diária, LCI/LCA — foco em segurança e liquidez."
    elif pontos <= 7:
        perfil = "Moderado"
        sugestao = "Mistura de Renda Fixa (Tesouro IPCA+, CDB) com uma parcela em FIIs de tijolo/papel."
    else:
        perfil = "Arrojado"
        sugestao = "Maior parcela em FIIs e outros ativos de maior risco/retorno, com uma reserva em Renda Fixa."

    st.success(f"### Seu perfil: **{perfil}**")
    st.write(f"**Sugestão de alocação exemplo:** {sugestao}")
    st.warning(
        "⚠️ Este resultado é apenas educacional e simplificado. Para uma análise de "
        "perfil de investidor completa e válida, consulte sua corretora ou um profissional certificado."
    )
