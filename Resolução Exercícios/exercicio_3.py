quantidade_minutos = int(input("Minutos: "))

# divisao inteira por 60, vai nos dar a quantidade de horas
# que os minutos equivalem
horas = quantidade_minutos // 60

# caso tenha resto na nossa divisao, o resto será a quantidade de minutos
minutos = quantidade_minutos % 60

print(f"Isso equivale a: {horas} hora(s) e {minutos} minuto(s).")

