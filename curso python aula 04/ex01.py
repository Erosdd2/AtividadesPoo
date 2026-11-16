class Gafanhoto:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."

g1 = Gafanhoto()
g1.nome = "Marcos"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())   

g2 = Gafanhoto()
g2.nome = "Maria"
g2.idade = 16
g2.aniversario()
print(g2.mensagem())   

g3 = Gafanhoto()
print(g3.mensagem())


class Aluno:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        return f"{self.nome} é Aluno de informática do IFRN campus Ceará-Mirim e tem {self.idade} anos de idade."

g1 = Aluno()
g1.nome = "Eros"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())