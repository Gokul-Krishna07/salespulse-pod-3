
import csv
from src.revenue import calculate_revenue_metrics

sales_data = []

with open("data/sales.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        sales_data.append({
            "Quantity": int(row["Quantity"]),
            "UnitPrice": float(row["UnitPrice"]),
            "UnitCost": float(row["UnitCost"])
        })

# Use only valid records
valid_data = [row for row in sales_data if row["Quantity"] > 0]

# Calculate revenue metrics
result = calculate_revenue_metrics(valid_data)

print("\nSALES PULSE - REVENUE ANALYSIS")
print("--------------------------------")

for metric, value in result.items():
    if metric in ["Total Valid Orders", "Total Quantity Sold"]:
        print(f"{metric}: {int(value):,}")
    else:
        print(f"{metric}: ₹{value:,.2f}")
