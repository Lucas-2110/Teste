''''
Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. 
Instancie um restaurante e atribua valores aos seus atributos.
'''

class Restaurante:
    def __init__(self, nome, categoria, ativo, pratos, avaliacao):
        self.nome = nome 
        self.categoria = categoria
        self.ativo = False
        self.pratos = pratos
        self.avaliacao = avaliacao
        
restaurante_exemplo = Restaurante(nome = 'Pizzaria', categoria = 'Italiana', ativo = True, pratos = 'Pizza', avaliacao = 8)