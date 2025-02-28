# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.

# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.
# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.




person = {
    'nome' : 'João',
    'idade' : 42,
    'cidade' : 'Teresina',
    'email' : 'joao@exemplo.com'
}

person['nome'] = 'Ana'
person['cidade'] = 'Recife'
person['profissão'] = 'Enfermeira'
print(person)
del(person['idade'])
print(person)



# square_numbers = {
#     '1' : 1,
#     '2' : 4,
#     '3' : 9,
#     '4' : 16,
#     '5' : 25,
# }

squares_numbers = { str(i): i**2 for i in range(1,6)}
print(squares_numbers)



if '2' in squares_numbers:
    print("True")
else:
    print('False')




frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)