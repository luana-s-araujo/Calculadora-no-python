#abaixo do código está um passo a passo simplificado
#{} as chaves representam os dígitos

def calculadora():
    operacao = input('''
Qual a operação?
Digite:
+ se for adição
- se for subtração
* se for multiplicação
/ se for divisão
''')

    digito1 = int(input('digito 1: '))
    digito2 = int(input('digito 2: '))

    if operacao == '+':
        print('{} + {} = '.format(digito1, digito2))
        print(digito1 + digito2)

    elif operacao == '-':
        print('{} - {} = '.format(digito1, digito2))
        print(digito1 - digito2)

    elif operacao == '*':
        print('{} * {} = '.format(digito1, digito2))
        print(digito1 * digito2)

    elif operacao == '/':
        print('{} / {} = '.format(digito1, digito2))
        print(digito1 / digito2)

    else:
        print('Operação não escolhida ou digito incorreto')

    # Add again() function to calculate() function
    repetir()

def repetir():
    repetir_operacao = input('''
Vc quer usar novamente a calculadora?
Digite S para SIM ou N para NÃO.
''')

    if repetir_operacao.upper() == 'S':
        calculadora()
    elif repetir_operacao.upper() == 'N':
        print('Obrigada por testar essa calculadora :) ')
    else:
        repetir()

calculadora()


#definir com o def uma função inicial
#antes de pedir os dados, solicitar qual a operacao desejada com um input
#pedir dados com o input
#colocando os operadores atraves do print e .format
#operadores estes para + - * /
#iniciar a soma com um if
#usar elif para - * /
#usar else para nenhuma operacao escolhida ou digito incorreto
#definir com o def uma segunda funcao para poder usar novamente a calculadora
#na segunda def: if para SIM, elif para NÃO, else repetir a pergunta
