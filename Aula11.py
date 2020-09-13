"""
Vamos estudar mais sobre Herança, agora vamos ver o que é
Sobreposição de método, lembrando que para usarmos herança
devemos atribuir a nossa super-class com o self.__class__.__name__
"""


class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.idade = idade
        self.sexo = sexo
        self.nome = nome
        self.nomeclass = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclass} Está falndo neste momento..')


class Cliente(Pessoa):
    pass


class ClienteVip(Cliente):
    pass
