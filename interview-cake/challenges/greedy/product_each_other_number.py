### ENONCE
# You have a list of integers, and for each index you want to find the product of 
# every integer except the integer at that index. 
# Write a function get_products_of_all_ints_except_at_index() that takes a list of 
# integers and returns a list of the products. Here's the catch: You can't use division 
# in your solution!

### CODE
import unittest

def brute_force_get_products_of_all_ints_except_at_index(int_list):
    taille = len(int_list)
    if taille < 2:
        raise Exception
    products = []
    for i in range(taille):
        product = 1
        for j in range(taille):
            if i!=j:
                product = product*int_list[j]
        products.append(product)

    return products


def get_products_of_all_ints_except_at_index(int_list):
    taille = len(int_list)
    if taille < 2:
        raise Exception
    
    products = [1 for i in range(taille)]

    product = 1
    for i in range(0, taille):
        products[i] = product
        product = product*int_list[i]
    
    product = 1
    for j in range(taille-1, -1, -1):
        products[j] = products[j] * product
        product = product*int_list[j]

    return products

### TESTS

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)