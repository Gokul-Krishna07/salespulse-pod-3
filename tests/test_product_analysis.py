
import csv
from src.product_analysis import analyze_products

sales_data = []

# Read sales data
with open("data/sales.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        sales_data.append(row)

# Filter valid records for testing
valid_data = [
    row for row in sales_data
    if row["ProductName"].strip()
    and row["Category"].strip()
    and int(row["Quantity"]) > 0
    and float(row["UnitPrice"]) >= 0
]


# Perform product analysis
result = analyze_products(valid_data)

print("\nSALES PULSE - PRODUCT ANALYSIS")
print("--------------------------------")

print("\nProduct-wise Quantity Sold:")
for product, quantity in result["Product Quantity"].items():
    print(f"{product}: {quantity}")

print("\nProduct-wise Revenue:")
for product, revenue in result["Product Revenue"].items():
    print(f"{product}: ₹{revenue:,.2f}")

print("\nCategory-wise Revenue:")
for category, revenue in result["Category Revenue"].items():
    print(f"{category}: ₹{revenue:,.2f}")

print("\nTop Selling Product:", result["Top Selling Product"])
print("Highest Revenue Product:", result["Highest Revenue Product"])
