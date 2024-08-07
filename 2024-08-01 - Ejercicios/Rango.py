from Entero import Entero


#PARA RESOLVER OPEN-CLOSED CREARIA OTRA CLASE LLAMADA "LIMITE" Y LE PONDRIA UN ATRIBUTO DE SI ES ABIERTO O CERRADO DICHO LIMITE

class Rango:
    def __init__(self,limiteInf: Entero, limiteSup:Entero, is_limiteInf_open: bool, is_limiteSup_open: bool) :
        self.__limiteInf = limiteInf
        self.__limiteSup = limiteSup
        self.is_limiteInf_open = is_limiteInf_open
        self.is_limiteSup_open = is_limiteSup_open


    def to_string(self):
        return f"[{self.limiteInf.number},{self.limiteSup.number}]"
    
    def contains_certain_number(self, entero: Entero):
        if entero.number >= self.limiteInf.number and entero.number <= self.limiteSup.number:
            return True
    
    def calcular_tamaño(self):
        tamaño = 0
        limitinf_modifier = 0
        limitsup_modifier = 0

        if self.is_limiteInf_open:
            limitinf_modifier = 1
        if not(self.is_limiteSup_open):
            limitsup_modifier = 1
            
        # EL IN RANGE ES (CERRADO, ABIERTO). HAY QUE CAMBIAR ESO
        # si sumas +1 cambias el estado de abierto a cerrado

        for i in range(self.limiteInf.number + limitinf_modifier,
                        self.limiteSup.number + limitsup_modifier):
            tamaño +=1

        return tamaño
        
        
    def check_if_included_in_other_range(self, other_rango : 'Rango'):
        # [1,5] // [2,3]
        if self.limiteInf.number < other_rango.limiteInf.number and self.limiteSup.number > other_rango.limiteSup.number : 
                return True
        else: 
            return False

#    Rango A: [5, 10]
#    Rango B: [6, 9]
#    
    def check_if_intersects_with_other_range(self, other_rango: 'Rango'):
        rango = range(self.limiteInf.number, self.limiteSup.number)

        if other_rango.limiteInf.number in rango or other_rango.limiteSup.number in rango:
            return True
        else: 
            return False

    
    

    @property
    def limiteInf(self):
        return self.__limiteInf
        
    @property
    def limiteSup(self):
        return self.__limiteSup
    