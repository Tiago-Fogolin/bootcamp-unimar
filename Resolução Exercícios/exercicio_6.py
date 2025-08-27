primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

if primeiro_numero > segundo_numero:
    print(f"O maior número é o {primeiro_numero}")
elif primeiro_numero < segundo_numero:
    print(f"O maior número é o {segundo_numero}")
else:
    print("Os dois números são iguais")