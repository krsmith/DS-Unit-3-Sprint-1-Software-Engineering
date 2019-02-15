import numpy as np
from acme import Product

adjective = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products():
    """should generate a given number of products (default
  30), randomly, and return them as a list"""
    products = [Product(
                name=f'{np.random.choice(adjective)} {np.random.choice(noun)}',
                price=np.random.randint(5, 101),
                weight=np.random.randint(5, 101),
                flammability=np.random.uniform(0, 2.5))
                for _ in range(30)]
    return products


def inventory_report(products):
    """takes a list of products, and prints a "nice" summary"""
    report_name = 'ACME CORPORATION OFFICIAL INVENTORY REPORT'
    npr = f'Unique product names: {len(set([prod.name for prod in products]))}'
    avg_price = sum([prod.price for prod in products]) / 30
    avg_weight = sum([prod.weight for prod in products]) / 30
    avg_flam = sum([prod.flammability for prod in products]) / 30

    return report_name, npr, f'Average price: {avg_price}', f'Average weight: {avg_weight}', f'Average flammability: {avg_flam}'
    # Not sure how to get return statement to split in two lines


if __name__ == '__main__':
    print(inventory_report(generate_products()))
