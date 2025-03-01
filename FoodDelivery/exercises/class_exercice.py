class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao


    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade}\nProfissão: {self.profissao}'
    

    def incrementar_ano(self):
        self.idade += 1


    @property
    def saudacao(self):
        if self.profissao: 
            return f'Olá! Meu nome é {self.nome}, tenho {self.idade}, e trabalho como {self.profissao}!'
        else:
            return f'Olá! Meu nome é {self.nome}, tenho {self.idade}'
        

ana_pessoa = Pessoa('ana', 5)
print(ana_pessoa)
ana_pessoa.incrementar_ano()
print(ana_pessoa)
print(ana_pessoa.saudacao)


        