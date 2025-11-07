#se calcula los numeros cuadrados del 1 al 10

class Cuadrado:
    def __iter__(self):
        for m in range(1, 11):
            yield m ** 2

for v in Cuadrado():
    print(v)
