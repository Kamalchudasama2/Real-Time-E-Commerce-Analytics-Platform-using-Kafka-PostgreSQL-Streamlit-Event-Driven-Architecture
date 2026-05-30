from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

# Kafka Producer

producer = KafkaProducer(
bootstrap_servers='localhost:9092',
value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

products = {
"Laptop": "Electronics",
"Phone": "Electronics",
"Keyboard": "Accessories",
"Mouse": "Accessories",
"Monitor": "Electronics"
}

cities = [
"Bangalore",
"Mumbai",
"Delhi",
"Hyderabad",
"Chennai"
]

while True:


    product = random.choice(list(products.keys()))

    order = {
        "order_id": random.randint(1000, 9999),
        "customer_id": random.randint(10000, 99999),
        "product": product,
        "category": products[product],
        "price": random.randint(500, 5000),
        "quantity": random.randint(1, 5),
        "city": random.choice(cities),
        "order_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.send("ecommerce_orders", value=order)
    producer.flush()

    print(f"Sent Order: {order}")

    time.sleep(2)

