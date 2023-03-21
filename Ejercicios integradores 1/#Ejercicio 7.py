#Ejercicio 7
class Cuenta:
  def __init__(self,titular='',cantidad=0):
    self.titular = titular
    self.cantidad= cantidad

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

    def retirar(self, cantidad):
      if cantidad>0:
       self.cantidad= self.cantidad-cantidad










