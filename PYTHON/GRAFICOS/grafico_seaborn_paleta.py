import os
os.system('cls')

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cores = []

df = pd.read_csv('imigrantes.csv')

df.set_index('País',inplace=True) # Colocar o culuna pais como indice

def grafico(paleta,tema):
    sns.set_theme(style=tema)
    #Ordenando do Maior para o menor e pegando os 10 peimeiros
    top10=df.sort_values('Total',ascending=True).head(10) 
    print(top10)
    fig,ax = plt.subplots(figsize=(10,5))
    ax=sns.barplot(data=top10,y=top10.index,x='Total',orient='h',palette=paleta)
    ax.set_title('Países com maior Imigração para o Canadá',loc='left',fontsize=16)
    ax.set_xlabel('Números de Imigrantes',fontsize=16)
    ax.set_ylabel('PAISES')
    #sns.despine() # Tirar a borda acima e direita
    plt.show()

grafico('tab10','dark') # usando a paleta de cores Blues se colocarms r ela inverte as cores

#''' Paletas Blues, rocket, coolwarm, deep, muted, pastel, bright, dark, colorblind, tab10
# '''
 
#TEMAS - "darkgrid" , "whitegrid" , "dark" , "white" and "ticks"