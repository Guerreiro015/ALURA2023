import os
os.system('cls')

#!/usr/bin/env python
# coding: utf-8

# ### assert em Python
# 
# - Verifica que uma condição está sendo satisfeita para garantir a continuação do código
# - Usado na construção, no desenvolvimento do código

# In[ ]:


print("Início")

assert 1 < 2

print("Final")


# ### Caso Prático
# 
# - Verificar se uma condição que deveria ser satisfeita, realmente está sendo

# In[ ]:


import requests

requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
requisicao_dic = requisicao.json()

cotacao = requisicao_dic["USDBRL"]["bid"]
cotacao = float(cotacao)
print(cotacao)


# In[ ]:


preco_produto = 100


# In[ ]:


assert cotacao > 0

faturamento = preco_produto * cotacao
print(f'\nComo o código passou no assert o Faturamento foi {faturamento: ,.2f}')

