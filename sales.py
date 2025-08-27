import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('sales.csv')
print("Sales Report 2025\n\n")
print(f"{data}")

print("\n\n")
print(data.head()) # to print some data or rows of data
print("\n\n")
print(data.info()) # 
print("\n\n")
print(data.describe())

print("\n\n")

best_selling = data.groupby("Product")["Quantity"].sum()
print(best_selling[::-1])


print("Best selling products are : \n\n")
print(best_selling)


top_product = best_selling.idxmax()
top_quantity = best_selling.max()

print(f"Top Sold Product : {top_product}\nQuantity : {top_quantity}")

# chart

best_selling.plot(kind="bar")

plt.title("Best Selling Products !\n")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.show()