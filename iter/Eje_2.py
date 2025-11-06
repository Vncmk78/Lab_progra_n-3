class Impares:
    def __iter__(self):
        for m in range(1, 21):
            if m % 2 != 0:
                yield m

for v in Impares():
    print(v)
