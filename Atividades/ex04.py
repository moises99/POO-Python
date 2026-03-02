from rich import print 
from time import sleep as sl
class Livro:
    def __init__(self,titulo,total_paginas):
        self.titulo = titulo
        self.paginas = total_paginas
    def avancar_pagina(self,avancar_pg):
        self.pg = 1
        self.avancar_pg = avancar_pg + 1

        while self.pg < self.avancar_pg:
            if self.pg >= self.paginas:
              print(f' voce avançou {self.paginas-1} paginas e chegou ao FIM DO LIVRO')
              break
            else:
              self.pg +=1
              print(f'Página {self.pg} -> ',end="")
              sl(.2)
              if  self.pg == self.avancar_pg: 
                print(f' Você avançou {self.avancar_pg-1} páginas e está na página {self.pg}.')
    



livro = Livro('Aprendendo POO',20)
print(f'Você acabou de abrir o livro [bold red]{livro.titulo}[/] que tem [bold red]{livro.paginas} páginas[/], agora você está na pagina 1.')
livro.avancar_pagina(5)








