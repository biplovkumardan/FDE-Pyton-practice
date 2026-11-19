from customer import register_customer
from product import show_products
from cart import add_to_cart
from price_calculator import calculate_total
from payment import make_payment




def main():
    print("=== MINI E-COMMERCE APPLICATION ===")

    customer = register_customer("Biplov")
    products = show_products()

    cart = []
    cart.append(add_to_cart(products, "Laptop", 1))
    cart.append(add_to_cart(products, "Headphones", 2))

    total = calculate_total(cart)
    make_payment(customer, total)
main()
