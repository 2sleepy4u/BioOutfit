from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Qui verrà utilizzato l'algoritmo!"

@app.route('/impostazioni')
def impostazioni():
    return "Qui verranno modificate impostazioni varie!"

@app.route('/inserisci')
def inserisci():
    return "Qui verranno inseriti i vestiti!"

@app.route('/modifica')
def modifica():
    return "Qui verranno modificati i vestiti!"

