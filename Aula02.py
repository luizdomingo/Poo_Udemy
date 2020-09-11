from random import randint

class Pessoa:
    ano_atual = 2020
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano(self): # Aqui temos o que chamamos de metodo da class, quando usamos a alavra self
        print(self.ano_atual - self.idade)


    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento): # usamos quando for pegar um metodo global da class
        idade = cls.ano_atual - ano_nascimento         # não usamos a palavra self, usamos o cls.
        return cls(nome, idade)  


    @staticmethod
    def gerar_id():                     # no metodo static nos não usamos a palavra self nem a palavra cls
        aleatorio = randint(250, 500)   # passa a ser uma funçao normal, para usarmos o @staticmetod 
        return aleatorio                # precisamos atribuila a uma instancia


p1 = Pessoa('luiz', 32)
print(p1.nome, p1.idade)        
p1.get_ano()
print(p1.gerar_id())
