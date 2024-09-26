# Laços

# Solicita ao usuário um número inteiro
numero = int(input("Digite um número inteiro: "))

# Exibe a tabuada do número de 1 a 10
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")