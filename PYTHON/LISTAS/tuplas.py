import os
os.system("cls")

conta = ("ana",1000)

# As tuplas usam os parenteses em vez de colchetes
# As tuplas não posem set alteradas

def deposito(valor):
    saldo = conta[1]+valor
    nome = conta[0]
    return (nome,saldo)

print(f"Conta antes do depósito {conta}")

conta = deposito(500)

print(f"Conta depois do depósito {conta}")

# Conclusão não conseguimos modificar mas conseguimos criar outra tupla com os valores alterados


class banco:

  def __init__(self, nome):
    self._nome = nome
    self._saldo = 0

  def deposita(self, valor):
    self._saldo += valor

  def __str__(self):
    return f"\nNome do cliente: {self._nome} -- > Saldo -> R$: {self._saldo: .2f}"
  
print(banco("Antonio"))

class ContaCorrente(banco):

  def passa_o_mes(self):
    self._saldo -= 2

class ContaPoupanca(banco):

  def passa_o_mes(self):
    self._saldo *= 1.01
    self._saldo -= 3


cliente1 = ContaCorrente("Antonio")
cliente1.deposita(1000)
cliente1.passa_o_mes()

cliente2 = ContaPoupanca("Ana")
cliente2.deposita(1000)
cliente2.passa_o_mes()


print(cliente1)
print(cliente2)

contas = [cliente1,cliente2]


for x in contas:
  print(x)
