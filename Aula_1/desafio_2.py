""""
Pergunte ao usuário sua idade e, com base nisso, 
use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.
"""

idade = int(input('Digite a sua idade: '))

if idade <= 12:
    print(f'Sua idade é {idade} anos, você é uma criança')
elif idade <= 18:
    print(f'Sua idade é {idade} anos, você é um adolescente')
else:
    print(f'Sua idade é {idade} anos, você é um adulto')