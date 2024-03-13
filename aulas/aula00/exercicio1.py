#listas:
produtos = ["baquetas", "tambor", "palheta", "prato"]
preco = ["50", "200.5", "5.5", "300"]
quantidade = ["10", "4", "10", "5"]

#loop:
for i in range(len(produtos)):
    print(f"{i+1} - {produtos[i]}: R$ {preco[i]}")

#escolha:
while True:
    try:
        escolha_produto = int(input("numero do produto ou '0'(zero) para encerrar:"))
        if escolha_produto not in range(1, len(produtos) + 1) and escolha_produto != 0:
            raise ValueError
        break
    except ValueError:
        print("Inválido; Escolha entre 1 e {} ou 0 para encerrar". format(len(produtos)))

while True:
    try:
        quantidade_comprada = int(input("Digite a quantidade que deseja comprar: "))
        if quantidade_comprada > quantidade_disponivel:
            raise ValueError
        break
    except ValueError:
        print("Quantidade inválida. O valor máximo é: {}".format(quantidade_disponivel))

if escolha_produto !=0:
    produto_escolhido = produtos[escolha_produto -1]
    preco_escolhido = preco[escolha_produto -1]
    quantidade_disponivel = quantidade[escolha_produto -1]

    print("Produto escolhido:{}".format(produto_escolhido))
    print("Preço: R${}".format(preco_escolhido))
    print("Quantidade disponível: {}".format(quantidade_disponivel))


#Atualiza quantidade disponível:
quantidade[escolha_produto -1] -= quantidade_comprada

#Calcula total:
total_compra = quantidade_comprada * preco_escolhido

#Recibo
print("Recibo:")
print("{} {} x R${} = R${}".format(quantidade_comprada, produto_escolhido, preco_escolhido, total_compra))
