#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, adjective, noun


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

#   `Product` class: at least 1 that tests default values (as shown), and one that
#   builds an object with different values and ensures their `stealability()` and
#   `explode()` methods function as they should


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products:
        """checks that it really does receive a list of length 30"""

    def test_legal_names:
        """checks that the generated names for a default batch of
    products are all valid possible names to generate
    (adjective,space, noun, from the lists of possible words)"""

# *Hint* - `test_legal_names` is the trickiest of these, but may not be as bad as
# you think. Check out `assertIn` from `unittest`, and remember that Python is
# pretty handy at string processing. But if you get stuck, move on and revisit.


if __name__ == '__main__':
    unittest.main()
