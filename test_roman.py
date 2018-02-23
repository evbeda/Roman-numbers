
## importar la clase de test
import unittest
from Roman import roman

## declaracion del test
class TestRoman(unittest.TestCase):

    def test_roman_decimal_roman_one(self):
        resultado = roman(1)
        self.assertEqual(resultado, 'I')

    def test_roman_decimal_roman_ten(self):
        resultado = roman(10)
        self.assertEqual(resultado, 'X')


    def test_roman_decimal_roman_845(self):
        resultado = roman(845)
        self.assertEqual(resultado, 'DCCCXLV') 

    def test_roman_decimal_roman_minor(self):
        resultado = roman(-1)
        self.assertEqual(resultado, None)   

    ## definir primer test
    


if __name__ == "__main__":
    unittest.main()
