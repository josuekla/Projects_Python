import os

restaurantes = [{'nome' : 'Picanha na hora', 'categoria' : 'carnes', 'ativo' : True},
                {'nome' : 'Acaí show', 'categoria' : 'acaí', 'ativo' : False},
                {'nome' : 'JHamburgues', 'categoria' : 'Hamburger', 'ativo' : True}]

def exibir_menu():
    '''Essa função é para exibir o menu'''
    print("𝐹𝑜𝑜𝒹 𝒹𝑒𝓁𝒾𝓋𝑒𝓇𝓎\n")
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. alterar o estado do restaurante')
    print('4. Sair\n')

class Funcoes:
    '''Classe de todas as funções principais do programa'''
    def cadastrar_restaurante():
        '''Cadastramento de novos restaurantes e suas categorias
        
        Inputs:
        - Cadastro de novo restaurante
        - Definir a categoria do restaurante

        Outputs:
        Novo cadastro de restaurante
        
        '''
        Funcoes.exibir_subtitulo("Cadastrando novos restaurantes")
        nome_restaurante_novo = input("Digite o nome do novo restaurante que deseje cadastrar: ")
        categoria_restaurante = input(f"Digite o nome da categoria do restaurante {nome_restaurante_novo}: ")
        dados_restaurante = {'nome' : nome_restaurante_novo, 'categoria': categoria_restaurante, 'ativo': False}
        restaurantes.append(dados_restaurante)
        print(f"O restaurante {nome_restaurante_novo} foi cadastrado com sucesso!")
        Funcoes.voltar_ao_menu_principal()
    def listar():
        '''Listamento de todos os restaurantes cadastrado'''
        os.system("cls")
        Funcoes.exibir_subtitulo("Listando todos os restaurantes")
        print(f"{'Nome do restaurante'.ljust(23)} | {'categoria'.ljust(20)} | {'Estado de ativação'.ljust(20)}")
        print("-" * 100)
        for restaurante in restaurantes:
            ativo = "Ativado" if restaurante['ativo'] else 'Desativado'
            print(f" - {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {ativo}")
            print(f" - {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {ativo}")
        Funcoes.voltar_ao_menu_principal()
        
        

    def activate_restaurant():
        '''Função para ativar o desativar o estado do restaurante'''
        Funcoes.exibir_subtitulo("alterando o estado de ativação do restaurantes")
        input_restaurante_ativacao = input("Digite o nome do restaurante que deseje alterar de estado: ")
        restaurante_encontrado = False

        for restaurante in restaurantes:
            if restaurante['nome'] == input_restaurante_ativacao:
                restaurante_encontrado = True
                restaurante['ativo'] = not restaurante['ativo']

                mensagem = f"O restaurante {input_restaurante_ativacao} foi ativado com sucesso!" if restaurante['ativo'] else f"O restaurante {input_restaurante_ativacao} foi desativado com sucesso"
                
                print(mensagem)
        
        if not restaurante_encontrado: 
            print("Restaurante não encontrado, tente novamente.")
        Funcoes.voltar_ao_menu_principal()
    def sair():
        '''Sair do programa'''
        os.system("cls")
        Funcoes.exibir_subtitulo("Você está saindo.") 

    def voltar_ao_menu_principal():
        '''Voltar para o menu'''
        input("\nDigite qualquer tecla para voltar para o menu. ")
        main()

    def opcao_invalida():
        '''Função para mostrar um erro e voltar para o Menu'''
        print('Opção inválida, escolha um número de 1 ao 4!')
        Funcoes.voltar_ao_menu_principal()

    def exibir_subtitulo(texto):
        '''Função para exibir o títulos para todas as funções que for preciso'''
        os.system('cls')
        linha = '=' * len(texto)
        print(linha)
        print(texto)
        print(linha)
        print()

def escolhas():
    '''Função de lógica de todas as escolhas do usuário no sistema.'''

    try:
        escolha_cliente = int(input("Escolha uma das opções:"))
        print(f"Você escolheu a opção {escolha_cliente}")


        if escolha_cliente == 1:
            Funcoes.cadastrar_restaurante()
        elif escolha_cliente == 2:
            Funcoes.listar()
        elif escolha_cliente == 3:
            Funcoes.activate_restaurant()
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
