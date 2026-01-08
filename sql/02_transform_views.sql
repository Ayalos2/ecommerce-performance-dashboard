CREATE OR REPLACE VIEW `ecommerce_dw.f_vendas` AS
SELECT
    venda_id,
    data as data_venda,
    produto,
    categoria_produto,
    canal,
    campanha,
    CAST(receita AS FLOAT64) as receita,
    CAST(custo AS FLOAT64) as custo,
    CAST(custo_marketing AS FLOAT64) as custo_marketing,
    (CAST(receita AS FLOAT64) - (CAST(custo AS FLOAT64) + CAST(custo_marketing AS FLOAT64))) as lucro_liquido
FROM `ecommerce_dw.vendas_ecommerce`;