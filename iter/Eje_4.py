#se imprimen las palabras en mayusculas con iter y next 

class Mayusculas:
    def __init__(self, cadenas):
        self.cadenas = cadenas
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.indice >= len(self.cadenas):
            raise StopIteration
        palabra = self.cadenas[self.indice].upper()
        self.indice += 1
        return palabra

palabras = Mayusculas(["hola", "mundo", "python"])
for m in palabras:
    print(m)
