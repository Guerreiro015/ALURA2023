import os
os.system('cls')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cores = []

df = pd.read_excel('CUSTO0823.xlsx')

df=pd.DataFrame(df)

#df.set_index('Sindicatos',inplace=True)

print(df)

#ax = sns.lineplot(df.loc['Brasil', anos], label='Brasil', lw=4)

#df.set_index('Folha',inplace=True) # Colocar o culuna pais como indice

fig,ax = plt.subplots(figsize=(10,4))

ax=sns.lineplot(y=df['Sindicatos'],x=df['Salário'],label='Siemaco')
# ax=sns.lineplot(data=df,y=df['Sindicatos'],x=df['Salário'],label='Steriiisp')
# ax=sns.lineplot(data=df,y=df['Sindicatos'],x=df['Salário'],label='Selur')

ax.set(title='Salários por Regionais',xlabel='Valor Salários',ylabel='Regionais')

plt.show()
