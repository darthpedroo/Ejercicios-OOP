from Entero import Entero
import unittest

class TestMain(unittest.TestCase):


    def test_entero_to_string(self):
        num = 1

        entero = Entero(num)
        entero_to_string = entero.to_string()
        self.assertEqual(str(num), entero_to_string)

    def test_sumar_enteros(self):
        num1 = 1
        num2 = 2        
        entero1 = Entero(num1)
        entero2 = Entero(num2)

        res = entero1.sumar(entero2)
        self.assertEqual(num1+num2, res.number)
    
    def test_restar_enteros(self):
        num1 = 1
        num2 = 2        
        entero1 = Entero(num1)
        entero2 = Entero(num2)

        res = entero1.restar(entero2)
        self.assertEqual(num1-num2, res.number)
    
    def test_multiplicar_enteros(self):
              
        entero1 = Entero(10)
        entero2 = Entero(20)

        res = entero1.multiplicar(entero2)
        self.assertEqual(10*20, res.number)

    def test_dividir_enteros(self):
        num1 = 10
        num2 = 20

        entero1 = Entero(num1)
        entero2= Entero(num2)
        res = entero1.dividir(entero2)
        self.assertEqual(num1//num2, res.number)
    
    def test_dividir_por_0(self):
        num1 = 10
        num2 = 0

        entero1 = Entero(num1)
        entero2= Entero(num2)
        
        with self.assertRaises(ZeroDivisionError):
            res = entero1.dividir(entero2)
        
    def test_number_is_negative(self):
        num = -10

        entero = Entero(num)
        self.assertTrue(entero.is_negative())
        self.assertFalse(entero.is_positive())
        self.assertFalse(entero.is_zero())

    def test_number_is_positive(self):
        num = 10

        entero = Entero(num)
        self.assertFalse(entero.is_negative())
        self.assertTrue(entero.is_positive())
        self.assertFalse(entero.is_zero())

    def test_number_is_zero(self):
        num = 0

        entero = Entero(num)
        self.assertFalse(entero.is_negative())
        self.assertFalse(entero.is_positive())
        self.assertTrue(entero.is_zero())    

    def test_entero_mayor(self):
        num1 = 60
        num2 = 10 

        entero1 = Entero(num1)
        entero2 = Entero(num2)

        self.assertTrue(entero1.mayor(entero2))
        self.assertFalse(entero2.mayor(entero1))

    def test_entero_mayor_o_igual(self):
        num1 = 60
        num2 = 60
        num3 = 50 

        entero1 = Entero(num1)
        entero2 = Entero(num2)
        entero3 = Entero(num3)

        self.assertTrue(entero1.mayor_o_igual(entero2))
        self.assertTrue(entero1.mayor_o_igual(entero3))
        self.assertFalse(entero3.mayor_o_igual(entero1))
        
    def test_entero_menor(self):
        num1 = 60
        num2 = 10 

        entero1 = Entero(num1)
        entero2 = Entero(num2)

        self.assertFalse(entero1.menor(entero2))
        self.assertTrue(entero2.menor(entero1))

    def test_entero_mayor_o_igual(self):
        num1 = 60
        num2 = 60
        num3 = 500 

        entero1 = Entero(num1)
        entero2 = Entero(num2)
        entero3 = Entero(num3)

        self.assertTrue(entero1.menor_o_igual(entero2))
        self.assertTrue(entero1.menor_o_igual(entero3))
        self.assertFalse(entero3.menor_o_igual(entero1))



        




if __name__ == "__main__":
    unittest.main()
