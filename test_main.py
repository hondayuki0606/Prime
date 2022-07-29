import unittest

from main import is_prime


class PrimeTest(unittest.TestCase):

    def test_is_prime_ok(self):
        for i in [2, 3, 5, 7, 11, 13]:
            self.assertTrue(is_prime(i))

    def test_is_prime_ng(self):
        for i in [4, 6, 8, 9, 10, 12]:
            self.assertFalse(is_prime(i))

    def test_is_prime_negative(self):
        for i in [-2, -3, -5, -7, -11, -13]:
            self.assertTrue(is_prime(i))

    def test_is_raise_typeerror(self):
        with self.assertRaises(TypeError):
            is_prime('string')
