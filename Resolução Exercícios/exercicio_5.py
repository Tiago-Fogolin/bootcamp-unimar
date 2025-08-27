altura = float(input("Informe a sua altura em metros: "))
peso = float(input("Informe o seu peso: "))

imc = peso / (altura ** 2)

# podemos usar o round para arredondar a imc
# o primeiro valor do round é o que queremos arrendodar
# o segundo é quantas casas decimais desejamos que o numero final tenha
print(f"O seu IMC é: {round(imc, 2)}")