# Transactional Sales Data Pipeline

## 📌 Project Overview
This project demonstrates an end-to-end **data engineering pipeline** that processes raw transactional sales data and transforms it into structured, analytics-ready data stored in a lightweight data warehouse.

The pipeline follows real-world data engineering practices including data ingestion, transformation, storage, and analytical querying.

---

## 🏗️ Architecture
**Raw CSV → Python ETL → SQLite Data Warehouse → SQL Analytics**

---

## 🛠️ Tech Stack
- **Python** – Data extraction, transformation, and loading (ETL)
- **Pandas** – Data manipulation and transformation
- **SQLite** – Lightweight data warehouse
- **SQL** – Analytical queries
- **Git & GitHub** – Version control

---

## 📂 Project Structure
transactional-sales-data-pipeline/
│
├── data/
│ ├── raw/ # Raw transactional sales data (1000+ records)
│ └── processed/ # Cleaned and transformed data
│
├── scr/
│ ├── extract.py # Extract raw CSV data
│ ├── transform.py # Data cleaning and feature engineering
│ └── laod.py # Load data into SQLite warehouse
│
├── sql/
│ └── analytics.sql # Analytical SQL queries
│
├── config/ # Configuration files
├── logs/ # Pipeline logs
│
├── README.md
└── gitignore

yaml
Copy code

---

## 🔄 Data Pipeline Flow

### 1️⃣ Extract
- Reads raw CSV sales data
- Validates schema and structure

### 2️⃣ Transform
- Calculates order value
- Extracts order month
- Standardizes data types
- Prepares fact-level data

### 3️⃣ Load
- Loads transformed data into SQLite data warehouse
- Stores data in a **fact_sales** table

---

## 📊 Analytics Use Cases
- Daily total revenue
- Daily order volume
- Aggregated sales performance over time

Example query:
```sql
SELECT order_date, COUNT(order_id), SUM(order_value)
FROM fact_sales
GROUP BY order_date;
🎯 Key Learnings
Building a real ETL pipeline

Data modeling for analytics

Handling large raw datasets

Writing production-style Python scripts

SQL aggregation on warehouse tables

Git-based project workflow

🚀 Future Improvements
Add incremental loading

Implement logging & monitoring

Move to cloud data warehouse (BigQuery / Redshift)

Orchestrate pipeline with Airflow

👤 Author
Huzaifa Farooq
Aspiring Data Engineer
📍 Pakistan

GitHub: https://github.com/huzaifafarooq0009-pixel

LinkedIn: https://www.linkedin.com/in/huzaifa-farooq-2b366033a