from flask import Flask, render_template, redirect, request

app = Flask(__name__)

order = []

listOfPizzas = [
    { # Margherita
        "id" : 1,
        "name" : "Margherita",
        "ingredients" : "Tomato sauce, mozzarella",
        "price" : 4.0,
        "image" : "pizza.png"
    },
    { # Pepperoni
        "id" : 2,
        "name" : "Pepperoni",
        "ingredients" : "Tomato sauce, mozzarella, pepperoni",
        "price" : 5.0,
        "image" : "pizza.png"
    },
    { # BBQ Chicken
        "id" : 3,
        "name" : "BBQ Chicken",
        "ingredients" : "Tomato sauce, mozzarella, chicken, BBQ sauce",
        "price" : 6.5,
        "image" : "pizza.png"
    },
    { # Shoarma
        "id" : 4,
        "name" : "Shoarma",
        "ingredients" : "Tomato sauce, mozzarella, chicken shoarma, garlic sauce",
        "price" : 6.5,
        "image" : "pizza.png"
    },
    { # Prosciutto
        "id" : 5,
        "name" : "Prosciutto",
        "ingredients" : "Tomato sauce, parmesan cheese, prosciutto crudo, arugula",
        "price" : 5.5,
        "image" : "pizza.png"
    },
    { # Calzone
        "id" : 6,
        "name" : "Calzone",
        "ingredients" : "Tomato sauce, mozzarella, salami, folded in",
        "price" : 6.5,
        "image" : "pizza.png"
    },
    { # Contadina
        "id" : 7,
        "name" : "Contadina",
        "ingredients" : "Tomato sauce, mozzarella, cherry tomatoes, arugula",
        "price" : 5.5,
        "image" : "pizza.png"
    },
    { # Nutella
        "id" : 8,
        "name" : "Nutella",
        "ingredients" : "Nutella, powdered sugar",
        "price" : 4.0,
        "image" : "pizza.png"
    },
    { # Vegan
        "id" : 9,
        "name" : "Vegan",
        "ingredients" : "Tomato sauce, vegan mozzarella, cherry tomatoes",
        "price" : 4.5,
        "image" : "pizza.png"
    }
]

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/cart", methods=["GET"])
def cart():
    return render_template("cart.html")

@app.route("/cartcontent", methods=["GET", "POST"])
def cartcontent():
    if request.method == "POST":
        order.append(request.form["order"])
    return render_template("cart_content.html", order = order)

@app.route("/pizzas", methods=["GET", "POST"])
def pizzas():
    return render_template("pizzas.html", listOfPizzas = listOfPizzas)

@app.route("/drinks", methods=["GET"])
def drinks():
    return render_template("drinks.html")

@app.route("/desserts", methods=["GET"])
def desserts():
    return render_template("desserts.html")