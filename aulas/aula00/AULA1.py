# Método que não recebe parâmetro
# e NÃO tem retorno:
def imprimireu():
    print("Nome: Ricardo")
    print("Hobby: Música")

# Método que não recebe parâmetro
# e TEM retorno:
def getpi():
    return 3.14

# Método que recebe parâmetro
# e NÃO tem retorno:
def print_area_circ(raio):
    area = getpi() * (raio * raio)
    print("Área do círculo: ", area)

# Método que recebe parâmetro
# e TEM retorno:
def calcula_area_circ(raio):
    area = getpi() * (raio * raio)
    return area

imprimireu()
print_area_circ(3)


