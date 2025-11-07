#se crea la funcion que calcula la serie fibonacci

def fibonacci():
    a, b = 0, 1
    for m in range(10):
        yield a
        a, b = b, a + b

for num in fibonacci():
    print(num)
