class Pessoa:
  #Metodo construtor
  def __init__(self,n,i):
    #atributos de instância
    self.nome = n
    self.idade = i

  #Metodos da instância
  def aniversario(self):
    self.idade = self.idade + 1

  def __str__(self):
    return f"O {self.nome} tem {self.idade}"

  def __getstate__(self):
    return f" {self.nome} ; {self.idade}"

#Declaração de um objeto
g1 = Pessoa('Moises',29)
print(g1.__dict__)
print(g1.__getstate__())