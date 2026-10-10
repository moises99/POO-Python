from hashlib import sha256

class ContaBancaria:
    def __init__(self,id,titular,saldo,senha):
        self._id = id
        self._titular = titular
        self.__saldo = saldo
        self.__hash = None
        self.__autorizacao = True
        self.__senha = senha #Chama o setter e passa a senha que veio por parametro
    
    
    @property
    def __senha(self):
        return self.senha
    @__senha.setter
    def __senha(self,chave):#Exige um padrao de senha
        if len(chave) >= 6:
            self.__hash = sha256(chave.encode("utf-8")).hexdigest()
        else: 
            print( f'A senha deve ter mais de 6 caracteres')

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
            return f'Deposito de {valor} realizado com sucesso'
        else:
            print('Valor invalido')

    def sacar(self,valor,chave):
        if self.validar_senha(chave):#Chama o metodos validar a senha, se verdadeito autorizar uma tentativa de saque
            if valor <= self.__saldo:#Compara o valor do saque com o saldo em conta, se saldo for superior será autorizado
                self.__saldo -= valor
                return f'Saque de {valor} realizado, saldo atual: {self.__saldo}'
            else:
                return f'Saldo insulficiente,saque negado. Saldo atual: {self.__saldo}'
        else:
            return 'Senha invalida,saque negado'

    def validar_senha(self,chave):#Valida se as senhas são iguais
        chave_criptografada = sha256(chave.encode("utf-8")).hexdigest()
        if self.__hash == chave_criptografada:
            self.__autorizacao = True
            return True
        return False


    @property
    def dados(self):
        if self.__autorizacao: # Se autorirzado mostra as informações da conta
            self.__autorizacao = False
            return f'Conta:{self._id}\nTitular: {self._titular}\nSaldo:{self.__saldo}'
        return f'Senha invalida, nenhuma informação disponivél'
    @dados.setter
    def dados(self,chave):
        if self.validar_senha(chave):#Chama o metodos validar a senha, se verdadeito autorizar visualizar os dados
            return f'Conta:{self._id}\nTitular: {self._titular}\nSaldo:{self.__saldo}'
        return f'Senha invalida, nenhuma informação disponivél'





#Abertura da conta
print('Criando conta')
cb = ContaBancaria(1010,'Moises',2000,'1245454545454d4sdfsd5!!@!@!@345')
print(cb.dados)
sacar = cb.sacar(500,'1245454545454d4sdfsd5!!@!@!@345')
print(sacar)
print(cb.dados)