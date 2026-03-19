# 📊 Personal Data Pipeline: Calculadora de Produtividade

Este projeto é um ecossistema de dados focado na análise de economia de tempo através da reprodução acelerada de vídeos. Desenvolvido para portfólio, ele aplica conceitos de **Engenharia de Dados** como ingestão, persistência em banco relacional e visualização de KPIs.

## 🚀 Funcionalidades

- **Ingestão de Dados:** Interface gráfica (Tkinter) para entrada de tempos e velocidades.
- **Análise de Dados Relacionais:** Persistência robusta utilizando **SQLite**, permitindo consultas estruturadas e integridade dos dados.
- **Configuração Desacoplada:** Gerenciamento de metas de performance via arquivo `JSON`.
- **Data Analytics:** Scripts que transformam dados brutos do banco em insights de produtividade.
- **Data Visualization:** Gráficos de barras empilhadas com **Matplotlib** comparando tempo real vs. tempo original.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **SQLite3:** Banco de dados relacional (SQL).
- **Pandas:** Manipulação de DataFrames e execução de queries SQL.
- **Matplotlib:** Geração de gráficos estatísticos.
- **JSON:** Armazenamento de parâmetros de configuração.

## 📈 Arquitetura do Pipeline

1. **Coleta:** O usuário insere os dados na interface.
2. **Armazenamento:** Os dados são validados e inseridos na tabela `calculos` do SQLite.
3. **Processamento:** O Pandas lê o banco e o `config.json` para calcular o ROI de tempo.
4. **Visualização:** O sistema gera um dashboard textual e um gráfico comparativo.

## 🔧 Como Executar

1. Clone o repositório.
2. Ative seu ambiente virtual: `source .venv/Scripts/activate`
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute o app principal: `python app.py`

---
**Autor:** Elvis Barros  
*Foco em Engenharia de Dados | SQL | Python | AWS*