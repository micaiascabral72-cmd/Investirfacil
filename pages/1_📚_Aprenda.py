import streamlit as st

st.set_page_config(page_title="Aprenda - InvestFácil", page_icon="📚", layout="wide")

st.title("📚 Aprenda")
st.markdown("Conceitos essenciais para quem está começando a investir.")

tema = st.selectbox(
    "Escolha um tema:",
    [
        "O que é Renda Fixa?",
        "O que é um FII (Fundo Imobiliário)?",
        "Tesouro Direto",
        "CDB, LCI e LCA",
        "Dividend Yield (DY)",
        "Imposto de Renda em investimentos",
    ],
)

conteudo = {
    "O que é Renda Fixa?": """
### Renda Fixa

Na renda fixa, você **empresta dinheiro** para uma instituição (governo, banco ou
empresa) e recebe de volta com juros combinados previamente (fixos) ou atrelados
a um indexador (como o CDI ou a inflação).

**Vantagens:** previsibilidade, menor risco, boa para reserva de emergência.

**Exemplos:** Tesouro Direto, CDB, LCI, LCA, Debêntures.
""",
    "O que é um FII (Fundo Imobiliário)?": """
### Fundo de Investimento Imobiliário (FII)

Um FII reúne o dinheiro de vários investidores para investir em imóveis
(shoppings, galpões logísticos, agências, lajes corporativas) ou em títulos
ligados ao setor imobiliário (CRIs).

Você compra **cotas** do fundo na bolsa, assim como uma ação, e recebe
**rendimentos mensais** (geralmente isentos de Imposto de Renda para pessoa física).

**Vantagens:** renda passiva mensal, acesso ao mercado imobiliário com pouco dinheiro,
liquidez maior que comprar um imóvel diretamente.

**Riscos:** oscilação do preço da cota, vacância dos imóveis, risco do gestor.
""",
    "Tesouro Direto": """
### Tesouro Direto

Programa do governo federal que permite investir em títulos públicos com
valores a partir de poucos reais.

**Principais tipos:**
- **Tesouro Selic** — acompanha a taxa Selic, ótimo para reserva de emergência
- **Tesouro Prefixado** — taxa combinada no momento da compra
- **Tesouro IPCA+** — protege contra a inflação, bom para objetivos de longo prazo
""",
    "CDB, LCI e LCA": """
### CDB, LCI e LCA

- **CDB (Certificado de Depósito Bancário):** você empresta dinheiro para um banco.
  Tem Imposto de Renda regressivo (quanto mais tempo, menor a alíquota).
- **LCI/LCA (Letra de Crédito Imobiliário/Agronegócio):** parecidos com o CDB, mas
  **isentos de Imposto de Renda** para pessoa física. Costumam ter prazo mínimo de carência.

Todos costumam ser protegidos pelo **FGC** (Fundo Garantidor de Créditos) até R$ 250 mil por CPF/instituição.
""",
    "Dividend Yield (DY)": """
### Dividend Yield (DY)

É o percentual que representa quanto um investimento pagou em rendimentos/dividendos
em relação ao seu preço, geralmente calculado em base anual.

**Fórmula simples:**

DY = (Rendimento distribuído no período ÷ Preço da cota ou ação) × 100

Um DY mais alto não significa necessariamente um investimento melhor — é importante
olhar a sustentabilidade desse rendimento no tempo.
""",
    "Imposto de Renda em investimentos": """
### Imposto de Renda

- **FIIs:** rendimentos mensais geralmente isentos de IR para pessoa física (com regras
  específicas). Ganho de capital na venda da cota é tributado em 20%.
- **Renda Fixa (CDB, Tesouro):** tributação regressiva conforme o tempo:
  - Até 180 dias: 22,5%
  - 181 a 360 dias: 20%
  - 361 a 720 dias: 17,5%
  - Acima de 720 dias: 15%
- **LCI/LCA:** isentos de IR para pessoa física.

*Sempre confira a legislação vigente, pois regras tributárias podem mudar.*
""",
}

st.markdown(conteudo[tema])
