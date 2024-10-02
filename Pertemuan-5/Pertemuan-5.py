nama = ["celio",
        "shandy",
        "farrel",
        "ghazali",
        "vito",
        "yuyun",
        "adri",
        "rizal",
        "adi",
        "ifnu"
]

matkul = ["APD","APL","BASDAT","STRUKDAT",""]

print("sebelum: ")
print(nama)
print("")
print("sesudah:")


##MENAMBAH ELEMEN
# nama.insert(2,"afrizal")
# print(nama)
## mengubah elemen
# nama[4]= "fufufafa"
# print(nama)
## menghapus elemen (del)
# hapus = nama.pop(2)
# print(nama)
# print(hapus)

## slicing list
# print(nama[1:9:2])

## nested list
# data = ["farel","celio",{1,2,["halo",23,2,3,True]}]

#  print(data[2][2][::-1])

# print(data[::-1])

matkul = [1,2,3,4,{5,6,7, [2,3,4]}]
# print(matkul[4][2][::-1])
## perulangan nested list
for i in matkul:
   # print(i, end='-')
   for j in i:
      print(j)


