from flask import Flask, render_template, request
from random import randint
import requests

app = Flask(__name__)

def sorteio_personagem():
  resposta = requests.get(f"https://rickandmortyapi.com/api/character/{randint(1, 826)}", verify=False)
  return resposta.json()

personagem = sorteio_personagem()

@app.route('/')
def hello():
    return render_template('index.html', url=personagem['image'], name=personagem['name'], status=personagem['status'], especie=personagem['species'])

@app.route('/', methods=['POST'])
def sorteio():
   personagem = sorteio_personagem()
   return render_template('index.html', url=personagem['image'], name=personagem['name'], status=personagem['status'], especie=personagem['species'])

if __name__ == '__main__':
    app.run(debug=True)