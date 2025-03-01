class ContaBancaria:
    def __init__(self, titular, saldo, cpf, profissao):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        self._cpf = 

    def __str__(self):
        return f'Olá {self._titular}! O seu saldo é R${self._saldo}'
    
    @classmethod
    def ativar_conta(self):
        print("Ativando a conta")
        self.ativo = True
    
conta_1 = ContaBancaria('João Silva Lima', 690)
conta_2 = ContaBancaria('Thais Silva Lima', 6090)
print(conta_1.ativo)
conta_1.ativar_conta()
print(conta_1.ativo)

print(conta_1)
print(conta_2)

print()