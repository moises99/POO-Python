from rich import print
from rich.panel import Panel

class Game:
    def __init__(self,nome,nick):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def add_jogos_favoritos(self,jogo):
       self.jogos_favoritos.append(jogo)
        

    
    def ficha(self):
        conteudo = f'Nome real: {self.nome}\n'
        conteudo+= 'Jogos Favoritos:\n'
        minha_lista = [
            i for i in self.jogos_favoritos
        ]
        conteudo+= f'🎮 {"\n🎮 ".join(minha_lista)}'
        painel = Panel(conteudo,title=f'Jogador : {self.nick}',expand=False)
        print(painel)

        # print(*self.jogos_favoritos, sep="\n")

j1 = Game('Meu Nome','Meu Nick')
j1.add_jogos_favoritos('Jogo favorito 1')
j1.add_jogos_favoritos('Jogo favorito 2')
j1.add_jogos_favoritos('Jogo favorito 3')
j1.ficha()






