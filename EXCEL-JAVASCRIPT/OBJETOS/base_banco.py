
class banco:
    import os
    os.system("cls")
    def __init__(self,nome,numero,saldo,limite):
        self.nome = nome
        self.numero = numero
        self.saldo = saldo
        self.limite = limite


    def deposito(self,depositado):
        self.depositado = depositado
        self.saldo += depositado
    
    def sacar(self,valor):
        self.valor = valor
        self.saldo -= self.valor

    def transferir(self,valor,destino):
        self.sacar(valor)
        destino.deposito(valor)

        


#/////////////////////////////////////////

# cliente2 = banco("lucas",222,1000,5050) # Criando a conta

# print(f"O cliente {cliente2.nome} abriu a conta com R$: {cliente2.saldo}") # fazendo o depósito

# deposito_cliente2 = int(input(f"Digite o Valor do depósito para o {cliente2.nome}, R$: ")) # verificando o saldo

# cliente2.deposito(deposito_cliente2)

# print(f"O cliente {cliente2.nome} depositou R$: {deposito_cliente2} e ficou com R$: {cliente2.saldo} de saldo\n")






