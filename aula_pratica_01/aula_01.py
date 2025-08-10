# %%
# Importação das bibliotecas essenciais para análise de dados
import pandas as pd
import numpy as np

# %%
# Leitura do arquivo CSV contendo os dados da pesquisa
df = pd.read_csv(
    r'C:\Users\guilh\Documents\UNINTER\S2B2 - Análise Exploratória de Dados\aula_pratica_01\data\pes_2012.csv'
)

# %%
# Visualização inicial: mostra as 10 primeiras linhas do DataFrame
print(df.head(10))

# %%
# Exibe a dimensão do DataFrame (número de linhas e colunas)
print(df.shape)

# %%
# Informações gerais: tipos de dados, valores nulos, etc.
df.info()

# %%
# Mostra os tipos de dados de cada coluna
print(df.dtypes)

# %%
# Exibe a coluna 'V4718' (duas formas equivalentes)
print(df['V4718'])
print(df.V4718)

# %%
# Remove colunas com pelo menos um valor nulo (não altera o DataFrame original)
df_sem_colunas_nulas = df.dropna(axis='columns')
# O parâmetro axis='columns' indica que a operação é feita nas colunas

# %%
# Remove linhas com pelo menos um valor nulo (não altera o DataFrame original)
df_sem_linhas_nulas = df.dropna()
# O padrão é axis=0, ou seja, a operação é feita nas linhas

# %%
# Cria um novo DataFrame sem linhas com valores nulos
ndf = df.dropna()
print(ndf.head(10))

# %%
# Converte as colunas 'V4718' e 'V4720' para tipo numérico, substituindo erros por NaN
df['V4718'] = pd.to_numeric(df['V4718'], errors='coerce')
df['V4720'] = pd.to_numeric(df['V4720'], errors='coerce')

# %%
# Verifica novamente os tipos de dados após conversão
print(df.dtypes)

# %%
# Seleciona colunas do tipo objeto (strings, categorias, etc.)
print(df.select_dtypes(include=['object']))

# %%
# Seleciona colunas do tipo numérico (inteiros, floats, etc.)
print(df.select_dtypes(include=['number']))

# %%
# Exemplo de valor quantitativo discreto: tipo e valor de uma célula específica
print(type(df.V0101.iloc[1]))  # Mostra o tipo do valor na linha 1 da coluna 'V0101'
print(df.V0101.iloc[132])      # Mostra o valor na linha 132 da coluna 'V0101'

# %%
# Média da coluna 'V8005' (idade) usando pandas
pdmedia = ndf.V8005.mean()
print(f'A média das idades é: {pdmedia}')
print(type(pdmedia))

# %%
# Média da coluna 'V8005' usando numpy
npmedia = np.mean(ndf.V8005)
print(f'A média das idades é: {npmedia}')
print(type(npmedia))

# %%
# Diferentes formas de representar a média numericamente
print("%.2f" % pdmedia)         # Arredondamento para 2 casas decimais
print("%.5f" % pdmedia)         # Arredondamento para 5 casas decimais
print('{:e}'.format(pdmedia))   # Notação científica
print('{:.2e}'.format(pdmedia)) # Notação científica com 2 casas decimais

# Versões usando f-string:
print(f"{pdmedia:.2f}")      # 2 casas decimais
print(f"{pdmedia:.5f}")      # 5 casas decimais
print(f"{pdmedia:e}")        # Notação científica
print(f"{pdmedia:.2e}")      # Notação científica com 2 casas decimais

# %%
# Frequência absoluta de valores em colunas qualitativas e quantitativas
print(ndf.V0404.value_counts()) # Frequência qualitativa (ex: características físicas)
print(ndf.V8005.value_counts()) # Frequência quantitativa (ex: idade)

# %%
# Frequência relativa (proporção) para coluna qualitativa
total_v0404 = len(ndf.V0404)
print("Número total de observações em V0404:", total_v0404)
print(np.divide(ndf.V0404.value_counts(), total_v0404))

# %%
# Frequência relativa (proporção) para coluna quantitativa
total_v8005 = len(ndf.V8005)
print("Número total de observações em V8005:", total_v8005)
print(np.divide(ndf.V8005.value_counts(), total_v8005))
