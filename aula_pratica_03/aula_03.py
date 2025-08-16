# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

# %%
df1 = pd.read_csv(r'..\data\pes_2012.csv')
df1.head()
# %% Transforma dados em float e remove linhas com NaN
df1['V4718'] = pd.to_numeric(df1['V4718'], errors='coerce')
df1['V4720'] = pd.to_numeric(df1['V4720'], errors='coerce')
# %%
df = df1.dropna()  # Remove linhas com NaN e atribui a df
df.head()
# %%
sns.set_theme(style='ticks', palette='light:m_r')

# %%
# Regra do logaritmo: K = 1 + 3,3 * log10(N)
sizes = df.V8005
plt.figure(figsize=(8, 8))  # Define o tamanho da figura

# Cálculo da quantidade de classes
k = int(1 + 3.3 * np.log10(len(sizes)))
# %%
sns.histplot(sizes, bins=k)
plt.xlabel('Idade')
plt.ylabel('Qtd pessoas')
plt.show()
print(k)
# %% Usando regra da potência para obter o número de classes
sizes = df.V8005
plt.figure(figsize=(8, 8))  # Define o tamanho da figura

# Cálculo da quantidade de classes
# Lembrando que 2^k = n é o mesmo que log2(n) = k
c = math.log(len(sizes), 2) # Fórmula do log na base 2
k = int(c) + 1
print(f'k = {k}')

sns.histplot(sizes, bins=k)
plt.xlabel('Idade')
plt.ylabel('Qtd pessoas')
plt.show()

# %% Histograma
sizes = df.V8005

sns.histplot(sizes, bins = 15, cumulative=False)
plt.xlabel('Idade')
plt.ylabel('Qtd pessoas')
plt.show()

# %% Distribuição
sizes = df.V8005
sns.displot(sizes, bins = 15, cumulative=False, kde = True)
# sns.distplot(sizes)
plt.xlabel('Idade') 
plt.ylabel('Qtd pessoas')
plt.show()

# %% Densidade
sizes = df.V8005
sns.kdeplot(data=sizes, fill=True)

plt.xlabel('Idade')
plt.ylabel('Densidade')
plt.show()

# %% Polígono de frequência
sizes = df.V0404.value_counts()
sns.relplot(data=sizes, kind='line', height=5)

plt.xlabel('Idade')
plt.ylabel('Qtd pessoas')
plt.show()

# %% Gráfico de Dispersão
plt.figure(figsize=(8, 8))  # Define o tamanho da figura
# sns.relplot(x=df.V8005, y=df.V4720, kind='scatter')
sns.scatterplot(x=df.V8005, y=df.V4720) # Gráfico de dispersão

plt.xlabel('Idade')
plt.ylabel('Rendimento')
plt.show()

# %% Ordenação de dados
df.V0404.sort_values() # Ordem alfabetica

df.V8005.sort_values() # Ordem numérica crescente

df.V8005.sort_values(ascending=False) # Ordem numérica decrescente