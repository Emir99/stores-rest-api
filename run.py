from app4 import app4
from db import db

db.init_app(app4)


@app4.before_first_request
def create_table():
    db.create_all()