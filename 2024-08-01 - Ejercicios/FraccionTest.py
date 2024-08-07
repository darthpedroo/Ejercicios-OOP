from Fraccion import Fraccion, FraccionInvalidaError
from Entero import Entero
import unittest
import math

class TestMain(unittest.TestCase):

    def test_fraction_to_value(self):
        numerador = 10
        denominador = 3

        entero1  = Entero(numerador)
        entero2  = Entero(denominador)
        fraccion = Fraccion(entero1,entero2)

        fraccion_to_value = f"{numerador}/{denominador}"

        self.assertEqual(fraccion_to_value,fraccion.to_string())

    def test_check_if_fracion_is_invalid(self):
        numerador = 10
        denominador = 0

        entero1  = Entero(numerador)
        entero2  = Entero(denominador)
        fraccion = Fraccion(entero1,entero2)

        with self.assertRaises(FraccionInvalidaError):
            e = fraccion.check_if_fraction_is_valid()
    
    def test_simplify(self):
        numerador = 10
        denominador = 0

        entero1  = Entero(numerador)
        entero2  = Entero(denominador)
        fraccion = Fraccion(entero1,entero2)

        gcd = math.gcd(numerador,denominador)
        new_numerador = numerador/gcd
        new_denominador = denominador/gcd

        self.assertEqual(new_numerador,fraccion.simplify().numerador.number)
        self.assertEqual(new_denominador,fraccion.simplify().denominador.number)

    def test_check_if_two_fractions_are_equivalent(self):
        numerador1 = 10
        denominador1 = 20
        numerador2 = 5
        denominador2 = 10


        entero1  = Entero(numerador1)
        entero2  = Entero(denominador1)
        fraccion1 = Fraccion(entero1,entero2)
        
        entero3= Entero(numerador2)
        entero4 = Entero(denominador2)

        fraccion2 = Fraccion(entero3,entero4)

        self.assertTrue(fraccion1.check_if_two_fractions_are_equivalent(fraccion2))
        
    def test_sumar(self):
        numerador1 = 10
        denominador1 = 20
        numerador2 = 10
        denominador2 = 30


        entero1  = Entero(numerador1)
        entero2  = Entero(denominador1)
        fraccion1 = Fraccion(entero1,entero2)
        
        entero3= Entero(numerador2)
        entero4 = Entero(denominador2)
        fraccion2 = Fraccion(entero3,entero4)

        self.assertEqual("5/6", fraccion1.sumar(fraccion2).to_string())

    def test_restar(self):
        numerador1 = 4
        denominador1 = 4
        numerador2 = 1
        denominador2 = 2


        entero1  = Entero(numerador1)
        entero2  = Entero(denominador1)
        fraccion1 = Fraccion(entero1,entero2)
        
        entero3= Entero(numerador2)
        entero4 = Entero(denominador2)
        fraccion2 = Fraccion(entero3,entero4)

        self.assertEqual("1/2", fraccion1.restar(fraccion2).to_string())

    def test_multiplicar(self):
        numerador1 = 2
        denominador1 = 2
        numerador2 = 50
        denominador2 = 10


        entero1  = Entero(numerador1)
        entero2  = Entero(denominador1)
        fraccion1 = Fraccion(entero1,entero2)
        
        entero3= Entero(numerador2)
        entero4 = Entero(denominador2)
        fraccion2 = Fraccion(entero3,entero4)

        self.assertEqual("5/1", fraccion1.multiplicar(fraccion2).to_string())

    def test_dividir(self):
        numerador1 = 2
        denominador1 = 3
        numerador2 = 7
        denominador2 = 5


        entero1  = Entero(numerador1)
        entero2  = Entero(denominador1)
        fraccion1 = Fraccion(entero1,entero2)
        
        entero3= Entero(numerador2)
        entero4 = Entero(denominador2)
        fraccion2 = Fraccion(entero3,entero4)

        self.assertEqual("10/21", fraccion1.dividir(fraccion2).to_string())

if __name__ == "__main__":
    unittest.main()
