import pandas as pd

df = pd.read_csv("./Pandas_Project/Shop Sales Summary/Sales Records.csv")

total_revenue = df["Total Revenue"].sum()

print(f"Total Revenue : {total_revenue}")

largest_sale = df["Total Cost"].max()
smallest_sale = df["Total Cost"].min()

print(f"Largest Sale : {largest_sale}")
print(f"Smallest Sale : {smallest_sale}")
print(df.head())