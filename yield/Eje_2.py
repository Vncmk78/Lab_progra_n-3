def impares(lista):
    for m in lista:
        if m % 2 != 0:
            yield m

numeros = [1, 2, 3, 4, 5, 6, 7]
for num in impares(numeros):
    print(num)
