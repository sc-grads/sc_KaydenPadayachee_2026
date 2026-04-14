import pandas as pd
import os
import logging


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "Messy_Sales_Data.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")

os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(OUTPUT_DIR, "clean_sales.csv")

logging.info(f"Loading data from: {DATA_PATH}")


df = pd.read_csv(DATA_PATH)


df = df.drop_duplicates()

for col in ["quantity", "price"]:
    df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

for col in ["product", "category", "region", "salesperson"]:
    df[col] = df[col].fillna("None").astype(str).str.strip().str.title()


df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])


df["revenue"] = df["quantity"] * df["price"]
df["month"] = df["date"].dt.to_period("M").astype(str)


df.to_csv(OUTPUT_FILE, index=False)

logging.info(f"Clean file saved to: {OUTPUT_FILE}")
print("DONE")