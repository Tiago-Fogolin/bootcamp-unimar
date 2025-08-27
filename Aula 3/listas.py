# Exemplos de definição de listas
nomes = ["Ana", "Bruno", "Carlos"]        # lista só de strings
numeros = [10, 20, 30, 40]                # lista só de inteiros
misturada = ["Maçã", 42, 3.14, True]        # lista misturada

print("Nomes:", nomes)
print("Números:", numeros)
print("Misturada:", misturada)


# Acessando índices da lista
print("Primeiro nome:", nomes[0])     # índice 0
print("Segundo nome:", nomes[1])      # índice 1
print("Último nome (com -1):", nomes[-1])  # índice negativo


# Adicionando elementos
# o append sempre adiciona o elemento no final
numeros.append(50)         
print("Após append:", numeros)

# Removendo elementos
removido_pop = nomes.pop()      # remove o último
nomes.pop(1) # remove no índice 1
print("Elemento removido com pop:", removido_pop)
print("Lista após os pops:", nomes)

numeros.remove(50)
print("Lista após remove:", numeros)


# Acessando o último elemento
print("Com índice negativo:", numeros[-1])
print("Com len()-1:", numeros[len(numeros) - 1])
