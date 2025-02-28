class Restaurante:
    # def __init__(self, nome, categoria, ativo=False):
    #     self.nome = nome
    #     self.categoria = categoria
    #     self.ativo = ativo
    nome = ''
    categoria = ''
    ativo = False

pizzaria = Restaurante()
pizzaria.nome = 'pizza'
pizzaria.categoria = 'italiana'
pizzaria.nome = 'blizô'
pizzaria.ativo = True

print(pizzaria.nome)
print(pizzaria.ativo)


restaurante_chines = Restaurante()
restaurante_chines.nome = 'shushi'
restaurante_chines.categoria = 'japonês'

print("A categoria do restaurante chinês é japonesa? ")
if restaurante_chines.categoria == 'japonês':
    print(f'Sim! A categoria do restaurante {restaurante_chines.nome} é {restaurante_chines.categoria}!')
else:
    print('Não.')
