class Gafanhoto():
  def __init__(self):#metodo construtor
  #atributos da instância
    self.nome = ''
    self.idade = 0
    self.sexo = ''

  #metodos de instância
  def aniversario(self):
    self.idade = self.idade + 1

  def mensagem(self):
    return f"O {self.nome} tem {self.idade}."


#Declaracao do objeto
g1 = Gafanhoto()
g1.nome = 'Moises'
g1.idade = 29
g1.aniversario()
print(g1.mensagem())