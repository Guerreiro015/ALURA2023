import os
os.system('cls')

from  bytebank import Funcionario

lucas=Funcionario("Lucas Souza",'01/01/2001',1000)

print(lucas.idade())

def teste_idade():
  
  funcionario_teste=Funcionario("Lucas Souza",'01/01/2001',1000)
  print(f'Teste da Idade do Funcionário = {funcionario_teste.idade()}')

  funcionario_teste=Funcionario("Antonio Souza",'01/01/1972',1000)
  print(f'Teste da Idade do Funcionário = {funcionario_teste.idade()}')

  funcionario_teste=Funcionario("Luana Souza",'28/08/1998',1000)
  print(f'Teste da Idade do Funcionário = {funcionario_teste.idade()}')
teste_idade()


