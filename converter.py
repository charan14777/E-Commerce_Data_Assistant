import pandas as pd
import sqlite3

conn = sqlite3.connect('backend/db/ecommerce.db')

data_files = {
    "ad_sales": "backend/data/ad_sales.csv",
    "total_sales": "backend/data/total_sales.csv",
    "eligibility": "backend/data/eligibility.csv"
}

for table, path in data_files.items():
    df = pd.read_csv(path)
    df.to_sql(table, conn, if_exists='replace', index=False)

conn.close()
print("Data successfully loaded into ecommerce.db")
