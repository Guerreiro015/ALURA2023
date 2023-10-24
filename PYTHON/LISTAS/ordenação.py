import os
os.system("cls")

# #########   ORDENAÇÃO SIMPLES     ###################
idades = [15, 87, 65, 56, 32, 49, 37, 32]

ordenar = sorted(idades) # Colocar em ordem
contra = sorted(idades, reverse = True)# Ordenar ao contrário
idades.sort() # ordena a propia lista

print("\n",ordenar) #
print(contra) #
print(idades)


# #########   ORDENAÇÃO DE OBJETOS     ###################

class banco:
    def __init__(self,nome):
        self._nome = nome
        self._saldo = 0
        
    def salario(self,valor):
        self._saldo +=valor

    def __str__(self):
        return f'\nNome do cliente: {self._nome} Saldo: R$:  {self._saldo} '
    
    
Pedro = banco("Pedro")
antonio = banco("antonio")
antonio2 = banco("Antonio")
francisca = banco("Francisca")

Pedro.salario(400)
francisca.salario(500)
antonio.salario(100)
antonio2.salario(2000)
clientes = [antonio,francisca,Pedro,antonio2]

for x in clientes:
    print(x)
print("\n","+"*10," Usando o Extrai_saldo".upper(),"*"*40)
#ordenar por salário = Podemos usar a funcçao que criamos extrai saldo
def extrai_saldo(banco):
    return banco._saldo

for x in sorted(clientes, key=extrai_saldo):
    print(x)

print("-"*40)

#ordenar por Nomes = Podemos usando uma funçao 
#Letras minúsculas ficar ordenados por ùltimo
def extrai_nome(banco):
    return banco._nome

for x in sorted(clientes, key=extrai_nome):
    print(x)

print("-"*40)



# Agora vamos usar o  modo mais simples usando o metodo ( attrgetter )
# Precisamos importar primeiro o método

from operator import attrgetter

print("\n","+"*10," USANDO O attrgetter".upper(),"*"*40)
for x in sorted(clientes, key=attrgetter("_saldo")):
  print(x)

print("-"*40)

for x in sorted(clientes, key=attrgetter("_nome")):
  print(x)
print("-"*40)
############+++++++++++++======================###############################
############################################################################

#Vamos usar um metodo lt para ordenar e não precisamos usar o extrai_saldo]
class banco:
    def __init__(self,nome):
        self._nome = nome
        self._saldo = 0
        
    def salario(self,valor):
        self._saldo +=valor

    def __lt__(self,outro): # Esta função verifica se um elemento é menor que outro
        self._saldo < outro._saldo

    def __str__(self):
        return f'\nNome do cliente: {self._nome} Saldo: R$:  {self._saldo} '
    
    
Pedro = banco("Pedro")
antonio = banco("antonio")
antonio2 = banco("Antonio")
francisca = banco("Francisca")

Pedro.salario(400)
francisca.salario(500)
antonio.salario(100)
antonio2.salario(2000)
clientes = [antonio,francisca,Pedro,antonio2]

for x in clientes:
    print(x)
print("-"*40)

#ordenar por salário = Podemos usar a funcçao que criamos sem extrai saldo
# def extrai_saldo(banco):
#     return banco._saldo


print("\n","+"*10," USANDO o (it) sem o extrai_saldo","*"*20)
for x in sorted(clientes):
    print(x)

print("-"*40)


