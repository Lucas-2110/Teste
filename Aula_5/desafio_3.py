''''
Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. 
Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
'''

class ContaBancaria:
    def __init__(self, titular, saldo, ativo = False):
        self.tiular = titular
        self.saldo = saldo 
        self._ativo = ativo
    
    def __str__(self):
        return f'Conta de: {self.tiular} - Saldo: {self.saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    
cliente1 = ContaBancaria('Lucas', 2500)
ContaBancaria.ativar_conta(cliente1)
cliente2 = ContaBancaria('João', 200)