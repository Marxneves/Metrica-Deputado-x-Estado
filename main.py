from flask import Flask, render_template
from lib import DadosAbertos

app = Flask(__name__)


@app.route("/")
def deputados():
   obj = DadosAbertos()
   list_dep = obj.deputados()

   estados = {}

   for dep in list_dep:
       estado = dep['siglaUf']
       if estado in estados:
             estados[estado] += 1
       else:
          estados[estado] =  1
   #print(estados)
          
   bar_labels=estados.keys()
   bar_values=estados.values()

   return render_template('index.html', max=80, labels=bar_labels, values=bar_values)

if __name__ == "__main__":
   app.run(host='0.0.0.0', debug=True, port=8080)