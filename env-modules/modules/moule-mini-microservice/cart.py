def add_to_cart(products, product_name, quantity):
    if product_name not in products:
        raise ValueError(f"Product not found: {product_name}")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    item = {
        "product": product_name,
        "price": products[product_name],
        "quantity": quantity,
    }

    print(f"Added to cart: {product_name} x {quantity}")
    return item