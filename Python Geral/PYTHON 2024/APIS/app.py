import requests

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response=requests.get(url)

if response.status_code == 200:
    dados_jason=response.json()
    print(dados_jason)

else:
    print('Dados não Encontrados')

def nomes_restaurantes():
    a=[]
    b=''
    for i in dados_jason:
        if b != i['Company']:
            b=i['Company']
            a.append(i['Company'])    
    print(a)

print('\nNomes dos Restaurantes')
nomes_restaurantes()
input('\nContinuar')
    
lojas=[]
def procura(loja):
    for i in dados_jason:
        
        if i['Company']==loja:
            x={'Loja:':i['Company'],'Lanche': i['Item'], 'Preco': i['price'],'Descrição': i['description']}
            
            lojas.append(x)
    for y in lojas:        
        print(f"\nLanchonete: -> {y['Loja:']}\nLanche: -> {y['Lanche']} \nDescrição do lanche: -> {y['Descrição']} \nPreço: -> {y['Preco']} ")   

procura('Wendy’s')


def nomes_restaurantes():
    a=[]
    b=''
    for i in dados_jason:
        if b != i['Company']:
            b=i['Company']
            a.append(i['Company'])    
    print(f'Nomes dos RESTAURANTES:\n')      
    input("Continue")  
    print(a)
    for i in a:    
        procura(i)
        input('Continue')

nomes_restaurantes()





