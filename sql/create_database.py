import pandas as pd
import sqlite3

df = pd.read_csv("data/raw/supply_chain_data.csv")

conn = sqlite3.connect("supply_chain.db")

df.to_sql(
    "supply_chain_data",
    conn,
    if_exists="replace",
    index=False
)

print("Database created successfully")