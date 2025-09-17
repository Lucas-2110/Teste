''''
Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
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
    
livro1 = Livro('Bananas de pijama', 'Desconhecido', 2003)
livro2 = Livro('Turma da Mônica', 'Maurício de Souza', 1987)
livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)

print(livro1)
print(livro2)
print(livro3)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")
