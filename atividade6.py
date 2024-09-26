# Exceções e Laços

##Solicita ao usuário um número inteiro

try:
    numero = int(input("Digite um número inteiro: "))
    print(f"Você digitou o número: {numero}")
except ValueError:
    print("Erro: Por favor, digite um número inteiro")
