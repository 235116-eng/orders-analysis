import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

customers = [
    (1, "Ali", "Islamabad"),
    (2, "Sara", "Lahore"),
    (3, "Bilal", "Karachi"),
    (4, "Ayesha", "Islamabad"),
    (5, "Hamza", "Lahore"),
    (6, "Noor", "Peshawar")
]

orders = [
    (1, 1, 4500),
    (2, 1, 7200),
    (3, 2, 3000),
    (4, 2, 5800),
    (5, 3, 4000),
    (6, 3, 3500),
    (7, 4, 6500),
    (8, 5, 5800),
    (9, 6, 2500),
    (10, 4, 7000)
]

cursor.executemany(
    "INSERT OR IGNORE INTO customers VALUES (?, ?, ?)",
    customers
)

cursor.executemany(
    "INSERT OR IGNORE INTO orders VALUES (?, ?, ?)",
    orders
)

conn.commit()
conn.close()

print("Database created successfully.")