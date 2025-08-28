quantidade_notas = 3
soma_notas = 0
contador = 0

while contador < quantidade_notas:
    nota = float(input("Digite uma nota: "))
    soma_notas += nota

    contador += 1

media = soma_notas / quantidade_notas
print(f"A média das notas é: {media}")

