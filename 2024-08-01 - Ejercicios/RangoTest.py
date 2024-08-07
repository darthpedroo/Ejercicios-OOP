from Fraccion import Fraccion, FraccionInvalidaError
from Entero import Entero
from Rango import Rango
import unittest
import math

class TestMain(unittest.TestCase):

    def test_to_string(self):
        num1 = 1
        num2 = 5
        limiteInf = Entero(num1)
        limiteSup = Entero(num2)

        

        rango = Rango(limiteInf,limiteSup, True, True)

        self.assertEqual('[1,5]', rango.to_string())

    def test_contains_certain_number(self):
        num1 = 1
        num2 = 5
        
        yNum = 3
        yEntero = Entero(yNum)
        xNum = 100
        xEntero = Entero(xNum)

        limiteInf = Entero(num1)
        limiteSup = Entero(num2)

        rango = Rango(limiteInf,limiteSup, True, True)

        self.assertTrue(rango.contains_certain_number(yEntero))
        self.assertFalse(rango.contains_certain_number(xEntero))

    def test_calcular_tamaño(self):
        num1 = 1
        num2 = 5
        tamaño = 3
        

        limiteInf = Entero(num1)
        limiteSup = Entero(num2)

        rango = Rango(limiteInf,limiteSup, True, True)
        #rango.calcular_tamaño()

        self.assertEqual(tamaño, rango.calcular_tamaño())

    def test_check_if_included_in_other_range(self):
        num1 = 1
        num2 = 8
        num3 = 3
        num4 = 4
        limiteInf = Entero(num1)
        limiteSup = Entero(num2)
        limiteInf2 = Entero(num3)
        limiteSup2 = Entero(num4)

        rango = Rango(limiteInf,limiteSup, True, True)
        rango2 = Rango(limiteInf2,limiteSup2, True, True)

        self.assertTrue(rango.check_if_included_in_other_range(rango2))

    def test_check_if_intersects_with_other_range(self):
        num1 = 5
        num2 = 10
        num3 = 6
        num4 = 9
        limiteInf = Entero(num1)
        limiteSup = Entero(num2)
        limiteInf2 = Entero(num3)
        limiteSup2 = Entero(num4)

        rango = Rango(limiteInf,limiteSup, True, True)
        rango2 = Rango(limiteInf2,limiteSup2, True, True)

        self.assertTrue(rango.check_if_intersects_with_other_range(rango2))


if __name__ == "__main__":
    unittest.main()