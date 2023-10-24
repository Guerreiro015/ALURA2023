import os
os.system('cls')

import pandas as pd
import matplotlib.pyplot as plt

lojas = ['A', 'B', 'C', 'D']

vendas_2022 = {'Jan': [100, 80, 150, 50],
    'Fev': [120, 90, 170, 60],
    'Mar': [150, 100, 200, 80],
    'Abr': [180, 110, 230, 90],
    'Mai': [220, 190, 350, 200],
    'Jun': [230, 150, 280, 120],
    'Jul': [250, 170, 300, 140],
    'Ago': [260, 180, 310, 150],
    'Set': [240, 160, 290, 130],
    'Out': [220, 140, 270, 110],
    'Nov': [400, 220, 350, 190],
    'Dez': [300, 350, 400, 250]
}


df = pd.DataFrame(vendas_2022, index=lojas)

print(df)


# Criar a figura e os subplots
fig, ax = plt.subplots(figsize=(10, 4))

# Ajustar os espaçamentos entre os subplots
plt.subplots_adjust(wspace=0.3, hspace=0.4)

# Adicionando um título geral para os subplots
fig.suptitle('Vendas no período de janeiro/2022 a dezembro/2022 nas lojas A,B,C e D')

# Adicionar os gráficos em cada um dos subplots
ax.plot(df.loc['A'],label='Loja A',lw=3)

ax.plot(df.loc['B'],label='Loja B',color='red')

ax.plot(df.loc['C'],label='Loja C')

ax.plot(df.loc['D'],label='Loja D',lw=3)

# Adicionando rótulos para os eixos X e Y
ax.set_title('GRÁFICO DAS VENDAS')
ax.set_xlabel('Mês')
ax.set_ylabel('Número de vendas')
ax.legend()
ax.grid() #grade
# Exibir a figura
plt.show()

