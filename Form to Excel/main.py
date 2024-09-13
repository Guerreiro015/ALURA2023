# from fasthtml.common import *
from fasthtml.common import FastHTML, serve

app = FastHTML()

@app.get("/")
def homepage():
    return"<h1> SEja bem Vindo ao meu site alkterado</h1>"

serve()
