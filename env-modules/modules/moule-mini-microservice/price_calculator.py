def calculate_total(cart):
    return sum(
        item["price"] * item["quantity"]
        for item in cart
    )