# 📊 Dashboard Executivo de Performance (E-commerce)

## 🏢 Visão Geral do Negócio
Projeto de Business Intelligence end-to-end desenvolvido para monitorar a saúde financeira de um e-commerce fictício. O objetivo foi sair da análise operacional e entregar indicadores táticos para C-Level, focando em **Margem Líquida**, **Eficiência de Canal (ROI)** e **Sazonalidade**.

**Link para o Dashboard Interativo:** [Insira o link do Looker Studio aqui]

![Dashboard Preview](assets/dashboard_screenshot.png)

## 🛠️ Arquitetura da Solução
A solução foi arquitetada focando em escalabilidade e baixo custo, utilizando o stack moderno de dados (ELT).

* **Ingestão:** Script Python (`faker`/`pandas`) simulando transações realistas (+1.500 linhas) com variância sazonal.
* **Data Warehouse:** Google BigQuery.
* **Modelagem:** Star Schema (Esquema Estrela) implementado via SQL Views para otimizar a performance de leitura.
* **Visualização:** Looker Studio conectado diretamente ao BigQuery (Live Connection).

## 🧠 Principais Insights (Storytelling)
1.  **O Paradoxo do Tráfego Pago:** Identificado via Gráfico de Dispersão que o canal "Influencers" possui o maior CAC (Custo de Aquisição) com o menor retorno, sugerindo corte imediato.
2.  **Sazonalidade:** Pico de vendas em Outubro/Novembro, mas com queda na margem devido ao aumento de custos de ads (Black Friday).
3.  **Hero Product:** O "Notebook Pro" representa 40% da receita, indicando risco de concentração de portfólio.

## 💻 Como Reproduzir
1.  Execute `notebooks/data_generator.py` para gerar o CSV.
2.  Carregue o CSV no Google BigQuery.
3.  Execute os scripts na pasta `/sql` para criar as Views Dimensionais.
4.  Conecte o Looker Studio à View `f_vendas`.


<img width="1404" height="918" alt="dashboard_screeshot" src="https://github.com/user-attachments/assets/068bbabc-4426-405c-9b0e-98774d3b2462" />

---
*Projeto desenvolvido por Reginaldo Ayalos - 2026*
