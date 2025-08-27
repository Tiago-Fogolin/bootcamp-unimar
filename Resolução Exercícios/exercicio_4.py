nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

# assim como na matemática, as operações entre parenteses são realizadas primeiro
media = (nota_1 + nota_2 + nota_3) / 3

# podemos usar o round para arredondar a nota
# o primeiro valor do round é o que queremos arrendodar
# o segundo é quantas casas decimais desejamos que o numero final tenha
nota_arredondada = round(media, 1)
print(f"A média das notas é: {nota_arredondada}")