''''
Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo
como False por padrão. Crie uma instância utilizando o construtor.
'''

class Restaurante:
    def __init__(self, nome, categoria, pratos, avaliacao, ativo = False):
        self. nome = nome 
        self.categoria = categoria
        self.ativo = ativo
        self. pratos = pratos
        self.avaliacao = avaliacao

novo_restaurante = Restaurante(nome = 'Santa Maria', categoria = 'Italiana', pratos = 'Massa', avaliacao = 9, ativo = True)