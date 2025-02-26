import os

restaurantes = [{'nome' : 'Picanha na hora', 'categoria' : 'carnes', 'ativo' : True},
                {'nome' : 'Acaí show', 'categoria' : 'acaí', 'ativo' : False},
                {'nome' : 'JHamburgues', 'categoria' : 'Hamburger', 'ativo' : True}]

def exibir_menu():
    print("𝐹𝑜𝑜𝒹 𝒹𝑒𝓁𝒾𝓋𝑒𝓇𝓎\n")
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

class Funcoes:
    def cadastrar_restaurante():
        Funcoes.exibir_subtitulo("Cadastrando novos restaurantes")
        nome_restaurante_novo = input("Digite o nome do novo restaurante que deseje cadastrar: ")
        categoria_restaurante = input(f"Digite o nome da categoria do restaurante {nome_restaurante_novo}: ")
        dados_restaurante = {'nome' : nome_restaurante_novo, 'categoria': categoria_restaurante, 'ativo': False}
        restaurantes.append(dados_restaurante)
        print(f"O restaurante {nome_restaurante_novo} foi cadastrado com sucesso!")
        Funcoes.voltar_ao_menu_principal()
    def listar():
        os.system("cls")
        Funcoes.exibir_subtitulo("Listando todos os restaurantes")
        for restaurante in restaurantes:
            print(f" - {restaurante['nome']} | {restaurante['categoria']} | {restaurante['ativo']}")
        Funcoes.voltar_ao_menu_principal()
        
        

    def ativar():
        pass 
    def sair():
        os.system("cls")
        Funcoes.exibir_subtitulo("Você está saindo.") 

    def voltar_ao_menu_principal():
        input("\nDigite qualquer tecla para voltar para o menu. ")
        main()

    def opcao_invalida():
        print('Opção inválida, escolha um número de 1 ao 4!')
        Funcoes.voltar_ao_menu_principal()

    def exibir_subtitulo(texto):
        os.system('cls')
        print(texto)
        print()
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
    except Exception as e:
        Funcoes.opcao_invalida()
     

def main():
    os.system("cls")
    exibir_menu()
    Funcoes()
    escolhas()

if __name__ == '__main__':
    main()
