#PROPIEDADES OS GETTERS E SETTER SERVEM PARA ADICIONAR PROPIEDADES AOS OBJETOS
 # @name.deleter
    # def name(self):
    #     print('Deleting name')
    #     del self._name

import os
os.system("cls")

class Persona:
    def __init__(self, name,limite,saldo):
        self._name = name
        self._limite = limite
        self._saldo = saldo

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, valor):
        if type(valor) != type(str()):
            print('''\n A troca de nome não foi possível
            nome não pode ser mumero''')
        else:
            print('\nNome alterado para ',valor)
            self._name = valor.title()
            print(f"Seu novo nome é {self._name} e seu saldo é R$: {self._saldo: .2f} ")

    @property 
    def saldo(self):
       return self._saldo



    @property
    def deposito(self):
        return self.deposito

    @deposito.setter
    def deposito(self, valor):
        if type(valor) == type(str()):
            print('''\n Tentativa de deposito falhou
            O deposito não pode ser strings''')
        else:
            print(f"\nDeposito de {valor: .2f} feito com sucesso")
            self._saldo += valor
            print(f"Seu novo saldo é de {self._saldo: .2f}")
    

    @property
   
    def saque(self):
        return self.saque
    
    @saque.setter 
    def saque(self,valor):
        if type(valor) == type(str()):
            print('''\nTentativa de saque falhou
            O valor do saque não pode ser strings''')
        else:
            if valor > self._saldo:
                print(f"\n{self._name} seu saque de R$: {valor: .2f} não foi realizado, saldo de {self._saldo: .2f} insuficiente")
            else:
                self._saldo -= valor 
                print(f"\n{self._name} seu saque de {valor: .2f} foi realizado com sucesso")
                print(f'\n{self._name} seu novo saldo é de R$: {pessoa.saldo: .2f}')
        




pessoa = Persona('Antonio',500,1620)

print(f'\nO cliente {pessoa.name} foi cadastrado com sucesso, com um saldo de: {pessoa.saldo: .2f}')

pessoa.name = 1111

pessoa.name = "Francisca"

pessoa.deposito = "ffff"
pessoa.deposito = 80

pessoa.saque = "ddd"
pessoa.saque = 2000
pessoa.saque = 200
pessoa.saldo

#del p.name



 