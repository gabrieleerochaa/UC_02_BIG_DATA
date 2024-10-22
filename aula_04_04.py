import pandas as pd

vendedores_01 = {
    "nome":["maria", "joao", "manoel"],
    "vendas_01" : [800,900,700],
    "vendas_02" : [700,500,600],
    "vendas_03" : [1000,1100,900],
    "vendas_04" : [900,1000,1200]
}

vendedores_02 = {
    'Meses':['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho'],
    'Maria':[800,700,1000,900,1200,600,600],
    'João':[900,500,1100,1000,900,500,700],
    'Manoel':[700,600,900,1200,900,700,400]
}

df_vendedores_01 = pd.DataFrame(vendedores_01)
print(df_vendedores_01)

print("----------------------------------")
df_vendedores_02 = pd.DataFrame(vendedores_02)
print(df_vendedores_02)


