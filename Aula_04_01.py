import pandas as pd
alunos = [
    ["joao", 18,100],
    ['Maria', 15,80],
    ["Antonia", 18,100],
    ['Erica', 20,60],
    ["Pedro", 16,10]
]

# Criando as Colunas da Tabela Alunos
colunas = ["nome", "idade", "media"]
# Criando o Dataframe
df_alunos = pd.DataFrame(alunos,columns=colunas)
# Exibindo os Dados
print("\n-- Informções sobre as idades dos Alunos")
print(df_alunos)
#Realizando os Cálculos das Idades
soma_idade = df_alunos ["idade"].sum (axis=0)
média_idade = df_alunos ["idade"].mean (axis=0)
maior_idade = df_alunos ["idade"].max (axis=0)
menor_idade = df_alunos ["idade"].min(axis=0)
maior_nome = df_alunos [df_alunos['idade'] == maior_idade]['Nome']
menor_nome = df_alunos [df_alunos['idade'] == menor_idade]['Nome']
#Realizando os Cálculos das Médias
soma_media = df_alunos ["media"].sum(axis=0)
média_media = df_alunos ["media"].mean(axis=0)
maior_media = df_alunos ["media"].max (axis=0)
menor_media = df_alunos ["media"].min(axis=0)
maior_media_nome = df_alunos[df_alunos['Média'] == maior_media]['Nome']
menor_media_nome = df_alunos[df_alunos['Média'] == menor_media]['Nome']
#Exibindo os Calculos das idades
print("\n-- Informações sobre as Idades dos Alunos --")
print(f"A soma das idades é {soma_idade} anos.")
print(f"A média das idades é {menor_idade} anos.")
print(f"A maior idade é{maior_idade} anos. ")
print(f"A menor idade é{menor_idade} anos")
print(f"O nome do aluno mais velho é {maior_nome.values[0]}")
print(f"O nome do aluno mais novo é {menor_nome.values[0]}")
# Exibindo os Cálculos das Médias
print("\n-- Informações sobre as Médias dos Alunos --")
print(f"A soma das médias é {soma_media:.1f}")
print(f"A média da turma é {média_media:.1f}")
print(f"A maior média é {maior_media:.1f}")
print(f"A menor média é {menor_media:.1f}")
print(f"O nome do aluno com maior média é {maior_media_nome.values[0]}")
print(f"O nome do aluno com menor média é {menor_media_nome.values[0]}")
