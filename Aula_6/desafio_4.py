'''
Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e
retorna uma lista dos livros disponíveis publicados nesse ano.
'''

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, disponivel = True):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = disponivel

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao}'
    
    def emprestar_livro(self):
        self._disponivel = False

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis

livro1 = Livro('Bananas de pijama', 'Desconhecido', 2003)
livro2 = Livro('Turma da Mônica', 'Maurício de Souza', 1987)
livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)

Livro.livros = [livro1, livro2, livro3]

print(livro1)
print(livro2)
print(livro3)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")