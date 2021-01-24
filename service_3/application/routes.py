from application import app
from flask import request, Response
import random 

@app.route("/psa", methods=["GET"])
def get_psa ():
    psa  = ["10- Gem Mint - Pristine", "9 - Mint",  "8- Near Mint-Mint",
     "7- Near Mint", "6- Excellent- Near Mint", "5- Excellent","4- Very Good - Excellent","3 - Very Good",
     "2- good", "1- Poor", "0- Destroyed"]
    return Response(str(random.choice(psa)), mimetype='text/plain')
