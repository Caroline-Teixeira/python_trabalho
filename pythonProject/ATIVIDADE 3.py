# FUNÇÕES

# Função e cálculos do objeto
def dimesoesObjeto():
    while True:  # Laço de Dimensões
        while True:  # Laço de Medidas
            try:  # Para o comprimento
                comprimento = float(input('Digite o comprimento do objeto (em cm): '))
            except ValueError:  # em caso de erro
                print(
                    'Você digitou alguma dimensão do objeto com valor não numérico. \nPor favor entre com as Dimensões desejadas novamente.')
                continue

            try:  # Para a largura
                largura = float(input('Digite o largura do objeto (em cm): '))
            except ValueError:
                print(
                    'Você digitou alguma dimensão do objeto com valor não numérico. \nPor favor entre com as Dimensões desejadas novamente.')
                continue

            try:  # Para a altura
                altura = float(input('Digite a altura do objeto (em cm): '))
                break  # Quebra o "Laço de medidas"
            except ValueError:
                print(
                    'Você digitou alguma dimensão do objeto com valor não numérico. \nPor favor entre com as Dimensões desejadas novamente.')
                continue

        # Calculo da dimensão, com a variável d:
        d = comprimento * largura * altura
        if (d < 100000):
            print("O volume do objeto (em cm³) é: {}".format(d))

            v = float  # valor do multiplicador das dimensões em reais
            if d < 1000:
                v = 10
            elif d >= 1000 and d < 10000:
                v = 20
            elif d >= 10000 and d < 30000:
                v = 30
            elif d >= 30000 and d < 50000:
                v = 50

            return v
            break  # Quebra o "Laço de Dimensões"

        else:  # se ultrapassar o limite permitido
            print(
                "Não aceitamos objetos com dimensões tão grandes.\nPor favor entre com as Dimensões desejadas novamente.")
            continue


# Função que verifica o peso do objeto
def pesoObjeto():
    while True:  # laço para o peso
        while True:  # laço para valores corretos
            try:
                peso = float(input('Digite o peso do objeto (em kg): '))
                break

            except ValueError:  # se ultrapassar o limite permitido
                print('Você digitou o peso do objeto com valor não numérico. \nPor favor entre com o Peso desejado novamente.')
                continue

        if (peso < 30):
            print("O peso do objeto (em kg) é: {}".format(peso))

            p = float  # valor do multiplicador do peso
            if peso < 0.1:
                p = 1

            elif 0.1 <= peso < 1.5:
                p = 1.5

            elif 1 <= peso < 10:
                p = 2

            elif 10 <= peso < 30:
                p = 3

            return p
            break
        else:
            print("Não aceitamos objetos com peso tão grandes.\nPor favor entre com o Peso Desejado novamente.")
            continue


# Função que verifica a rota
def rotaObjeto():
    while True:  # laço para a rota
        print("Selecione a rota")
        print("RS - De Rio de Janeiro até São Paulo\nSR - De São Paulo até Rio de Janeiro\nBS - De Brasília até São Paulo\nSB - De São Paulo até Brasília\nBR - De Brasília até Rio de Janeiro\nRB - Rio de Janeiro até Brasília")
        rota = input("")

        r = 0  # valor do multiplicador da rota

        if rota.upper() == 'RS' or rota.upper() == 'SR':
            r = 1
        elif rota.upper() == 'BS' or rota.upper() == 'SB':
            r = 1.2
        elif rota.upper() == 'BR' or rota.upper() == 'RB':
            r = 1.5
        else:
            print("Você digitou uma rota que não existe.\nPor favor entre com a Rota desejada novamente.")
            continue
        return r
        break



# PROGRAMA PRINCIPAL
print("Bem vindo a Loja de Logistica da Caroline Francieli Teixeira - RU 1035263")
dim = dimesoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dim * peso * rota  # calculo do preço total
print("Total a pagar: R$ {:.2f} (dimensões: {} * peso: {} * rota: {}) ".format(total, dim, peso, rota))

