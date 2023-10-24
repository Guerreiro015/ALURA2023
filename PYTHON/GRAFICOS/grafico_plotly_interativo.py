import os
os.system('cls')

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('imigrantes.csv')
print(df)


df.set_index('País',inplace=True) # Colocar o culuna pais como indice
print(df)


anos=list(map(str,range(1980,2014))) # Crianndo uma lista com os anos como strings
print(anos)

#Extração da série de dados para o Brasil
#criamos uma variável chamada brasil igual à df.loc[]
# e variável anos nos colchetes.

brasil=df.loc['Brasil',anos]

print(brasil)

#Vamos criar um dataframe com as informaçoes da variavel brasil

#primeito vamos criar um dicionario com os dados

brasil_dicio={'ano': brasil.index.tolist(),'imigrantes': brasil.values.tolist()} # tolist para criar a lista

print(brasil_dicio)

dados_brasil=pd.DataFrame(brasil_dicio)

print(dados_brasil)

fig = px.line(dados_brasil, x='ano', y='imigrantes',
              title="Imigração do Brasil para o Canadá")
fig.update_traces(line_color='blue',line_width=4)
#fig.update_traces(line_color='green', line_width=4)
fig.update_layout(width=1000, height=500, 
                  xaxis={'tickangle': -45},
                  font_family='Arial',
                font_size=14,
                font_color='Red',
                title_font_color='black',
                title_font_size=22,
                  xaxis_title="ANOS",
                  yaxis_title='Números de Imigrantes')

fig.show()

plt.show()









