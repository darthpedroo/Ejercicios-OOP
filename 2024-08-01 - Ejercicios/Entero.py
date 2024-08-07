class Entero:

    def __init__(self, number: int):
        self.__number = number

    def to_string(self):
        return str(self.number)
    
    def sumar(self, otro_entero: 'Entero'):
        res = self.number + otro_entero.number
        return Entero(res)

    def restar(self,otro_entero: 'Entero'):
        res = self.number - otro_entero.number
        return Entero(res) 
    
    def multiplicar(self, otro_entero: 'Entero'):
        res = self.number * otro_entero.number
        return Entero(res)

    def dividir(self, otro_entero: 'Entero'):
        
        res = self.number // otro_entero.number
        return Entero(res)

    def mayor(self, otro_entero):
        return self.number > otro_entero.number
        
    def mayor_o_igual(self, otro_entero):
        return self.number >= otro_entero.number

    def menor(self, otro_entero):
        return self.number < otro_entero.number

    def menor_o_igual(self, otro_entero):
        return self.number <= otro_entero.number





    def is_negative(self):
        return self.number < 0

    def is_positive(self):
        return self.number > 0
    
    def is_zero(self):
        return self.number == 0
        

    

     
    
    

    @property
    def number(self):
        return self.__number
    
    @number.setter
    def number(self, new_number):
        self.__number = new_number