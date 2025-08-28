# o while executa o que estiver dentro dele, enquanto a condição passada for verdadeira

# exibindo olá 10 vezes
contador = 0
while contador < 10:
    print("Olá")
    contador += 1

# exibindo os números pares de 1 a 20
numero = 1
while numero <= 20:
    if numero % 2 == 0:
        print(numero)
    numero += 1


# percorredo lista com while
frutas = ["maçã", "banana", "uva", "laranja"]
indice = 0

while indice < len(frutas):
    print(frutas[indice])
    indice += 1

# parando o loop no meio
numero = 1
while numero <= 10:
    if numero == 5:
        print("Achei o número 5, parando o loop!")
        break
    print(numero)
    numero += 1

# pulando execuções com o continue
numero = 0
while numero < 10:
    numero += 1
    if numero == 5:
        continue 
    print(numero)