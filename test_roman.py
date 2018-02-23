
## importar la clase de test
import unittest

## declaracion del test
class TestRoman(unittest.TestCase):

	## definir primer test
	def test_roman_decimal_roman(self):
   		resultado = None ## code
        self.assertEqual(resultado, 'valor')

if __name__ == "__main__":
    unittest.main()
