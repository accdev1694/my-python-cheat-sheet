# Print the name and price of each product.
# Calculate the total value of each product (price * quantity).
# Print the total value of each product.

store_products = {
    'product1': {
        'name': 'Laptop',
        'price': 1200,
        'quantity': 5
    },
    'product2': {
        'name': 'Smartphone',
        'price': 800,
        'quantity': 10
    },
    'product3': {
        'name': 'Tablet',
        'price': 400,
        'quantity': 8
    }
}

for name, details in store_products.items():
    print(f"{details['name']}: {details['price']}")
    print(f"Total Value = {details['price'] * details['quantity']}")
    print()





