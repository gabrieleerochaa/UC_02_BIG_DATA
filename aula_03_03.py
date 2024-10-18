import pandas as pd

maria = pd.Series([800,700,1000,900,1200,600,600])
joao = pd.Series([900,500,1100,1000,900,500,700])
manoel = pd.Series([700,600,900,1200,900,700,400])
print("\n.. Informações sobre a Vendedora Maria. ")
print(f"O total de venda é R${maria.sum():.2f}" )
print(f"A Média de vendas é R${maria.mean():.2f}")
print(f"O maior valor de vendas é R${maria.max():.2f}")
print(f"O menor valor de vendas é R${maria.min():.2f}")

print("\n.. Informações sobre a Vendedor Joao. ")
print(f"O total de venda é R${joao.sum():.2f}" )
print(f"A Média de vendas é R${joao.mean():.2f}")
print(f"O maior valor de vendas é R${joao.max():.2f}")
print(f"O menor valor de vendas é R${joao.min():.2f}")

print("\n.. Informações sobre a Vendedor Manoel. ")
print(f"O total de venda é R${manoel.sum():.2f}" )
print(f"A Média de vendas é R${manoel.mean():.2f}")
print(f"O maior valor de vendas é R${manoel.max():.2f}")
print(f"O menor valor de vendas é R${manoel.min():.2f}")
