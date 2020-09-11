from datetime import datetime


class Pessoa:
    def falar(self):
        print('Luiz está Falando')


# criando uma classe usando o metodo especial do python
class Pessoa1:
    ano_nascimento = int(datetime.strftime(datetime.now(), '%Y'))

    # ano_nascimento = 2020
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falando_1(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        if self.falando:
            print(f'{self.nome} Já está falando')
            return
        print(f'{self.nome} Está falando {assunto}')
        self.falando = True

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome}, ja esta comendo')
            return
        print(f'{self.nome} Está comendo {alimento}')
        self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} Não está comendo')
            return
        print(f'{self.nome} Parou de comer')
        self.comendo = False

    def get_idade(self):
        print(f'O ano de nascimento de {self.nome} é {self.ano_nascimento - self.idade}')
