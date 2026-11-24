class ContaBancaria:
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"conta {self.id} criada com sucesso. saldo atual de R${self.saldo:,.2f}") 

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:.2f} de saldo"

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print (f"deposito de R${valor:,.2f} autorizado na conta {self.id}")

    def sacar (self, valor):
        if valor > self.saldo:
            print(f"saque negado de R$ {valor:,.2f} na conta {self.id}: saldo insuficiente")
        else:    
            self.saldo = self.saldo - valor
            print(f"saque de R${valor:,.2f} autorizado na conta {self.id}")


c1 = ContaBancaria (id= 122, nome = "Jonas", saldo= 5000)
c1.depositar(500)
c1.sacar(3_000_000)
print(c1)