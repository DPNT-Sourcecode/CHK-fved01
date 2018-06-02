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
        self.assertEqual(result, 20)

    def test_checkout_13(self):
        result = checkout('FFF')
        self.assertEqual(result, 20)

    def test_checkout_14(self):
        result = checkout('FFFFFF')
        self.assertEqual(result, 40)

    def test_checkout_15(self):
        result = checkout('FFFF')
        self.assertEqual(result, 30)

    def test_checkout_16(self):
        result = checkout('F')
        self.assertEqual(result, 10)

    def test_checkout_17(self):
        result = checkout('S')
        self.assertEqual(result, 20)

    def test_checkout_18(self):
        result = checkout('Z')
        self.assertEqual(result, 21)

    def test_checkout_19(self):
        result = checkout('SSS')
        self.assertEqual(result, 45)

    def test_checkout_20(self):
        result = checkout('SSSS')
        self.assertEqual(result, 65)

    # def test_checkout_21(self):
    #     result = checkout('STXS')
    #     self.assertEqual(result, 65)
    #
    # def test_checkout_22(self):
    #     result = checkout('STXZ')
    #     self.assertEqual(result, 66)

    def test_checkout_23(self):
        result = checkout('SSSZ')
        self.assertEqual(result, 65)

    def test_checkout_24(self):
        result = checkout('STXS')
        self.assertEqual(result, 62)

    def test_checkout_25(self):
        result = checkout('STXZ')
        self.assertEqual(result, 62)


if __name__ == '__main__':
    unittest.main()
