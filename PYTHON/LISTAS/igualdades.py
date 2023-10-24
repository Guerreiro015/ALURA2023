import os
os.system("cls")

import time


class banco:
    def __init__(self,nome):
        self._nome = nome
        self._saldo = 0
        
    def salario(self,valor):
        self._saldo +=valor

    def __str__(self) -> str:
        return f'Nome do cliente: {self._nome} Saldo: R$:  {self._saldo} '


Cliente1 = banco("Antonio")
Cliente2 = banco("Antonio")


print(Cliente1)
print(Cliente2)

Cliente1.salario(500)
Cliente2.salario(500)

if Cliente1 == Cliente2:
    print(Cliente1)
    print(Cliente2)
    print("Parecem iguais mas não são iguais\n") 
else:
    print("Parecem iguais mas não são iguais\n")

#######################################################################################

#para que os objetos retornem que são iguais precisamos usar a função (  __eq__ )


class banco:
   def __init__(self, nome):
     self.nome = nome
     self.saldo = 0

   def __eq__ (self, outro):
        return self.nome == outro.nome


   def salario(self,valor):
            self.saldo +=valor
        
   def __str__(self) -> str:
            return f'Nome do cliente: {self.nome} Saldo: R$:  {self.saldo} '

 
Cliente1 = banco("Antonio")
Cliente2 = banco("Antonio")


print(Cliente1)
print(Cliente2)

Cliente1.salario(500)
Cliente2.salario(500)

if Cliente1 == Cliente2:
    print(Cliente1)
    print(Cliente2)
    print("Parecem iguais e são iguais mesmmo\n") 
else:
    print("Parecem iguais mas não são iguais\n")


