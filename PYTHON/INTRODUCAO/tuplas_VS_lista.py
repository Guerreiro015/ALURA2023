import os
os.system("cls")

dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
semana = ("Domingo", "Segunda", "Terça", "Terça", "Quinta", "Sexta", "Sábado")
num = range(0,10)
# lista e formada usando colchetes
# tuplas é formada com parenteses
# A lista pode ser moficicada 
# A tupla NÃO pode ser modificada
# o RANGE também é um tipo de lista
dias.append('outro domimgo')
print(dias)

dias.pop()
print(dias)

print(semana)
print(num[5])

print(semana.index("Quinta"))
print(semana.count("Terça"))

sem = tuple(dias) # Transformar lista em tupla
print(sem,"\n")
dia = list(semana) # Transformar tupla em lista
print(dia,"\n")

dias.append(semana) # Incluindo uma tupla dentro da lista
print(dias)


# Não podemos usar del, remove(), pop() ou clear() com uma tupla
# podemos usar com lista

del dias[0] # deleta pelo indice do lista
print(dias)

dias.remove("Segunda") # Remove o item selecionado
print(dias)

dias.pop() # Remove o último item
print(dias)
dias.pop(3) # remove pelo indice
print(dias)

dias.clear() # limpa tudo
print(dias)

# Alem de lista e tupla existe também o SET - USAMOS CHAVES {}
# O set não aceita  incluir valores duplicado
# No set usamos add ao invés de append

colecao = {111, 222, 333}
print (colecao)

colecao.add(444)
print (colecao)

print("="*50)

# Um set é uma coleção não ordenada de elementos. Cada elemento é único, isso significa que não existem elementos duplicados dentro do set.

# Respire fundo e fique tranquilo pois o set será abordado ainda com mais detalhe em outros cursos. Vamos continuar?

# compreenson lista - for simplificado direto

palavra = "banana".upper()
listas = ["A" for letra in palavra]

print(listas,"\n")

frutas = ["maçã", "banana", "laranja", "melancia"] # Transformar em maíusculas
lista = []
for fruta in frutas:
    lista.append(fruta.upper())

lote = [indice.upper() for indice in frutas]

print(listas,"\n")
print(lote,"\n")

print("="*50)



