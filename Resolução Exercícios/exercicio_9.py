numero_1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (soma, sub, div ou mult): ")

# transformando a operação que o usuário passou tudo para minúsculo
operacao = operacao.lower()

if operacao == "soma":
    print("Resultado:", numero_1 + num2)
elif operacao == "sub":
    print("Resultado:", numero_1 - num2)
elif operacao == "div":
    print("Resultado:", numero_1 * num2)
elif operacao == "mult":
    print("Resultado:", numero_1 / num2)
else:
    print("Operação inválida")
