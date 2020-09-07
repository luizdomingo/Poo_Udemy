class Carro():
    preco = 50000  # Aqui temos uma variavel de class
    # dessa forma esta variavel fica disponivel para todas as isntancia desta class

    
    def __init__(self, cor, fabricante):
        #self.preco = preco  # Aqui são atributos da class
        self.cor = cor
        self.fabricante = fabricante

p1 = Carro('azul','corsa')
print(p1.fabricante)
print(Carro.preco)