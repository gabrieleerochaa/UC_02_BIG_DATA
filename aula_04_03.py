import pandas as pd

vendedores = {
    "nome":["maria", "joao", "manoel"],
    "vendas_01" : [800,900,700],
    "vendas_02" : [700,500,600],
    "vendas_03" : [1000,1100,900],
    "vendas_04" : [900,1000,1200]
}

df_vendedores = pd.DataFrame(vendedores)

print(df_vendedores)