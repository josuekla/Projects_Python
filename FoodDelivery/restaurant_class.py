class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria, ):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo =  False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome.ljust(20)} | {self._categoria}'
    

    @classmethod
    def listar_restaurantes(cls):
        print(f"{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Ativo"}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return f'⌧' if self._ativo else '□'

    def alternar_estado(self):
        self._ativo = not self._ativo
    

class Inputs():
    def __init__(self, pergunta):
        pass

    def fazer_perguntas(self, pergunta):
        self.pergunta


restaurante_pizzaria = Restaurante('pizzaria paulistana', 'Italiana')
restaurante_pizzaria.alternar_estado()
restaurante_pizzaria.alternar_estado()
restaurante_123go = Restaurante('FastFood123go', 'fastfoods')


Restaurante.listar_restaurantes()