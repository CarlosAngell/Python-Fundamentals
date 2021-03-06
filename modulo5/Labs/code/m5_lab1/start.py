'''
classe: m5_lab1
descricao: Construa uma aplicação WEB que mostra uma tabela com cadastro do deputado (Foto, Id,Nome, Estado e Partido) 
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 09 de maio de 2019
'''
from flask import Flask, render_template
from lib import DadosAbertos

app = Flask(__name__)

@app.route("/")
def deputados():
   obj = DadosAbertos()
   list_dep = obj.deputados()

   return render_template('lista.html', listas=list_dep)



if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)