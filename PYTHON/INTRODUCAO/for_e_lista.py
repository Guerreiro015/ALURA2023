import os
os.system("cls")

dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]

fruta = "maracuja"
x=0
for lista in dias:
    print(lista)
    x +=1
print(x,' itens')

for lista in fruta:
    print(lista)
    x +=1
print(x,' itens')

for lista in range(10):
    print(lista)

for lista in range(1,10):
    print(lista)

for lista in range(0,100,10):
    print(lista)

mês='''janeiro fevereiro março abril maio junho julho agosto
  setembro outubro novembro dezembro'''.split()
print(mês[3-1])

for lista in mês:
  print(lista)

dias = '''segunda terca quarta'''.strip()
for lista in dias:
    print(lista)

