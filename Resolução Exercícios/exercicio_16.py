lista_compras = []

with open("lista.txt", "r") as arquivo:
    linha = arquivo.readline()
    itens = linha.split(";")
    lista_compras = itens

while True:
    print("1. Ver a lista de compras")
    print("2. Adicionar um item na lista")
    print("3. Parar o programa")

    comando = input("Digite um comando: ")

    if comando == '1':
        print(f"Lista de compras: {lista_compras}")
        input("Aperte enter para voltar: ")
    elif comando == '2':
        item = input("Escreva um item para adicionar na lista: ")
        lista_compras.append(item)
    elif comando == '3':
        break
    else:
        print("Comando inválido.")

with open("lista.txt", "w") as arquivo:
    for item in lista_compras:
        if item != lista_compras[-1]:
            arquivo.write(item + ";")
        else:
            arquivo.write(item)