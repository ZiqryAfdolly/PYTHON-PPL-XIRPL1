# Public
class siswa:
    def __init__(self, nama):
        self.nama = nama

perkenalan = siswa('Euroski')       

print(f'1. Siswa Kami bernama {perkenalan.nama} Ganteng \n')

# Protected
class tanaman:
    def __init__(self, nama):
        self._nama = nama

class tanamanBangke(tanaman):
    def __init__(self, nama):
        super().__init__(nama)

    def perkenalan(self):
        print(f'tanaman saya adalah BungaI {self._nama}\n')

bunga = tanamanBangke('Bangke')
bunga.perkenalan
()                  

# Private
class kepsek:
    def __init__(self, nama):
        self.__nama = nama

    def tampilkan_nama_kepsek(self):
        print(f'3. Kepsek Kami Bernama {self.__nama} \n')

pakLilik = kepsek('Pak Lilik')
pakLilik.tampilkan_nama_kepsek()            