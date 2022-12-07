# Fungsi Garis 
def garis():
  print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

# SELAMAT DATANG DI JP HOTEL.
garis()
print("--Selamat datang DI JPHOTEL, Silahkan Pilih--")
print("--NO-----TIPE----------HARGA--")
print("--01-----Suite-----1.000.000--")
print("--02-----Royal-------500.000--")
print("--03-----BPJS--------250.000--")

# Sampe Resepsionsi (input Data)
garis()
cust = input("Masukan Nama Lengkap : ")
tipe = int(input("Tipe : "))
lama_inap = int(input("Masukan Lama Menginap : "))

# Tipe Kamar
garis()
if tipe == 1:
  tipe_kamar = ("Suite")
elif tipe == 2:
  tipe_kamar = ("Royal")
elif tipe == 3:
  tipe_kamar = ("BPJS")

# Kalkulasi Harga Total
if tipe == 1:
  total_harga = 1000000*lama_inap
elif tipe == 2:
  total_harga = 500000*lama_inap
elif tipe == 3:
  total_harga = 250000*lama_inap

# Struck Hotel
print ("Terimakasih Atas Nama : ", cust)
print ("Tipe Kamar Yang Dipilh : ", tipe_kamar)
print ("Lama Inap : ", lama_inap)
garis()
print ("TOTAL : ","Rp", total_harga ,",00")