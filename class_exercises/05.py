class Conta_corrente:
    def __init__(self, nmr_da_conta, nome_do_correntista, saldo=0):
        self.nmr_da_conta = nmr_da_conta
        self.nome_do_correntista = nome_do_correntista
        self.saldo = saldo

    def status(self):
        return (f'Nome: {self.nome_do_correntista} \nNumero da conta: {self.nmr_da_conta} \nSaldo: R${round(self.saldo, 2)}')

    def alterar_nome(self, new_name):
        self.nome_do_correntista = new_name
        return new_name

    def deposito(self, deposito):
        self.saldo += deposito
        return self.saldo
    
    def meusaque(self, saque):
        if self.saldo > saque:
            self.saldo -= saque
        else:
            print("Saldo insuficiente")
        return self.saldo
    
nome_do_correntista = str(input("Insira o nome do titular: "))
saldo = float(input("Insira o valor do deposito: "))
nmr_da_conta = int(input("Insira o numero da conta: "))
     
c1 = Conta_corrente(nmr_da_conta, nome_do_correntista, saldo)
print(c1.status())

c1.alterar_nome("Jorgin")
print("\n"+ " - NOME ALTERADO - \n" + c1.status())

c1.deposito(100)
print("\n"+ " - DEPOSITO - \n" + c1.status())

c1.meusaque(290)
print("\n"+ " - SAQUE - \n" + c1.status())



# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve 
# possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são 
# os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor 
# default zero e os demais atributos são obrigatórios.



