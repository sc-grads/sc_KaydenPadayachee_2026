import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "Messy_Sales_Data.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

os.makedirs(OUTPUT_DIR, exist_ok=True)

CLEAN_FILE = os.path.join(OUTPUT_DIR, "clean_sales.csv")

logging.info(f"Loading data from: {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

df = df.drop_duplicates()

df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0)
df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0)
df["product"] = df["product"].fillna("None").str.strip().str.title()
df["category"] = df["category"].fillna("None").str.strip().str.title()
df["region"] = df["region"].fillna("None").str.strip().str.title()
df["salesperson"] = df["salesperson"].fillna("None").str.strip().str.title()


df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])


df["revenue"] = df["quantity"] * df["price"]
df["month"] = df["date"].dt.to_period("M").astype(str)


df.to_csv(CLEAN_FILE, index=False)
logging.info("Clean file saved")


sales_by_region = df.groupby("region")["revenue"].sum().reset_index()
sales_by_region.to_csv(os.path.join(OUTPUT_DIR, "sales_by_region.csv"), index=False)

sales_by_product = df.groupby("product")["revenue"].sum().reset_index()
sales_by_product.to_csv(os.path.join(OUTPUT_DIR, "sales_by_product.csv"), index=False)

monthly_revenue = df.groupby("month")["revenue"].sum().reset_index()
monthly_revenue.to_csv(os.path.join(OUTPUT_DIR, "monthly_revenue.csv"), index=False)

salesperson_performance = df.groupby("salesperson")["revenue"].sum().reset_index()
salesperson_performance.to_csv(
    os.path.join(OUTPUT_DIR, "salesperson_performance.csv"), index=False
)

logging.info("All aggregated datasets created successfully.")

print("DONE")