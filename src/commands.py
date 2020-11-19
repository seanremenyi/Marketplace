from main import db
from flask import Blueprint
import random

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created!")

@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    print("Tables deleted")
    
@db_commands.cli.command("seed")
def seed_db():
    from models.Items import Item
    from faker import Faker
    faker = Faker()
    
    for i in range(20):
        item = Item()
        item.name=faker.catch_phrase()
        item.cost = random.randint(10, 1000)
        db.session.add(item)
        
    db.session.commit()
    print("Tables seeded")
        