from asyncio import DefaultEventLoopPolicy
from flask import Flask,render_template

# criar a 1 pagina no site
# route -> caminho a seguir
# função -> O que vai ser exibido no site
# vamos usar servirdor heroko gratis

app = Flask(__name__)

@app.route("/") #Decorate logo acima da função
def homepage():
    return render_template('index.html')


@app.route("/contatos")
def contatos():
   return render_template('contatos.html')


@app.route('/cliente', defaults={"nome_cliente": "USUÁRIO"} )
@app.route('/cliente/<nome_cliente>')
def cliente(nome_cliente):
   return render_template('cliente.html',nome_cliente=nome_cliente)
   # para executarmos um variavel python no html colocamos ela entre duas chaves{{variavel}}


@app.route('/usuario')
def usuario():
   nome="FAISCA"
   dados={
      'nome': 'Antonio',
      'filho': 'Lucas',
      'filha': 'Luana',
      'esposa': 'Francisca'
   }
   return render_template('usuario.html', nome=nome,dados=dados)

if __name__ == __name__:  
  app.run(debug=True) # Colocando o true o site atusliza as informaões automoaticamnte
