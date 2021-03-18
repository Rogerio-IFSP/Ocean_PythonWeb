from flask import Flask

app = Flask("microblog")

#@ é comando decoreter (è um operador do PYTHOM que fica em cima de uma função e faz 
#alguma coisa com essa função)
#o @ chama um URL route
@app.route("/")
def index():
    return "Olá Mundo!"

# para executar
app.run()