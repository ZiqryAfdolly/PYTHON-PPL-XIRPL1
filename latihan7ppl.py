# Latihan OverLoading

class angka:
    def __init__(self, angka):
        self.angka = angka

    def __add__(self, objek): #Magic Method
        return self.angka + objek.angka          

X1 = angka(20)
X2 = angka(30) 
print (X1 + X2)

