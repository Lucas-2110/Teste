''''
Crie uma instância da classe e imprima o valor da propriedade titular.
'''

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
    
cliente1 = ContaBancariaPythonica('Lucas', 2500)
print(cliente1)