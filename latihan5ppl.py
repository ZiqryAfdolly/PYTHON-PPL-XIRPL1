# bikin 3 object : Orang, Pelajar, Pekerja
# Orang adalah Class Induk
# dan Pelajar , Pekerja = Kelas Turunan

class orangTua:
    def __init__(self, nama, usia):
        self.nama = nama
        self.usia = usia

    def perkenalan(self):
        print("Hallo Saya adalah", self.nama, "usia saya", self.usia, "tahun\n")

class anakPertama(orangTua):
    def __init__(self, nama, usia, sekolah):
        orangTua.__init__(self, nama, usia)
        self.sekolah = sekolah

class anakKedua(orangTua):
    def __init__(self, nama, usia, sekolah):
        super().__init__(nama, usia)
        self.sekolah = sekolah

andi = orangTua('Muji','45')
andi.perkenalan()        

tito = anakPertama('karyono','10', 'SMK JP 1\n')
tito.perkenalan()
print(f'Saya Sekolah di{tito.sekolah}\n')

cahyo = anakKedua('Parto','5', 'Paud Apel')
cahyo.perkenalan()
print(f'Saya sekolah di {cahyo.sekolah}\n')

