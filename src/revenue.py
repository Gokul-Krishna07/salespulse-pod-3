
def calculate_revenue_metrics(valid_data):

    total_revenue = sum(
        row["Quantity"] * row["UnitPrice"]
        for row in valid_data
    )

    total_valid_orders = len(valid_data)

    average_order_value = (
        total_revenue / total_valid_orders
        if total_valid_orders > 0 else 0
    )

    total_quantity_sold = sum(
        row["Quantity"] for row in valid_data
    )

    estimated_gross_profit = sum(
        row["Quantity"] * (row["UnitPrice"] - row["UnitCost"])
        for row in valid_data
    )

    return {
        "Total Revenue": total_revenue,
        "Total Valid Orders": total_valid_orders,
        "Average Order Value": average_order_value,
        "Total Quantity Sold": total_quantity_sold,
        "Estimated Gross Profit": estimated_gross_profit
    }
