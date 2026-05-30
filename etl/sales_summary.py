import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5433",
    database="ecommerce",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()

print("Generating Analytics Tables...")

# ==========================
# CITY SALES
# ==========================

cursor.execute("TRUNCATE city_sales")

cursor.execute("""
INSERT INTO city_sales
SELECT
    city,
    COUNT(*) AS total_orders,
    SUM(revenue) AS total_revenue,
    CURRENT_TIMESTAMP
FROM orders
GROUP BY city
""")

# ==========================
# PRODUCT SALES
# ==========================

cursor.execute("TRUNCATE product_sales")

cursor.execute("""
INSERT INTO product_sales
SELECT
    product,
    COUNT(*) AS total_orders,
    SUM(revenue) AS total_revenue,
    CURRENT_TIMESTAMP
FROM orders
GROUP BY product
""")

# ==========================
# DAILY SALES
# ==========================

cursor.execute("TRUNCATE daily_sales")

cursor.execute("""
INSERT INTO daily_sales
SELECT
    DATE(order_timestamp),
    COUNT(*) AS total_orders,
    SUM(revenue) AS total_revenue,
    CURRENT_TIMESTAMP
FROM orders
GROUP BY DATE(order_timestamp)
""")

conn.commit()

print("Analytics Tables Updated Successfully!")

cursor.close()
conn.close()