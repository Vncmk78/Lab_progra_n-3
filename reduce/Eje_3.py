from functools import reduce

numeros = [7, 3, 9, 1, 5]
mayor = reduce(lambda a, b: a if a > b else b, numeros)
print(mayor)
