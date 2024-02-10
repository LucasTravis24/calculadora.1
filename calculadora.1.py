#Calculadora 1

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Qual operador (+-*/): ')

    numeros_validos = None
    numero_1_float = 0 
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um dos números ou operador é invalidos')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Realizando sua conta, veja abaixo:')

    if operador == '+':
        print(numero_1_float + numero_2_float)
    elif operador == '-':
        print(numero_1_float - numero_2_float)

    elif operador == '*':
        print(numero_1_float * numero_2_float)
    elif operador == '/':
        print(numero_1_float / numero_2_float)
    else:
         print('Voce nunca deveria  ter chegado aqui')

    sair = input('quer sair [si]im: ').lower().startswith('s')
    print('Até logo!!!')

    if sair is True:
        break


#Depois que acabei de fazer essas linhas de codigo
#tiveram muitos problemas
#o principal era la no try!
#e muitos outros problemas
#na digitação
#o que não é bom
#preciso me atentar mais a isso
#no fim eu aprendi e corrigi meus erros 
#o que realmente importa
#agora e continuar praticando e controlando esses meus erros