import os
os.system('cls')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cores = []

df = pd.read_csv('imigrantes.csv')

df.set_index('País',inplace=True) # Colocar o culuna pais como indice

#Ordenando do Maior para o menor e pegando os 10 peimeiros
top10=df.sort_values('Total',ascending=True).head(10) 
print(top10)
fig,ax = plt.subplots(figsize=(10,5))
ax=sns.barplot(data=top10,y=top10.index,x='Total',orient='h')
ax.set_title('Países com maior Imigração para o Canadá',loc='left',fontsize=16)
ax.set_xlabel('Números de Imigrantes',fontsize=16)
ax.set_ylabel('PAISES')




plt.show()
