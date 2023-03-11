from datetime import date
class Pessoa:
    def __init__(self, nome, idade):
        self.nome=nome
        self.idade=idade
    @classmethod
    def apartiAnoNascimento(cls,nome, ano):
        return cls(nome, date.today().year-ano)
    @staticmethod
    def ehMaiordeIdade(idade):
        return idade  >=18
p=Pessoa('Joao', 26)
p2=Pessoa.apartiAnoNascimento('Ana', 2006)
print(p.idade)
print(p2.idade)
print(Pessoa.ehMaiordeIdade(17))