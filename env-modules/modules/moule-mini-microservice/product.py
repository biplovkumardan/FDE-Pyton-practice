def show_products():
    products = {
        "Laptop": 50000,
        "Mobile": 20000,
        "Headphones": 2000,
    }

    print("\nAvailable products:")
    for name, price in products.items():
        print(f"{name}: Rs. {price}")

    return products