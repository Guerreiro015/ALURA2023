import sqlite3 as lite

# Criando banco de dados
con = lite.connect("INSS.bd")

# Criando tabela
with con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE dados(id INTEGER PRIMARY KEY AUTOINCREMENT,
                de1 DECIMAL,ate1 DECIMAL,ali1 DECIMAL,par1 DECIMAL,
                de2 DECIMAL,ate2 DECIMAL,ali2 DECIMAL,par2 DECIMAL,
                de3 DECIMAL,ate3 DECIMAL,ali3 DECIMAL,par3 DECIMAL,
                de4 DECIMAL,ate4 DECIMAL,ali4 DECIMAL,par4 DECIMAL,
                deir1 DECIMAL,ateir1 DECIMAL,aliir1 DECIMAL,parir1 DECIMAL,
                deir2 DECIMAL,ateir2 DECIMAL,aliir2 DECIMAL,parir2 DECIMAL,
                deir3 DECIMAL,ateir3 DECIMAL,aliir3 DECIMAL,parir3 DECIMAL,
                deir4 DECIMAL,ateir4 DECIMAL,aliir4 DECIMAL,parir4 DECIMAL,
                deir5 DECIMAL,aliir5 DECIMAL,parir5 DECIMAL,tetoinss DECIMAL,
                dedudep DECIMAL,dedusimp DECIMAL
                 )''')

    