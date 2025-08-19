# %% Importação das bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="ticks", palette="crest") # Define o tema dos gráficos
# %% Leitura dos dados
df1 = pd.read_csv(r'..\data\pes_2012.csv')
df1.head()

# %% Séries: Temporais e Geográficas
series = pd.read_csv(r'..\data\daily-total-female-births.csv', header=0, index_col=0, parse_dates=True)
series.head()
# %%
