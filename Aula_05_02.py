import pandas as pd
# Importando a Base de Dados
endereco_dados = 'BASES\FINANCEIRA.csv'
# Criando o DataFrame
df_Financeira = pd.read_csv(endereco_dados, sep=',',encoding= 'iso-8859-1')
# Exibindo os Dados do DataFrame
print("----BASE DE DADOS----")
print(df_Financeira.head())