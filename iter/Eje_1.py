#contador con iter del 10 al 15

class Contador:
    def __init__(self, inicio, fin):
        self.actual = inicio
        self.fin = fin

    def __iter__(self):
        return self  # el propio objeto es el iterador

    def __next__(self):
        if self.actual <= self.fin:
            valor = self.actual
            self.actual += 1
            return valor
        else:
            raise StopIteration

for numero in Contador(10, 15):
    print(numero)
