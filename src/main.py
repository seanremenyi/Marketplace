from flask import Flask
app = Flask(__name__)
from controllers import registerable_controllers

for controller in registerable_controllers:
    app.register_blueprint(controller)




# def add(a,b):
#     return (a+b)
    

