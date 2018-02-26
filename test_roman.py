
## importar la clase de test
import unittest
from Roman import roman
from roman_to_decimal import decimal

## declaracion del test
class TestRoman(unittest.TestCase):

    def test_roman_decimal_roman_one(self):
        resultado = roman(1)
        self.assertEqual(resultado, 'I')

    def test_roman_decimal_roman_two(self):
        resultado = roman(2)
        self.assertEqual(resultado, 'II')

    def test_roman_decimal_roman_four(self):
        resultado = roman(4)
        self.assertEqual(resultado, 'IV')
    def test_roman_decimal_roman_ten(self):
        resultado = roman(10)
        self.assertEqual(resultado, 'X')


    def test_roman_decimal_roman_845(self):
        resultado = roman(845)
        self.assertEqual(resultado, 'DCCCXLV') 

    def test_roman_decimal_roman_minor(self):
        resultado = roman(-1)
        self.assertEqual(resultado, "Can't convert to roman number!")

    def test_roman_decimal_roman_not_type(self):
        resultado = roman(10.5)
        self.assertEqual(resultado, "Only int numbers")   

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
        self.assertEqual(decimal('CCXASDASHDUASBD'), 'Input is not a roman number')

    def test_roman_decimal_3999(self):
        resultado = roman(3999)
        self.assertEqual(resultado, 'MMMCMXCIX')

    def test_roman_decimal_4000(self):
        resultado = roman(4000)
        self.assertEqual(resultado, 'Not a valid number')   

    ## definir primer test
    


if __name__ == "__main__":
    unittest.main()
