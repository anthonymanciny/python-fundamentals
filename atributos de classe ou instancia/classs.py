class Estudante:
    escola = 'Dio'

    def __init__(self, nome , matricula) -> None:
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} ({self.matricula}) - {self.escola}"

def mostra_valores(*objs):
    for obj in objs:
        print(obj)

aluno003 = Estudante("Anthony",895652)


mostra_valores(aluno003)

aluno003.matricula = 4
mostra_valores(aluno003)
