# ----------imporitng modules-----------------
from unittest.mock import patch 
from flask import url_for
from flask_testing import TestCase

from application import app

class TestBase(TestCase):
    def create_app(self):
        return app 

# ---------Test Class-------------
class TestResponse(TestBase):
    def test_get_evaluation(self):
        # ----------------Testing pikachu values--------------------------------
        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Pikachu - Yellow (Lightning)","psa": "10- Gem Mint - Pristine"})
        self.assertEqual(b"5000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Pikachu - Yellow (Lightning)","psa": "9 - Mint"})
        self.assertEqual(b"3000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Pikachu - Yellow (Lightning)","psa": "8- Near Mint-Mint"})
        self.assertEqual(b"2000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Pikachu - Yellow (Lightning)","psa": "7- Near Mint"})
        self.assertEqual(b"1000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Pikachu - Yellow (Lightning)","psa": "6- Excellent- Near Mint"})
        self.assertEqual(b"750", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Pikachu - Yellow (Lightning)","psa": "5- Excellent"})
        self.assertEqual(b"500", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Pikachu - Yellow (Lightning)","psa": "4- Very Good - Excellent"})
        self.assertEqual(b"300", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Pikachu - Yellow (Lightning)","psa": "3 - Very Good"})
        self.assertEqual(b"200", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Pikachu - Yellow (Lightning)","psa": "2- good"})
        self.assertEqual(b"50", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Pikachu - Yellow (Lightning)","psa": "1- Poor"})
        self.assertEqual(b"20", response.data)



# -------------------------------Testing charizard Values-----------------------------


        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Charizard - Red (Fire)","psa": "10- Gem Mint - Pristine"})
        self.assertEqual(b"35000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Charizard - Red (Fire)","psa": "9 - Mint"})
        self.assertEqual(b"20000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Charizard - Red (Fire)","psa": "8- Near Mint-Mint"})
        self.assertEqual(b"10000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Charizard - Red (Fire)","psa": "7- Near Mint"})
        self.assertEqual(b"5000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Charizard - Red (Fire)","psa": "6- Excellent- Near Mint"})
        self.assertEqual(b"3000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Charizard - Red (Fire)","psa": "5- Excellent"})
        self.assertEqual(b"1000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Charizard - Red (Fire)","psa": "4- Very Good - Excellent"})
        self.assertEqual(b"500", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Charizard - Red (Fire)","psa": "3 - Very Good"})
        self.assertEqual(b"250", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Charizard - Red (Fire)","psa": "2- good"})
        self.assertEqual(b"150", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Charizard - Red (Fire)","psa": "1- Poor"})
        self.assertEqual(b"50", response.data)



# ----------------------------------Testing Mudkip --------------------------------

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Mudkip - Blue (Water)","psa": "10- Gem Mint - Pristine"})
        self.assertEqual(b"500", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Mudkip - Blue (Water)","psa": "9 - Mint"})
        self.assertEqual(b"350", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Mudkip - Blue (Water)","psa": "8- Near Mint-Mint"})
        self.assertEqual(b"300", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Mudkip - Blue (Water)","psa": "7- Near Mint"})
        self.assertEqual(b"200", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Mudkip - Blue (Water)","psa": "6- Excellent- Near Mint"})
        self.assertEqual(b"100", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Mudkip - Blue (Water)","psa": "5- Excellent"})
        self.assertEqual(b"50", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Mudkip - Blue (Water)","psa": "4- Very Good - Excellent"})
        self.assertEqual(b"20", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Mudkip - Blue (Water)","psa": "3 - Very Good"})
        self.assertEqual(b"10", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Mudkip - Blue (Water)","psa": "2- good"})
        self.assertEqual(b"5", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Mudkip - Blue (Water)","psa": "1- Poor"})
        self.assertEqual(b"2", response.data)




# --------------------------------Testing Venusaur-------------------------

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Venusaur - Green (Grass)","psa": "10- Gem Mint - Pristine"})
        self.assertEqual(b"20000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Venusaur - Green (Grass)","psa": "9 - Mint"})
        self.assertEqual(b"10000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Venusaur - Green (Grass)","psa": "8- Near Mint-Mint"})
        self.assertEqual(b"6000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Venusaur - Green (Grass)","psa": "7- Near Mint"})
        self.assertEqual(b"5000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Venusaur - Green (Grass)","psa": "6- Excellent- Near Mint"})
        self.assertEqual(b"4000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Venusaur - Green (Grass)","psa": "5- Excellent"})
        self.assertEqual(b"3000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Venusaur - Green (Grass)","psa": "4- Very Good - Excellent"})
        self.assertEqual(b"2000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Venusaur - Green (Grass)","psa": "3 - Very Good"})
        self.assertEqual(b"1000", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Venusaur - Green (Grass)","psa": "2- good"})
        self.assertEqual(b"300", response.data)

        response = self.client.post(url_for('get_evaluation'), json={"pokemon":"Venusaur - Green (Grass)","psa": "1- Poor"})
        self.assertEqual(b"10", response.data)