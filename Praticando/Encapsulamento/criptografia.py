from hashlib import sha256
from rich import inspect
class Criptografia:
    def __init__(self):
        self.__hash = None

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self,senha):
        self.__hash = sha256(senha.encode("utf-8")).hexdigest()

    def validar(self,chave):
        usuario = sha256(chave.encode("utf-8")).hexdigest()
        if usuario == self.__hash:
            return True
        else:
            return False


a = Criptografia()
a.senha = 'abc'
validacao_senha = a.validar('abc')

if validacao_senha:
    print('Senha Válida')
else:
    print('Senha Inválida')
