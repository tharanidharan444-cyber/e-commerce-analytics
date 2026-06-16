import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="ecommerce"
)

cursor = conn.cursor()

print("\n===== E-COMMERCE ANALYTICS DASHBOARD =====\n")

# Total Customers
cursor.execute("SELECT COUNT(*) FROM customers")
customers = cursor.fetchone()[0]
print("Total Customers :", customers)

# Total Products
cursor.execute("SELECT COUNT(*) FROM products")
products = cursor.fetchone()[0]
print("Total Products  :", products)

# Total Orders
cursor.execute("SELECT COUNT(*) FROM orders")
orders = cursor.fetchone()[0]
print("Total Orders    :", orders)

print("\nTOP SELLING PRODUCTS\n")

query = """
SELECT p.product_name,
SUM(oi.quantity) AS total_sales
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sales DESC
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row[0], "-", row[1], "units")

print("\nCUSTOMER PURCHASE REPORT\n")

query = """
SELECT c.customer_name,
COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.customer_name
"""

cursor.execute(query)

for row in cursor.fetchall():
    print(row[0], "-", row[1], "orders")

conn.close()
