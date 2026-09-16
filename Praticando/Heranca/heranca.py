class Pessoa:
    def __init__(self,nome = '',idade = 0,curso = ''):
        self.nome = nome
        self.idade = idade
        self.curso = curso
    
class Aluno(Pessoa):
    def __init__(self,nome,idade,turma,curso):
        super().__init__(nome,idade,curso)
        self.turma = turma

class Professor(Pessoa):
    def __init__(self,nome,idade,especializacao,curso):
        super().__init__(nome,idade,curso)
        self.especializacao = especializacao
        

    

p1 = Pessoa('Moises',30)
print(p1.__dict__)

a1 = Aluno('Moises',10,'T001','T.i')
print(a1.__dict__)

prof = Professor('Moises',40,'Mestrado','Gestao')
print(prof.__dict__)

