from abc import ABC,abstractmethod
from rich import print
from rich.table import Table
class Transporte(ABC):
    def __init__(self,distancia):
        self.distancia = distancia
        #self.frete = 0
           
    @abstractmethod
    def calc_frete(self):
        ...

class Caminhao(Transporte):
    def __init__(self,distancia):
        super().__init__(distancia)
        self.fator = 1.20

    def calc_frete(self):
        if self.distancia < 50:
            return f"[red]indisponivel. Distancia minima ed 50 KM.[/]"
        else:
            return f"[green]R${self.fator * self.distancia:.2f}[/]".replace('.',',')


class Drone(Transporte):
    def __init__(self,distancia):
        super().__init__(distancia)
        self.fator = 9.5

    def calc_frete(self):
        if self.distancia > 10:
            return f"[red]Indisponivel. Distancia maxima de 10 KM.[/]"
        else:
            return f"[green]R${self.fator * self.distancia:.2f}[/]".replace('.',',')

class Moto(Transporte):
    def __init__(self,distancia):
        super().__init__(distancia)
        self.fator = 0.50

    def calc_frete(self):
        return f"[green]R${self.fator * self.distancia:.2f}[/]".replace('.',',')



dist = 11

veiculo_moto = Moto(dist)
valor_moto = veiculo_moto.calc_frete()

veiculo_caminhao = Caminhao(dist)
valor_caminhao = veiculo_caminhao.calc_frete()

veiculo_drone = Drone(dist)
valor_drone = veiculo_drone.calc_frete()



tabela = Table(title='FRETES')
tabela.add_column("Veiculo")
tabela.add_column('Distancia')
tabela.add_column('Valor')

tabela.add_row(f"{type(veiculo_moto).__name__}",f"{dist} KM",(f"{valor_moto}"))
tabela.add_row(f"{type(veiculo_caminhao).__name__}",f"{dist} KM",f"{valor_caminhao}")
tabela.add_row(f"{type(veiculo_drone).__name__}",f"{dist} KM",f"{valor_drone}")

print(tabela)