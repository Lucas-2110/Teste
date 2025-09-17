''''
Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e 
atribua valores aos seus atributos através de um método construtor.
'''

class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome 
        self.idade = idade
        self.email = email
        self.telefone = telefone

cliente1 = Cliente(nome = 'Lucas', idade = 20, email = 'l@gamil.com', telefone = 99999999)
cliente2 = Cliente(nome = 'Ana', idade = 20, email = 'a@gmail.com', telefone = 8888888)
cliente3 = Cliente(nome = 'Julia', idade = 14, email = 'j@gmail.com', telefone = 7777777)