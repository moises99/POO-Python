from rich import print 
from time import sleep as sl
class Livro:
    def __init__(self,titulo,total_paginas):
        self.titulo = titulo
        self.paginas = total_paginas
        self.pg = 1
    def avancar_pagina(self,avancar_pg):
          for c in range(avancar_pg):
            if self.pg >= self.paginas:
              print(f'Parabéns, voce terminou o livro [bold red]{self.titulo}[/].')
              break
            self.pg +=1
            print(f'Página {self.pg} -> ',end="")
            sl(.2)
          if avancar_pg <= self.paginas:
            print(f' Você avançou {avancar_pg} páginas e está na página {self.pg}.')

    
livro = Livro('Aprendendo POO',20)

print(f'Você acabou de abrir o livro [bold red]{livro.titulo}[/] que tem [bold red]{livro.paginas} páginas[/], agora você está na pagina 1.')

livro.avancar_pagina(5)
livro.avancar_pagina(3)
livro.avancar_pagina(10)
livro.avancar_pagina(100)

