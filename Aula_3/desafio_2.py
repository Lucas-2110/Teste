""""
Utilizando o dicionário criado no item 1:

Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
Adicione um campo de profissão para essa pessoa;
Remova um item do dicionário.
"""

pessoa = [{'nome' : 'Lucas', 'idade' : '20', 'cidade' : 'São Paulo'}]

# Atualizando informação:
pessoa['idade'] = 21
# Adicionando informação:
pessoa['profissão'] = 'Desenvolvedor'
# Removendo elemento:
del pessoa['cidade']

print(pessoa)
