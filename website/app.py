from flask import Flask, render_template, request
from kafka import KafkaProducer

import json
import random
from datetime import datetime

app = Flask(__name__)

# =======================================
# KAFKA PRODUCER
# =======================================

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# =======================================
# HOME PAGE
# =======================================

@app.route("/")
def home():
    return render_template("home.html")

# =======================================
# ORDER PAGE
# =======================================

@app.route("/order/<product>/<price>")
def order_page(product, price):

    return render_template(
        "order.html",
        product=product,
        price=price
    )

# =======================================
# SUBMIT ORDER
# =======================================

@app.route("/submit-order", methods=["POST"])
def submit_order():

    product = request.form["product"]
    price = int(request.form["price"])

    order = {

        "order_id": random.randint(1000, 9999),

        "customer_id": random.randint(10000, 99999),

        "customer_name": request.form["customer_name"],

        "product": product,

        "category": "Electronics",

        "price": price,

        "quantity": int(request.form["quantity"]),

        "city": request.form["city"],

        "order_timestamp":
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.send(
        "ecommerce_orders",
        value=order
    )

    producer.flush()

    print("Order Sent To Kafka")
    print(order)

    return render_template(
        "success.html",
        order=order
    )

# =======================================
# MAIN
# =======================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )