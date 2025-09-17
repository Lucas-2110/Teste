""""
Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar
se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.
"""

usuario_correto = 'Lucas'
senha_correta = 'Lucas2110'

usuario = input('Digite o usuário: ')
senha = input('Digite a senha: ')

if usuario == usuario_correto and senha == senha_correta:
    print('Login realizado')
else:
    print('Usuário ou senha, inválido!')