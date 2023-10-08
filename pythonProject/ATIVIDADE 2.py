print('Bem-vindo a Loja da Caroline Francieli Teixeira - RU 1035263')
print('*'*20 + "Cardápio" + '*'*20)
print("| Código |       Descrição       |  Valor  |")
print("|   100  |    Cachorro Quente    |   9,00  |")
print("|   101  | Cachorro Quente Duplo |  11,00  |")
print("|   102  |         X-Egg         |  12,00  |")
print("|   103  |       X-Salada        |  12,00  |")
print("|   104  |        X-Bacon        |  14,00  |")
print("|   105  |        X-Tudo         |  17,00  |")
print("|   200  |   Refrigerante Lata   |   5,00  |")
print("|   201  |       Chá Gelado      |   4,00  |")
print('*'* 48)

acumulador = 0 #Variavel 'Acumulador' de pedidos em reais

while True: #while 1
    codigo = int(input('Entre com o código desejado: '))
    if codigo != 100 and codigo != 101 and codigo != 102 and codigo != 103 and codigo != 104 and codigo != 105 and codigo != 200 and codigo != 201:
        print("Opção inválida")
        continue #se o usuário digitar o código errado, volta para o começo do while 1

    if (codigo == 100):
        print("Você pediu um Cachorro Quente no valor de 9,00")
        acumulador = acumulador + 9

    elif (codigo == 101):
        print("Você pediu um Cachorro Quente Duplo no valor de 11,00")
        acumulador = acumulador + 11

    elif (codigo == 102):
        print("Você pediu um X-Egg no valor de 12,00")
        acumulador = acumulador + 12

    elif (codigo == 103):
        print("Você pediu um X-Salada no valor de 12,00")
        acumulador = acumulador + 12

    elif (codigo == 104):
        print("Você pediu um X-Bacon no valor de 14,00")
        acumulador = acumulador + 14

    elif (codigo == 105):
        print("Você pediu um X-Tudo no valor de 17,00")
        acumulador = acumulador + 17

    elif (codigo == 200):
        print("Você pediu um Refrigerante Lata no valor de 5,00")
        acumulador = acumulador + 5

    elif (codigo == 201):
        print("Você pediu um Chá Gelado no valor de 4,00")
        acumulador = acumulador + 4

    while True: #Para confirmar a continuação do pedido (while 2)
        print("Deseja pedir mais alguma coisa? ")
        print("1 - sim")
        print("0 - não")
        p = int(input(""))  #Variavel 'p' que recebe/encerra pedidos
        if p == 1 or p == 0:
            break #quando o usuário digita os valores corretos
        else:
            print("Digite o comando certo (1 ou 0)") #Para que o usuário apenas digite '1' or '0', senão continua no while 2

    if p == 1:
        continue

    elif (p == 0):  #para encerrar o pedido
        print("O valor total a ser pago é {:.2f}".format(acumulador))
        break
