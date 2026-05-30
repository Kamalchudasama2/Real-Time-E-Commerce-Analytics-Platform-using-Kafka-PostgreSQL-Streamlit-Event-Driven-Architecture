from kafka import KafkaConsumer
import psycopg2
import json
import logging

# ======================================
# LOGGING CONFIGURATION
# ======================================

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.getLogger("kafka").setLevel(logging.WARNING)
# ======================================
# KAFKA CONSUMER
# ======================================

consumer = KafkaConsumer(
    "ecommerce_orders",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

# ======================================
# POSTGRES CONNECTION
# ======================================

conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    port="5433",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

print("Listening for Kafka events...")
logging.info("Kafka Consumer Started")

# ======================================
# DATA VALIDATION FUNCTION
# ======================================

VALID_CITIES = [
    "Bangalore",
    "Mumbai",
    "Delhi",
    "Chennai",
    "Hyderabad"
]

def validate_order(order):

    required_fields = [
        "order_id",
        "customer_id",
        "product",
        "price",
        "quantity",
        "city"
    ]

    # Check missing fields

    for field in required_fields:

        if field not in order:

            logging.error(
                f"Validation Failed - Missing Field: {field}"
            )

            return False

    # Price validation

    if order["price"] <= 0:

        logging.error(
            f"Invalid Price: {order['price']}"
        )

        return False

    # Quantity validation

    if order["quantity"] <= 0:

        logging.error(
            f"Invalid Quantity: {order['quantity']}"
        )

        return False

    # City validation

    if order["city"] not in VALID_CITIES:

        logging.error(
            f"Invalid City: {order['city']}"
        )

        return False

    return True

# ======================================
# MAIN CONSUMER LOOP
# ======================================

for message in consumer:

    order = message.value

    try:

        # -------------------------
        # VALIDATION LAYER
        # -------------------------

        if not validate_order(order):

            print(
                f"Rejected Order: {order.get('order_id')}"
            )

            continue

        revenue = (
            order["price"] *
            order["quantity"]
        )

        insert_query = """
        INSERT INTO orders (
            order_id,
            customer_id,
            customer_name,
            product,
            category,
            price,
            quantity,
            city,
            order_timestamp,
            revenue
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(
            insert_query,
            (
                order["order_id"],
                order["customer_id"],
                order.get(
                    "customer_name",
                    "Unknown"
                ),
                order["product"],
                order["category"],
                order["price"],
                order["quantity"],
                order["city"],
                order["order_timestamp"],
                revenue
            )
        )

        conn.commit()

        print(
            f"Inserted Order: {order['order_id']}"
        )

        logging.info(
            f"Inserted Order: {order['order_id']}"
        )

    except Exception as e:

        logging.error(
            f"Database Insert Failed: {str(e)}"
        )

        print(
            f"Error Processing Order: {e}"
        )