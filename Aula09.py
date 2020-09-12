# Vamos estudar mais sobre Composição em Python orientado a Objetos
class Cliente:
    def __init__(self, Nome, Idade):
        self.nome = Nome
        self.idade = Idade
        self.enderecos = []

    # Vamos criar o método que inseri os endereços na lista da nossa classe Cliente
    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado


#c = Cliente('Luiz', 32)
# c.inserir_endereco('Natal','Rio grande do norte')
# c.listar_enderecos()

