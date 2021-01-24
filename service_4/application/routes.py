# -------------importing modules -------------
from application import app
from flask import request, Response
import random 

@app.route("/evaluation", methods=["GET","POST"])
def get_evaluation ():
    evaluation_value = 0
    card_info = request.get_json()
    # ------If statements to check the worth of the pokemon cards------
    if card_info["pokemon"] == "Pikachu - Yellow (Lightning)" and card_info["psa"] == "10- Gem Mint - Pristine":
        evaluation_value = 5000
    if card_info["pokemon"] == "Pikachu - Yellow (Lightning)" and card_info["psa"] == "9 - Mint":
        evaluation_value = 3000
    if card_info["pokemon"] == "Pikachu - Yellow (Lightning)" and card_info["psa"] == "8- Near Mint-Mint":
        evaluation_value = 2000
    if card_info["pokemon"] == "Pikachu - Yellow (Lightning)" and card_info["psa"] == "7- Near Mint":
        evaluation_value = 1000
    if card_info["pokemon"] == "Pikachu - Yellow (Lightning)" and card_info["psa"] == "6- Excellent- Near Mint":
        evaluation_value = 750
    if card_info["pokemon"] == "Pikachu - Yellow (Lightning)" and card_info["psa"] == "5- Excellent":
        evaluation_value = 500
    if card_info["pokemon"] == "Pikachu - Yellow (Lightning)" and card_info["psa"] == "4- Very Good - Excellent":
        evaluation_value = 300
    if card_info["pokemon"] == "Pikachu - Yellow (Lightning)" and card_info["psa"] == "3 - Very Good":
        evaluation_value = 200
    if card_info["pokemon"] == "Pikachu - Yellow (Lightning)" and card_info["psa"] == "2- good":
        evaluation_value = 50
    if card_info["pokemon"] == "Pikachu - Yellow (Lightning)" and card_info["psa"] == "1- Poor":
        evaluation_value = 20

    # ------If statements to check the worth of the pokemon cards------

    if card_info["pokemon"] == "Charizard - Red (Fire)" and card_info["psa"] == "10- Gem Mint - Pristine":
        evaluation_value = 35000
    if card_info["pokemon"] == "Charizard - Red (Fire)" and card_info["psa"] == "9 - Mint":
        evaluation_value = 20000
    if card_info["pokemon"] == "Charizard - Red (Fire)" and card_info["psa"] == "8- Near Mint-Mint":
        evaluation_value = 10000
    if card_info["pokemon"] == "Charizard - Red (Fire)" and card_info["psa"] == "7- Near Mint":
        evaluation_value = 5000
    if card_info["pokemon"] == "Charizard - Red (Fire)" and card_info["psa"] == "6- Excellent- Near Mint":
        evaluation_value = 3000
    if card_info["pokemon"] == "Charizard - Red (Fire)" and card_info["psa"] == "5- Excellent":
        evaluation_value = 1000
    if card_info["pokemon"] == "Charizard - Red (Fire)" and card_info["psa"] == "4- Very Good - Excellent":
        evaluation_value = 500
    if card_info["pokemon"] == "Charizard - Red (Fire)" and card_info["psa"] == "3 - Very Good":
        evaluation_value = 250
    if card_info["pokemon"] == "Charizard - Red (Fire)" and card_info["psa"] == "2- good":
        evaluation_value = 150
    if card_info["pokemon"] == "Charizard - Red (Fire)" and card_info["psa"] == "1- Poor":
        evaluation_value = 50

    # ------If statements to check the worth of the pokemon cards------


    if card_info["pokemon"] == "Mudkip - Blue (Water)" and card_info["psa"] == "10- Gem Mint - Pristine":
        evaluation_value = 500
    if card_info["pokemon"] == "Mudkip - Blue (Water)" and card_info["psa"] == "9 - Mint":
        evaluation_value = 350
    if card_info["pokemon"] == "Mudkip - Blue (Water)" and card_info["psa"] == "8- Near Mint-Mint":
        evaluation_value = 300
    if card_info["pokemon"] == "Mudkip - Blue (Water)" and card_info["psa"] == "7- Near Mint":
        evaluation_value = 200
    if card_info["pokemon"] == "Mudkip - Blue (Water)" and card_info["psa"] == "6- Excellent- Near Mint":
        evaluation_value = 100
    if card_info["pokemon"] == "Mudkip - Blue (Water)" and card_info["psa"] == "5- Excellent":
        evaluation_value = 50
    if card_info["pokemon"] == "Mudkip - Blue (Water)" and card_info["psa"] == "4- Very Good - Excellent":
        evaluation_value = 20
    if card_info["pokemon"] == "Mudkip - Blue (Water)" and card_info["psa"] == "3 - Very Good":
        evaluation_value = 10
    if card_info["pokemon"] == "Mudkip - Blue (Water)" and card_info["psa"] == "2- good":
        evaluation_value = 5
    if card_info["pokemon"] == "Mudkip - Blue (Water)" and card_info["psa"] == "1- Poor":
        evaluation_value = 2

    # ------If statements to check the worth of the pokemon cards------

    if card_info["pokemon"] == "Venusaur - Green (Grass)" and card_info["psa"] == "10- Gem Mint - Pristine":
        evaluation_value = 20000
    if card_info["pokemon"] == "Venusaur - Green (Grass)" and card_info["psa"] == "9 - Mint":
        evaluation_value = 10000
    if card_info["pokemon"] == "Venusaur - Green (Grass)" and card_info["psa"] == "8- Near Mint-Mint":
        evaluation_value = 6000
    if card_info["pokemon"] == "Venusaur - Green (Grass)" and card_info["psa"] == "7- Near Mint":
        evaluation_value = 5000
    if card_info["pokemon"] == "Venusaur - Green (Grass)" and card_info["psa"] == "6- Excellent- Near Mint":
        evaluation_value = 4000
    if card_info["pokemon"] == "Venusaur - Green (Grass)" and card_info["psa"] == "5- Excellent":
        evaluation_value = 3000
    if card_info["pokemon"] == "Venusaur - Green (Grass)" and card_info["psa"] == "4- Very Good - Excellent":
        evaluation_value = 2000
    if card_info["pokemon"] == "Venusaur - Green (Grass)" and card_info["psa"] == "3 - Very Good":
        evaluation_value = 1000
    if card_info["pokemon"] == "Venusaur - Green (Grass)" and card_info["psa"] == "2- good":
        evaluation_value = 300
    if card_info["pokemon"] == "Venusaur - Green (Grass)" and card_info["psa"] == "1- Poor":
        evaluation_value = 10
    # returning the string value of the allocated evaluation_value    
    return Response(str(evaluation_value),mimetype='text/plain')
