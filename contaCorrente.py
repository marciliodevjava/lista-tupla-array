class ContaCorrente:

    def __init__(self, codigo=int):
        self.__codigo = codigo
        self.__saldo = 0

    def __str__(self):
        return f'Codigo {self.__codigo} \nSaldo RS: {self.__saldo}\n'

    def deposita(self, saldo):
        self.__saldo += saldo

    def saca(self, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            print(f'Saque realidado R$: {valor}')
        else:
            print(f'Não foi possivel realizar o saque solicitado.')

    def transferir(self, conta, valor):
        if self.__saldo >= valor:
            self.__saldo -= valor
            conta.deposita(valor)
            print(f'Deposito realizado')
        else:
            print(f'Não foi possivel realizar o deposito')

    def deposita_todas_contas(contas):
        for conta in contas:
            conta.deposita(50)


conta = ContaCorrente(1)
conta1 = ContaCorrente(2)
conta.deposita(100)
print(conta)
conta.saca(25)
print(conta)

conta.transferir(conta1, 50)
print(conta)
print(conta1)

print()
conta_sady = ContaCorrente(256)
conta_sady.deposita(100)
print(conta_sady)
conta_sady.transferir(conta1, 25)
print(conta_sady)
print()

print(conta1)
print()

conta_list = [conta, conta1, conta_sady]
print("Lista conta")
print(conta_list[0])

list = ContaCorrente
list.deposita_todas_contas(conta_list)

print("Contas depositadas")

for con in conta_list:
    print(con)
    print("Conta depositada")


guilherme = ('Guilherme', 21, 36)
daniela = ('Daniela', 22, 26)
pedro = ('Pedro', 23, 59)


