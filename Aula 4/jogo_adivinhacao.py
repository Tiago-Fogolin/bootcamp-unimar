import random

# sorteia número de 1 a 10
numero_secreto = random.randint(1, 10)

tentativas = 0

while True:
    entrada  = input("Digite um número de 1 a 10 (ou 'sair' para encerrar): ")
    tentativas += 1

    if entrada.lower() == "sair":
        print("Jogo encerrado.")
        break

    if int(entrada) == numero_secreto:
        print(f"Parabéns, você ganhou em {tentativas} tentativas.!")
        break

