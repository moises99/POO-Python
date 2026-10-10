
class Diario:
    def __init__(self,senha):
        self.__senha = senha
        self.__segredos = []

    @property
    def escrever(self):
        return self.__segredos
    @escrever.setter
    def escrever(self,segredo):
        self.__segredos.append(segredo)

    @property
    def ler(self):
        return self.__segredos
    @ler.setter
    def ler(self,senha):
        senha = input('Para ler o diario, informe a senha...')
        while not self.__senha == senha:
            print('Senha invalida')
            senha = input('Para ler o diario, informe a senha...')
        [print(f'{v} - Lendo: {segredos}...') for v,segredos in enumerate(self.__segredos)]
    
senha = input('Defina uma senha para seu Diario...')
meu_diario = Diario(senha)
meu_diario.escrever = ('Aprendendo POO')
meu_diario.escrever = ('Aprendendo POO com Python')
meu_diario.ler = senha
