import pandas as pd
import os
from datetime import datetime

# the places that each thing is stored in
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "Messy_Sales_Data.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

# creates the folder
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

# puts it in the file path
CLEAN_FILE = os.path.join(OUTPUT_DIR, "clean_sales.csv")
LOG_CSV = os.path.join(REPORTS_DIR, "process_log.csv")

# storing logs
logs = []

# logging function
def log(step, status, details=""):
    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "step": step,
        "status": status,
        "details": details
    }
    logs.append(entry)
    print(f"{entry['timestamp']} | {step} | {status} | {details}")

# start
log("start", "success", f"Loading data from {DATA_PATH}")

# load data
try:
    df = pd.read_csv(DATA_PATH)
    log("load data", "success", f"{len(df)} rows loaded")
except Exception as e:
    log("load data", "error", str(e))
    raise

# remove duplicates
initial_rows = len(df)
df = df.drop_duplicates()
log("removing duplicates", "success", f"{initial_rows - len(df)} removed")

# clean text columns
df["product"] = df["product"].fillna("None").str.strip().str.title()
df["category"] = df["category"].fillna("None").str.strip().str.title()
df["region"] = df["region"].fillna("None").str.strip().str.title()
df["salesperson"] = df["salesperson"].fillna("None").str.strip().str.title()



# convert to numeric (keep NaN)
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

# fill missing using rounded product-wise average
df["quantity"] = df.groupby("product")["quantity"].transform(
    lambda x: x.fillna(round(x.mean()))
)

# fallback for any remaining missing values
remaining_missing = df["quantity"].isna().sum()

if remaining_missing > 0:
    df["quantity"] = df["quantity"].fillna(0)
    log("quantity cleaning", "warning", f"{remaining_missing} values filled with fallback 0")
else:
    log("quantity cleaning", "success", "All missing quantities filled using rounded product averages")

# ensure integers
df["quantity"] = df["quantity"].astype(int)



# clean price
df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0)

log("cleaned data", "success")

# clean dates
df["date"] = pd.to_datetime(df["date"], errors="coerce")
before = len(df)
df = df.dropna(subset=["date"])
log("date cleaning", "success", f"{before - len(df)} invalid dates removed")

# feature engineering
df["revenue"] = df["quantity"] * df["price"]
df["month"] = df["date"].dt.to_period("M").astype(str)

log("features", "success")

# save clean data
df.to_csv(CLEAN_FILE, index=False)
log("clean file saved", "success", CLEAN_FILE)

# aggregations
df.groupby("region")["revenue"].sum().reset_index().to_csv(
    os.path.join(OUTPUT_DIR, "sales_by_region.csv"), index=False
)

df.groupby("product")["revenue"].sum().reset_index().to_csv(
    os.path.join(OUTPUT_DIR, "sales_by_product.csv"), index=False
)

df.groupby("month")["revenue"].sum().reset_index().to_csv(
    os.path.join(OUTPUT_DIR, "monthly_revenue.csv"), index=False
)

df.groupby("salesperson")["revenue"].sum().reset_index().to_csv(
    os.path.join(OUTPUT_DIR, "salesperson_performance.csv"), index=False
)

log("aggregation phase", "success", "All reports created")

# save logs
log_df = pd.DataFrame(logs)
log_df.to_csv(LOG_CSV, index=False)

print("DONE - Logs saved to CSV")