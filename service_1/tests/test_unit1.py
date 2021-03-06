from unittest.mock import patch 
from flask import url_for
from flask_testing import TestCase
import requests_mock 

from application import app, db
from application.models import Pokemons


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app 
    def setUp(self):
        db.create_all()
        db.session.add(Pokemons(pokemon_name="Pikachu - Yellow (Lightning)",pokemon_psa="10- Gem Mint - Pristine",pokemon_evaluation="5000"))
        db.session.commit()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
# mocking the response from other services to ensure that the hompepage is showing the related information 
class TestResponse(TestBase):
    def test_pika(self):
        with requests_mock.mock() as m:
            m.get('http://pokemon-stack_pokemon-backend:5000/pokemon', text = "Pikachu - Yellow (Lightning)")
            m.get('http://pokemon-stack_pokemon-backend3:5000/psa',text = "10- Gem Mint - Pristine")
            m.post("http://pokemon-stack_pokemon-backend4:5000/evaluation", json="5000")
            response = self.client.get(url_for('index'))
            self.assertIn(b"Pikachu - Yellow (Lightning)", response.data)
            self.assertIn(b"10- Gem Mint - Pristine", response.data)
            self.assertIn(b"5000", response.data)

