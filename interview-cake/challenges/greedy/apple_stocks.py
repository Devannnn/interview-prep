### ENONCE
# Write an efficient function that takes stock_prices and returns the best profit 
# I could have made from one purchase and one sale of one share of Apple stock yesterday.

### CODE
def brute_force_get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        return None
    best_profit = stock_prices[1] - stock_prices[0]
    for i in range(len(stock_prices)):
        for j in range(i+1, len(stock_prices)):
            current_profit = stock_prices[j] - stock_prices[i]
            if current_profit > best_profit:
                best_profit = current_profit
    return best_profit

def get_max_profit(stock_prices):
    if len(stock_prices) < 2:
        return None
    min_price_seen = min(stock_prices[0], stock_prices[1])
    best_profit = stock_prices[1] - stock_prices[0]
    for current_time in range(2,len(stock_prices)):
        current_price = stock_prices[current_time]
        potential_profit = current_price - min_price_seen
        best_profit = max(potential_profit, best_profit)
        min_price_seen = min(min_price_seen, current_price)
    return best_profit

### TESTS
import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_big_increase_then_small_increase(self):
        actual = get_max_profit([2, 10, 1, 4])
        expected = 8
        self.assertEqual(actual, expected)                

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)

### COMPLEXITY
# O(n) time
# O(1) space