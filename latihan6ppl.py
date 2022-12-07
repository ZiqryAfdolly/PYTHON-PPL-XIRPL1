# Jenis enkapsulasi : public, protected, privete

# membuat public class

class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0,5 * alas * tinggi

#instasiasi 
segitiga_besar = segitiga(100, 80)

# print
print('Ini adalah public class')
print(f'Alas : {segitiga_besar.alas}')
print(f'Tinggi : {segitiga_besar.tinggi}')
print(f'Luas : {segitiga_besar.luas}\n')

# membuat protected class
class mobil: #class induk
    def __init__(self,merk):
        self._merk = merk #protected classs declaration


class mobillefwan(mobil): #class turunan
    def __init__(self, merk, total_gear):
        super().__init__(merk) #panggil merk dibagian sini
        self._total_gear = total_gear          

    def pamer(self):
        # hak akses _merk  dari subclass
        print (f'ini adalah mobil {self._merk} dengan total gear nya {self._total_gear}')

# instamsiasi
print('Ini adalah protected class')
ferrari = mobillefwan('Ferrari',8)
ferrari.pamer()

# Membuat privete class
class motor:
    def __init__(self, merk):
        self._merk = merk #privete class declaration

    def tampilkan_merk(self):
        print(f'Merk Motornya : {self._merk}') 



#instansiasi
print('Ini adalah private class')
moge = motor('Harley')
moge.tampilkan_merk()
