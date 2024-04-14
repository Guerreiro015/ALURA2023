import os
os.system("cls")

# compreenson lista - for simplificado direto

palavra = "banana".upper()
listas = ["A" for letra in palavra]

print(listas,"\n")

frutas = ["maçã", "banana", "laranja", "melancia"] # Transformar em maíusculas
lista_frutas = []

for fruta in frutas: #" maneira do for normal"
    lista_frutas.append(fruta.upper())
# ==================================================
lote = [indice.upper() for indice in frutas] # Maneira do for lista compreesson ( simplificado)
#===================================================
print(lista_frutas,"\n")
print(lote,"\n")

print("="*50)

inteiros = [1,3,4,5,7,8]
total = [som * 2 for som in inteiros] # exemplos
print('\n',total)

frutas = ["maçã", "banana", "laranja", "melancia"]
sacola = []
sacolao = [n.capitalize() for n in frutas] # exemplos
print(" ".join(sacolao))


soma = [item for item in frutas if item == "banana"]
total = [item for item in inteiros if item > 4]
print(soma)
print(total)

#-------------------------------------------------------------
#-------------------------------------------------------------
inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        pares.append(numero)

print("\n",pares)

par = [x for x in inteiros if x % 2 == 0] # usando a condiçao if para saber se o resto % é 0

print(par)


palavra = "MARACUJA"
compre = [("=") for a in palavra]
compre2 = [n.lower() for n in palavra]
compre3 = [n.lower() for n in palavra if n == "A"]

print("\n",' '.join(compre))
print("\n",' '.join(compre2))
print("\n",' '.join(compre3))



