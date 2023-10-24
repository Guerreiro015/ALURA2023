
# CRIAÇÃO DE BANCO DE DADOS MySQL - COM Python

import mysql.connector

def criar_bd(banco,tabela):
      conn = mysql.connector.connect(user='root', password='lucas0108', host='localhost')
      cursor = conn.cursor()
      comando=(f'CREATE DATABASE IF NOT EXISTS {banco}')
      cursor.execute(comando)

      conn = mysql.connector.connect(user='root', password='lucas0108', host='localhost',database=f'{banco}')
      cursor = conn.cursor()      
            

      comando= f'''CREATE TABLE IF NOT EXISTS {tabela} (
    id int(11) NOT NULL, 
    nome VARCHAR(45) NOT NULL, 
    nickname VARCHAR(45) NOT NULL,
    senha VARCHAR(45) NOT NULL,
    PRIMARY KEY(id) )'''

      cursor.execute(comando)

criar_bd('base','escola') # Instanciando a criação do banco de dados
# base = nome do banco de dados
# escola = nome da tabela dentro do banco de dados



