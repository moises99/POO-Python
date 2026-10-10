from abc import ABC
from datetime import datetime

class Pessoa(ABC):
    def __init__(self,nome:str ,nascimento: int):
        self._nome: str = nome
        self._nascimento: int = None
        self.nascimento: int = nascimento
    
    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self,ano):
        if ano == None:
            ...
        else:
            if isinstance(ano, int):
                if 1926 <= ano <= 2025:
                    self._nascimento = ano
                else:
                    raise ValueError(f'O ano deve ser entre 1926 e 2025')
            else:
                raise TypeError('Verifique o ano e tente novamente, o ano deve ser um numero inteiro')
    
    @property
    def idade(self) -> int:
        if self.nascimento:
            return datetime.now().year - self.nascimento
        else:
            raise ValueError(f'Idade não pode ser vazio')
        

class Aluno(Pessoa):
    def __init__(self,nome: str = None,nascimento: int = None ,curso=None):
        super().__init__(nome,nascimento)
        self._nome: str = nome
        self._curso = None
        self.curso_oficiais: str = ['ADS','ADM']
        self.curso = curso
    
    @property
    def curso(self):
        return self._curso
    @curso.setter
    def curso(self,curso):
        if curso == None:
            ...
        else:
            if curso in self.curso_oficiais:
                self._curso = curso
            else:
                raise NameError(f'Curso indisponivel {curso}, veja a lista de disponibilidade {self.curso_oficiais}')

    def add_curso(self,curso):
        if curso not in self.curso_oficiais:
            self.curso_oficiais.append(curso)
    
    def __str__(self):
        return (f'O aluno {al._nome} com idade {al.idade} está matriculado no curso de {al.curso}')



al = Aluno('Moises',2000,'ADM')
print(al)
