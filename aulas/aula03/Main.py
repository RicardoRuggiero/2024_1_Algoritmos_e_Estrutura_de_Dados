from Pessoa import Pessoa
from Cidade import Cidade
#
C4 = Cidade(nome="Osório")
print(C4)
#
C1 = Cidade()
C2 = Cidade(nome = "Porto Alegre")
C3 = Cidade(1, "Tramandaí")
C5 = Cidade(id = 2)
print("C1: ", C1)
C1.nome = "POA"
print("C1: ",C1)
print("C2: ",C2)
print("C3: ",C3)
print(C5)
#
p1 = Pessoa("Rick")
p2 = Pessoa("Raul", 20)
p3 = Pessoa("Mara", 30, C1 )
p4 = Pessoa("Leo", cid = C2 )
p5 = Pessoa("Eduarda", idade = 40)
print(p4.idade)
print(p1.nome)
print(p2.nome)
print(p3.nome)
print(p4.nome)
print(p5.nome)
