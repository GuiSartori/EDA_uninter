# %% Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="ticks", palette="crest") # Define o tema dos gráficos
# %% Leitura dos dados
df = pd.read_csv(r'..\data\pes_2012.csv')
df.head()

# %% Séries: Temporais e Geográficas
series = pd.read_csv(r'..\data\daily-total-female-births.csv', header=0, index_col=0, parse_dates=True)

series.head()
# %% 
plt.figure(figsize=(15, 5))  # Define o tamanho da figura
plt.plot(series)
plt.ylabel('Total')
plt.xlabel('Data de aniversário')
plt.show()

# %% Série geográfica
sizes = df.UF
sns.displot(y=sizes)
plt.xlabel('UF')
plt.xlabel('Qtd pessoas')
plt.show()

# %% Somatórios
def somatorio(x):
    '''
    Calcula o somatório de 1 a x
    '''
    if x == 1:
        return 1
    else:
        return x + somatorio(x-1)

x = int(input('Digite um número: '))
print(f'O somatório de {x} é: {somatorio(x)}')

# %% Somatório dos quadrados do tempo
def somatorio(x):
    if x == 1:
        return 1
    else:
        return x**2 + somatorio(x-1)

x = int(input('Digite um número: '))
print(f'O somatório dos quadrados de {x} é: {somatorio(x)}')

# %% Somatório de (xi-k)**2
def somatorio(x, k):
    if x == 1:
        return 1
    else:
        return (x-k)**2 + somatorio(x-1, k)

x = int(input('Calcular os somatórios de 1 a x - Digite um número: '))
k = int(input('O valor médio dos dados (k) - Digite um número: '))
print(f'O somatório dos quadrados de {x} - {k} é: {somatorio(x, k)}')

# %%
