import os
os.system("cls")


# o enumerate é usado para mostrar os elementos e a posição do elemento

idades = [15, 87, 65, 56, 32, 49, 37, 32]

ordenar = sorted(idades) # Colocar em ordem
contra = sorted(idades, reverse = True)# Ordenar ao contrário
idades.sort() # ordena a propia lista

print("\n",ordenar) #
print(contra) #
print(idades)

for x in idades:
    print (x)


posicao = range(len(idades))

for x in range(len(idades)):
    print(x,idades[x])


# Temos que mostrar pro enumerate como queremos o elemento

resu = list(enumerate(idades)) # lista de tuplas
print("\n",resu,"\n")

for x in enumerate(idades): # Varias tuplas
    print(x)

# Desempacotando

for x,y in enumerate(idades): # Valores desempacotados

    print(x," - ",y)

# Continuando o desempacotamento tuplas

clientes = [
('Guilherme', 37, 1981),
('Daniela', 31, 1987),
('Paulo', 39, 1979),
('Luana',23, 1998)
]

for nome,idade,ano in clientes:
    print('Nome: ',nome," --- Idade: ",idade) # podemos escolher apenas alguns campos


for nome,_,_ in clientes: # podemos usar underline para ignorar outros campos
    print('Nome: ',nome)

