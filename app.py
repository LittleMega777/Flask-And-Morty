from flask import Flask, render_template, request
from random import randint
import requests

app = Flask(__name__)

def sorteio_personagem():
  resposta = requests.get(f"https://rickandmortyapi.com/api/character/{randint(1, 826)}", verify=False)
  return resposta.json()["image"]

@app.route('/')
def hello():
    return render_template('index.html', url=sorteio_personagem())

@app.route('/', methods=['POST'])
def sorteio():
   button_value = request.form['button']
   return render_template('index.html', url=sorteio_personagem())

if __name__ == '__main__':
    app.run(debug=True)