from abc import ABC,abstractmethod
class BebidaQuente(ABC):
    def preparar(self):
        print(f'--- Iniciando Preparo do {type(bebida).__name__}---')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print(f'--- Seu {type(bebida).__name__} está pronto---')
    def ferver_agua(self):
        print('1 - Ferver agua a 100 graus.')
        
    @abstractmethod
    def misturar(self):
        ...
    @abstractmethod
    def servir(self):
        ...
        
class Cafe(BebidaQuente):
    def misturar(self):
        print('2 - Passando água pressurizada pelo pó de café moído.')
    def servir(self):
        print('3 - Servindo em chicara pequena.')


class Cha(BebidaQuente):
    def misturar(self):
        print('2 - Mergulhando o sachê de ervas na água.')
    def servir(self):
        print('3 - Servindo na caneca de porcelana com limão.')


class Leite(BebidaQuente):
    def misturar(self):
        print('2 - Passando vapor pressurizado pelo bico do leite.')
    def servir(self):
        print('3 - Servindo na caneca grande, já com café.')  

bebida = Cafe()
bebida.preparar()