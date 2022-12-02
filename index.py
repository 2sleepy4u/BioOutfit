from collections import namedtuple
from glob import escape
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "HOME"

@app.route('/generate/<fashion>')
def outfit(fashion):
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

