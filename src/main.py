from flask import Flask
app = Flask(__name__)

@app.route("/")
def home_page():
    return "This is my homepage! Pretty cool."





# def add(a,b):
#     return (a+b)
    

