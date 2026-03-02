from rich import print
from rich.panel import Panel
class Churrasco():
    def __init__(self, titulo,quantidade):
        self.titulo = titulo
        self.quantidade = quantidade

    def analisar(self):
        def moeda(moeda):
            return f"{moeda:,.2f}".replace(',', 'x').replace('.',',').replace('x','.')
        qtdc = (400 * self.quantidade) / 1000
        total = 82.40 * qtdc
        valor_por_pessoa = total / self.quantidade
        paniel = Panel(f'''Analisando o [bold blue]{self.titulo}[/] com [bold yellow]{self.quantidade} convidados[/]
Cada participante comera 400G de carne e cada KG custa R$82,40
Recomendamos comprar [bold green]{qtdc}KG[/] de carne
Custo total será de [bold red]R${moeda(total)}[/]
custando [bold purple] R${moeda(valor_por_pessoa)}[/] por pessoa''',title=self.titulo,expand=False)
        print(paniel)


c1 = Churrasco('Churras 01🍖 ', 15)
c1.analisar()

c2 = Churrasco('Churras 02 🍖 ', 10)
c2.analisar()