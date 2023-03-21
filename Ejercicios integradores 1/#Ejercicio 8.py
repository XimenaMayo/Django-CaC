#Ejercicio 8
class CuentaJoven:
  def __init__(self,titular='',cantidad=0,bonificacion=0, edad=0):
    self.titular = titular
    self.cantidad= cantidad
    self.bonificacion=bonificacion

    @property
    def bonificacion(self):
      return self.__bonificacion
    
    @bonificacion.setter
    def bonifcacion(self, bonificacion):
      self.__bonificacion = bonificacion

    @property
    def titular(self):
      return self.__titular
    
    @titular.setter
    def titular(self, titular):
      self.__titular = titular 
      
      @property
      def cantidasd(self):
        return self.__cantidad

    def mostrar(self):
      print("Titular:", self.__titular, "Dinero disponible:", self.__cantidad)
    
    def ingresar(self, cantidad):
      if cantidad>0:
        self.cantidad:self.cantidad+cantidad

def es_titular_valido():
    if edad>=25:
      return True
    else:
      return False

def retirar(self, cantidad):
      if cantidad>0 and es_titular_valido==True:
       self.cantidad= self.cantidad-cantidad
      else:
         print('El titular no es válido para retirar dinero')

def mostrar(self):
      print("Cuenta Joven", self.bonificacion)
    

x=CuentaJoven('Pepe',50,50,20)
print(x.es_titular.valido)

