import numpy as np


def generate_products():
    """should generate a given number of products (default
  30), randomly, and return them as a list"""
    adjective = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
    noun = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
    name = np.random.choice(adjective) + np.random.choice(noun)
    price = np.random.randint(5, 101)
    weight = np.random.randint(5, 101)
    flammability = np.random.uniform(0, 2.5)


def inventory_report():
    """takes a list of products, and prints a "nice" summary"""
    pass


# You should implement only depending on `random` from the standard library, your
# `Product` class from `acme.py`, and built-in Python functionality.

# For the report, you should calculate and print the following values:

# - Number of unique product names in the product list
# - Average (mean) price, weight, and flammability of listed products

# At the bottom of `acme_report.py` you should put the following code:

# ```python
# if __name__ == '__main__':
#     inventory_report(generate_products())
# ```

# This will let you test by running `python acme_report.py`. You should see output
# like:

# ```
# $ python acme_report.py 
# ACME CORPORATION OFFICIAL INVENTORY REPORT
# Unique product names: 19
# Average price: 56.8
# Average weight: 54.166666666666664
# Average flammability: 1.258097155966675
# ```

# It's OK for the specifics to vary (how you message/format), but it should output
# and clearly identify all four relevant numbers.