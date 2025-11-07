#se calcula los primeros 10 numeros pares

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = list(filter(lambda m: m % 2 == 0, numeros))
print(pares)
