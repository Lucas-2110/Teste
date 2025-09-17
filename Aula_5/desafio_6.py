''''
Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. 
Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.
'''

class ClienteBanco:
    def __init__(self, nome, telefone, email, idade, cpf ):
        self.nome = nome 
        self.telefone = telefone
        self.email = email
        self.idade = idade
        self.cpf = cpf

cliente1 = ClienteBanco('Lucas', 99999999, 'l@gmail.com', 20, 1111111111)
cliente2 = ClienteBanco('Ana', 99999999, 'a@gmail.com', 20, 1111111111)
cliente3 = ClienteBanco('João', 99999999, 'j@gmail.com', 25, 1111111111)