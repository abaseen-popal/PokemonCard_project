# Importing moduels 
from application import app,db
from application.models import Pokemons
from sqlalchemy import desc 
import requests
from flask import render_template, request


@app.route('/')
def index():
    # Getting the result from different services to show in the frontend 
    pokemon_response = requests.get("http://pokemon-stack_pokemon-backend:5000/pokemon")
    psa_response = requests.get("http://pokemon-stack_pokemon-backend3:5000/psa")
    evaluation_response = requests.post("http://pokemon-stack_pokemon-backend4:5000/evaluation", json={"pokemon":pokemon_response.text,"psa": psa_response.text })
    # service 4 saves values in a json format 
    
    new_pokemon = Pokemons(pokemon_name=pokemon_response.text, pokemon_psa=psa_response.text,pokemon_evaluation=evaluation_response.text)
    # The values are saved from the different services and then are pushed into the database  
    db.session.add(new_pokemon)
    db.session.commit()
    
    all_pokemon = Pokemons.query.order_by(desc("id")).limit(5).all()
    # querying the database to get the latest 5 values 
    return render_template("index.html",pokemon=pokemon_response.text, psa=psa_response.text,all_pokemon=all_pokemon, evaluation=evaluation_response.text)
    # Renduring the values into the template 
