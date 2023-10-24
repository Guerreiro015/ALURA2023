from flask import Flask, render_template, request, redirect, session,flash
from flask import Flask, url_for

app = Flask(__name__)
app.secret_key='alura'

logado='nao'

class jogo():
  def __init__(self,nome,categoria,console,ano):
    self.nome=nome
    self.categoria=categoria
    self.console=console
    self.ano=ano


jogo1=jogo('God of War','Aventura','ps5','2001')
jogo2=jogo('Skyrin','Neve','ps2','2005')
jogo3=jogo('Clash','Cachorrinho','X-box','2013')
jogo4=jogo('Tomb Raider','Exploração','ps1','2003')
jogo5=jogo('Mortal Kombat','Lutinha','ps4',"2023")

lista_jogos=[jogo1,jogo2,jogo3,jogo4,jogo5]

class usuarios():
   def __init__(self,nome,nickname,senha):
     self.nome=nome
     self.nickname=nickname
     self.senha=senha

usuario1=usuarios('Marcos',"marcos",'123')     
usuario2=usuarios('Antonio',"antonio",'1234')     
usuario3=usuarios('Lucas',"lucas",'12345')   

usuarios={usuario1.nickname: usuario1,
          usuario2.nickname: usuario2,
          usuario3.nickname: usuario3,
   
}


@app.route('/')
def login():
   return render_template('login.html',titulo='LOGIN')

@app.route('/index')
def index():
   if 'usuario_logado' not in session or session['usuario_logado'] == None:
        flash('Nenhum Usuário Logado')
        return redirect(url_for('login'))
   else:
        tit="jogos de 2023"
        return render_template('index.html',titulo=tit,jogos=lista_jogos)

@app.route('/novo_jogo')
def novo_jogo():
  if 'usuario_logado' not in session or session['usuario_logado'] == None:      
        flash('Nenhum Usuário Logado')
        return redirect(url_for('login'))
  else:
        return render_template('novo_jogo.html', titulo="novo jogo")


@app.route('/criar', methods=['POST'])
def criar():
  nome=request.form['nome']
  categoria=request.form['categoria']
  console=request.form['console']
  ano=request.form['ano']
  jogar=jogo(nome,categoria,console,ano)
  lista_jogos.append(jogar)
  return redirect(url_for('index'))

# @app.route('/autenticar', methods=['POST'])
# def autenticar():
  # usuario=request.form['usuario']
  # senha=request.form['senha']
  # if usuario == 'antonio' and senha == '123':
  #   session['usuario_logado']=request.form['usuario']
  #   flash(request.form['usuario']+' Logado com Sucesso')
  #   return redirect(url_for('index'))
  # else:
  #   flash(request.form['usuario']+' Não Conseguiu Logar')
  #   return redirect(url_for('login'))
@app.route('/autenticar', methods=['POST'])
def autenticar():  
  if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash('Usuário '+ usuario.nickname + ' logado com sucesso!')
            return redirect(url_for('index'))
        else:
            flash('Usuário não logado.')
            return redirect(url_for('login'))
  else:
    flash('Digite o nome de um usuário.')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
  flash('Usuário Desconectado')
  session['usuario_logado'] = None
  return redirect(url_for('login'))





if __name__ == __name__:  
  app.run(debug=True)

  # trecho da app
#app.run(host='0.0.0.0', port=8080)
