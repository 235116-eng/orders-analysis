import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

print("Customer orders (joined):")

cursor.execute("""
SELECT customers.name, orders.amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
""")

for row in cursor.fetchall():
    print(row)

print("\nTotal spend per customer:")

cursor.execute("""
SELECT customers.name, SUM(orders.amount) AS total_spend
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, customers.name
ORDER BY total_spend DESC
""")

for row in cursor.fetchall():
    print(row)

print("\nCities with avg order > 5000:")

cursor.execute("""
SELECT customers.city, AVG(orders.amount) AS average_order
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customers.city
HAVING AVG(orders.amount) > 5000
""")

for row in cursor.fetchall():
    print(row)

conn.close()