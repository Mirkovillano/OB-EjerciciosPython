numeros = []
contador = 0
while contador <=100:
    numeros.insert(contador, contador)
    contador += 1

numeros.reverse()

print(numeros)