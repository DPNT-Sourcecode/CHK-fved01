import unittest

from lib.solutions.checkout import checkout


class TestSum(unittest.TestCase):
    def test_checkout_1(self):
        result = checkout('ABC')
        self.assertEqual(result, 100)

    def test_checkout_2(self):
        result = checkout('ABCB')
        self.assertEqual(result, 100)


if __name__ == '__main__':
    unittest.main()
