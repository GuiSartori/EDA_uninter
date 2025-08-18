# %% Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% Leitura dos dados
df1 = pd.read_csv('../AED/pes_2012.csv')
df1.head()

# %% Conversão de tipos das colunas relevantes
print(type(df1.V4718.iloc[0]))  # Mostra o tipo do primeiro valor da coluna V4718
df1["V4718"] = pd.to_numeric(df1["V4718"], errors='coerce')  # Converte para numérico, erros viram NaN
df1["V4720"] = pd.to_numeric(df1["V4720"], errors='coerce')  # Converte para numérico, erros viram NaN

# %% Remoção de linhas com valores ausentes
df = df1.dropna()
df.head()  # Exibe as primeiras linhas do DataFrame limpo

# %% Configuração do estilo dos gráficos
sns.set_theme(style="whitegrid")  # Define o tema dos gráficos

# %% Gráfico de contagem do sexo (V0302)
sns.countplot(y=df["V0302"], palette="Set1")
plt.title('Distribuição de Sexo')
plt.xlabel('Contagem')
plt.ylabel('Sexo')
plt.show()

# %% Gráfico de contagem do sexo com barras agrupadas por sexo
sns.countplot(x=df["V0302"], hue=df["V0302"])
plt.title('Distribuição de Sexo')
plt.xlabel('')
plt.ylabel('')
plt.legend(title='Sexo', labels=['Masculino', 'Feminino'])
plt.show()

# %% Gráfico de cor/raça (V0404) agrupado por sexo (V0302)
sns.countplot(x=df["V0404"], hue=df["V0302"])
plt.title('Distribuição de Cor/Raça por Sexo')
plt.xlabel('')
plt.ylabel('')
plt.legend(loc='best')
plt.show()

# %% Gráfico de sexo (V0302) agrupado por cor/raça (V0404)
sns.countplot(x=df["V0302"], hue=df["V0404"])
plt.title('Distribuição de Cor/Raça por Sexo')
plt.xlabel('')
plt.ylabel('')
plt.legend(bbox_to_anchor=(1.05, 0.7), loc='upper left', title='Cor/Raça')
plt.show()

# %% Gráfico de setores (pizza) por cor/raça (V0404)
sizes = df.V0404.value_counts()  # Conta os valores únicos de V0404
labels = sizes.index  # Rótulos para o gráfico
plt.figure(figsize=(8, 8))  # Define o tamanho da figura
plt.pie(
    sizes,
    labels=labels,
    explode=(0, 0, 0.1, 0.3, 0.5), # Destaque para algumas fatias
    autopct='%1.3f%%', # Mostra porcentagem com 3 casas decimais
    labeldistance=1, # Distância dos rótulos
    startangle=90 # Começa o gráfico do topo
)
plt.legend(bbox_to_anchor=(1.05, 0.7), loc='upper left', title='Cor/Raça')
plt.title('Distribuição de Cor/Raça')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.
plt.show()

# %%
sizes = df.V0404.value_counts() # Tamanho das fatias
sizes.plot( # Plotagem do gráfico
    kind='pie',
    autopct='%1.1f%%',
    figsize=(8, 8),
    startangle=90,
    legend=True,
    labeldistance=1
) 
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is drawn as a circle.
plt.legend(
    bbox_to_anchor=(1.05, 0.7),
    loc='upper left',
    title='Cor/Raça'
)
# %% Gráfico de frequência absoluta
sizes = df.V0404
plt.figure(figsize=(5, 5))
sns.histplot(sizes, bins=5)
plt.ylabel('')
plt.title('Frequência Absoluta de Cor/Raça')
# %% Gráfico de frequência acumulada
sizes = df.V0404
plt.figure(figsize=(5, 5))
sns.histplot(sizes, bins=5, cumulative=True)
plt.ylabel('')
plt.title('Frequência Acumulada de Cor/Raça')
# %%
sizes = df.V0404.sort_values(ascending=False)
plt.figure(figsize=(5, 5))
sns.histplot(sizes, bins=5, cumulative=True)
plt.ylabel('')
plt.title('Frequência Acumulada de Cor/Raça')
# %% Gráfico de frequência relativa
sizes = np.divide(df.V0404.value_counts(), len(df.V0404))  # Frequência relativa 
plt.plot(sizes)
plt.figure(figsize=(5, 5))
plt.ylabel('Frequência Relativa')
plt.show()
# %%
