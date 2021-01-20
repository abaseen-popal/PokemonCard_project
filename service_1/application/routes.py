from application import app,db
from application.models import Pokemons
from sqlalchemy import desc 
import requests
from flask import render_template, request


@app.route('/')
def index():
    pokemon_response = requests.get("http://pokemon-names_pokemon-backend:5000/pokemon")
    psa_response = requests.get("http://pokemon-psa_pokemon-backend3:5000/psa")
    evaluation_response = requests.post("http://pokemon-eva_pokemon-backend4:5000/evaluation", json={"pokemon":pokemon_response.text,"psa": psa_response.text })
    
    
    new_pokemon = Pokemons(pokemon_name=pokemon_response.text, pokemon_psa=psa_response.text,pokemon_evaluation=evaluation_response.text)
    db.session.add(new_pokemon)
    db.session.commit()
    
    all_pokemon = Pokemons.query.order_by(desc("id")).limit(5).all()
    
    return render_template("index.html",pokemon=pokemon_response.text, psa=psa_response.text,all_pokemon=all_pokemon, evaluation=evaluation_response.text)
    
