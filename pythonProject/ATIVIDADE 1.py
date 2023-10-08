print('Bem vindo a loja da Caroline Francieli Teixeira - RU 1035263')

p = float(input('Entre com o valor do produto: ')) #'p' recebe o valor do produto
q = int(input('Entre com o valor da quantidade: ')) #'q' recebe o valor da quantidade
preco = p * q #calculo do preço sem desconto
print("O valor sem desconto foi: R$ {:.2f}".format(preco))

if q <= 9:
    print("O valor com desconto foi: R$ {:.2f} (Desconto de 0%)".format(preco))

elif q > 9 and q <= 99:
    total = preco - (preco * 0.05) #cálculo do preço com 5% de desconto
    print("O valor com desconto foi: R$ {:.2f} (Desconto de 5%)".format(total))

elif q >= 100 and q <= 999:
    total = preco - (preco * 0.10) #cálculo do preço com 10% de desconto
    print("O valor com desconto foi: R$ {:.2f} (Desconto de 10%)".format(total))


else:
    total = preco - (preco * 0.15) #cálculo do preço com 15% de desconto
    print("O valor com desconto foi: R$ {:.2f} (Desconto de 15%)".format(total))