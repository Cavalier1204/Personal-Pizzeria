from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/cart", methods=["GET"])
def cart():
    return render_template("cart.html")

@app.route("/pizzas", methods=['GET', 'POST'])
def pizzas():
    if request.method == 'POST':
        print(request.method)
        print(request.query_string)
        return redirect("/cart")
    return render_template("pizzas.html")

@app.route("/drinks", methods=["GET"])
def drinks():
    return render_template("drinks.html")

@app.route("/desserts", methods=["GET"])
def desserts():
    return render_template("desserts.html")