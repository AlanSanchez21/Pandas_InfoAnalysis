import pandas as pd
import matplotlib.pyplot as plt
    # Reading the CSV file 
df = pd.read_csv("orders.csv")
    #===================================#
df["TotalPrice"] = df["Quantity"] * df["Price"]
    #===================================#
print("=== DATASET OVERVIEW ===")
print(f"Shape: {df.shape}")
print(df.dtypes)
print(df.describe().round(2))
    #===================================#
print("\n=== REVENUE BY CATEGORY ===")
category_revenue = df.groupby("Category")["TotalPrice"].sum().sort_values(ascending=False)
print(category_revenue)
    #===================================#
print("\n=== TOP 5 ORDERS ===")
print(df.sort_values("TotalPrice", ascending=False)[["CustomerName","Product","TotalPrice"]].head())
    #===================================#
print("\n=== SHIPPING STATUS ===")
print(df.groupby("Shipped")["TotalPrice"].agg(["count","sum"]))
    #===================================#
print("\n=== TOP 10 COUNTRIES BY REVENUE ===")
print(df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False).head(10))
    #================== Bar Chart =================#
category_revenue.plot(kind="bar", color=["#4C72B0","#DD8452","#55A868"])
plt.title("Total Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue (USD)")
plt.tight_layout()
plt.show()