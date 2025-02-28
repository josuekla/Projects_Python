class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria, ativo = False):
        self.nome = nome
        self.categoria = categoria 
        self.ativo =  ativo
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome.ljust(20)} | {self.categoria}'
    

    def listar_restaurantes():
        print("Listando todos os restaurantes")
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_pizzaria = Restaurante('pizzaria paulistana', 'Italiana',)
restaurante_123go = Restaurante('FastFood123go', 'fastfoods',)


Restaurante.listar_restaurantes()