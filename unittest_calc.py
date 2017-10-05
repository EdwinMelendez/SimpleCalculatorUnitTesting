import unittest
import Calculator


C = Calculator.calc()


class TestCalc(unittest.TestCase):

    def setUp(self):
        pass

    def test_multiply_3_5_and_13_7(self):
        self.assertEqual(C.mult(3, 5), C.mult(13, 7))

    def test_division_12_4_and_4_5(self):
        self.assertEqual(C.div(12, 4), C.div(4, 5))

    def test_subtraction_12_4_and_4_5(self):
        self.assertEqual(C.sub(12, 4), C.sub(4, 5))

    def test_addition_12_4_and_4_5(self):
        self.assertEqual(C.add(12, 4), C.add(4, 5))

    def test_square_12_and_4(self):
        self.assertEqual(C.square(12), C.square(4))


if __name__ == '__main__':
    unittest.main()
