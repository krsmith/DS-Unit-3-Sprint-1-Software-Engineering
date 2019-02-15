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

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Test default product flammability being .5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, .5)

    def test_stealability(self):
        """Test stealability output"""
        prod = Product('Test', price=100, weight=20)
        self.assertEqual(prod.stealability(), "Very stealable!")

    def test_explode(self):
        """Test explode output"""
        prod = Product('Test', flammability=.1, weight=4)
        self.assertEqual(prod.explode(), "...fizzle.")


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        """checks that it really does receive a list of length 30"""
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """checks that the generated names for a default batch of
        products are all valid possible names to generate
        (adjective,space, noun, from the lists of possible words)"""
        products = generate_products()
        names = [prod.name for prod in products]
        for x in names:
            self.assertEqual(len(x.split(' ')), 2)

        for x in names:
            split = x.split(' ')
            adj = split[0]
            nn = split[1]
            self.assertIn(adj, adjective)
            self.assertIn(nn, noun)

# *Hint* - `test_legal_names` is the trickiest of these, but may not be as bad as
# you think. Check out `assertIn` from `unittest`, and remember that Python is
# pretty handy at string processing. But if you get stuck, move on and revisit.


if __name__ == '__main__':
    unittest.main()
