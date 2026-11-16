import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
df = pd.read_csv(BASE_DIR/"Grocery Category.csv")

Category = df["Category"].unique()
items = df["Category"].value_counts()
proportion = df["Category"].value_counts(normalize=True)
print(Category)
print(proportion)
print(items)
print(df.shape)
print(df.info())

