# estudando sobre os metodos get e set
class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


    def desconto(self, percentual): # criando um metodo para desconto no preco do produto
        self.preco = self.preco - (self.preco * percentual / 100)


    # Usando o Getter -> este metodo ou decorador, entrega um resultado
    @property
    def preco(self):
        return self._preco

    # Usando o setter -> este metodo tem como função configurar um atributo ou metodo de uma class
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor   



camisa = Produto('Camisa', 235)
bermuda = Produto('bermuda masculina',169)
camisa.desconto(25)
bermuda.desconto(18)
print(camisa.preco)
print(f'{bermuda.preco:.2f}')
