#Ejercico 6
from typing import Self


class Persona:
  def __init__(self, nombre='', edad=0, DNI=''):
     self.nombre=nombre
     self.edad=edad
     self.DNI=DNI

     @property
     def nombre(self):
        return self.__nombre
     @nombre.setter
     def nombre(self, nombre1):
        if type(nombre1)==str:
           self.nombre=nombre1
        else: 
           print('Nombre incorrecto, ingrese solo letras dentro de su nombre')

     @property
     def edad(self):
        return self.__edad
     @edad.setter
     def nombre(self, edad1):
        if edad1>0:
           self.edad=edad1
        else: 
           print('Edad incorrecta, ingrese un numero correcto')
     

     @property
     def DNI(self):
        return self.__DNI
     @DNI.setter
     def nombre(self, DNI1):
        if DNI1>0 :
           self.DNI=DNI1
        else: 
           print('DNI incorrecto, verifique que el numero ingresado sea correcto')

  def mostrar(self):
    print("Nombre:", self.nombre, "Edad:", self.edad, "DNI:",self.DNI)

  def Es_mayor_de_edad(self):
    if self.edad>=18:
      print("Es mayor de edad")
    else:
       print("No es mayor de edad")




p = Persona('Pepe', 15, '12345678')
print(p.mostrar())
print(p.Es_mayor_de_edad())






  
      
  
