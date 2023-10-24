import os
os.system("cls")

idades = [20, 39, 18, 27, 19]

for elemento in idades: 
  print("Recebi o elemento", elemento)

idades = [20, 39, 18]
idades.append(10) # Adicionar um elemennto no final
idades.insert(0,15) # Adicionar um elemento na posição estipulada
idades.extend([30, 12, 15]) # Adicionar mais de um elemento

print(idades)

if 15 in idades:
  idades.remove(15) # Remover um elemento semore o 1º encontrado

print(idades)

for x in idades:
  print(x + 1) # Alterar o valor de cada item

nova_idade = []
for x in idades:
  nova_idade.append(x + 1) # Alterar o valor de cada item em uma nova variavel
print(nova_idade)

nova_idade = [x+1 for x in idades] # Simplificando o for


nova_idade = [x+1 for x in idades if x > 18] # usando o if para alterrar apenas alguns valores
print(nova_idade)






