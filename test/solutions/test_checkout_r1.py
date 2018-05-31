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

    def test_checkout_5(self):
        result = checkout(12)
        self.assertEqual(result, -1)

    def test_checkout_6(self):
        result = checkout('S')
        self.assertEqual(result, -1)

    def test_checkout_7(self):
        result = checkout('aAAAbCBB')
        self.assertEqual(result, -1)

    def test_checkout_8(self):
        result = checkout('')
        self.assertEqual(result, 0)

    def test_checkout_9(self):
        result = checkout('A')
        self.assertEqual(result, 50)

    def test_checkout_10(self):
        result = checkout(u'A')
        self.assertEqual(result, 50)

    def test_checkout_11(self):
        result = checkout('EEEBB')
        self.assertEqual(result, 150)

    def test_checkout_12(self):
        result = checkout('FF')
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
