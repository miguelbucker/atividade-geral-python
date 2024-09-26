# Esturutra de Decisão e Laços

soma = 0

print("Insira um número (Digite o 0 para sair)")

while True:
    valor = input("Digite o valor: ")
    if valor == "0":
        break
    try:
        valor_numero = float(valor)
        soma += valor_numero
    except ValueError:
        print("Por favor, insira um número válido.")

print("A soma dos números digitados é:", soma)
