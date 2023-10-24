import os
os.system("cls")

class banco:
    def __init__(self,name,vendas):
        self._name = name
        self._vendas = vendas

    @property
    def name(self):
        return self._name.upper()

    @name.setter
    def name(self,value):
        self._name = value

    @property
    def vendas(self):
        return self._vendas
    
    @vendas.setter
    def vendas(self,valor):
        self._vendas = valor


cliente =banco("Luana",0)

print(f"\nA cliente {cliente.name} foi cadastrada com R$: {cliente.vendas} de vendas")
cliente.name="antonio"
cliente.vendas = 100
print(f"\nCliente alterado para {cliente.name} e vendas alterada para R$: {cliente.vendas}\n")

