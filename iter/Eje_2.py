#se calcula los impares del 1 al 20

class Impares:
    def __iter__(self):
        for m in range(1, 21):
            if m % 2 != 0:
                yield m

for v in Impares():
    print(v)
