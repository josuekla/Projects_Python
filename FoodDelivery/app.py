import os
def exibir_menu():
    print("𝐹𝑜𝑜𝒹 𝒹𝑒𝓁𝒾𝓋𝑒𝓇𝓎\n")
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

class Funcoes:
    def cadastrar_restaurante():
        pass
    def listar():
        pass 
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

