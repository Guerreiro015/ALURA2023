import os
os.system("cls")

class banco:
    def __init__(self,nome):
        self.nome = nome
        self.saldo = 0
        print(f"Conta de {nome} criado com sucesso\n")

    def deposito(self,valor):
        print(f'Saldo anterior de {self.nome} era de {self.saldo}')
        self.saldo += valor
        print(f'Depósito de {valor} para {self.nome}, feito com sucesso')
        print(f'Seu novo saldo é de R$: {self.saldo} \n')

    def saque(self,valor):
        if self.saldo <= valor:
            print(f"Desculpe {self.nome}, seu saldo é insuficente para um saque de {valor}")
            print(f'Seu saldo atual é de apenas R$: {self.saldo} \n')
        else:
            self.saldo -= valor
            print(f'O saque de {valor} na conta de {self.nome}, realizado com sucesso')
            print(f'Seu novo saldo é de R$: {self.saldo} \n')
        

    def __str__(self):
        return f'O cliente {self.nome} tem {self.saldo} de saldo\n'
    
ana = banco("Ana")
pedro = banco("Pedro")
ana.deposito(500)
pedro.deposito(2220)
ana.saque(600)
pedro.saque(3000)
pedro.deposito(1000)
pedro.saque(3000)


contas = [ana,pedro,ana]

for x in contas:
    print(x)

print(contas[1]) # como os objetos estão em uma lista podem chammado assim

contas[1].deposito(450)
print(pedro)

def depositoGeral(valor):
    for x in contas:
        x.deposito(valor)

depositoGeral(100)

def saqueGeral(valor):
    for x in contas:
        x.saque(valor)

saqueGeral(150)

contas.insert(0,"Agencia")

print(contas)
