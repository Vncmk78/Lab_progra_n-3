class Cuadrado:
    def se_crea(self):
        m = []
        for v in range(1, 11):
            m.append(v ** 2)
        return m

obj = Cuadrado()
print(obj.se_crea())
