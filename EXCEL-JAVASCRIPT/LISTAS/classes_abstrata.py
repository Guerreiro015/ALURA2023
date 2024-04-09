# Faltou importar o que eu tenho que importar. Para isso,
#  eu faço from abc import ABCMeta, abstractmethod.
#  Usamos o ABCmeta como uma meta classe, metaclass.
#  É uma configuração que precisamos colocar: class Conta(metaclass=ABCMeta):.
#  O abstractmethod já está no nosso código, mais abaixo.

import os
os.system("cls")

from abc import ABCMeta, abstractmethod

class banco(metaclass=ABCMeta):

  def __init__(self, nome):
    self._nome = nome
    self._saldo = 0

  def deposita(self, valor):
    self._saldo += valor

  @abstractmethod
  def passa_o_mes(self):
   pass

  def __str__(self):
    return f"\nNome do cliente: {self._nome} -- > Saldo -> R$: {self._saldo: .2f}"
  
#print(banco("Antonio"))

# A partir no momento que crio função abstrata (Passa_mes(self)) na classe mãe
# todos classes filhas tem que ter esta função incluida

class ContaCorrente(banco):
  def passa_o_mes(self):
    self._saldo -= 2

class ContaPoupanca(banco):
  def passa_o_mes(self):
    self._saldo *= 1.01
    self._saldo -= 3

class contaInvestimento(banco):
  def passa_o_mes(self):
   self._saldo += 10

cliente1 = ContaCorrente("Antonio")
cliente1.deposita(1000)
cliente1.passa_o_mes()

cliente2 = ContaPoupanca("Ana")
cliente2.deposita(1000)
cliente2.passa_o_mes()

cliente3 = contaInvestimento("Luana")
cliente3.deposita(1000)
cliente3.passa_o_mes()


print(cliente1)
print(cliente2)
print(cliente3)

contas = [cliente1,cliente2,cliente3]


for x in contas:
  print(x)
