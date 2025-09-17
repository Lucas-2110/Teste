''''
Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ 
para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario 
que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma 
mensagem de saudação personalizada com base na profissão da pessoa.
'''

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return f'{self._nome} | {self._idade} anos | {self._profissao}'
    
    @property
    def saudacao(self):
        if self._profissao:
            return f'Olá, {self._nome}! seu trabalho é {self._profissao}'
        else:
            return f'Olá, {self._nome}'
    
    def aniversario(self, idade):
        self._idade += 1