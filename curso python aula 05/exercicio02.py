class Gafanhoto:
    def __init__(self, n = "", i = 0):
        self.nome = n
        self.idade = i

    def aniversario(self):
        self.idade = self.idade + 1

    def __str__ (self):
        return f"{self.nome} é Gafanhoto e tem {self.idade} anos de idade."

    def __getstate__(self,):
        return f"estado: nome = {self.nome}; idade = {self.idade} "

g1 = Gafanhoto(n = "Marcos", i = 17)
g1.aniversario()
print(g1)   

g2 = Gafanhoto (n = "Maria", i = 16)
g2.aniversario()
print(g2)   

g3 = Gafanhoto(n = "Eros", i = 18)
print(g3)
print(g3.__dict__) #Atributte
print(g3.__getstate__()) #Method
print(g3. __class__)