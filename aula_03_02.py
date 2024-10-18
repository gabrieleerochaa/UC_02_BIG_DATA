import pandas as pd

# Criando uma função para formatar número
def formatar(valor):
    return "{:.2f}%".format(valor)

# Criando o Código
roubo = pd.Series([100,90,80,120,110,90,70])
furto = pd.Series([80,60,70,60,100,50,30])
recuperacao = pd.Series([70,50,90,80,100,70,50])
roubo_furto = roubo + furto
tx_recuperacao = ((recuperacao / roubo_furto) * 100).apply(formatar)
print("\n- Total Geral de Roubos -")
print(f"{roubo_furto.sum()}")
print("\n- Total de Roubos Diários -")
print(f"{roubo_furto}")
print("\n- Taxa de Recuperação Diária -")
print(f"{tx_recuperacao}")