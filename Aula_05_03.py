import pandas as pd
# Importanto os Dados via Web
endereco_dados = 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
# Criando o Dataframe
df_ococrrencias = pd.read_csv(endereco_dados, sep=';', encoding = 'iso-8859-1')
# Exibindo o Dataframe
print(df_ococrrencias.head())