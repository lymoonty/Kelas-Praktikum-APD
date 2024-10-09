# # deklarasi dictionary contoh
# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# #contoh 2
# daftar_buku = {}
# daftar_buku["Buku1"] = "Harry Potter"
# daftar_buku["Buku2"] = "Percy Jackson"
# daftar_buku["Buku3"] = "Twillight"
# print(daftar_buku)

#Buat dictionary contoh 1
# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra",
# "NIM" : 2109106079,
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" :True,
# "Social Media" : {
# "Instagram" : "@aldyrmdhns_",
# "Discord" : "\'Izanami#6848"
# }
# }

# print(Biodata['Social Media']["Discord"])
# print(Biodata['KRS'][1])
# print(Biodata.get('KRS'))


# perulangan pada python
# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# #tanpa menggunakan items
# for i in Nilai:
#   print(i)
# print("")

# #menggunakan items
# for i, j in Nilai.items():
#  print(f"Nilai {i} anda adalah {j}")

#menambah item di dictionary

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
#  "B. Inggris" : 81,
#  "Kimia" : 78,
# "Fisika" : 80
#  }
# print(Nilai)

# Nilai.update({"Biologi":80})

# menghapus dictionary penggunaan del,pop, kalau clear lngsng menghapus semua
# del Nilai["Kimia"]
# print(Nilai)

# simpan = Nilai.pop("fisika")
# print(Nilai)
# print(simpan)

# print("jumlah data = ",len(Nilai))

#copy and fromkeys
# Buku = {
# "No Longer Human" : "Osamu Dazai",
# "Harry Potter" : "J.K. Rowlings",
# "Hamlet" : "William Shakespeare"
# }
# pinjam = Buku.copy()
# print("Dictionary yang Telah Disalin : ", pinjam)

#contoh 2 
# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)

#keys and value
# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
#menggunakan keys
# for i in Nilai.keys():
#   print(i)
# print("")  
# #menggunakan value
# for i in Nilai.values():
#   print(i)

#setdefault
#sebelum Setdefault
# print(Nilai)
# print("")
# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")
# #setelah menggunakan setdefault
# print(Nilai)

#Dictionary of List and Nested Dictionary
# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#  print(f"Musik milik {i} adalah : ")
#  for song in j:
#   print(song)
#  print("")

 # nested dictionary
# mahasiswa = {
#  101 : {"Nama" : "Aldy", "Umur" : 19},
#  111 : {"Nama" : "Abdul", "Umur" : 18}
#  }
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#      print (key_a, " : ", value_a)
#     print("")

# #Menambahkan Item pada Nested Dictionary
# mahasiswa[101]["Angkatan"] = 2023
# print(mahasiswa)

# #Mengubah Item pada Nested Dictionary
# mahasiswa[101]["Nama"] = "Rizal"
# print(mahasiswa)

# #Menghapus Item pada Nested Dictionary
# del mahasiswa[101]["Umur"]
# print(mahasiswa)

#studi kasus 1
# mahasiswa = {
#  102 : {"Nama" : "bila", "Umur" : 19, "NIM" : 41, "jurusan" : "informatika", "angkatan" : 34},
#   }
#  #Menambahkan Item pada Nested Dictionary
# mahasiswa[102]["NIM"] = 24
# print(mahasiswa)

#  #Mengubah Item pada Nested Dictionary
# mahasiswa[102]["Nama"] = "putri"
# print(mahasiswa)

# #Menghapus Item pada Nested Dictionary
# del mahasiswa[102]["Umur"]
# print(mahasiswa)

#studi kasus 2 
Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81,
"Kimia" : 78,
 "Fisika" : 80
 }


