from abc import ABC

class Poligono(ABC):
    def __init__(self,quantidade_lados = 4):
        self.quantidade_lados = quantidade_lados
    
    #@abstractmethod    
    def perimetro(self):
        ...
    #@abstractmethod
    def area(self):
        ...
class Quadrado(Poligono):
    def __init__(self,tamanho_lado):
      super().__init__(4)
      self.lado = tamanho_lado
      
    def perimetro(self):
        return self.lado * self.quantidade_lados
    def area(self):
        return self.lado * self.lado
        
        
   
   
class Circulo(Poligono):
    def __init__(self,raio):
        self.raio = raio
    
    def perimetro(self):
        return 2 * 3.14 * self.raio
        
    def area(self):
        return 3.14 * (self.raio**2)
        

q = Circulo(20)
calc_perimetro = q.perimetro()
calc_area = q.area()
print(f" O perimetro é {calc_perimetro:.1f}")
print(f"A area é {calc_area}")