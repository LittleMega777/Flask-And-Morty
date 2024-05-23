from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route('/')
def hello():
    messagem_app_py = "Hello World"
    return render_template('index.html', message=messagem_app_py)

@app.route('/sorteio')
def hello1():
    message = randint(1, 800) # random + int = inteiro aleatorio
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)