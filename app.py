from flask import Flask, render_template, redirect, request

app = Flask(__name__)

order = {} # Pizza ID : Amount
totalPrice = 0

menuItems = [

    # Pizzas
    
    { # Margherita
        "id" : 0,
        "type" : 1,
        "name" : "Margherita",
        "ingredients" : "Tomato sauce, mozzarella",
        "price" : 4.0,
        "image" : "pizza.png"
    },
    { # Pepperoni
        "id" : 1,
        "type" : 1,
        "name" : "Pepperoni",
        "ingredients" : "Tomato sauce, mozzarella, pepperoni",
        "price" : 5.0,
        "image" : "pizza.png"
    },
    { # BBQ Chicken
        "id" : 2,
        "type" : 1,
        "name" : "BBQ Chicken",
        "ingredients" : "Tomato sauce, mozzarella, chicken, corn, BBQ sauce",
        "price" : 6.5,
        "image" : "pizza.png"
    },
    { # Shoarma
        "id" : 3,
        "type" : 1,
        "name" : "Shoarma",
        "ingredients" : "Tomato sauce, mozzarella, onion, chicken shoarma, garlic sauce",
        "price" : 6.5,
        "image" : "pizza.png"
    },
    { # Prosciutto
        "id" : 4,
        "type" : 1,
        "name" : "Prosciutto",
        "ingredients" : "Tomato sauce, parmesan cheese, prosciutto crudo, arugula, olive oil",
        "price" : 5.5,
        "image" : "pizza.png"
    },
    { # Calzone
        "id" : 5,
        "type" : 1,
        "name" : "Calzone",
        "ingredients" : "Tomato sauce, mozzarella, cherry tomatoes, onion, salami",
        "price" : 6.5,
        "image" : "pizza.png"
    },
    { # Contadina
        "id" : 6,
        "type" : 1,
        "name" : "Contadina",
        "ingredients" : "Tomato sauce, mozzarella, cherry tomatoes, arugula",
        "price" : 5.5,
        "image" : "pizza.png"
    },
    { # Nutella
        "id" : 7,
        "type" : 1,
        "name" : "Nutella",
        "ingredients" : "Nutella, powdered sugar, strawberries",
        "price" : 4.0,
        "image" : "pizza.png"
    },
    { # Vegan
        "id" : 8,
        "type" : 1,
        "name" : "Vegan",
        "ingredients" : "Tomato sauce, vegan mozzarella, cherry tomatoes, onion, bell peppers, olives, mushrooms",
        "price" : 6.0,
        "image" : "pizza.png"
    },
    
    # Drinks
    
    { # Water
        "id" : 9,
        "type" : 2,
        "name" : "Water",
        "price" : 1.5,
        "image" : "cola.png"
    },
    { # Cola
        "id" : 10,
        "type" : 2,
        "name" : "Coca-Cola",
        "price" : 3.0,
        "image" : "cola.png"
    },
    { # Fanta
        "id" : 11,
        "type" : 2,
        "name" : "Fanta Orange",
        "price" : 3.0,
        "image" : "cola.png"
    },
    { # Cassis
        "id" : 12,
        "type" : 2,
        "name" : "Fanta Cassis",
        "price" : 3.0,
        "image" : "cola.png"
    },
    { # Sprite
        "id" : 13,
        "type" : 2,
        "name" : "Sprite",
        "price" : 3.0,
        "image" : "cola.png"
    },
    { # Apple juice
        "id" : 14,
        "type" : 2,
        "name" : "Apple juice",
        "price" : 2.0,
        "image" : "cola.png"
    },
    { # Chocolate milkshake
        "id" : 15,
        "type" : 2,
        "name" : "Chocolate milkshake",
        "price" : 3.0,
        "image" : "cola.png"
    },
    { # Strawberry milkshake
        "id" : 16,
        "type" : 2,
        "name" : "Strawberry milkshake",
        "price" : 3.0,
        "image" : "cola.png"
    },
    { # Banana milkshake
        "id" : 17,
        "type" : 2,
        "name" : "Banana milkshake",
        "price" : 3.0,
        "image" : "cola.png"
    },
    
    # Desserts
    
    { # Ice cream
        "id" : 18,
        "type" : 3,
        "name" : "Ice cream",
        "price" : 3.0,
        "image" : "cookie.png"
    }
]

listOfPizzas = []
listOfDrinks = []
listOfDesserts = []

for item in menuItems:
    match item["type"]:
        case 1:
            listOfPizzas.append(item)
        case 2:
            listOfDrinks.append(item)
        case 3:
            listOfDesserts.append(item)

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
        orderId = int(request.form["add"])
        if orderId in order.keys():
            order[orderId] += 1
        else:
            order[orderId] = 1
        totalPrice += float(menuItems[orderId]["price"])

    elif request.method == "DELETE":
        orderId = int(request.form["subtract"])
        if (order[orderId] - 1) < 1:
            del order[orderId]
        else:
            order[orderId] -= 1
        totalPrice -= float(menuItems[orderId]["price"])

    return render_template("cart_content.html", order = order, menuItems = menuItems, totalPrice = totalPrice)

@app.route("/deletecartitem", methods=["DELETE"])
def deleteCartItem():
    global totalPrice
    orderId = int(request.form["delete"])
    totalPrice -= float(menuItems[orderId]["price"] * order[orderId])
    del order[orderId]
    return render_template("cart_content.html", order = order, menuItems = menuItems, totalPrice = totalPrice)

@app.route("/pizzas", methods=["GET", "POST"])
def pizzas():
    return render_template("pizzas.html", listOfPizzas = listOfPizzas, menuItems = menuItems)

@app.route("/drinks", methods=["GET", "POST"])
def drinks():
    return render_template("drinks.html", listOfDrinks = listOfDrinks, menuItems = menuItems)

@app.route("/desserts", methods=["GET", "POST"])
def desserts():
    return render_template("desserts.html", listOfDesserts = listOfDesserts, menuItems = menuItems)