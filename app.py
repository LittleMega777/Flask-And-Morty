from flask import Flask, render_template, jsonify
from random import randint
import requests
import urllib3
from models import personagem
urllib3.disable_warnings()

app = Flask(__name__)

character = personagem.RandomCharacter()

@app.route('/')
def hello():
    return render_template('index.html', url=character.img, name=character.name,
                            status=character.status, especie=character.specie)

@app.route('/get_random_data', methods=['GET'])
def sorteio():
   data = character.sorteio_personagem()
   return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)