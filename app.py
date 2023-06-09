from flask import Flask, render_template
from requests import get


app = Flask(__name__)

@app.route('/')
def index():
    content = get('https://tmare.ndelpech.fr/tps/pokemons')
    pokemons=content.json()
    pokemon=get('https://tmare.ndelpech.fr/tps/pokemons/{}'.format(pokemons[150]['id'])).json()
    return pokemon['name']['fr']

@app.route('/poke')
def corp():
    content = get('https://studies.delpech.info/pbi/pokemons/dataset/json')
    pokemons=content.json()
    print(pokemons)
    return render_template ('corp.jinja',pokemons=pokemons)

@app.route('/pokeInfo2/<string:i>')
def pokeInfo2(i):
    content = get('https://studies.delpech.info/pbi/pokemons/dataset/' + i + '/json')
    pokemons=content.json()
    return render_template ('pagePokemon.jinja',pokemons=pokemons)

