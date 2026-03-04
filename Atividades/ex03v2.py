from rich import print
from rich.panel import Panel


class Compra:
    carne = 400
    valor_kg = 82.40
    def __init__(self,titulo,qtd):
        self.titulo = titulo
        self.quantiade_pessoa = qtd
    
    #Retorna a quantidade em KG de carne por pessoa.
    def quantiade_de_carne(self):
        return (Compra.carne * self.quantiade_pessoa) / 1000
    #Retorna o total em R$ gasto
    def total(self):
        return Compra.valor_kg * self.quantiade_de_carne()
    
    #Retorna o valor em R$ gasto por pessoa
    def valor_por_pessoa(self):
        return self.total() / self.quantiade_pessoa
    
    #Formata os valores em Real
    def moeda(moeda):
        return f"R${moeda:,.2f}".replace(',', 'x').replace('.',',').replace('x','.')
    

    def Analisar(self):
        cont = f"Analisando o [bold green]{self.titulo}[/] com [bold green]{self.quantiade_pessoa}[/] pessoas"
        cont += f"\nCada participante comerá [bold green]{Compra.carne}G[/] de carne e cada KG custará [bold green]{Compra.moeda(Compra.valor_kg)}[/]."
        cont += f"\nRecomendamos a compra de [bold yellow]{self.quantiade_de_carne()}KG[/] de carne."
        cont += f"\nCusto total de [bold red]{Compra.moeda(self.total())}[/]."
        cont += f"\nCustando por pessoa [bold red]{Compra.moeda(self.valor_por_pessoa())}[/]."
        painel = Panel(cont,title=self.titulo,expand=False)
        print(painel)
    
c1 = Compra('Churras V2', 80)
c1.Analisar()
