print("Olá, Mundo!")

print(2 + 2)  

# Cria uma lista com os números entre 1 e 20
numeros = list(range(1, 21))
print(numeros)

# Percorre a lista e imprime numeros pares e divisiveis por 4
for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)