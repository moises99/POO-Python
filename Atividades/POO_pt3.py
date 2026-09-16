from time import sleep as sl


class ContaBancaria:
    '''
    Criação de uma conta bancaria passando ID,NOME E SALDO
    '''
    #Metodo construtor
    def __init__(self,i,t,s=0):
        #Atributos da instância
        self.id = i
        self.titular = t
        self.saldo = s
        print(f'O cliente ID:{self.id} {self.titular} possui um daldo de R${self.saldo:,.2f}')
    #Metodos da instância
    def sacar(self,valor):
        if self.saldo > valor:
          self.saldo = self.saldo - valor
          print(f'{self.titular} realizou um saque de R${valor:,.2f}')
        else:
          print(self.titular,'seu saldo é insulficiente')
    def depositar(self, valor):
        self.saldo += valor
        print(f'{self.titular} realizou um novo deposito de R${valor:,.2f}')
    def __str__(self):
      return f"Saldo atual: R${self.saldo:,.2f}"

#Declaração do objetos
conta1 = ContaBancaria(99,'Moises',3000)
sl(1)
#Metodo depositar
conta1.depositar(250)
sl(1)
#metodo sacar
conta1.sacar(100)
sl(1)
print(conta1)
sl(1)

