#Cria uma classe Produto com nome e preço e um metodo que gera uma etiqueta do produto
from rich import print
from rich.panel import Panel
from rich.text import Text

class Produto():
    def __init__(self,nome_produto,preco_produto):
        self.nome = nome_produto
        self.preco = float(preco_produto)

    def etiqueta(self):
        tam = len(self.nome) + 8
        painel = Panel(Text(f'{self.nome} \n{'-'*tam:^6} \n{moeda(self.preco):.^{tam}}',justify="center",style="blue"),title="Produto".upper(),style="purple",expand=False,)
        print(painel)

#Formtação para moeda
def moeda(moeda):
    return f"R${moeda:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")

lista = ["Samsung s22","Placa de Vído NVIDIA RTX 5070 WINDFORCE","PC GAMER Core 2 DUO","Processador intel","Processador AMD"]
lpreco = [3000,4500,23000,1700,1200]
for chave,produto in enumerate(lista):
    p1 = Produto(produto,lpreco[chave])
    p1.etiqueta()
