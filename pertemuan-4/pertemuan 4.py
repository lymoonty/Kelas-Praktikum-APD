# # perulangan 
# for j in range(12):
#       print("alooo")



## penggunaan lain perulangan for
# print("Menu Rumah Makan Informatika 24: ")
# print("--------------------------------")
# simpan = ["mie ayam", "nasi goreng", "bakso", "soto", "mie goreng"]
# for i in simpan:
#     print(i)



# print("Menu Rumah Makan Informatika 24: ")
# print("--------------------------------")
# simpan = ["mie ayam", "nasi goreng", "bakso", "soto", "mie goreng"]
# for i, menu in enumerate(simpan,start=1):
#     print(f"{i}.{menu}")

# # contoh lain memakai len
# print("Menu Rumah Makan Informatika 24: ")
# print("--------------------------------")
# simpan = ["mie ayam", "nasi goreng", "bakso", "soto", "mie goreng"]
# for i in range(len(simpan)):
#     print(f"{i+1}. {simpan[i]}")



# # for didalam for
# makanan = ["mie","sop","bakso"]
# minuman = ["susu","teh","air putih"]

# for i in makanan:
#     for j in minuman:
#         print(f"{i} & {j}")



# # perulangan while
# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya' or 'Ya'):
#   hitung += 1
#   jawab = input("Ulang lagi tidak? ")
#   print(f"Total perulangan: {hitung}")

# # penggunaan while tetapi bisa dihitung
#  
#
#   


# # penggunaan break
# i = 0
# while i < 5:
#     print(i)
#     break
#     i+=1
#     i = i+1

# hitung = 0
# while True:
#   hitung += 1
#   ulang = input("Masih Ingin Mengulang? ")
#   if ulang == "tidak" or ulang =="Tidak":
#     print("oke kita lanjut")
#     break

# print(f"Total Perulangan: {hitung}")

# continue
# print(“Daftar bilangan ganjil dari 1-10”)
# for i in range(10):
#     if i % 2 == 0:
#        continue
#     print(i)


# # kasus pertama 
# total = 0
# while True:
#     angka=int(input("masukkan angka positif (input negatif jika ingin berhenti: "))
#     if angka < 0:
#         break
#     total += angka

# print("jumlah total adalah:"),


# # kasus 2
# Meminta input dari pengguna untuk range maksimal
range_maksimal = int(input("Masukkan range maksimal: "))

# Inisialisasi variabel untuk menyimpan jumlah bilangan prima
hitung_prima = 0

# Loop untuk memeriksa setiap angka dari 1 hingga range_maksimal
for angka in range(1, range_maksimal):
    angka += 1
    apakah_prima = True  # Anggap angka tersebut prima

    # Cek apakah angka memiliki pembagi selain 1 dan dirinya sendiri
    for i in range(2, angka):
        if angka % i == 0:
            apakah_prima = False  # Jika ada pembagi, bukan bilangan prima
            # print(f"{angka} bukan prima")
            break
    # Jika angka tersebut prima, tambahkan jumlah hitung_prima
    if apakah_prima == True:
        print(f"{angka} prima")
        hitung_prima += 1

# output
print(f"Jumlah bilangan prima antara 1 hingga {range_maksimal} adalah: {hitung_prima}")





