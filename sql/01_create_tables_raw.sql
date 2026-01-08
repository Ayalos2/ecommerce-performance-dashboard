CREATE TABLE ecommerce_dw.tb_vendas_final (
    venda_id INT64,
    data DATE,
    produto STRING,
    categoria_produto STRING,
    canal STRING,
    campanha STRING,
    receita FLOAT64,
    custo FLOAT64,
    custo_marketing FLOAT64
);