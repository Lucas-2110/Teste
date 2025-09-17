""""
Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse 
número, indo de 1 a 10.
"""

numero = int(input('Digite um número: '))

for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} * {i} = {resultado}')