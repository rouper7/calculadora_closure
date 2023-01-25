# Escreva um código que use closures  para criar uma calculadora básica que possa ser usada para calcular a soma, subtração, multiplicação e divisão de dois números.


def sinal(sinal):    
    def calcular(x,y):
        nonlocal sinal
        if sinal=='-':
            return x-y
        elif sinal=='+':
            return x+y
        elif sinal=='*':
            return x*y
        elif sinal=='/':
            return x/y
        else:
            return print('digite somente os sinais')
    return calcular
    

subtracao=sinal('-')
somar=sinal('+')
smultiplicar=sinal('*')
dividir=sinal('/')
print(subtracao(20,10))
#made by rouper7
    

                    

