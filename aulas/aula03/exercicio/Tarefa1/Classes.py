class Pedido:
    #
    def __init__(self, id, endereco, Pessoa):
        #
        self.id = id
        self.end = endereco
        self.produtos = []
        self.cliente = Pessoa
        #
    def addProduto(self, produto):
        if produto.qtd > 0:
            self.produtos.append(produto)
            return produto
        else:
            print("Não há estoque!")
        ###fazer um for para percorrer o array self.produtos somando os preços de todos os produtos de todo o array /\
class Produto:
    #
    def __init__(self, id, nome, preco, qtd, categoria = Categoria(id, nome)):
        #
        self.id = id
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.cat = categoria
        #
class Categoria:
    #
    def __init__(self, id, nome):
        #
        self.id = id
        self.nome = nome
        #
class Pessoa:
    #
    def __init__(self, nome, idade=18, cid = Cidade(None, "Tangamandápio")):
        #
        self.nome = nome
        self.idade = idade
        self.cidade = cid
        #
class Cidade:
    #
    def __init__(self, id = 0, nome = "Itati"):
        #
        self.id = id
        self.nome = nome
        #
