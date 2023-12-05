# import os

# UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/static/uploads'

n1= 19898.9999999999999

t =2 # Numero de casas

d = int(n1 * 10**t)/10**t

print('Truncado', d)

teste=f'Arredondado {n1: .2f}'
print(teste)