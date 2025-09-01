n = int(input("Digite um número: "))
soma = 0

for numero in range(1, n+1):
    soma += numero

print(f"A soma dos números de 1 até N é: {soma}")