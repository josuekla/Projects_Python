class Restaurante:
    def __init__(self, nome, categoria, ativo = False):
        self.nome = nome
        self.categoria = categoria 
        self.ativo =  ativo

    def __str__(self):
        return f'{self.nome.ljust(20)} | {self.categoria}'

restaurante_pizzaria = Restaurante('pizzaria paulistana', 'Italiana',)
restaurante_123go = Restaurante('FastFood123go', 'fastfoods',)



print(restaurante_pizzaria)
print(restaurante_123go)
