while True:
    entrada = input("Digite um número (ou 'sair' para encerrar): ")

    if entrada.lower() == "sair":
        break

    numero = int(entrada)
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
