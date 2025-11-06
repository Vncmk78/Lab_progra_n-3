from functools import reduce

palabras = ["Hola", " ", "Mundo", "!"]
frase = reduce(lambda a, b: a + b, palabras)
print(frase)
