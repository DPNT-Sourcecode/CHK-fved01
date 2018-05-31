import unittest

from lib.solutions.checkout import checkout


class TestSum(unittest.TestCase):
    def test_checkout_1(self):
        result = checkout('ABC')
        self.assertEqual(result, 100)

    def test_checkout_2(self):
        result = checkout('ABCB')
        self.assertEqual(result, 115)

    def test_checkout_3(self):
        result = checkout('ABCBB')
        self.assertEqual(result, 145)

    def test_checkout_4(self):
        result = checkout('AAAABCBB')
        self.assertEqual(result, 275)



if __name__ == '__main__':
    unittest.main()
