### ENONCE
# Given a list of integers, find the highest product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.

### CODE
import unittest

def brute_force_highest_product_of_3(list_of_ints):
    max_product = list_of_ints[0]*list_of_ints[1]*list_of_ints[2]
    for indice1 in range(len(list_of_ints)):
        for indice2 in range(indice1+1, len(list_of_ints)):
            for indice3 in range(indice2+1, len(list_of_ints)):
                tmp_product = list_of_ints[indice1]*list_of_ints[indice2]*list_of_ints[indice3]
                if tmp_product > max_product:
                    max_product = tmp_product
    return max_product

def get_indice_minimum(list_of_ints):
    min = list_of_ints[0]
    indice = 0
    for i in range(len(list_of_ints)):
        if list_of_ints[i] < min:
            min = list_of_ints[i]
            indice = i
    return indice

def get_indice_minimum_abs(list_of_ints):
    min = abs(list_of_ints[0])
    indice = 0
    for i in range(len(list_of_ints)):
        if abs(list_of_ints[i]) < min:
            min = abs(list_of_ints[i])
            indice = i
    return indice

def product_3(list_of_ints, candidate, indice_min):
    return list_of_ints[(indice_min+1)%3]*list_of_ints[(indice_min+2)%3]*candidate


def highest_product_of_3(list_of_ints):

    highest_product = list_of_ints[0]*list_of_ints[1]*list_of_ints[2]

    values_product = [list_of_ints[0],list_of_ints[1],list_of_ints[2]]
    max_product = highest_product
    values_abs_product = [list_of_ints[0],list_of_ints[1],list_of_ints[2]]
    max_abs_product = highest_product

    for indice in range(3, len(list_of_ints)):
        candidate = list_of_ints[indice]

        indice_minimum = get_indice_minimum(values_product)
        tmp_product = product_3(values_product, candidate, indice_minimum)
        if tmp_product > max_product:
            values_product[indice_minimum] = candidate
            max_product = tmp_product

        indice_minimum_abs = get_indice_minimum_abs(values_abs_product)
        tmp_abs_product = product_3(values_abs_product, candidate, indice_minimum_abs)
        if abs(tmp_abs_product) > abs(max_abs_product):
            values_abs_product[indice_minimum_abs] = candidate
            max_abs_product = tmp_abs_product

        highest_product = max(max_product, max_abs_product, highest_product)
    
    return highest_product


### TESTS
class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)

### COMPLEXITY
# O(n) time
# O(1) space