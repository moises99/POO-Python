from rich import print
class Caneta:
    def __init__(self,cor):
        self.caneta = cor
        self.tampa = False
    
    def escrever(self,texto):
        if self.tampa:
            if self.caneta == 'Vermelha':
                print(f'[bold red]{texto}[/]')
            elif self.caneta == 'Azul':
                print(f'[bold blue]{texto}[/]')
            elif self.caneta == 'Verde':
                print(f'[bold green]{texto}[/]')
    
    def destampar(self):
        self.tampa = True

    def quebrar_linha(self,n=0):
        for _ in range(n):
            print('\n')






c1 = Caneta('Vermelha')
c2 = Caneta('Azul')
c3 = Caneta('Verde')

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever('Seu texto em vermelho')
c1.quebrar_linha()
c2.escrever('Seu texto em azul')
c3.escrever('Seu texto em verde')

