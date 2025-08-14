# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
df1 = pd.read_csv(r'..\data\pes_2012.csv')
df1.head()
# %%
df1['V4718'] = pd.to_numeric(df1['V4718'], errors='coerce')
df1['V4720'] = pd.to_numeric(df1['v4720'], errors='coerce')
# %%
