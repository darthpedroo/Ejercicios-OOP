from Entero import Entero
import math

class FraccionInvalidaError(Exception):
    def __init__(self, message):
        pass

class Fraccion:
    

    

    def __init__(self, numerador: Entero, denominador: Entero ):
        self.__numerador = numerador
        self.__denominador = denominador
   
    def to_string(self):
        return f"{self.numerador.number}/{self.denominador.number}"


    def check_if_fraction_is_valid(self):
        if self.denominador.number == 0:
            raise FraccionInvalidaError("MENUDA CASTAÑA, TU FRACCION NO ES VALIDA")

    def simplify(self):
        greatest_common_divisor = math.gcd(self.numerador.number, self.denominador.number)
        new_numerador = Entero(self.numerador.number//greatest_common_divisor)
        new_denominador = Entero(self.denominador.number//greatest_common_divisor)
        return Fraccion(new_numerador, new_denominador)

    def check_if_two_fractions_are_equivalent(self,other_fraction):
        
        first_fraction = self.simplify()
        other_fraction = other_fraction.simplify()

        
        if (first_fraction.numerador.number == other_fraction.numerador.number) and (first_fraction.denominador.number == other_fraction.denominador.number):
            return True
        else:
            return False



    def sumar(self,other_fraction : 'Fraccion') ->'Fraccion':
        new_numerador = Entero(self.numerador.number * other_fraction.denominador.number + self.denominador.number * other_fraction.numerador.number)
        new_denominador = Entero(self.denominador.number * other_fraction.denominador.number)

        return Fraccion(new_numerador, new_denominador).simplify()
    
    def restar(self,other_fraction : 'Fraccion') ->'Fraccion':
        new_numerador = Entero(self.numerador.number * other_fraction.denominador.number - self.denominador.number * other_fraction.numerador.number)
        new_denominador = Entero(self.denominador.number * other_fraction.denominador.number)

        return Fraccion(new_numerador, new_denominador).simplify()

    def multiplicar(self,other_fraction : 'Fraccion') ->'Fraccion':
        new_numerador = Entero(self.numerador.number * other_fraction.numerador.number)
        new_denominador = Entero(self.denominador.number * other_fraction.denominador.number)

        return Fraccion(new_numerador, new_denominador).simplify()
        
    def dividir(self,other_fraction : 'Fraccion') ->'Fraccion':
        new_numerador = Entero(self.numerador.number * other_fraction.denominador.number)
        new_denominador = Entero(self.denominador.number * other_fraction.numerador.number)
        

        return Fraccion(new_numerador, new_denominador).simplify()
    

    @property
    def numerador(self):
        return self.__numerador
    
    @property
    def denominador(self):
        return self.__denominador
