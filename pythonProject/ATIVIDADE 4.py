#FUNÇÕES
#---- Variáveis Globais -----
lista_peca = []    #LISTA DE PEÇAS: que será alterada conforme adiciona/remove peças
codigo_peca = 0    #contagem de peças: zero (0) peças quando programa é iniciado


#---- Para Cadastrar Peças -----
def cadastra_peca(codigo):
    print('Você selecionou a opção Cadastrar Peças')
    print('Código da Peça: {}'.format(codigo))
    nome = input('Entre com o NOME da peça: ')
    fabricante = input('Entre com o FABRICANTE da peça: ')
    valor = float(input('Entre com o VALOR da peça (R$): '))
    dicionario_peca = {'Código' : codigo,
                       'Nome' : nome,
                       'Fabricante' : fabricante,
                       'Valor (R$)' : valor}
    lista_peca.append(dicionario_peca.copy())  #insere o dicionário de peças (LISTA)

#---- Para Consultar Peças -----
def consulta_peca():
    print('Você selecionou a opção Consultar Peças')
    while True:
        opcao_consultar = input('Escolha a opção desejada:\n' +
                            '1 - Consultar TODAS peças\n' +
                            '2 - Consultar Peças por CÓDIGO\n' +
                            '3 - Consultar Peças por FABRICANTE\n' +
                            '4 - RETORNAR\n' +
                            '>>')
        if opcao_consultar == '1':
            print('Você selecionou a opção: TODAS as Peças')
            for peca in lista_peca: #checa as peças na LISTA (varredura)
                print('-' * 30)
                for key, value in peca.items():  #varre todos os conjuntos chave e dados do dicionario de peças.
                    print('{}: {}'.format(key, value))
                print('-' * 30)

#num_desejado = variável que recebe a opção digitada pelo usuário
        elif opcao_consultar == '2':
            print('Você selecionou a opção: Peças por CÓDIGO')
            num_desejado = int(input('Digite o CÓDIGO da peça: '))
            for peca in lista_peca:  #checa as peças na LISTA (varredura)
                if peca['Código'] == num_desejado:
                    for key, value in peca.items():  # varre todos os conjuntos chave e dados do dicionario de peças referente ao [Código] informado
                        print('{}: {}'.format(key, value))
                    print('-' * 30)

        elif opcao_consultar == '3':
            print('Você selecionou a opção: Peças por FABRICANTE')
            num_desejado = input('Digite o FABRICANTE da peça: ')
            for peca in lista_peca:
                if peca['Fabricante'] == num_desejado:  # O valor do campo 'fabricante' desse dicionário é igual ao dado informado
                    print('-' * 30)
                    for key, value in peca.items():  # varre todos os conjuntos chave e dados do dicionario de peças referente ao [FABRICANTE] informado
                        print('{}: {}'.format(key, value))
                    print('-' * 30)


        elif opcao_consultar == '4':
            return  #volta para o menu principal
        else:
            print('Opção Inválida. Tente novamente')
            continue  # volta para o início do laço

#---- Para Remover Peças -----
def remove_peca():
    print('Você selecionou a opção Remover Peças')
    num_desejado = int(input('Digite o CÓDIGO da peça a ser REMOVIDA: '))
    for peca in lista_peca:
        if peca['Código'] == num_desejado:   #remove a peça de acordo com o código fornecido
            lista_peca.remove(peca)
            print('Produto Removido')


# --- PROGRAMA PRINCIPAL -----
print('Bem-vindo ao Controle de Estoque da Bicicletaria da Caroline Francieli Teixeira - RU 1035263')
while True: #laço principal
    opcao = input('Escolha a opção desejada:\n'+
             '1 - Cadastrar peças\n'+
             '2 - Consultar peça(s)\n'+
             '3 - Remover peças\n'+
             '4 - Sair\n'+
             '>>')
    if opcao == '1':
        codigo_peca = codigo_peca + 1  #é adicionado na váriavel global
        cadastra_peca(codigo_peca) #Função: Cadastrar Peças
    elif opcao == '2':
        consulta_peca()  #Função: Consultar Peças
    elif opcao == '3':
        remove_peca()    #Função: Remover Peças
    elif opcao == '4':
        break    #encerra o laço principal (sair)
    else:
        print('Opção Inválida. Tente novamente')
        continue   #volta para o início do laço principal1

