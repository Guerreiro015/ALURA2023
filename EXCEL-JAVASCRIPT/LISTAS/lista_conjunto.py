import os
os.system("cls")



usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]
print(usuarios_data_science,usuarios_machine_learning)

todos = usuarios_data_science
all = usuarios_data_science.copy()
print (todos)
print (all)

todos.extend(usuarios_machine_learning)
all.extend(usuarios_machine_learning)

print (todos)
print (all)

# Uma das formas seria usar um for e IF:
res = []
for i in todos:
    if i not in res:
      res.append(i)
print(res)  

# Maneira mais fácil de retirar as duplicidades é usando o (set) = conjunto
# O set forma um cojunnto e desconsidera todos os dados duplicados
# O conjuto pode ser iteravel mas não possui indexação

conjunto = set(todos)
conjunto2 = set(usuarios_data_science+usuarios_machine_learning)
conjunto3 = sorted(set(todos))


print("\n",conjunto)
print(conjunto2)
print(conjunto3)

print(type(conjunto))

# Colocando os dados já como {} conjunto podemos usar o sinal | = or, para juntar removendo as duplicatas
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
conjunto4 = usuarios_data_science | usuarios_machine_learning
print("\n",conjunto4)

#Colocando os dados já como {} conjunto podemos usar o sinal & = e , para mostrar apenas as duplicatas
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
conjunto5 = usuarios_data_science & usuarios_machine_learning
print("\n",conjunto5)

#Colocando os dados já como {} conjunto podemos usar o sinal - = menos , mostrar apenas os itens que únicos
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
conjunto6 = usuarios_data_science - usuarios_machine_learning
print("\n",conjunto6)

#Colocando os dados já como {} conjunto podemos usar o sinal ^ = excluxivo , mostrar apenas os itens exclusivos
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}
conjunto7 = usuarios_data_science ^ usuarios_machine_learning
print("\n",conjunto7)

# Os comjuntos são mutaveis, mas acrescentar um item usamos o add em vez do append
conjunto7.add(50)
print(f'\n Contém {len(conjunto7)} itens - > {conjunto7}')
print("\n",conjunto7)



# Desempacotando
desempacote = []
for i,y in enumerate(conjunto7):
   desempacote.append(y)
   print(i,y)
print(desempacote)

# Para tonarmos um conjumto não iteravel usamos o frozem

conjunto7 = frozenset(conjunto7)

print("\n",conjunto7)
print(type(conjunto7))

# Mas ainda conseguimos desempacotar
desempacote = []
for i,y in enumerate(conjunto7):
   desempacote.append(y)
   print(i,y)
print(desempacote)

print('\n','-'*50)
# Os comjuntos são mutaveis, mas acrescentar um item que ja existe ele desconsidera
usuarios = {1,5,76,34,52,13,17}
print(usuarios)

usuarios.add(13)
print(usuarios)


usuarios.add(765)
print(usuarios)

#Quebrando em espaços em branco e tirando as duplicidades
meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
lista =meu_texto.split() # Retira os espaços em branco e transforma em lista
print(lista)
lista = set(meu_texto.split()) # Retira os espaços em branco e transforma em conjunto sem duplicidade.


print(lista)


