import requests
from fastapi import FastAPI

url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
dados=[{'code': 'USD', 'codein': 'BRL', 'name': 'Dólar Americano/Real Brasileiro', 'high': '4.938', 'low': '4.8602', 'varBid': '-0.0219', 'pctChange': '-0.45', 'bid': '4.8743', 'ask': '4.8755', 'timestamp': '1704488400', 'create_date': '2024-01-05 18:00:00'}]
response=requests.get(url)

if response.status_code == 200:
    dados_jason=dados    
    print(dados_jason)

else:
    print('Dados não Encontrados')

def nomes_moedas():
    a=[]
    b=''
    for i in dados_jason:
        print(i)
        if b != i['name']:
            b=i['name']
            a.append(i['name'])    
    print(a)

print('\nNomes das Moedas')
nomes_moedas()
input('\nContinuar')
    

