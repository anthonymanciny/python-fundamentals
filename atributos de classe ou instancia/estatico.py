class Pessoa:
    def __init__(self,nome,idade) -> None:
        self.nome = nome
        self.idade = idade
    @classmethod
    def criar_dedatadenascimento(cls,dia,mes,ano,nome):
        print(cls)

# p = Pessoa("ANTHONY",25)
# print (p.nome, p.idade)

p= Pessoa.criar_dedatadenascimento(1999,5,26,'Anthony')

# print(p2.nome, p2.idade)