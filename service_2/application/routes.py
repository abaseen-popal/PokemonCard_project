from application import app
from flask import request, Response
import random 

@app.route("/pokemon",methods=["GET"])
def get_pokemon():
    pokemon = ["Pikachu - Yellow (Lightning)", "Charizard - Red (Fire)", "Mudkip - Blue (Water)","Venusaur - Green (Grass)", "Gengar - Purple (Ghost)"]
    return Response(str(random.choice(pokemon)), mimetype='text/plain')


