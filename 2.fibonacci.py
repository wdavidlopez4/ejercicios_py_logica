'''
cualquier numero de fibonacci
'''

def startupFibonacci(n):
    primerNumero = 1
    segundoNumero = 1

    if n == 1:
        print('0')
    elif n == 2:
        print('0', '1')
    else:
        print('0')
        print(primerNumero)
        print(segundoNumero)
        for i in range(n - 3):
            total = primerNumero + segundoNumero
            segundoNumero = primerNumero
            primerNumero = total
            print(total)


numero = int(input("ingerese el numero maximo: "))
startupFibonacci(numero)