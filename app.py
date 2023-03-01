import csv
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

order = {} # Pizza ID : Amount
totalPrice = 0
menuItems = []

with open("menuitems.csv", 'r') as rdata:
        rows = list(csv.reader(rdata))
        for row in rows:
            item = {}
            item["id"] = int(row[0])
            item["type"] = int(row[1])
            item["name"] = row[2]
            item["ingredients"] = row[3]
            item["price"] = float(row[4])
            item["image"] = row[5]
            print(item)
            menuItems.append(item)

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
    print(order)
    return render_template("cart_content.html", order = order, menuItems = menuItems, totalPrice = totalPrice)

@app.route("/deletecartitem", methods=["DELETE"])
def deletecartitem():
    global totalPrice
    orderId = int(request.form["delete"])
    totalPrice -= float(menuItems[orderId]["price"] * order[orderId])
    del order[orderId]
    return render_template("cart_content.html", order = order, menuItems = menuItems, totalPrice = totalPrice)

@app.route("/emptycart", methods=["DELETE"])
def emptycart():
    global totalPrice, order
    order = {}
    totalPrice = float(0)
    print(order)
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