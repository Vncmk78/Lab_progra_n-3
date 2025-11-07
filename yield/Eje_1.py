#se calcula los primeros 10 numeros pares

def pares():
    for m in range(10):
        yield m * 2

for num in pares():
    print(num)
