# dropping the databse initially and then create it 
from application import db
db.drop_all()
db.create_all()