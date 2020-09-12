from Aula01 import Pessoa
from Agregacao_composicao import CarrinhoDeCompras, Produtos
from pendulum import parse  # modulo usado para manipulação de datas
from Aula10 import *
# p1 = Pessoa()  # aqui estamos Atribuindo o objeto pessoa a uma variavél
# p1.falar()  # aqui estamos passando o método a variavél

f = Funcionario('Luiz', 32)
f.trabalhar()
f.falar()

a = Aluno('Clarice', 5)
a.estudar()
a.falar()
