"""
A partir do momento em que uma classe usa uma outra classe para sobreviver
"""


class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def iserir_produtos(self, produto):
        self.produtos.append(produto)

    def listar_produto(self):
        for intem in self.produtos:
            print(intem.nome, intem.valor)

    def somar_total(self):
        total = 0
        for intem in self.produtos:
            total += intem.valor
        return total


class Produtos:
    def __init__(self, nome, Valor):
        self.nome = nome
        self.valor = Valor
