''''
Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e 
o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
'''

class ContaBancaria:
    def __init__(self, titular, saldo, ativo = False):
        self.tiular = titular
        self.saldo = saldo 
        self._ativo = ativo
    
    def __str__(self):
        return f'Conta de: {self.tiular} - Saldo: {self.saldo}'
    
cliente1 = ContaBancaria('Lucas', 2500)
cliente2 = ContaBancaria('João', 200)