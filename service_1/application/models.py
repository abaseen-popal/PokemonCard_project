from application import db
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# Model of the database which collects pokemon cards by their name, psa and evaluation
class Pokemons(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    pokemon_name = db.Column(db.String(600),nullable=False)
    pokemon_psa = db.Column(db.String(600), nullable=False)
    pokemon_evaluation = db.Column(db.String(600), nullable=False)


