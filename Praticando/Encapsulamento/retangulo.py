from rich import inspect
class Retangulo:
    def __init__(self,v_base = 1,v_altura = 1) -> None:
        self.altura = v_altura
        self.base = v_base

    @property
    def base(self):
        return self._base
    @base.setter
    def base(self,base):
        try:
            if base < 0:
                self._base: int = 1
                raise ValueError('As medidas devem ser interitos positivas, valor da base' \
                ' substituido por 1.')
            else:
                self._base: int = base
        except ValueError as erro:
                print(erro)

    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self,altura):
        try:
            if altura < 0:
                self._altura: int = 1
                raise ValueError('As medidas devem ser interitos positivas, valor da altura' \
                ' substituido por 1.')
            else:
                self._altura: int = altura
        except ValueError as erro:
            print(erro)


    @property
    def area(self):
        return self.base * self.altura
    @property
    def medidas(self):
        return f'Base: {self.base}m.\nAltura: {self.altura}m.\nArea: {self.area}m².'


a = Retangulo(2,4)
print(a.medidas)

