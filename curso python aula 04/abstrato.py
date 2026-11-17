class Sala:
    def __init__(self, datainicio, duracao, listaalunos):
        self.datainicio = datainicio
        self.duracao = duracao
        self.listaalunos = listaalunos

    def exibir(self):
        print(self.datainicio, self.duracao, self.listaalunos)