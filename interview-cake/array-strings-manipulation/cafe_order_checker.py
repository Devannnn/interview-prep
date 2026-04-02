### ENONCE
# Given all three lists, write a function to check that my service is first-come, first-served. 
# All food should come out in the same order customers requested it.

### CODE

def is_first_come_first_served(take_out, dine_in, served):

    length_take_out = len(take_out)
    length_dine_in = len(dine_in)
    take_out_indice = 0
    dine_in_indice = 0

    for i in range(len(served)):
        if (take_out_indice < length_take_out) and (served[i] == take_out[take_out_indice]):
            take_out_indice+=1
        elif (dine_in_indice < length_dine_in) and (served[i] == dine_in[dine_in_indice]):
            dine_in_indice+=1
        else:
            return False
    return True

### TESTS
import unittest

class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)

    def test_order_numbers_are_not_sequential(self):
        result = is_first_come_first_served([27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
        self.assertTrue(result)

unittest.main(verbosity=2)