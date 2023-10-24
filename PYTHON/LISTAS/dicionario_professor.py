import os
os.system("cls")
from collections import defaultdict
from collections import Counter


texto1 = '''Parabéns e muitas felicidades!
Este é seu dia especial
E por isso deve festejar com alegria.
Espero que receba muito carinho
Homenagens e surpresas boas
Que hoje e sempre não falte a
Saúde, a paz e o amor.
Feliz aniversário! 
Tenha um feliz aniversário cheio
de sorrisos e gargalhadas, repleto
de paz, amor e muita alegria.
Parabéns por mais um ano de vida!
 '''
 
aparicoes = Counter(texto1.lower())
print(aparicoes.values())

aparicoes = Counter(texto1.lower())
total_de_caracteres = sum(aparicoes.values())
for letra, frequencia in aparicoes.items():
    tupla=(letra, frequencia / total_de_caracteres)
    print(tupla)

def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))
  mais_comuns = proporcoes.most_common(10)
  for caractere, proporcao in mais_comuns:
    print(f"\n{caractere} => {proporcao * 100:.2f}%")
analisa_frequencia_de_letras(texto1)


