class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro_one = Carro('Corrola', 'azul', 2017)

class Restaurante:
    def __init__(self, nome, categoria, cidade, ativo = False,  internacional = False):
        self.nome = nome
        self.categoria = categoria 
        self.cidade = cidade
        self.ativo = ativo
        self.internacional = internacional

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.cidade} | {self.ativo} | {self.internacional}'


restaurante_one = Restaurante('Nordestina', 'comida local', 'Pernambuco')


print(restaurante_one)


class Cliente:
    def __init__(this, nome, idade, genero, email):
        this.nome = nome
        this.idade = idade
        this.genero = genero
        this.email = email

cliente_one = Cliente('Ana', 27, 'F', 'ana@example.com') 
cliente_one = Cliente('Davi', 31, 'M', 'Davi@example.com') 
cliente_one = Cliente('Richard', 17, 'M', 'richard@example.com') 
