''''
Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo.
Inicie o atributo ativo como False por padrão.
'''

class ContaBancaria:
    def __init__(self, titular, saldo, ativo = False):
        self.tiular = titular
        self.saldo = saldo 
        self._ativo = ativo
    
    def __str__(self):
        return f'{self.tiular} | {self.saldo} | {self._ativo}'