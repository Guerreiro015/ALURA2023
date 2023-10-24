# import sqlite
import sqlite3 as lite

# Criando banco de dados
con = lite.connect("dados.bd")

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE inventario(id INTEGER PRIMARY KEY AUTOINCREMENT,\
                 nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_compra DATE, \
                valor_compra DECIMAL, serie TEXT, imagem TEXT)")



