
def analyze_products(valid_data):

    product_quantity = {}
    product_revenue = {}
    category_revenue = {}

    for row in valid_data:

        product = row["ProductName"]
        category = row["Category"]

        quantity = int(row["Quantity"])
        revenue = quantity * float(row["UnitPrice"])

        # Calculate product-wise quantity
        product_quantity[product] = (
            product_quantity.get(product, 0) + quantity
        )

        # Calculate product-wise revenue
        product_revenue[product] = (
            product_revenue.get(product, 0) + revenue
        )

        # Calculate category-wise revenue
        category_revenue[category] = (
            category_revenue.get(category, 0) + revenue
        )

    # Find top-selling and highest-revenue products
    top_selling_product = max(
        product_quantity, key=product_quantity.get
    ) if product_quantity else None

    highest_revenue_product = max(
        product_revenue, key=product_revenue.get
    ) if product_revenue else None

    return {
        "Product Quantity": product_quantity,
        "Product Revenue": product_revenue,
        "Category Revenue": category_revenue,
        "Top Selling Product": top_selling_product,
        "Highest Revenue Product": highest_revenue_product
    }
