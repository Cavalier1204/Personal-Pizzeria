from flask import Flask, render_template, redirect, request

app = Flask(__name__)

order = []
totalPrice = 0

listOfPizzas = [
    { # Margherita
        "id" : 0,
        "name" : "Margherita",
        "ingredients" : "Tomato sauce, mozzarella",
        "price" : 4.0,
        "image" : "pizza.png"
    },
    { # Pepperoni
        "id" : 1,
        "name" : "Pepperoni",
        "ingredients" : "Tomato sauce, mozzarella, pepperoni",
        "price" : 5.0,
        "image" : "pizza.png"
    },
    { # BBQ Chicken
        "id" : 2,
        "name" : "BBQ Chicken",
        "ingredients" : "Tomato sauce, mozzarella, chicken, BBQ sauce",
        "price" : 6.5,
        "image" : "pizza.png"
    },
    { # Shoarma
        "id" : 3,
        "name" : "Shoarma",
        "ingredients" : "Tomato sauce, mozzarella, chicken shoarma, garlic sauce",
        "price" : 6.5,
        "image" : "pizza.png"
    },
    { # Prosciutto
        "id" : 4,
        "name" : "Prosciutto",
        "ingredients" : "Tomato sauce, parmesan cheese, prosciutto crudo, arugula",
        "price" : 5.5,
        "image" : "pizza.png"
    },
    { # Calzone
        "id" : 5,
        "name" : "Calzone",
        "ingredients" : "Tomato sauce, mozzarella, salami, folded in",
        "price" : 6.5,
        "image" : "pizza.png"
    },
    { # Contadina
        "id" : 6,
        "name" : "Contadina",
        "ingredients" : "Tomato sauce, mozzarella, cherry tomatoes, arugula",
        "price" : 5.5,
        "image" : "pizza.png"
    },
    { # Nutella
        "id" : 7,
        "name" : "Nutella",
        "ingredients" : "Nutella, powdered sugar",
        "price" : 4.0,
        "image" : "pizza.png"
    },
    { # Vegan
        "id" : 8,
        "name" : "Vegan",
        "ingredients" : "Tomato sauce, vegan mozzarella, cherry tomatoes",
        "price" : 4.5,
        "image" : "pizza.png"
    }
]

def removeItem(delItemId):
    global order
    deleteIndex = order.index(delItemId)
    order.pop(deleteIndex)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/cart", methods=["GET"])
def cart():
    return render_template("cart.html")

@app.route("/cartcontent", methods=["GET", "POST", "DELETE"])
def cartcontent():
    global order, totalPrice
    if request.method == "POST":
        orderId = int(request.form["order"])   
        order.append(orderId)
        totalPrice += float(listOfPizzas[orderId]["price"])

    elif request.method == "DELETE":
        orderId = int(request.form["order"])
        removeItem(orderId)
        totalPrice -= float(listOfPizzas[orderId]["price"])

    return render_template("cart_content.html", order = order, listOfPizzas = listOfPizzas, totalPrice = totalPrice)

@app.route("/pizzas", methods=["GET", "POST"])
def pizzas():
    return render_template("pizzas.html", listOfPizzas = listOfPizzas)

@app.route("/drinks", methods=["GET"])
def drinks():
    return render_template("drinks.html")

@app.route("/desserts", methods=["GET"])
def desserts():
    return render_template("desserts.html")