--KPI Geral
SELECT
    COUNT(DISTINCT venda_id) AS total_pedidos,
    ROUND(SUM(receita), 2) AS receita_total,
    ROUND(SUM(lucro_liquido), 2) AS lucro_total,
    ROUND((SUM(lucro_liquido) / SUM(receita)) * 100, 2) AS margem_liquida_percentual
FROM `ecommerce_dw.f_vendas`;

--Analise Temporal
SELECT
    DATE_TRUNC(data_venda, MONTH) AS mes_referencia,
    ROUND(SUM(receita), 2) AS receita,
    ROUND(SUM(lucro_liquido), 2) AS lucro,
    ROUND((SUM(lucro_liquido) / SUM(receita)) * 100, 2) AS margem_pct
FROM `ecommerce_dw.f_vendas`
GROUP BY 1
ORDER BY 1;

--Matriz de Eficiência
SELECT
    canal,
    COUNT(venda_id) AS qtd_vendas,
    ROUND(SUM(receita), 2) AS faturamento,
    ROUND(SUM(custo_marketing), 2) AS gasto_marketing,
    ROUND((SUM(lucro_liquido) / SUM(receita)) * 100, 1) AS margem_pct
FROM `ecommerce_dw.f_vendas`
GROUP BY 1
ORDER BY margem_pct DESC;