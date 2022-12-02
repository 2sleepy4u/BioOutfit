from collections import namedtuple
from glob import escape
from flask import Flask, request, Response
import json

# custom
from utility.temperature import get_today_temperature, Trieste
from utility.genetic_algorithm import run_evolution
from utility.logging import suggestion_log

app = Flask(__name__)

@app.route('/')
def index():
    return "HOME"

@app.get('/generate')
def post_outfit():
    fashion     = int(request.args.get('fashion', 7))
    temperature = get_today_temperature(Trieste)
    temperature = int(request.args.get("temperature", temperature))

    if fashion > 10 or fashion < 1:
        return Response('{"Error": "Fashion level out of range (1-10)"}', status=201, mimetype='application/json')

    try:
        population, generations = run_evolution(
            temperature=temperature,
            min_temperature=-10,
            max_temperature=30,
            min_fashion=fashion,

            size=50,
            max_generations=100,
            max_fitness=70,
            verbose=False
        )
        result  = "<h2>Creazione outfit</h2>"
        result += f"<div>Livello di fashion minimo selezionato: {fashion}</div>"
        result += f"<div>Oggi in media ci sono {temperature} C°</div>"
        result += f"<h3>Ti consiglio questo outfit: </h3>"
        result += f"<p style='margin:10px;'>{suggestion_log(population)}</p>"
        result  = f"<div>{result}</div>"
        return result
    except ValueError:
        return Response("E' molto probabile che i capi di abbigliamento non siano abbastanza bilanciati!")
    
@app.post('/generate')
def get_outfit():
    data = request.get_json()
    data = json.dumps(data)

    fashion = data["fashion"]

    return f"Fashion level {escape(fashion)}"


# INSERT
@app.get('/insert')
def get_insert():
    data = {}
    data["name"]        = request.args.get('name', 'untitled')
    data["fashion"]     = request.args.get('fashion', 6)
    data["warmness"]    = request.args.get('warmness', 6)
    data = json.dumps(data)
    return f"{data}"

@app.post('/insert')
def post_insert():
    data = request.get_json()
    data = json.dumps(data)
    return f'{data}'


@app.route('/update', methods=["POST", "GET"])
def modifica():
    return "Qui verranno modificati i vestiti!"

