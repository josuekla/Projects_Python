import os

restaurantes = ["pizza", "carne"]

def exibir_menu():
    print("𝐹𝑜𝑜𝒹 𝒹𝑒𝓁𝒾𝓋𝑒𝓇𝓎\n")
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

class Funcoes:
    def cadastrar_restaurante():
        os.system("cls")
        print("Cadastro de novos restaurantes\n")
        nome_restaurante_novo = input("Digite o nome do novo restaurante que deseje cadastrar: ")
        restaurantes.append(nome_restaurante_novo)
        print(f"O restaurante {nome_restaurante_novo} foi cadastrado com sucesso!")
        input("\nDigite qualquer tecla para voltar para o menu")
        main()
    def listar():
        os.system("cls")
        print("listar todos os restaurantes\n")
        for restaurante in restaurantes:
            print(f".{restaurante}")
        input("\nDigite qualquer tecla para voltar para o menu")
        main()

    def ativar():
        pass 
    def sair():
        os.system("cls")
        print("Você saiu!\n")    
    def opcao_invalida():
        print('Opção inválida, escolha um número de 1 ao 4!')
        input("Digite qualquer tecla para voltar ao menu.")
        main()

def escolhas():

    try:
        escolha_cliente = int(input("Escolha uma das opções:"))
        print(f"Você escolheu a opção {escolha_cliente}")


        if escolha_cliente == 1:
            Funcoes.cadastrar_restaurante()
        elif escolha_cliente == 2:
            Funcoes.listar()
        elif escolha_cliente == 3:
            Funcoes.ativar()
        elif escolha_cliente == 4:
            Funcoes.sair()
        else:
            Funcoes.opcao_invalida()
    except():
        Funcoes.sair()

def main():
    os.system("cls")
    exibir_menu()
    Funcoes()
    escolhas()

if __name__ == '__main__':
    main()

