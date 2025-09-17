''''
Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida 
uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
'''

class Restaurante:
    def __init__(self, nome, categoria, pratos, avaliacao, ativo = False):
        self. nome = nome 
        self.categoria = categoria
        self.ativo = ativo
        self. pratos = pratos
        self.avaliacao = avaliacao

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
novo_restaurante = Restaurante(nome = 'Santa Maria', categoria = 'Italiana', pratos = 'Massa', avaliacao = 9, ativo = True)
print(novo_restaurante)
    