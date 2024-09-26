# Funções e Exceções

def dividir():

    try:
        numerador = 20
        denominador = 0
        resultado = numerador / denominador 
        print(resultado)

    except ZeroDivisionError:
        print("O valor não pode ser divido por zero")

dividir()