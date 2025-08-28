soma = 0

while True:
    numero = int(input("Digite um número (0 para encerrar): "))

    if numero == 0:
        break

    soma += numero

print(f"A soma total é: {soma}")
