from flask import Flask, render_template, jsonify
from random import randint
import requests
import urllib3

urllib3.disable_warnings()

app = Flask(__name__)

def sorteio_personagem():
  resposta = requests.get(f"https://rickandmortyapi.com/api/character/{randint(1, 826)}", verify=False)
  return resposta.json()

personagem = sorteio_personagem()

@app.route('/')
def hello():
    return render_template('index.html', url=personagem['image'], name=personagem['name'], status=personagem['status'], especie=personagem['species'])

@app.route('/get_random_data', methods=['GET'])
def sorteio():
   data = sorteio_personagem()
   return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)