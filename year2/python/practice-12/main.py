import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("sales.csv")
df = df.drop_duplicates()
df["customer"] = df["customer"].fillna("Невідомий клієнт")
df["quantity"] = df["quantity"].fillna(df["quantity"].median())
df = df[(df["price"] > 0) & (df["quantity"] > 0)]
df["sales"] = df["price"] * df["quantity"]
df["sales"] = df["sales"].fillna(df["sales"].median())

print("Початковий датасет:")
df.info()
print("\nІнформаційна статистика:")
print(df.describe())

summary = df.groupby("customer")["sales"].agg(total_sales="sum", average_order_value="mean", order_count="count").reset_index()

print("\n", summary)

plt.figure(figsize=(10, 6))
sns.set_style(style="whitegrid")
sns.barplot(data=summary, x="customer", y="total_sales", color="cyan")
plt.xlabel("Customer")
plt.ylabel("Total Sales")
plt.title("Total Sales by Customer")

plt.savefig("total_sales_by_customer.png", dpi=300)
plt.show()
plt.close()