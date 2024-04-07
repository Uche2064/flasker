from flask import Flask, render_template

# creer une instance de flask
app = Flask(__name__)

'''
FILTERS
safe
capitalize
lower
upper
title
trim
striptags
'''

# creer un decorateur
@app.route("/")
# def index():
#     return "<h1>Hello, world!</h1>"
def index():
    first_name = "John"
    stuff = "This is bold text"
    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template(
        "index.html", 
        first_name=first_name, 
        stuff=stuff,
        favorite_pizza=favorite_pizza
        )

@app.route("/user/<name>")
def user(name: str):
    return render_template("user.html", user_name=name)
    
# creer page d'erreur

# url invalide
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

# error interne
@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"), 500