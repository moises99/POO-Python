class Funciocionario():
    def __init__(self,nome_funcionario,setor_funcionario,cargo_funcionario):
        self.nome = nome_funcionario
        self.setor = setor_funcionario
        self.cargo = cargo_funcionario
    def apresentacao(self):
        return f"Olá eu sou {self.nome} sou {self.cargo} no departamento de {self.setor}"
    
f1 = Funciocionario("Moises","TI",'DEV')
print(f1.apresentacao())


