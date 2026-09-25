# 💰 InvestFácil

App educacional em Streamlit para ajudar iniciantes a entender e simular
investimentos em Fundos Imobiliários (FIIs), Renda Fixa e outras opções.

## Funcionalidades

- 📚 **Aprenda** — conceitos básicos explicados de forma simples
- 🧮 **Simuladores** — juros compostos e comparador Renda Fixa vs FII
- 📊 **Explorar FIIs** — cotações em tempo real via [brapi.dev](https://brapi.dev)
- 🎯 **Perfil de Investidor** — quiz rápido que sugere um perfil e alocação exemplo

> ⚠️ Este app tem finalidade **educacional** e não constitui recomendação de investimento.

## Como rodar localmente

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Como publicar no GitHub + Streamlit Community Cloud

1. Crie um repositório no GitHub e envie todos os arquivos deste projeto.
2. Acesse [share.streamlit.io](https://share.streamlit.io).
3. Clique em **New app**, selecione o repositório e o arquivo `app.py`.
4. Clique em **Deploy** — pronto, seu app estará no ar!

## Estrutura do projeto

```
investfacil/
├── app.py                      # Página inicial
├── pages/
│   ├── 1_📚_Aprenda.py
│   ├── 2_🧮_Simuladores.py
│   ├── 3_📊_Explorar_FIIs.py
│   └── 4_🎯_Perfil_Investidor.py
├── requirements.txt
└── README.md
```

## Próximos passos possíveis

- Adicionar dados de Tesouro Direto / Selic via API do Banco Central (SGS)
- Gráficos de histórico de preço dos FIIs
- Comparador entre múltiplos FIIs lado a lado
- Glossário de termos financeiros pesquisável
