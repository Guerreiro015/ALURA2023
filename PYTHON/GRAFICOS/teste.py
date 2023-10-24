import os
os.system('cls')

import pandas as pd

dados=pd.read_csv('imigrantes.csv')
print(dados)

df=dados.set_index('Country')
print(df)

df2=df.loc['Brazil']
print(df2)
