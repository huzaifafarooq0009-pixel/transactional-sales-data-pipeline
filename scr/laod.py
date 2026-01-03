import sqlite3
import pandas as pd

# Connect to database (creates file if not exists)
conn = sqlite3.connect("data/warehouse.db")
cursor = conn.cursor()

# Create fact_sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_sales (
    order_id INTEGER,
    order_date TEXT,
    customer_id INTEGER,
    product TEXT,
    quantity INTEGER,
    price INTEGER,
    order_value INTEGER,
    order_month INTEGER
)
""")
conn.commit()

# Load CSV data into fact_sales table
df = pd.read_csv("data/processed/sales_processed.csv")
df.to_sql("fact_sales", conn, if_exists="replace", index=False)

conn.close()

print("✅ fact_sales table created and data loaded successfully")

