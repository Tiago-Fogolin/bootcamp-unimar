# o valor inserido na variável com o input sempre será string (texto)
idade = input("Qual a sua idade? ")

# podemos ver isso com a função type
print(type(idade))

# então se precisamos fazer contas com esse valor, uma conversão será necessária
idade = int(idade) # convertendo idade para inteiro, e colocando esse novo valor novamente na variavel idade

print(f"Ano que vem você terá {idade+1} anos.")

# conversão para float
altura = float(input("Qual a sua altura em metros? "))

print(f"Sua altura em centímetros é {altura * 100}.")