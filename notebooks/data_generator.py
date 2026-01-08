import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configuração
np.random.seed(42)
num_registros = 1500
data_inicio = datetime(2024, 1, 1)

# Listas de Domínio
produtos = [
    {'nome': 'Notebook Pro', 'cat': 'Eletrônicos', 'base_price': 3500},
    {'nome': 'Smartphone X', 'cat': 'Eletrônicos', 'base_price': 2000},
    {'nome': 'Monitor 27"', 'cat': 'Periféricos', 'base_price': 1200},
    {'nome': 'Cadeira Gamer', 'cat': 'Móveis', 'base_price': 800},
    {'nome': 'Teclado Mecânico', 'cat': 'Periféricos', 'base_price': 300},
    {'nome': 'Mesa Escritório', 'cat': 'Móveis', 'base_price': 600}
]

canais = ['Google Ads', 'Facebook Ads', 'Email Marketing', 'Orgânico', 'Influencers']
campanhas = ['Verão Ofertas', 'Semana Tech', 'Black Friday', 'Institucional', 'Nenhuma']

dados = []

for i in range(num_registros):
    # Data aleatória no ano
    dias = random.randint(0, 365)
    data_venda = data_inicio + timedelta(days=dias)

    # Seleção de Produto
    prod = random.choice(produtos)

    # Seleção de Canal e Campanha
    canal = random.choice(canais)
    campanha = 'Nenhuma' if canal == 'Orgânico' else random.choice(campanhas)

    # Valores Financeiros (com variação para realismo)
    fator_preco = random.uniform(0.9, 1.1)
    receita = round(prod['base_price'] * fator_preco, 2)

    # Custo do Produto (CMV estimado em 60% a 70% da receita)
    custo_produto = round(receita * random.uniform(0.60, 0.70), 2)

    # Custo de Marketing (CAC variável por canal)
    if canal == 'Orgânico':
        custo_mkt = 0.0
    elif canal == 'Influencers':
        custo_mkt = round(random.uniform(50, 200), 2)
    else:
        custo_mkt = round(random.uniform(10, 80), 2)

    dados.append([
        1000 + i, # venda_id
        data_venda.strftime("%Y-%m-%d"),
        prod['nome'],
        prod['cat'],
        canal,
        campanha,
        receita,
        custo_produto,
        custo_mkt
    ])

df = pd.DataFrame(dados, columns=[
    'venda_id', 'data', 'produto', 'categoria_produto',
    'canal', 'campanha', 'receita', 'custo', 'custo_marketing'
])

# Exportar
df.to_csv('vendas_ecommerce.csv', index=False)
print("Arquivo 'vendas_ecommerce.csv' gerado com sucesso!")