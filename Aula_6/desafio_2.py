''''
Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e 
ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
'''

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, disponivel = True):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = disponivel

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao}'
    
livro1 = Livro('Bananas de pijama', 'Desconhecido', 2003)
livro2 = Livro('Turma da Mônica', 'Maurício de Souza', 1987)

print(livro1)
print(livro2)