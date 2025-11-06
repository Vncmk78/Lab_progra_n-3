class Cuadrados:
    def __iter__(self):
        for m in range(1, 11):
            yield m ** 2

for v in Cuadrados():
    print(v)
