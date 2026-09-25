import streamlit as st

st.set_page_config(
    page_title="InvestFácil",
    page_icon="💰",
    layout="wide",
)

st.title("💰 InvestFácil")
st.subheader("Seu primeiro passo no mundo dos investimentos")

st.markdown("""
Bem-vindo(a)! Este app foi criado para ajudar quem está **começando a investir**
a entender melhor **Fundos Imobiliários (FIIs)**, **Renda Fixa** e outras opções
disponíveis no mercado brasileiro.

### O que você encontra aqui:

- 📚 **Aprenda** — conceitos explicados de forma simples
- 🧮 **Simuladores** — calcule rendimentos e compare opções
- 📊 **Explorar FIIs** — dados em tempo real de fundos imobiliários
- 🎯 **Perfil de Investidor** — descubra seu perfil e veja sugestões de alocação

Use o menu ao lado para navegar entre as seções.
""")

st.warning(
    "⚠️ **Aviso importante:** este app tem finalidade **educacional** e não "
    "constitui recomendação de investimento. Rentabilidade passada não garante "
    "rentabilidade futura. Consulte um profissional certificado antes de investir."
)

st.markdown("---")
st.caption("Feito com Streamlit • Dados: brapi.dev e Banco Central do Brasil (SGS)")
