from rich import inspect
class Termometro:
    def __init__(self,temperatura = 0):
        self.__temperatura = temperatura

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self,valor):
        if 16 <= valor <= 30:
            self.__temperatura = valor
        else:
            if valor > 30:
                self.__temperatura = 30
                print(f"Temperatua maxima é {self.__temperatura} graus")
            else:
                self.__temperatura = 16
                print(f"Temperatua minima é {self.__temperatura} graus")

    @property
    def ftemperatura(self):
        return f'{self.__temperatura}ºC'


term = Termometro()
term.temperatura = 19
inspect(term, private=True,methods=True)

print(f'Temperatura atual é de: {term.ftemperatura}.')