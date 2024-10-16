### PROSEDUR
# def menu():
#     print("Menu pilihan")
#     print("1. tambah")
#     print("2. kurang")
#     print("3. kali")
#     print("4. bagi")

# menu()

### membuat fungsi
# def salam():
#   print ("Selamat Pagi, FT Muda")
# def kali():
#   x = 6*4
#   print(x)

# salam()
# kali()

# def salam(nama):
#     print("Selamat pagi",nama)

# (salam("chira"))

## memakai parameter (a,b) 
# def tambah(a,b):
#     hasil = a + b
#     print(hasil)

# tambah(7,3)  

## tidak memakai parameter ()
# def penjumlahan():
#     a = 7
#     b = 3
#     hasil = a + b
#     print(hasil)

# penjumlahan()

## MEMAKAI PARAMETER CONTOH 2
# a = int(input("Masukkan angka pertama: "))
# b = int(input("Masukkan angka kedua: "))
# def tambah(a,b):
#     hasil = a + b
#     print(hasil)

# tambah(a,b)


### FUNGSI
# a = int(input("Masukkan angka pertama: "))
# b = int(input("Masukkan angka kedua: "))

# def tambah(a,b):
#     hasil = a + b
#     return hasil
# print(tambah(a,b))

# nama = "kuroo" # global

# def salam():
#     nama = "rimuru" # lokal
#     print(nama)

# salam()

### CONTOH PENGGUNAAN RETURN
# rumus: sisi x sisi
# def luas_persegi(sisi):
#      luas = sisi * sisi
#      return luas
#  rumus: sisi x sisi x sisi
# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print ("Volume Persegi = ", volume)
# pemanggilan Fungsi
# volume_persegi(6)

buku =[]
def show_data():
  if len(buku) <= 0:
    print ("Belum Ada data")
  else:
    print("ID", "Nama Buku")
    for indeks in range(len(buku)):
      print (indeks, buku[indeks])

# fungsi untuk menambah data
def insert_data():
  buku_baru = input("Judul Buku : ")
  buku.append(buku_baru)

# fungsi untuk edit data
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks >= len(buku) or indeks < 0):
      print ("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

# fungsi untuk menghapus data
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks >= len(buku) or indeks < 0):
     print ("ID salah")
    else:
       buku.remove(buku[indeks])

# fungsi untuk menampilkan menu
def show_menu():
     print ("\n")
     print ("----------- MENU---------- ")
     print ("[1] Show Data")
     print ("[2] Insert Data")
     print ("[3] Edit Data")
     print ("[4] Delete Data")
     print ("[5] Exit")
menu = input("PILIH MENU> ")
print ("\n")

if menu == "1":
     show_data()
elif menu == "2":
     insert_data()
elif menu == "3":
     edit_data()
elif menu == "4":
     delete_data()
elif menu == "5":
     exit()
else:
    print ("Salah pilih!")
while (True):
  show_menu()