numero_inicio = int(input("Digite um número inicial: "))
numero_fim = int(input("Digite um número final: "))

for numero in range(numero_inicio, numero_fim+1):
    for multiplicador in range(1, 11):
        print(f"{numero} x {multiplicador} = {numero*multiplicador}")