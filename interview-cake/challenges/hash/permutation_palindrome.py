### ENONCE
# Write an efficient function that checks whether any permutation of an input string is a palindrome.

### CODE
def list_permutations(s):
    if len(s) == 0:
        return ['']
    elif len(s) == 1:
        return [s]
    else:
        perms = []
        for i in range(len(s)):
            current = s[i]
            rem = s[:i] + s[i+1:]
            for p in list_permutations(rem):
                perms.append(current + p)
        return perms
        

def is_palindrome(input):
    taille = len(input)
    for i in range(taille//2):
        if input[i] != input[taille-1-i]:
            return False
    return True

def has_palindrome_permutation(input):
    permutations = list_permutations(input)
    for X in permutations:
        if is_palindrome(X):
            return True
    return False

### TESTS
import unittest

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)