### ENONCE
# Write a function that takes an integer flight_length (in minutes) 
# and a list of integers movie_lengths (in minutes) and returns a boolean 
# indicating whether there are two numbers in movie_lengths whose sum equals flight_length.

### CODE
def brute_force_inflight_entertainment(movie_lengths, flight_length):

    for i in range(len(movie_lengths)):
        for j in range(i+1, len(movie_lengths)):
            if (movie_lengths[i] + movie_lengths[j] == flight_length):
                return True
    return False


def can_two_movies_fill_flight(movie_lengths, flight_length):
    duration_left = set()
    for i in range(len(movie_lengths)):
        if (movie_lengths[i] in duration_left):
            return True
        duration_left.add(flight_length - movie_lengths[i])
    return False

### TESTS
import unittest

class Test(unittest.TestCase):

    def test_short_flight(self):
        result = can_two_movies_fill_flight([2, 4], 1)
        self.assertFalse(result)

    def test_long_flight(self):
        result = can_two_movies_fill_flight([2, 4], 6)
        self.assertTrue(result)

    def test_one_movie_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8], 6)
        self.assertFalse(result)

    def test_two_movies_half_flight_length(self):
        result = can_two_movies_fill_flight([3, 8, 3], 6)
        self.assertTrue(result)

    def test_lots_of_possible_pairs(self):
        result = can_two_movies_fill_flight([1, 2, 3, 4, 5, 6], 7)
        self.assertTrue(result)

    def test_not_using_first_movie(self):
        result = can_two_movies_fill_flight([4, 3, 2], 5)
        self.assertTrue(result)

    def test_multiple_movies_shorter_than_flight(self):
        result = can_two_movies_fill_flight([5, 6, 7, 8], 9)
        self.assertFalse(result)

    def test_only_one_movie(self):
        result = can_two_movies_fill_flight([6], 6)
        self.assertFalse(result)

    def test_no_movies(self):
        result = can_two_movies_fill_flight([], 2)
        self.assertFalse(result)


unittest.main(verbosity=2)