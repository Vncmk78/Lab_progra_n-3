from functools import reduce

numeros = [2, 3, 4]
multiplicacion = reduce(lambda x, y: x * y, numeros)
print(multiplicacion)
