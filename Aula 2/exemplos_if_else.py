# Com o resultado de comparações, podemos executar ou não ações. Para isso utilizamos 
# o if



# if sozinho
idade = 18

if idade >= 18:
    print("Você é maior de idade.")

# if com else
idade = 16

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# if com elif e else
# Lembrando: o if pode vir sozinho, ou então acompanhado somente de elif, somente
# de else ou com os dois. Mas não podemos utilizar nem o elif e nem o else sozinhos,
# eles precisam de um  if antes.
idade = 7

if idade >= 18:
    print("Adulto")
elif idade >= 12:
    print("Adolescente")
elif idade >= 3:
    print("Criança")
else:
    print("Bebê")

# exemplo com and (as duas condições precisam ser verdadeiras)
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir.")
else:
    print("Não pode dirigir.")

# exemplo com or (uma das condições precisa ser verdadeira)
feriado = False
fim_de_semana = True

if feriado or fim_de_semana:
    print("Pode descansar.")
else:
    print("Dia de trabalho.")