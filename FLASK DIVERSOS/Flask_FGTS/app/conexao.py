
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine as ce
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
#pip install PyMySQL


engine = ce('mysql://root:lucas0108@localhost:3306/jogoteca')
base=declarative_base()
session=sessionmaker(bind=engine)
session=session()


class usuarios(base):
   __tablename__= "usuarios"

   id = Column(Integer, primary_key=True, autoincrement=True)
   nome = Column(String(45), nullable=False)
   nickname = Column(String(45), nullable=False)
   senha = Column(String(45), nullable=False)
   

   def __repr__(self): 
      return f'usuarios [id={self.id}, nome={self.nome}, nickname={self.nickname} senha={self.senha}]'
   


#insert
# dados_inserir=usuarios(nome='antonio', nickname='antonio',senha='1234') #instanciando
# session.add(dados_inserir) #inserindo
# session.commit() # gravando

busca='antonio'

# #Delete
# session.query(usuarios).filter(usuarios.nome==busca).delete()
# session.commit()

#update
session.query(usuarios).filter(usuarios.nome==busca).update({'senha': '12367'})
# session.commit()

#Select
dados=session.query(usuarios).all()
print(dados)
print(dados[0].nome,dados[0].senha)





session.close()

