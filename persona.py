class persona:


    def __init__(self,name,last,dni,age):
        self.name=name
        self.last=last
        self.dni=dni
        self.age=age

    def __puntuar_dni(self):
        dni = '{0:,}'.format(self.dni)
        dni = dni.replace(",",".")
        return dni
    

    def __str__ (self):

        return f"Datos persona: {self.last} {self.name}  DNI: {self.__puntuar_dni()} EDAD: {self.age}"




