import os
os.system('cls')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cores = []

df = pd.read_csv('imigrantes.csv')
#
#df.set_index('País',inplace=True) # Colocar o culuna pais como indice

#Ordenando do Maior para o menor e pegando os 10 peimeiros
top10=df.sort_values('Total',ascending=True).head(10) 
print(top10)

sns.barplot(data=top10,y='País',x='Total',orient='h')


plt.show()
