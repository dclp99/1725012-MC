#definir Fila
class Fila:
    def __init__(self):
        self.fila=[]

    def obtener(self):
        return self.fila.pop()

    def meter(self,e):
        self.fila.insert(0,e)
        return len(self.fila)

    @property
    def longuitud(self):
        return len(self.fila)


f=Fila()
f.meter(54)
f.meter(8)
f.meter(35)
f.meter(4)
print(f.longuitud)
