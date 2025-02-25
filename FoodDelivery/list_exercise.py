# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.
# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.




numeros = []
numeros_impares = []
# Lista de números de 1 a 10;
for i in range(1, 11):
    numeros.append(i)

#Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
for i in numeros:
    if i % 2 != 0:
        numeros_impares.append(i)
        
print(sum(numeros_impares))
print()



# Lista com quatro nomes;
nomes = ["João", "Miquel", "Vanessa", "Thaís"]
for index, nome in enumerate(nomes):
    print(index+1 , nome)
print()

# Lista com o ano que você nasceu e o ano atual.
ano_nascimento_atual = [2006, 2025]
for ano in ano_nascimento_atual:
    print(ano)
print()



# Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
print(sorted(numeros, reverse=True))

#Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.


pergunta_ao_usuário = int(input("Digite um número para ver a sua tabuada de 1 ao 10!"))

print("\nTabuada de adição!")
for numero in numeros:
    resultado = numero + pergunta_ao_usuário
    print(f"{pergunta_ao_usuário} + {numero} = {resultado}")

print("\nTabuada de subtração!")
for numero in numeros:
    resultado = numero - pergunta_ao_usuário
    print(f"{pergunta_ao_usuário} - {numero} = {resultado}")

print("\nTabuada de multiplicação!")
for numero in numeros:
    resultado = numero * pergunta_ao_usuário
    print(f"{pergunta_ao_usuário} X {numero} = {resultado}")
    
print("\nTabuada de divisão!")
for numero in numeros:
    resultado = numero / pergunta_ao_usuário
    print(f"{pergunta_ao_usuário} / {numero} = {resultado}")


