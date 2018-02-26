## importar la clase de test
import unittest
from Roman import roman
from roman_to_decimal import decimal
from romandecimalroman import  roman_to_roman

class TestRomanToInt(unittest.TestCase):


    def test_romandecimal_one(self):
        self.assertEqual(decimal('I'), 1)

    def test_romandecimal_two(self):
        self.assertEqual(decimal('II'), 2)

    def test_romandecimal_three(self):
        self.assertEqual(decimal('III'), 3)

    def test_romandecimal_four(self):
        self.assertEqual(decimal('IV'), 4)

    def test_romandecimal_nine(self):
        self.assertEqual(decimal('IX'), 9)

    def test_romandecimal_845(self):
        self.assertEqual(decimal('DCCCXLV'), 845)

    def test_romandecimal_3999(self):
        self.assertEqual(decimal('MMMCMXCIX'), 3999)

    def test_wrong_letter(self):
        with self.assertRaises(Exception) as e:
            decimal('CCXASDASHDUASBD'),
        self.assertEqual(
            e.exception.message,
            'Input is not a roman number'
        )

    ## definir primer test

class Roman_to_decimal_to_roman(unittest.TestCase):
    def test_all(self):
        for number in xrange(1, 4):
            roman_result = roman(number)
            result = decimal(roman_result)
            self.assertEqual(number, result)


if __name__ == '__main__':
    unittest.main()